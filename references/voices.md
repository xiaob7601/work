# 中文音色速查表（Edge TTS）

全部音色用 `--voice <ID>` 指定。中文普通话音色如下：

| 音色 ID | 性别 | 风格 | 适合场景 |
|---|---|---|---|
| `zh-CN-XiaoxiaoNeural` | 女 | 温暖、亲切 | **日常朗读/对话（默认）** |
| `zh-CN-XiaoyiNeural` | 女 | 活泼、俏皮 | 讲故事、儿童内容 |
| `zh-CN-YunjianNeural` | 男 | 激情、浑厚 | 体育解说、小说旁白 |
| `zh-CN-YunxiNeural` | 男 | 阳光、年轻 | 年轻向内容、轻松对话 |
| `zh-CN-YunxiaNeural` | 男 | 可爱、少年 | 卡通、动漫风格 |
| `zh-CN-YunyangNeural` | 男 | 专业、可靠 | 新闻播报、正式通知 |
| `zh-CN-liaoning-XiaobeiNeural` | 女 | 东北方言 | 幽默、方言内容 |
| `zh-CN-shaanxi-XiaoniNeural` | 女 | 陕西口音 | 方言、地域特色内容 |

其他常用中文变体：
- 台湾：`zh-TW-HsiaoChenNeural`（女）、`zh-TW-YunJheNeural`（男）
- 香港：`zh-HK-HiuMaanNeural`（女）、`zh-HK-WanLungNeural`（男）

## 语速/音量调节

```bash
# 放慢 10%（更适合朗读长文）
python speak.py --text "..." --rate -10%

# 加速 20%（适合新闻快报）
python speak.py --text "..." --rate +20%

# 音量调大 50%
python speak.py --text "..." --volume +50%
```

## 完整音色列表

运行 `python speak.py --list-voices` 可查看全部 400+ 音色（含英语、日语、韩语等 100+ 语言）。
