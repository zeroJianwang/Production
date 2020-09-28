import sys
from PyQt5.QtWidgets import *
class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self._InitUI()
        pass
    def _InitUI(self):
        hLayout = QHBoxLayout()
        vLayout = QVBoxLayout()

        btnTimeOutput = QPushButton(self.tr('Stander Time Output'))
        btnAddNew = QPushButton(self.tr('Add new product'))
        btnDailyInput = QPushButton(self.tr('Daily intput'))
        btnDataQuery = QPushButton(self.tr('Data Query'))

        hLayout.setSpacing(30)
        hLayout.addWidget(btnTimeOutput)
        hLayout.addWidget(btnAddNew)
        hLayout.addWidget(btnDailyInput)
        hLayout.addWidget(btnDataQuery)

        vLayout.addLayout(hLayout)

        self.setLayout(vLayout)
