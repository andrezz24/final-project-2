from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # white keys
        self.pushButton.clicked.connect(lambda: self.white_key_pressedF())
        self.pushButton_2.clicked.connect(lambda: self.white_key_pressedG())
        self.pushButton_3.clicked.connect(lambda: self.white_key_pressedA())
        self.pushButton_4.clicked.connect(lambda: self.white_key_pressedB())
        self.pushButton_5.clicked.connect(lambda: self.white_key_pressedC())
        self.pushButton_6.clicked.connect(lambda: self.white_key_pressedD())
        self.pushButton_7.clicked.connect(lambda: self.white_key_pressedE())
        self.pushButton_8.clicked.connect(lambda: self.white_key_pressedF())
        self.pushButton_9.clicked.connect(lambda: self.white_key_pressedG())
        self.pushButton_10.clicked.connect(lambda: self.white_key_pressedA())
        self.pushButton_11.clicked.connect(lambda: self.white_key_pressedB())
        self.pushButton_12.clicked.connect(lambda: self.white_key_pressedC())
        self.pushButton_13.clicked.connect(lambda: self.white_key_pressedD())
        self.pushButton_14.clicked.connect(lambda: self.white_key_pressedE())
        self.pushButton_15.clicked.connect(lambda: self.white_key_pressedF())
        self.pushButton_16.clicked.connect(lambda: self.white_key_pressedG())
        self.pushButton_17.clicked.connect(lambda: self.white_key_pressedA())
        self.pushButton_18.clicked.connect(lambda: self.white_key_pressedB())
        self.pushButton_19.clicked.connect(lambda: self.white_key_pressedC())
        self.pushButton_20.clicked.connect(lambda: self.white_key_pressedD())

        # black keys (sharps)
        self.pushButton_21.clicked.connect(lambda: self.black_key_pressedG_sharp())
        self.pushButton_22.clicked.connect(lambda: self.black_key_pressedA_sharp())
        self.pushButton_23.clicked.connect(lambda: self.black_key_pressedB_sharp())
        self.pushButton_24.clicked.connect(lambda: self.black_key_pressedD_sharp())
        self.pushButton_25.clicked.connect(lambda: self.black_key_pressedE_sharp())
        self.pushButton_26.clicked.connect(lambda: self.black_key_pressedG_sharp())
        self.pushButton_27.clicked.connect(lambda: self.black_key_pressedA_sharp())
        self.pushButton_28.clicked.connect(lambda: self.black_key_pressedB_sharp())
        self.pushButton_29.clicked.connect(lambda: self.black_key_pressedD_sharp())
        self.pushButton_30.clicked.connect(lambda: self.black_key_pressedE_sharp())
        self.pushButton_31.clicked.connect(lambda: self.black_key_pressedG_sharp())
        self.pushButton_32.clicked.connect(lambda: self.black_key_pressedA_sharp())
        self.pushButton_33.clicked.connect(lambda: self.black_key_pressedB_sharp())
        self.pushButton_34.clicked.connect(lambda: self.black_key_pressedD_sharp())
        self.pushButton_35.clicked.connect(lambda: self.black_key_pressedE_sharp())

    def white_key_pressedF(self) -> None:
        """
        Method that changes label to F note
        """
        self.label.setText('F')

    def white_key_pressedG(self) -> None:
        """
        Method that changes label to G note
        """
        self.label.setText('G')

    def white_key_pressedA(self) -> None:
        """
        Method that changes label to A note
        """
        self.label.setText('A')

    def white_key_pressedB(self) -> None:
        """
        Method that changes label to B note
        """
        self.label.setText('B')

    def white_key_pressedC(self) -> None:
        """
        Method that changes label to C note
        """
        self.label.setText('C')

    def white_key_pressedD(self) -> None:
        """
        Method that changes label to D note
        """
        self.label.setText('D')

    def white_key_pressedE(self) -> None:
        """
        Method that changes label to E note
        """
        self.label.setText('E')

    def black_key_pressedD_sharp(self) -> None:
        """
        Method that changes label to #D note
        """
        self.label.setText('#D')

    def black_key_pressedE_sharp(self) -> None:
        """
        Method that changes label to #E note
        """
        self.label.setText('#E')

    def black_key_pressedG_sharp(self) -> None:
        """
        Method that changes label to #G note
        """
        self.label.setText('#G')

    def black_key_pressedA_sharp(self) -> None:
        """
        Method that changes label to #A note
        """
        self.label.setText('#A')

    def black_key_pressedB_sharp(self) -> None:
        """
        Method that changes label to #B note
        """
        self.label.setText('#B')
