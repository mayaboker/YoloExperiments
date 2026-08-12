from pathlib import Path

SUPPORTED_IMAGE_SUFFIXES = {".bmp", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}
SUPPORTED_VIDEO_SUFFIXES = {".avi", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".webm"}


def discover_media(source: str | Path) -> list[Path]:
    source_path = Path(source)
    if not source_path.exists():
        raise FileNotFoundError(f"Data source does not exist: {source_path}")
    candidates = [source_path] if source_path.is_file() else source_path.rglob("*")
    media = sorted(
        path
        for path in candidates
        if path.suffix.lower() in SUPPORTED_IMAGE_SUFFIXES | SUPPORTED_VIDEO_SUFFIXES
    )
    if not media:
        raise ValueError(f"No supported images or videos found in: {source_path}")
    return media


def is_image(path: str | Path) -> bool:
    return Path(path).suffix.lower() in SUPPORTED_IMAGE_SUFFIXES


def is_video(path: str | Path) -> bool:
    return Path(path).suffix.lower() in SUPPORTED_VIDEO_SUFFIXES
