from HomeWork.page.tool import ManageTool

class TestTool:
    def setup(self):
        self.tool=ManageTool(reuse=True)
    def test_add_member(self):
        pass

    def test_sync_contact(self):
        pass

    def test_group_message(self):
        pass

    def test_add_materials(self):
        self.tool.add_materials().add_image("C:/Users/liming.wu/Pictures/Screenshots/Screenshot.png")
