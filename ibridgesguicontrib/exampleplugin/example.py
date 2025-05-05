"""Example tab class to extend the iBridgesGUI app."""
import logging
import PySide6.QtWidgets

from ibridges.session import Session
from ibridgesguicontrib.exampleplugin.tabExample import Ui_tabExample


class ExampleTab(PySide6.QtWidgets.QWidget, Ui_tabExample):
    """Example tab for the iBridges GUI."""

    name = "UU example tab"

    def __init__(self, session: Session, app_name: str, logger: logging.Logger):
        """Initialize the example tab."""
        super().__init__()
        super().setupUi(self)
        self.logger = logger
        self.logger.info("Init third party tab: %s", self.name)
        self.session = session
        self.fill_info()

    def fill_info(self):
        """Retrieve info from session and print it to tab elements."""
        self.server.setText(self.session.irods_session.host)
        self.port.setText(str(self.session.irods_session.port))
        self.home.setText(self.session.home)
        self.user.setText(self.session.irods_session.username)
