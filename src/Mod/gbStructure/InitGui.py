# gbStructure gui init module
# (c) 2001 Juergen Riegel LGPL

class gbStructureWorkbench (Workbench):
    "gbStructure workbench object"
    MenuText = "gbStructure"
    ToolTip = "gbStructure workbench"

    def Initialize(self):
        # load the module
        import gbStructureGui

    def GetClassName(self):
        return "gbStructureGui::Workbench"

Gui.addWorkbench(gbStructureWorkbench())
