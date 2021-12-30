from PyQt5.QtWidgets import QApplication
from bigapp.uis.bdialog import BDialog
import sys

class BApp(QApplication):
    def _init_(self):
        super(BApp,self)._init_(sys.argv)
        
        self.dlg=BDialog()
        self.dlg.show()
        