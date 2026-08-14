---
name: tts-speak
description: 文本转语音朗读（Text-to-Speech）。当用户要求"朗读、读出来、念给我听、语音播报、把回复读出来、生成语音、语音版、配音"时使用。Convert text into natural-sounding Chinese speech using Microsoft Edge TTS (free), generate an MP3 file and play it aloud on Windows. Also supports saving speech as audio files.
agent_created: true
---

# TTS Speak（文本转语音朗读）

## Overview

将任意文本（用户给的文字、AI 回复、文件内容）转换为自然流畅的中文语音，并在 Windows 上播放出来，或保存为 MP3 文件。基于微软 Edge TTS 在线合成，免费、无需 API Key、音质接近真人。

**适用场景：**
- 用户说"把我的回复读出来 / 朗读这段话 / 念给我听 / 语音播报"
- 把长文本转成语音文件（如通勤路上听新闻摘要、会议记录）
- 为文案、文章、台词生成配音 MP3

**环境要求：** 需联网（调用微软语音服务）。播放使用 Windows 自带能力，无需额外软件。

## Quick Start

运行脚本（使用托管 Python 虚拟环境，务必用完整路径）：

```bash
# 1. 朗读文本（默认女声 zh-CN-XiaoxiaoNeural）
"C:/Users/Administrator/.workbuddy/binaries/python/envs/default/Scripts/python.exe" \
  "C:/Users/Administrator/.workbuddy/skills/tts-speak/scripts/speak.py" --text "你好，欢迎使用语音朗读"

# 2. 朗读文件内容
python speak.py --file "C:/path/to/notes.txt"

# 3. 指定男声 + 放慢语速（新闻播报感）
python speak.py --text "今日要闻" --voice zh-CN-YunyangNeural --rate -10%

# 4. 只生成 MP3 不播放，输出到指定路径
python speak.py --text "..." --no-play --output "D:/speech/out.mp3"

# 5. 查看全部可用音色
python speak.py --list-voices
```

**参数一览：**
| 参数 | 说明 | 默认 |
|---|---|---|
| `--text` | 要朗读的文本 | - |
| `--file` | 从 UTF-8 文本文件读取内容（与 --text 二选一） | - |
| `--voice` | 音色 ID | `zh-CN-XiaoxiaoNeural` |
| `--rate` | 语速：`+10%` 加快 / `-10%` 减慢 | `+0%` |
| `--volume` | 音量：`+50%` 调大 | `+0%` |
| `--output` | 输出 mp3 路径 | 系统临时目录 |
| `--no-play` | 只生成文件、不播放 | 播放 |
| `--list-voices` | 列出所有音色 | - |

## 音色选择

常用中文音色与适用场景见 `references/voices.md`。要点：
- 日常朗读/对话：`zh-CN-XiaoxiaoNeural`（女，温暖）
- 活泼/讲故事：`zh-CN-XiaoyiNeural`（女，活泼）或 `zh-CN-YunxiNeural`（男，阳光）
- 新闻播报：`zh-CN-YunyangNeural`（男，专业）
- 用户未指定音色时，默认用 `zh-CN-XiaoxiaoNeural`

## 注意事项

1. **播放机制**：脚本优先用 pygame 静默播放（不弹窗）；若音频设备不可用，自动改用系统默认播放器打开 mp3。
2. **超长文本**：Edge TTS 单次合成对超长文本可能截断；超过约 3000 字的文本应分段生成（多次调用脚本，每次一段）。
3. **联网要求**：合成过程需访问微软语音服务；断网时脚本会报错，需提示用户。
4. **Windows 路径**：脚本内嵌了本机 Python 环境绝对路径，换机器后需修改为对应环境路径。

## Resources

### scripts/
- `speak.py` — 核心朗读脚本：文本/文件 → MP3 → 播放或保存。

### references/
- `voices.md` — 中文音色清单与适用场景速查表。
