# AI-Based Smart Traffic Management System using YOLOv7

An intelligent traffic management system that dynamically adjusts traffic signal timings using computer vision and deep learning. The system detects vehicles from traffic images using **YOLOv7**, estimates lane-wise traffic density, and allocates green signal durations based on real-time congestion.

---

## Overview

Urban traffic congestion leads to increased travel time, fuel consumption, and pollution. Conventional traffic lights operate on fixed timing and cannot respond to changing traffic conditions.

This project introduces an AI-driven adaptive traffic signal control system that detects vehicles using the YOLOv7 object detection model and dynamically updates signal timings according to traffic density.

The project combines computer vision, deep learning, and traffic simulation to demonstrate an intelligent traffic management solution for smart cities.

---

## Features

- Vehicle detection using YOLOv7
- Multi-class vehicle recognition
- Lane-wise vehicle counting
- Traffic density estimation
- Adaptive traffic signal timing
- Four-way traffic intersection simulation
- Graphical traffic visualization
- Modular Python implementation

---

## System Workflow

Traffic Images

↓

Image Preprocessing

↓

YOLOv7 Vehicle Detection

↓

Vehicle Classification

↓

Vehicle Counting

↓

Traffic Density Estimation

↓

Adaptive Signal Timing

↓

Traffic Simulation

---

## Technologies Used

### Languages

- Python

### Libraries

- OpenCV
- NumPy
- Pygame
- YOLOv7
- Deep Learning

### Concepts

- Computer Vision
- Object Detection
- Artificial Intelligence
- Traffic Density Estimation
- Intelligent Transportation Systems

---

## Repository Structure

```
Smart-Traffic-Management/

│

├── docs/

│ ├── Research_Paper.pdf

│ ├── Architecture.png

│ └── Workflow.png

│

├── images/

│ ├── Vehicle_Detection.png

│ ├── Simulation.png

│ ├── GUI.png

│ └── Results.png

│

source/
├── vehicle_detection.py
├── image_processor.py
├── simulation.py
├── config.py
└── main.py

│

├── videos/

│ └── Demo.mp4

│

└── README.md
```

---

## Methodology

The system processes traffic images captured from road intersections.

Each image is preprocessed and passed to the YOLOv7 detection model.

Detected vehicles are classified into multiple categories including:

- Car
- Bus
- Truck
- Motorcycle
- Auto-rickshaw

Vehicle counts are then used to estimate lane-wise traffic density.

An adaptive signal control algorithm computes the optimal green signal duration for each lane.

Finally, the complete traffic intersection is simulated using Pygame to visualize adaptive signal switching.

---

## Results

### Vehicle Detection Performance

| Metric | Value |
|---------|-------|
| Accuracy | **97.8%** |
| Precision | **95.0%** |
| Recall | **98.0%** |
| F1 Score | **96.5%** |
| mAP@50 | **97.6%** |

---

## Vehicle Types Detected

- Car
- Bus
- Truck
- Motorcycle
- Auto-rickshaw

---

## Sample Output

### Vehicle Detection

<img width="339" height="375" alt="output_1" src="https://github.com/user-attachments/assets/76dcb61d-a689-4aa4-9e3d-7f68483b5584" />


### Traffic Simulation

<img width="718" height="406" alt="image" src="https://github.com/user-attachments/assets/09d2658f-d2f1-4989-9725-e20610a87029" />

---

## Future Improvements

- Real-time CCTV integration
- Multi-camera traffic analysis
- Emergency vehicle priority
- Reinforcement Learning based signal optimization
- Cloud-based monitoring dashboard
- Edge AI deployment
- IoT-enabled smart intersections

---

## Research Publication

This work has been prepared as a research manuscript titled:

**YOLOv7-Based Vehicle Detection for Adaptive Traffic Signal Control**

*(IEEE Submission)*

---

## Author

**Malireddy Sravya Sri**

Electronics and Communication Engineering

Embedded Systems | Computer Vision | Intelligent Transportation Systems

LinkedIn

https://www.linkedin.com/in/sravya-sri-reddy-048b87378
