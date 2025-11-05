def classFactory(iface):
    from .coordinate_picker import CoordinatePicker
    return CoordinatePicker(iface)