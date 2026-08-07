from pathlib import Path

# ------------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_CONFIG = BASE_DIR / "models" / "yolov7.cfg"
MODEL_WEIGHTS = BASE_DIR / "models" / "yolov7.weights"
CLASS_NAMES = BASE_DIR / "models" / "coco.names"

IMAGE_DIR = BASE_DIR / "dataset" / "test_images"
OUTPUT_DIR = BASE_DIR / "output" / "detected_images"

# ------------------------------------------------------------------
# YOLO Configuration
# ------------------------------------------------------------------

CONFIDENCE_THRESHOLD = 0.50
NMS_THRESHOLD = 0.40

# ------------------------------------------------------------------
# Simulation Settings
# ------------------------------------------------------------------

WINDOW_SIZE = (1200, 800)
FPS = 60

SIMULATION_SECONDS = 300

MIN_GREEN_SECONDS = 10
MAX_GREEN_SECONDS = 60
YELLOW_SECONDS = 5

# ------------------------------------------------------------------
# Vehicle Settings
# ------------------------------------------------------------------

VEHICLE_TYPES = (
    "car",
    "bus",
    "truck",
)

VEHICLE_COLORS = {
    "car": (45, 130, 255),
    "bus": (255, 190, 40),
    "truck": (220, 75, 70),
}
