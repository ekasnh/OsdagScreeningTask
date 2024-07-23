import FreeCAD
import FreeCADGui
import Part

def generate_prism(length, width, height):
    doc = FreeCAD.newDocument("Prism")
    box = doc.addObject("Part::Box", "Box")
    box.Length = length
    box.Width = width
    box.Height = height
    doc.recompute()
    return doc

if __name__ == "__main__":
    length = 40.0
    width = 20.0
    height = 100.0
    generate_prism(length, width, height)
    if not FreeCADGui.isActiveDocument():
        FreeCADGui.showMainWindow()
