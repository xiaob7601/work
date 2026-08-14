#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
speak.py - 文本转语音并朗读（基于微软 Edge TTS，免费、音质自然）

用法:
  python speak.py --text "你好，世界"                # 直接朗读文本
  python speak.py --file notes.txt                  # 朗读文件内容
  python speak.py --text "..." --voice zh-CN-YunyangNeural --rate +10% --volume +0%
  python speak.py --text "..." --no-play --output D:/out.mp3   # 只生成音频文件
  python speak.py --list-voices                     # 列出全部音色

参数:
  --text    要朗读的文本
  --file    从 UTF-8 文本文件读取内容（与 --text 二选一）
  --voice   音色，默认 zh-CN-XiaoxiaoNeural（详见 references/voices.md）
  --rate    语速，如 +10%（加快）/-10%（减慢），默认 +0%
  --volume  音量，如 +50%，默认 +0%
  --output  输出 mp3 路径（默认保存到系统临时目录）
  --no-play 只生成文件不播放
  --list-voices  打印所有可用音色后退出
"""
import argparse
import asyncio
import os
import sys
import tempfile
import time


def list_voices():
    import edge_tts
    async def _run():
        voices = await edge_tts.list_voices()
        for v in voices:
            name = v["ShortName"]
            gender = v.get("Gender", "")
            tags = " ".join(v.get("VoiceTag", {}).get("VoicePersonalities", []))
            print(f"{name:40s} {gender:8s} {tags}")
    asyncio.run(_run())


def play_mp3_windows(path: str) -> bool:
    """用 pygame 静默播放 mp3（不弹窗）。失败返回 False 以便调用方兜底。"""
    try:
        os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
        pygame.mixer.quit()
        return True
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description="文本转语音朗读工具")
    parser.add_argument("--text", help="要朗读的文本")
    parser.add_argument("--file", help="从 UTF-8 文件读取文本")
    parser.add_argument("--voice", default="zh-CN-XiaoxiaoNeural", help="音色（默认 zh-CN-XiaoxiaoNeural）")
    parser.add_argument("--rate", default="+0%", help="语速，如 +10% / -10%")
    parser.add_argument("--volume", default="+0%", help="音量，如 +50%")
    parser.add_argument("--output", help="输出 mp3 路径（默认系统临时目录）")
    parser.add_argument("--no-play", action="store_true", help="只生成音频文件，不播放")
    parser.add_argument("--list-voices", action="store_true", help="列出所有可用音色")
    args = parser.parse_args()

    if args.list_voices:
        list_voices()
        return

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    else:
        text = args.text

    if not text or not text.strip():
        print("错误：没有可朗读的文本（请用 --text 或 --file 提供内容）", file=sys.stderr)
        sys.exit(1)

    if args.output:
        out_path = args.output
    else:
        out_path = os.path.join(tempfile.gettempdir(), f"wb_speak_{int(time.time())}.mp3")

    import edge_tts

    async def gen():
        comm = edge_tts.Communicate(text, args.voice, rate=args.rate, volume=args.volume)
        await comm.save(out_path)

    asyncio.run(gen())
    print(f"✅ 已生成语音文件：{out_path}")

    if args.no_play:
        print("（--no-play：仅生成，未播放）")
        return

    ok = play_mp3_windows(out_path)
    if ok:
        print("🔊 正在播放……")
    else:
        os.startfile(out_path)  # 兜底：调用系统默认播放器
        print("🔊 已调用系统默认播放器播放")


if __name__ == "__main__":
    main()
