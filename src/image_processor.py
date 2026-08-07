from pathlib import Path

import cv2


SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
}


def get_image_paths(folder: Path) -> list[Path]:
    """Return all supported image files from a folder."""

    if not folder.exists():
        return []

    return sorted(
        file
        for file in folder.iterdir()
        if file.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def read_image(image_path: Path):
    """Read an image using OpenCV."""

    return cv2.imread(str(image_path))


def save_image(output_path: Path, image) -> None:
    """Save an image to the output directory."""

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    success = cv2.imwrite(
        str(output_path),
        image,
    )

    if not success:
        raise OSError(
            f"Unable to save image: {output_path}"
        )
