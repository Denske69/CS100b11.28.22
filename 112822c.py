from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("Class List")

        labels = ['first name', 'last name', 'email']
        textboxes = {}

        layout = QHBoxLayout()
        self.setLayout(layout)

        for l in labels:
            #add the label
            lbl = QLabel(l)
            layout.addWidget(lbl)

            #now add a textbox for that label,
            # and also hold it in the dictionary so we can use it later
            txt = QLineEdit()
            layout.addWidget(txt)
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