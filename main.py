import sys
from PyQt5.QtWidgets import QApplication
from DlgLogin import *
from MainWindow import *
from DailyInput import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gLoginPage = DlgLogin()
    DailyPage = DailyInput()
    DailyPage.show()
    sys.exit(app.exec_())
