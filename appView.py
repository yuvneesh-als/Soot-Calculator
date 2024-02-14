import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from calculation import *


def absorbanceToPercentage(absorbance: str) -> None:
    """Set the value in txt_prcnt to soot percentage obtained from given absorbance in txt_abs"""
    percentage = getSootPercentage(float(absorbance))


def launch():
    """Launches the app"""
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    window = loader.load(r"./views/home.ui", None)

    window.btn_convert.clicked.connect(lambda: window.txt_prcnt.setText(str(getSootPercentage(float(window.txt_abs.toPlainText())))))

    window.show()
    app.exec_()


if __name__ == "__main__":
    launch()
