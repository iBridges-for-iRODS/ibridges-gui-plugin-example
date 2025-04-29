import pathlib
import PySide6.QtWidgets
from exampleplugin.ui_files.tabExample import Ui_tabExample

class ExampleTab(PySide6.QtWidgets.QWidget, Ui_tabExample):
    """Example tab for the iBridges GUI."""
    def __init__(self, session):
        """Initialize the example tab."""      
        super().__init__()
        if getattr(sys, "frozen", False) or ("__compiled__" in globals()):
            super().setupUi(self)
        else:
            UI_FILE_DIR = pathlib.Path("ui_files")
            load_ui(UI_FILE_DIR / "tabExample.ui", self)

    #def _initialize_irods_model(self, treeView):
    #    self.irodsmodel = IrodsModel(treeView)
    #    treeView.setModel(self.irodsmodel)

    #    home_coll_str = utils.path.IrodsPath(
    #        '/', self.context.irods_connector.zone, 'home')
    #    irods_root_coll = self.ienv_dict.get('irods_home', home_coll_str)
    #    
    #    self.irodsmodel.setHorizontalHeaderLabels([irods_root_coll,
    #                                          'Level', 'iRODS ID',
    #                                          'parent ID', 'type'])
    #    treeView.expanded.connect(self.irodsmodel.refresh_subtree)
    #    treeView.clicked.connect(self.irodsmodel.refresh_subtree)
    #    self.irodsmodel.init_tree()

    #    treeView.setHeaderHidden(True)
    #    treeView.header().setDefaultSectionSize(180)
    #    treeView.setColumnHidden(1, True)
    #    treeView.setColumnHidden(2, True)
    #    treeView.setColumnHidden(3, True)
    #    treeView.setColumnHidden(4, True)
    

    #def _get_paths_from_trees(self, treeView, local=False):
    #    index = treeView.selectedIndexes()[0]
    #    if local:
    #        path = self.localmodel.filePath(index)
    #    else:
    #        path = self.irodsmodel.irods_path_from_tree_index(index)
    #    return(index, path)

    def treeFunction(self):
        index, path = self._get_paths_from_trees(self.irodsTreeView)
        self.textField.setText(path)

        return(index, path)
