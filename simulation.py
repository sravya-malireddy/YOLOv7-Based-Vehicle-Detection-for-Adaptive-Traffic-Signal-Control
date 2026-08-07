from dataclasses import dataclass
import random

import pygame

from config import (
    FPS,
    MAX_GREEN_SECONDS,
    MIN_GREEN_SECONDS,
    VEHICLE_COLORS,
    VEHICLE_TYPES,
    WINDOW_SIZE,
    YELLOW_SECONDS,
)

ROAD_COLOR = (50, 50, 54)
GRASS_COLOR = (55, 125, 60)
LINE_COLOR = (225, 225, 225)

RED = (220, 55, 55)
GREEN = (40, 220, 70)
YELLOW = (255, 200, 0)


@dataclass
class Vehicle:
    direction: int
    kind: str
    position: float
    lane: int
    crossed: bool = False

    @property
    def speed(self) -> float:
        return {
            "car": 120,
            "bus": 80,
            "truck": 75,
        }[self.kind]


class TrafficSimulation:

    DIRECTIONS = ("North", "East", "South", "West")

    SIGNAL_POSITIONS = (
        (500, 15),
        (955, 355),
        (500, 755),
        (20, 355),
    )

    def __init__(self, detected_counts: dict[str, int] | None = None):

        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Smart Traffic Management")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("Arial", 22)
        self.title_font = pygame.font.SysFont("Arial", 30, bold=True)

        self.active_signal = 0
        self.yellow_signal = False

        self.remaining_time = self.green_time(detected_counts or {})

        self.vehicles: list[Vehicle] = []

        self.spawn_timer = 0.0

        self.running = True

    @staticmethod
    def green_time(counts: dict[str, int]) -> float:

        total = sum(counts.values())

        duration = MIN_GREEN_SECONDS + total * 2

        return max(
            MIN_GREEN_SECONDS,
            min(MAX_GREEN_SECONDS, duration),
        )

    def spawn_vehicle(self):

        direction = random.randrange(4)

        lane_count = sum(
            1
            for vehicle in self.vehicles
            if vehicle.direction == direction and not vehicle.crossed
        )

        if lane_count < 7:

            self.vehicles.append(
                Vehicle(
                    direction=direction,
                    kind=random.choice(VEHICLE_TYPES),
                    position=0,
                    lane=lane_count,
                )
            )

    def update(self, dt: float):

        self.spawn_timer += dt

        if self.spawn_timer >= 0.9:
            self.spawn_vehicle()
            self.spawn_timer = 0

        self.remaining_time -= dt

        if self.remaining_time <= 0:

            if self.yellow_signal:

                self.yellow_signal = False

                self.active_signal = (
                    self.active_signal + 1
                ) % len(self.DIRECTIONS)

                self.remaining_time = MIN_GREEN_SECONDS

            else:

                self.yellow_signal = True
                self.remaining_time = YELLOW_SECONDS

        for vehicle in self.vehicles:

            move = (
                vehicle.direction == self.active_signal
                and not self.yellow_signal
            )

            if move or vehicle.position < 210:
                vehicle.position += vehicle.speed * dt

            if vehicle.position > 480:
                vehicle.crossed = True

        self.vehicles = [
            vehicle
            for vehicle in self.vehicles
            if not vehicle.crossed
        ]

    def vehicle_rect(self, vehicle: Vehicle) -> pygame.Rect:

        center_x = WINDOW_SIZE[0] // 2
        center_y = WINDOW_SIZE[1] // 2

        offset = 24 + vehicle.lane * 24

        position = vehicle.position

        if vehicle.direction == 0:
            return pygame.Rect(
                center_x - offset,
                -55 + position,
                18,
                38,
            )

        if vehicle.direction == 1:
            return pygame.Rect(
                WINDOW_SIZE[0] + 55 - position,
                center_y - offset,
                38,
                18,
            )

        if vehicle.direction == 2:
            return pygame.Rect(
                center_x + offset,
                WINDOW_SIZE[1] + 55 - position,
                18,
                38,
            )

        return pygame.Rect(
            -55 + position,
            center_y + offset,
            38,
            18,
        )

    def draw(self):

        self.screen.fill(GRASS_COLOR)

        width, height = WINDOW_SIZE

        pygame.draw.rect(
            self.screen,
            ROAD_COLOR,
            (0, height // 2 - 105, width, 210),
        )

        pygame.draw.rect(
            self.screen,
            ROAD_COLOR,
            (width // 2 - 105, 0, 210, height),
        )

        pygame.draw.rect(
            self.screen,
            LINE_COLOR,
            (width // 2 - 2, 0, 4, height),
        )

        pygame.draw.rect(
            self.screen,
            LINE_COLOR,
            (0, height // 2 - 2, width, 4),
        )

        for index, direction in enumerate(self.DIRECTIONS):

            if index == self.active_signal:

                color = (
                    YELLOW
                    if self.yellow_signal
                    else GREEN
                )

            else:

                color = RED

            label = self.font.render(
                f"{direction}: {int(self.remaining_time)}s",
                True,
                color,
            )

            self.screen.blit(
                label,
                self.SIGNAL_POSITIONS[index],
            )

        for vehicle in self.vehicles:

            pygame.draw.rect(
                self.screen,
                VEHICLE_COLORS[vehicle.kind],
                self.vehicle_rect(vehicle),
                border_radius=4,
            )

        title = self.title_font.render(
            "SMART TRAFFIC MANAGEMENT",
            True,
            (255, 255, 255),
        )

        self.screen.blit(title, (390, 350))

        pygame.display.flip()

    def run(self):

        while self.running:

            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            self.update(dt)

            self.draw()

        pygame.quit()
