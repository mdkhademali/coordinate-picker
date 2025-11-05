## Coordinate Picker for QGIS

![QGIS Plugin](https://img.shields.io/badge/QGIS-Plugin-brightgreen?logo=qgis)
![Downloads](https://img.shields.io/badge/Downloads-100%2B-blue)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-yellow)
![Version](https://img.shields.io/badge/Version-1.0-orange)

---

<p align="center">
  <img src="icon.png" alt="Coordinate Picker Icon" width="80" height="80">
</p>

## Overview

**Coordinate Picker** is a lightweight QGIS plugin that lets you quickly pick map coordinates by clicking on the canvas.  
Each click drops a marker and displays the latitude and longitude instantly — also copied to your clipboard automatically.  

Perfect for surveyors, mappers, GIS students, or anyone who needs quick coordinate collection without extra hassle.

---

## Features

* Simple and clean toolbar button  
* One-click coordinate capture  
* Real-time marker placement  
* Coordinates auto-copied to clipboard  
* Works in any CRS (EPSG:4326 by default)  
* QGIS 3.x compatible  

---

## Installation

### Option 1: Manual Install
1. Download the latest release or clone this repository:
   ```bash
   git clone https://github.com/mdkhademali/coordinate-picker.git
   ```
2. Copy the entire folder to:
   ```
   C:\Users\<your_user>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\
   ```
3. Restart QGIS  
4. Go to **Plugins → Manage and Install Plugins → Installed**  
5. Enable **Coordinate Picker**

### Option 2: ZIP Installation
1. Download ZIP → `coordinate-picker.zip`  
2. In QGIS: **Plugins → Manage and Install Plugins → Install from ZIP...**  
3. Browse to the ZIP file → Click **Install Plugin**

---

## Usage

1. Launch QGIS  
2. Click on the **Coordinate Picker** icon in the toolbar  
3. Click anywhere on the map  
4. A marker appears and a message box shows:
   ```
   Latitude: 23.8103
   Longitude: 90.4125
   ```
5. The coordinates are automatically copied to clipboard  

---

## Requirements

| Component | Version |
|------------|----------|
| **QGIS** | 3.0 or higher |
| **Python** | 3.10+ |
| **PyQt5** | Installed with QGIS |
| **Operating System** | Windows / Linux / macOS |

---

## Future Plans

- Save multiple coordinates to CSV  
- CRS selection panel  
- Coordinate copy in multiple formats  
- Floating info panel  

---

## Contributing

Pull requests are welcome!  
If you find any issue, feel free to open an **Issue** on GitHub.

© mdkhademali
