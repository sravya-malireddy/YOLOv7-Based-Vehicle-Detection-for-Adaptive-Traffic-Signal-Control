"""
Main entry point for the AI-Based Smart Traffic Management System.

Workflow:
1. Load traffic images.
2. Detect vehicles using YOLOv7.
3. Count detected vehicles.
4. Save annotated output images.
5. Launch the adaptive traffic signal simulation.
"""

from config import (
    CLASS_NAMES,
    IMAGE_DIR,
    MODEL_CONFIG,
    MODEL_WEIGHTS,
    OUTPUT_DIR,
)

from image_processor import (
    get_image_paths,
    read_image,
    save_image,
)

from vehicle_detection import (
    VehicleDetector,
    count_by_type,
)

from simulation import TrafficSimulation


def process_images() -> dict[str, int]:
    """
    Detect vehicles from all traffic images.

    Returns:
        Dictionary containing the total number of detected
        cars, buses and trucks.
    """

    detector = VehicleDetector(
        MODEL_CONFIG,
        MODEL_WEIGHTS,
        CLASS_NAMES,
    )

    total_counts = {
        "car": 0,
        "bus": 0,
        "truck": 0,
    }

    image_paths = get_image_paths(IMAGE_DIR)

    if not image_paths:
        raise FileNotFoundError(
            f"No images found in '{IMAGE_DIR}'."
        )

    print("\nProcessing Images\n")

    for image_path in image_paths:

        image = read_image(image_path)

        if image is None:
            print(f"Skipped unreadable image: {image_path.name}")
            continue

        detections = detector.detect(image)

        counts = count_by_type(detections)

        for vehicle in total_counts:
            total_counts[vehicle] += counts[vehicle]

        annotated_image = detector.draw(image, detections)

        output_path = OUTPUT_DIR / f"detected_{image_path.name}"

        save_image(output_path, annotated_image)

        print(
            f"{image_path.name} -> "
            f"Cars: {counts['car']}, "
            f"Buses: {counts['bus']}, "
            f"Trucks: {counts['truck']}"
        )

    return total_counts


def main() -> None:
    """
    Execute the complete traffic management pipeline.
    """

    try:
        vehicle_counts = process_images()

        print("\nVehicle Detection Summary")
        print("-------------------------")

        for vehicle, count in vehicle_counts.items():
            print(f"{vehicle.capitalize():<8}: {count}")

    except FileNotFoundError as error:

        print(f"\nDetection skipped: {error}")

        vehicle_counts = {
            "car": 0,
            "bus": 0,
            "truck": 0,
        }

    simulation = TrafficSimulation(vehicle_counts)

    simulation.run()


if __name__ == "__main__":
    main()
