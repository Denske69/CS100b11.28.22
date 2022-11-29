from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("PyQt5")

        layout = QHBoxLayout()
        self.setLayout(layout)
        b = QLabel("Oingo")
        layout.addWidget(b)
        b = QLabel("Boingo")
        layout.addWidget(b)

        self.show()

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()