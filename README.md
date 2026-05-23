# 🪖 Helmet Detection using YOLOv8

A real-time **Helmet Detection System** built with Ultralytics YOLOv8. This project can detect helmets in both **videos** and **images**.

![Project Demo](demo.png) <!-- Replace with your screenshot later -->

## 📋 Project Overview

This project uses a custom-trained YOLOv8 model (`best.pt`) to detect whether a person is wearing a helmet or not.

### Features
- Video-based helmet detection
- Image-based helmet detection
- Frame extraction from video for dataset creation
- Bounding box visualization with class labels

## 📁 Project Structure
helmet-detection/
├── best.pt                 # Trained YOLOv8 model
├── main1.py                # Main script - Video Detection
├── main2.py                # Image Detection
├── img.py                  # Extract frames from video
├── coco1.txt               # Class names file
├── testvid.mp4             # Test video
├── test6.jpg               # Test image
├── he2.mp4                 # Source video
└── Images/                 # Output folder for extracted frames



## 🛠️ Technologies Used

- **Python**
- **YOLOv8** (Ultralytics)
- **OpenCV**
- **cvzone**
- **Pandas**

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Israr1822/helmet-detection.git
cd helmet-detection
