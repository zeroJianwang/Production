import sys
from PyQt5.QtWidgets import *
from MainWindow import MainPage
class DlgLogin(QWidget):
    def __init__(self):
        super().__init__()

        self.__InitUI()
        self.__Connection()

        pass
    def __InitUI(self):
        self.setWindowTitle(self.tr('Lonin'))
        Hlayout1 = QHBoxLayout()
        LbUser = QLabel(self.tr('Username'))
        lEditUser = QLineEdit()
        Hlayout1.setSpacing(5)
        Hlayout1.addWidget(LbUser)
        Hlayout1.addWidget(lEditUser)

        Hlayout2 = QHBoxLayout()
        LbPasswd = QLabel(self.tr('Passwd'))
        lEdtPasswd = QLineEdit()
        Hlayout2.setSpacing(5)
        Hlayout2.addWidget(LbPasswd)
        Hlayout2.addWidget(lEdtPasswd)

        Hlayout3 = QHBoxLayout()
        self.btnLogin = QPushButton(self.tr('Login'))
        self.btnCancel = QPushButton(self.tr('Cancel'))
        Hlayout3.setSpacing(5)
        Hlayout3.addWidget(self.btnLogin)
        Hlayout3.addWidget(self.btnCancel)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.setSpacing(15)
        self.setLayout(Vlayout)
        pass
    def OnBtnLoggin(self):
        QMessageBox.warning(self,'w','Login Seccess')
        gLoginPage.hide()
        gMainPage.show()
        pass
    def OnBtnCancel(self):
        QMessageBox.warning(self,'w','cacel')
        pass
    def __Connection(self):
        self.btnLogin.clicked.connect(self.OnBtnLoggin)
        self.btnCancel.clicked.connect(self.OnBtnCancel)
        pass
    pass
