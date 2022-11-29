from PyQt6.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(100,100,200,50)
        self.setWindowTitle("PyQt5")

        labels = ['first name', 'last name', 'email']
        textboxes = {}

        layout = QGridLayout()
        self.setLayout(layout)

        row = 0
        for l in labels:
            #add the label
            lbl = QLabel(l)
            layout.addWidget(lbl, row, 0)

            #now add a textbox for that label,
            # and also hold it in the dictionary so we can use it later
            txt = QLineEdit()
            layout.addWidget(txt, row, 1)
            textboxes[l] = txt

            row = row + 1

        #finally, add a button
        b = QPushButton("Submit")
        #we want this button to span both columns, so we'll use a different addWidget
        #addWidget(QWidget, row, column, rowspan, column span)
        layout.addWidget(b, len(labels), 0, 1, 2)

        b = QPushButton("Submit")
        button.clicked.connect(self.button_clicked)
        layout.addWidget(b)

    def button_clicked(self):
        self.labelResult.setText(self.textboxes['first name'].text())
        
        self.show()

def main():
    app = QApplication([])
    w = mainwindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()

