from qgis.PyQt.QtCore import QObject
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.PyQt.QtGui import QIcon, QColor
from qgis.core import (
    QgsProject,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform
)
from qgis.gui import QgsMapToolEmitPoint, QgsVertexMarker
from qgis.utils import iface

class CoordinatePicker(QObject):
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.action = None
        self.tool = None
        self.marker = None

    def initGui(self):
        """Add button to QGIS toolbar"""
        icon_path = ":/plugins/coordinate_picker/icon.png"
        self.action = QAction(QIcon(icon_path), "Coordinate Picker", self.iface.mainWindow())
        self.action.setStatusTip("Click on the map to get coordinates")
        self.action.triggered.connect(self.activate_tool)

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Coordinate Picker", self.action)

    def unload(self):
        """Remove plugin from QGIS interface"""
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&Coordinate Picker", self.action)

    def activate_tool(self):
        """Activate coordinate picking mode"""
        self.tool = PointClickTool(self.canvas, self.iface, self)
        self.canvas.setMapTool(self.tool)
        QMessageBox.information(
            self.iface.mainWindow(),
            "Coordinate Picker",
            "🖱️ Click anywhere on the map to get coordinates."
        )

    def show_marker(self, point):
        """Add a red marker where user clicked"""
        if self.marker:
            self.canvas.scene().removeItem(self.marker)

        marker = QgsVertexMarker(self.canvas)
        marker.setCenter(point)
        marker.setColor(QColor("red"))
        marker.setIconSize(10)
        marker.setIconType(QgsVertexMarker.ICON_CIRCLE)
        marker.setPenWidth(2)
        self.marker = marker


class PointClickTool(QgsMapToolEmitPoint):
    """Custom map tool to pick coordinates"""
    def __init__(self, canvas, iface, plugin):
        super().__init__(canvas)
        self.canvas = canvas
        self.iface = iface
        self.plugin = plugin

    def canvasReleaseEvent(self, event):
        """Triggered when user clicks on map"""
        point = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())

        # Convert to WGS84 (EPSG:4326)
        crs_src = self.canvas.mapSettings().destinationCrs()
        crs_dest = QgsCoordinateReferenceSystem("EPSG:4326")
        transform = QgsCoordinateTransform(crs_src, crs_dest, QgsProject.instance())
        wgs_point = transform.transform(point)

        lat = round(wgs_point.y(), 6)
        lon = round(wgs_point.x(), 6)

        # Show marker on map
        self.plugin.show_marker(point)

        # Copy to clipboard
        try:
            import pyperclip
            pyperclip.copy(f"{lat}, {lon}")
            copied_msg = "\n✅ Copied to clipboard."
        except Exception:
            copied_msg = ""

        # Show popup message
        QMessageBox.information(
            self.iface.mainWindow(),
            "Coordinate Picker",
            f"Latitude: {lat}\nLongitude: {lon}{copied_msg}"
        )