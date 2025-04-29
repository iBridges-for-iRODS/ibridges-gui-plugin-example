import sys
import pathlib
import PySide6.QtWidgets

from ibridgesguicontrib.exampleplugin.tabExample import Ui_tabExample

class ExampleTab(PySide6.QtWidgets.QWidget, Ui_tabExample):
    """Example tab for the iBridges GUI."""
    name = "UU example tab"    

    def __init__(self, session, app_name):
        """Initialize the example tab."""      
        super().__init__()
        super().setupUi(self)
        self.session = session
        self.fill_info()

    def fill_info(self):

        self.server.setText(self.session.irods_session.host)
        self.port.setText(str(self.session.irods_session.port))
        self.home.setText(self.session.home)
        self.user.setText(self.session.irods_session.username)
