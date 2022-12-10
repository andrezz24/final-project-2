from controller import *


def main():
    """
    Method that runs the controller file.
    """
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec_()


if __name__ == '__main__':
    main()