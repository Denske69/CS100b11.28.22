from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("PyQt5")

        labels = ['first name', 'last name', 'email']
        textboxes = {}

        layout = QFormLayout()
        self.setLayout(layout)

        for l in labels:
            #now add a label and a textbox,
            # and also hold the textbox in the dictionary so we can use it later
            txt = QLineEdit()
            layout.addRow(l, txt)
            textboxes[l] = txt

        #finally, add a button
        b = QPushButton("Submit")
        layout.addWidget(b)

        self.show()

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()
    