import json
from mcp.server.fastmcp import FastMCP
from flux3_video_api import Flux3VideoAPI

# Initialize FastMCP server
mcp = FastMCP("FLUX 3 Video API Server")

# Helper to get API client
def get_api():
    return Flux3VideoAPI()

@mcp.tool()
def text_to_video(prompt: str, aspect_ratio: str = "9:16", resolution: str = "720p", duration: int = 5, generate_audio: bool = True) -> str:
    """
    Generate a video from a text prompt using FLUX 3.

    :param prompt: Descriptive text prompt for the video scene and motion.
    :param aspect_ratio: Video aspect ratio ('21:9', '2:1', '16:9', '4:3', '1:1', '3:4', '9:16').
    :param resolution: '720p' or '1080p'. $0.25/sec at 720p, $0.42/sec at 1080p.
    :param duration: Duration in seconds (5-20), billed rounded up to the next second.
    :param generate_audio: Whether to generate synchronized native audio, no extra charge.
    """
    api = get_api()
    result = api.text_to_video(prompt, aspect_ratio, resolution, duration, generate_audio)
    return json.dumps(result, indent=2)

@mcp.tool()
def text_to_video_draft(prompt: str, aspect_ratio: str = "9:16", duration: int = 5, generate_audio: bool = True) -> str:
    """
    Fast, lower-cost draft mode of text_to_video for rapid ideation and prompt iteration.

    :param prompt: Descriptive text prompt for the video scene and motion.
    :param aspect_ratio: Video aspect ratio ('21:9', '2:1', '16:9', '4:3', '1:1', '3:4', '9:16').
    :param duration: Duration in seconds (5-20). Billed flat at $0.09/sec.
    :param generate_audio: Whether to generate synchronized native audio, no extra charge.
    """
    api = get_api()
    result = api.text_to_video_draft(prompt, aspect_ratio, duration, generate_audio)
    return json.dumps(result, indent=2)

@mcp.tool()
def image_to_video(prompt: str, image_url: str, aspect_ratio: str = "", resolution: str = "720p", duration: int = 5, generate_audio: bool = True) -> str:
    """
    Animate a static image into a video using FLUX 3.

    :param prompt: Text prompt guiding the animation.
    :param image_url: URL of the start-frame image.
    :param aspect_ratio: Video aspect ratio, optional ('21:9', '2:1', '16:9', '4:3', '1:1', '3:4', '9:16').
    :param resolution: '720p' or '1080p'. $0.25/sec at 720p, $0.42/sec at 1080p.
    :param duration: Duration in seconds (5-20), billed rounded up to the next second.
    :param generate_audio: Whether to generate synchronized native audio, no extra charge.
    """
    api = get_api()
    result = api.image_to_video(prompt, image_url, aspect_ratio or None, resolution, duration, generate_audio)
    return json.dumps(result, indent=2)

@mcp.tool()
def start_end_to_video(prompt: str, image_url: str, end_image_url: str, aspect_ratio: str = "", resolution: str = "720p", duration: int = 5, generate_audio: bool = True) -> str:
    """
    Generate a video transition between a start and end keyframe using FLUX 3.

    :param prompt: Text prompt describing the action/transformation connecting the two frames.
    :param image_url: URL of the start (first) keyframe image.
    :param end_image_url: URL of the end (last) keyframe image.
    :param aspect_ratio: Video aspect ratio, optional.
    :param resolution: '720p' or '1080p'. $0.25/sec at 720p, $0.42/sec at 1080p.
    :param duration: Duration in seconds (5-20), billed rounded up to the next second.
    :param generate_audio: Whether to generate synchronized native audio, no extra charge.
    """
    api = get_api()
    result = api.start_end_to_video(prompt, image_url, end_image_url, aspect_ratio or None, resolution, duration, generate_audio)
    return json.dumps(result, indent=2)

@mcp.tool()
def video_extend(prompt: str, video_url: str, aspect_ratio: str = "", resolution: str = "720p", duration: int = 5, generate_audio: bool = True) -> str:
    """
    Continue an existing video clip with new prompt-guided motion using FLUX 3.

    :param prompt: Text prompt describing the next action/scene development/camera movement.
    :param video_url: URL of the source clip to extend. Must be under 50MB and under 15 seconds.
    :param aspect_ratio: Video aspect ratio, optional.
    :param resolution: '720p' or '1080p'. $0.25/sec at 720p, $0.42/sec at 1080p.
    :param duration: Length of the extension in seconds (5-20), billed rounded up to the next second.
    :param generate_audio: Whether to generate synchronized native audio for the extension, no extra charge.
    """
    api = get_api()
    result = api.video_extend(prompt, video_url, aspect_ratio or None, resolution, duration, generate_audio)
    return json.dumps(result, indent=2)

@mcp.tool()
def video_extend_draft(prompt: str, video_url: str, aspect_ratio: str = "", duration: int = 5, generate_audio: bool = True) -> str:
    """
    Fast, lower-cost draft mode of video_extend for testing continuity and camera movement.

    :param prompt: Text prompt describing the continuation.
    :param video_url: URL of the source clip to extend. Must be under 50MB and under 15 seconds.
    :param aspect_ratio: Video aspect ratio, optional.
    :param duration: Length of the draft extension in seconds (5-20). Billed flat at $0.09/sec.
    :param generate_audio: Whether to generate synchronized native audio, no extra charge.
    """
    api = get_api()
    result = api.video_extend_draft(prompt, video_url, aspect_ratio or None, duration, generate_audio)
    return json.dumps(result, indent=2)

@mcp.tool()
def video_upscale(video_url: str, prompt: str = "", upscale_factor: float = 0, creativity: int = 0) -> str:
    """
    Upscale any video beyond its native resolution using FLUX 3 Video Upscaler.

    :param video_url: URL of the source video to upscale.
    :param prompt: Optional text prompt describing the desired enhancement direction.
    :param upscale_factor: Optional multiplier (1-4) controlling output resolution scaling.
    :param creativity: 0 = Precise ($1.43/run), 1 = Creative ($2.00/run, more detail reconstruction).
    """
    api = get_api()
    result = api.video_upscale(video_url, prompt or None, upscale_factor or None, creativity)
    return json.dumps(result, indent=2)

@mcp.tool()
def upload_file(file_path: str) -> str:
    """
    Upload a local file (image or video) to MuAPI for use in generation tasks.

    :param file_path: Local path to the file.
    """
    api = get_api()
    result = api.upload_file(file_path)
    return json.dumps(result, indent=2)

@mcp.tool()
def get_task_status(request_id: str) -> str:
    """
    Check the status and get results of a generation task.

    :param request_id: The ID returned from a generation tool call.
    """
    api = get_api()
    result = api.get_result(request_id)
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    mcp.run()
