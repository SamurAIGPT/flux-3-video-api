# FLUX 3 Video API: Python Wrapper for Black Forest Labs' FLUX 3 Video Family

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=flux-3-video-api)

[![PyPI version](https://img.shields.io/pypi/v/flux-3-video-api.svg)](https://pypi.org/project/flux-3-video-api/)
[![GitHub stars](https://img.shields.io/github/stars/SamurAIGPT/flux-3-video-api.svg)](https://github.com/SamurAIGPT/flux-3-video-api/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A focused Python wrapper for the **FLUX 3 video API** — Black Forest Labs' unified multimodal frontier model, delivered via [muapi.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-api). Generate cinematic video clips with native synchronized audio from a text prompt (Text-to-Video), from a static image (Image-to-Video), between two keyframes (Start-End-to-Video), or continue an existing clip (Video Extend) — plus fast draft modes and a video upscaler. All seven FLUX 3 video endpoints are **live now**.

> 🌌 **FLUX 3** was announced by Black Forest Labs on July 23, 2026 as a unified multimodal frontier model — one architecture generates image, video, and native synchronized audio, and extends to action-prediction for robotics. The full FLUX 3 video API is **live now** on [MuAPI](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-api) — no waitlist required, just an API key.

<p align="center">
  <a href="https://www.youtube.com/watch?v=pq0B_A0K770">
    <img src="docs/assets/flux-3-api-video-thumbnail.png" alt="FLUX 3 API: Image & Video Generation from One Multimodal Model" width="640">
  </a>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=pq0B_A0K770"><b>📺 FLUX 3 API: Image & Video Generation from One Multimodal Model →</b></a>
</p>

## Related Projects

- [MiniMax-H3-API](https://github.com/Anil-matcha/MiniMax-H3-API) — Python SDK for MiniMax H3 text-to-video, image-to-video, and first/last-frame video generation.
- [Flux-3-Dev-API](https://github.com/Anil-matcha/Flux-3-Dev-API) — Python SDK covering the full FLUX 3 family, including image endpoints
- [awesome-flux-3-api-prompts](https://github.com/Anil-matcha/awesome-flux-3-api-prompts) — Curated FLUX 3 API guide, prompts, parameters, and examples
- [flux-3-video-edit](https://github.com/Anil-matcha/flux-3-video-edit) — Python SDK for FLUX 3 Video Extend (continuing an existing clip)
- [flux-3-video-upscaler](https://github.com/Anil-matcha/flux-3-video-upscaler) — Python SDK for upscaling FLUX 3 (or any) video output beyond its native resolution
- [flux-3-omni](https://github.com/Anil-matcha/flux-3-omni) — Python SDK for FLUX 3's multi-reference Omni Reference mode (coming soon)
- [Seedance-2.5-API](https://github.com/SamurAIGPT/Seedance-2.5-API) — Python wrapper for ByteDance's Seedance 2.5 video model
- [veo4-video-generator](https://github.com/SamurAIGPT/veo4-video-generator) — Ready-made video generator built on Google's Veo 4
- [muapi-skills](https://github.com/SamurAIGPT/muapi-skills) — Skills runtime for generative media API prompts
- [muapi-cli](https://github.com/SamurAIGPT/muapi-cli) — CLI for running MuAPI generation tasks, including FLUX 3

## 🚀 Why Use the FLUX 3 Video API?

FLUX 3 is Black Forest Labs' unified multimodal frontier model — the same weights that generate images also generate video and native synchronized audio in a single request.

- **Native Synchronized Audio**: `generate_audio` produces dialogue, sound effects, and music matched to the visuals — no separate audio pipeline required, no extra charge.
- **Seven Live Endpoints**: Text-to-Video, Image-to-Video, Start-End-to-Video, Video Extend, Video Upscaler, plus fast draft modes of Text-to-Video and Video Extend.
- **Unified Model Architecture**: Same frontier model family as FLUX 3's image endpoints — consistent visual style across image and video outputs.
- **Developer-First**: Simple Python SDK backed by MuAPI's infrastructure — one API key, seven FLUX 3 video endpoints.

## 🌟 Key Features

- ✅ **FLUX 3 Text-to-Video**: Transform a text prompt into a cinematic video clip, 5–20 seconds long.
- ✅ **FLUX 3 Text-to-Video Draft**: Fast, lower-cost draft mode for rapid prompt iteration before a final-quality render.
- ✅ **FLUX 3 Image-to-Video**: Animate a static image into a video clip using `image_url`, with motion physically consistent with the source frame.
- ✅ **FLUX 3 Start-End-to-Video**: Generate a controlled transition between a start keyframe and an end keyframe you supply.
- ✅ **FLUX 3 Video Extend**: Continue an existing clip with new prompt-guided motion and scene development.
- ✅ **FLUX 3 Video Extend Draft**: Fast, lower-cost draft mode for testing continuity before a final extension.
- ✅ **FLUX 3 Video Upscaler**: Upscale any video (FLUX 3 output or otherwise) beyond its native resolution.
- ✅ **Native Audio Generation**: `generate_audio=True` produces synchronized voice, sfx, and music from the same generation call, no extra charge.
- ✅ **Flexible Resolutions**: `720p` or `1080p` output on the standard endpoints.
- ✅ **Flexible Aspect Ratios**: `21:9`, `2:1`, `16:9`, `9:16` (TikTok/Reels/Shorts), `4:3`, `1:1`, `3:4`.
- ✅ **File Upload**: Upload local images or videos directly via `upload_file` for use as start frames or source clips.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install flux-3-video-api
```

### From Source
```bash
# Clone the FLUX 3 Video API repository
git clone https://github.com/SamurAIGPT/flux-3-video-api.git
cd flux-3-video-api

# Install required dependencies
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 FLUX 3 Video MCP Server

You can use FLUX 3 video generation as an **MCP (Model Context Protocol)** server, so AI models (like Claude Desktop or Cursor) can directly invoke the tools.

### Running the MCP Server
1. Ensure `MUAPI_API_KEY` is set in your environment.
2. Run the server:
   ```bash
   python3 mcp_server.py
   ```
3. To test with the MCP Inspector:
   ```bash
   npx -y @modelcontextprotocol/inspector python3 mcp_server.py
   ```

---

## 💻 Quick Start (Python)

```python
from flux3_video_api import Flux3VideoAPI

# Initialize the FLUX 3 Video client
api = Flux3VideoAPI()

# 1. Generate Video from Text (Text-to-Video)
print("Generating AI video using FLUX 3...")
submission = api.text_to_video(
    prompt="A cinematic slow-motion shot of a cyberpunk city in the rain, neon lights reflecting on puddles",
    aspect_ratio="16:9",
    resolution="720p",
    duration=5,
    generate_audio=True,
)

# 2. Wait for completion
result = api.wait_for_completion(submission["request_id"])
print(f"Success! View your FLUX 3 video here: {result.get('outputs', [result.get('url')])}")
```

```python
# 3. Animate a static image (Image-to-Video)
submission = api.image_to_video(
    prompt="The clouds drift slowly and the water ripples",
    image_url="https://example.com/landscape.jpg",
    aspect_ratio="16:9",
    resolution="720p",
    duration=5,
)
result = api.wait_for_completion(submission["request_id"])
print(result.get("outputs", [result.get("url")]))
```

```python
# 4. Continue an existing clip (Video Extend)
submission = api.video_extend(
    prompt="The camera pulls back to reveal a sunrise breaking over the skyline",
    video_url="https://example.com/clip.mp4",
    resolution="720p",
    duration=5,
)
result = api.wait_for_completion(submission["request_id"])
print(result.get("outputs", [result.get("url")]))
```

---

## 📡 API Endpoints & Reference

All endpoints are async: the `POST` call returns `{"request_id": "...", "status": "processing"}` immediately; poll `GET https://api.muapi.ai/api/v1/predictions/{request_id}/result` until `status` is `completed` or `failed`, then read the video URL from `outputs`.

### 1. FLUX 3 Text-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-text-to-video` · **$0.25/sec @720p, $0.42/sec @1080p**

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-text-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A majestic eagle soaring over the snow-capped Himalayas",
      "aspect_ratio": "16:9",
      "resolution": "720p",
      "duration": 5,
      "generate_audio": true
  }'
```

### 2. FLUX 3 Text-to-Video Draft
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-text-to-video-draft` · **$0.09/sec flat**

Fast, lower-cost draft mode for rapid ideation, storyboarding, and prompt iteration before rendering a final-quality clip with Text-to-Video. Same fields minus `resolution`.

### 3. FLUX 3 Image-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-image-to-video` · **$0.25/sec @720p, $0.42/sec @1080p**

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-image-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The clouds move slowly across the sky",
      "image_url": "https://example.com/mountain.jpg",
      "aspect_ratio": "16:9",
      "resolution": "720p",
      "duration": 5,
      "generate_audio": true
  }'
```

### 4. FLUX 3 Start-End-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-start-end-to-video` · **$0.25/sec @720p, $0.42/sec @1080p**

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-start-end-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The scene morphs from a busy daytime street to the same street quiet at night",
      "image_url": "https://example.com/start.jpg",
      "end_image_url": "https://example.com/end.jpg",
      "resolution": "720p",
      "duration": 5,
      "generate_audio": true
  }'
```

### 5. FLUX 3 Video Extend
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-video-extend` · **$0.25/sec @720p, $0.42/sec @1080p**

Continues an existing clip (source `video_url` must be under 50MB and under 15 seconds) with new prompt-guided motion.

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-video-extend" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The camera pulls back to reveal a sunrise breaking over the skyline",
      "video_url": "https://example.com/clip.mp4",
      "resolution": "720p",
      "duration": 5,
      "generate_audio": true
  }'
```

### 6. FLUX 3 Video Extend Draft
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-video-extend-draft` · **$0.09/sec flat**

Fast, lower-cost draft mode for testing continuity before a final extension. Same fields as Video Extend minus `resolution`.

### 7. FLUX 3 Video Upscaler
**Endpoint**: `POST https://api.muapi.ai/api/v1/flux-3-video-upscaler` · **$1.43/run (Precise), $2.00/run (Creative)**

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/flux-3-video-upscaler" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "video_url": "https://example.com/clip.mp4",
      "upscale_factor": 2,
      "creativity": 0
  }'
```

---

## 📖 Documentation & Guides

For prompt engineering and advanced use cases across the full FLUX 3 model family (image and video), see [awesome-flux-3-api-prompts](https://github.com/Anil-matcha/awesome-flux-3-api-prompts).

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `text_to_video` | `prompt`, `aspect_ratio`, `resolution`, `duration`, `generate_audio` | Generate a video clip from a text prompt (5-20s), with optional native synchronized audio. |
| `text_to_video_draft` | `prompt`, `aspect_ratio`, `duration`, `generate_audio` | Fast, lower-cost draft mode of `text_to_video`. |
| `image_to_video` | `prompt`, `image_url`, `aspect_ratio`, `resolution`, `duration`, `generate_audio` | Animate a static image into a video clip. |
| `start_end_to_video` | `prompt`, `image_url`, `end_image_url`, `aspect_ratio`, `resolution`, `duration`, `generate_audio` | Generate a transition between a start and end keyframe. |
| `video_extend` | `prompt`, `video_url`, `aspect_ratio`, `resolution`, `duration`, `generate_audio` | Continue an existing clip with new prompt-guided motion. |
| `video_extend_draft` | `prompt`, `video_url`, `aspect_ratio`, `duration`, `generate_audio` | Fast, lower-cost draft mode of `video_extend`. |
| `video_upscale` | `video_url`, `prompt`, `upscale_factor`, `creativity` | Upscale any video beyond its native resolution. |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI for use in generation tasks. |
| `get_result` | `request_id` | Check task status for a FLUX 3 video generation task. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for FLUX 3 video generation tasks. |

---

## 🔗 Official Resources
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-api)
- **Early Access**: [Get a FLUX 3 API key](https://muapi.ai/flux-3?utm_source=github&utm_medium=readme&utm_campaign=flux-3-video-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: FLUX 3 Video API, FLUX 3 Text-to-Video, FLUX 3 Image-to-Video, FLUX 3 Start-End-to-Video, FLUX 3 Video Extend, FLUX 3 Video Upscaler, Black Forest Labs Video AI, FLUX 3 Python SDK, MuAPI, AI Video Generation API, Text-to-Video API, Image-to-Video API, FLUX Video Generator, Native Audio Video Generation, Cinematic AI Video, FLUX 3 API Documentation.
