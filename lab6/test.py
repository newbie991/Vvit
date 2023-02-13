from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
     QVBoxLayout,QHBoxLayout ,QBoxLayout ,QWidget,QPushButton,QMessageBox)

import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.op=''
        self.num1=0
        self.num2=0
        self.dot=False

        #create layout
        self.vbox = QVBoxLayout(self)
        self.vbox.addStretch(1)
        self.hbox_label = QHBoxLayout()
        self.hbox_input = QHBoxLayout()
        self.hbox_operations = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_operations)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_result)

        
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.label = QLabel(self)
        self.hbox_label.addWidget(self.label)
        self.hbox_label.addStretch(1)

        #create buttons
        #crete 1 row
        self.b_curly_bracket1 = QPushButton('(',self)
        self.b_curly_bracket2 = QPushButton(')',self)
        self.b_pct=QPushButton('%',self)
        self.b_clear=QPushButton('C',self)

        self.hbox_operations.addWidget(self.b_curly_bracket1)
        self.hbox_operations.addWidget(self.b_curly_bracket2)
        self.hbox_operations.addWidget(self.b_pct)
        self.hbox_operations.addWidget(self.b_clear)


        #create 2 row
        self.b_7 = QPushButton("7", self)
        self.b_8 = QPushButton("8", self)
        self.b_9 = QPushButton("9", self)
        self.b_div = QPushButton("÷", self)

        self.hbox_first.addWidget(self.b_7)
        self.hbox_first.addWidget(self.b_8)
        self.hbox_first.addWidget(self.b_9)
        self.hbox_first.addWidget(self.b_div)

        #create 3 row
        self.b_4 = QPushButton("4", self)
        self.b_5 = QPushButton("5", self)
        self.b_6 = QPushButton("6", self)
        self.b_mul = QPushButton("*", self)

        self.hbox_second.addWidget(self.b_4)
        self.hbox_second.addWidget(self.b_5)
        self.hbox_second.addWidget(self.b_6)
        self.hbox_second.addWidget(self.b_mul)

        #create 4 row
        self.b_1 = QPushButton("1", self)
        self.b_2 = QPushButton("2", self)
        self.b_3 = QPushButton("3", self)
        self.b_minus = QPushButton("-", self)

        self.hbox_third.addWidget(self.b_1)
        self.hbox_third.addWidget(self.b_2)
        self.hbox_third.addWidget(self.b_3)
        self.hbox_third.addWidget(self.b_minus)


        #create 5 row
        self.b_0 = QPushButton("0", self)
        self.b_dot = QPushButton(".", self)
        self.b_result = QPushButton("=", self)
        self.b_plus = QPushButton("+", self)

        self.hbox_result.addWidget(self.b_0)
        self.hbox_result.addWidget(self.b_dot)
        self.hbox_result.addWidget(self.b_result)
        self.hbox_result.addWidget(self.b_plus)

        #bg color
        self.b_minus.setStyleSheet('background: rgb(150,150,150);')
        self.b_plus.setStyleSheet('background: rgb(150,150,150);')
        self.b_div.setStyleSheet('background: rgb(150,150,150);')
        self.b_curly_bracket1.setStyleSheet('background: rgb(150,150,150);')
        self.b_curly_bracket2.setStyleSheet('background: rgb(150,150,150);')
        self.b_mul.setStyleSheet('background: rgb(150,150,150);')
        self.b_pct.setStyleSheet('background: rgb(150,150,150);')
        self.b_clear.setStyleSheet('background: rgb(150,150,150);')
        self.b_result.setStyleSheet('background: rgb(65,105,225);')

        
        #button click 
        #nubmer
        self.b_0.clicked.connect(lambda: self.button_num_click("0"))
        self.b_1.clicked.connect(lambda: self.button_num_click("1"))
        self.b_2.clicked.connect(lambda: self.button_num_click("2"))
        self.b_3.clicked.connect(lambda: self.button_num_click("3"))
        self.b_4.clicked.connect(lambda: self.button_num_click("4"))
        self.b_5.clicked.connect(lambda: self.button_num_click("5"))
        self.b_6.clicked.connect(lambda: self.button_num_click("6"))
        self.b_7.clicked.connect(lambda: self.button_num_click("7"))
        self.b_8.clicked.connect(lambda: self.button_num_click("8"))
        self.b_9.clicked.connect(lambda: self.button_num_click("9"))

        #dot
        self.b_dot.clicked.connect(self.button_dot_click)


        #operation
        self.b_plus.clicked.connect(lambda: self.button_operation_click("+"))
        self.b_minus.clicked.connect(lambda: self.button_operation_click("-"))
        self.b_mul.clicked.connect(lambda: self.button_operation_click("*"))
        self.b_div.clicked.connect(lambda: self.button_operation_click("/"))

        #result
        self.b_result.clicked.connect(self.button_result_click)

        #C clear
        self.b_clear.clicked.connect(self.button_clear)
        
        
        #set label = '0'
        self.label.setText('0')


    def button_num_click(self,e):
        print('clicked', e)
        text =self.label.text()
        if text == '0' or text=="Error":
            text = ''
        self.label.setText(text+e)

    def button_dot_click(self):
        if not(self.dot):
            text =self.label.text()
            self.label.setText(text+'.')
            self.dot=True

    def button_operation_click(self,op):
        if self.op != "":
            self.button_result_click()
        self.dot=False
        self.num1=float(self.label.text())
        self.op = op
        self.label.setText("0")

    def button_result_click(self):
        self.num2 =float(self.label.text())
        ans=0
        match self.op:
            case "+":
                ans=self.num1 + self.num2
            
            case "-":
                ans=self.num1 - self.num2

            case "*":
                ans=self.num1 * self.num2

            case "/":
                if self.num2==0:
                    self.button_clear()
                    return
                ans=self.num1 / self.num2

            case "%":
                pass

            case "(":
                pass

            case ")":
                pass
        
        self.dot=False
        ans = round(ans,6)
        if float(ans).is_integer():
            ans = int(ans)
        
        self.label.setText(str(ans))

        self.op = ""

    def button_clear(self):
        self.label.setText('0')
        self.op = ""
        self.num1=0
        self.num2=0
        self.dot=False





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()