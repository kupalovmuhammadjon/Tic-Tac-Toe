import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class InnerWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        pen = QPen(Qt.black, 8, Qt.SolidLine) 
        qp.setPen(pen)
        qp.drawLine(186, 0, 186, 600)
        qp.drawLine(374, 0, 374, 561)
        qp.drawLine(0, 186, 561 , 186)
        qp.drawLine(0, 374, 561 , 374)
        qp.end()


class TicTacToe(QMainWindow):
    __buttonsls = []
    def __init__(self):
        super().__init__()
        self.count = 0
        self.setMinimumSize(700, 750)
        self.setMaximumSize(700, 750)
        self.setWindowTitle("TicTacToe")
        self.setWindowIcon(QIcon("D:/codes/tictactoe/icon.ico"))
        self.setStyleSheet("background-color: #DFECFF")

        self.whowinlb = QLabel(self)
        self.whowinlb.setGeometry(250, 10, 200, 50)
        self.whowinlb.setFont(QFont("Montserrat", 15, weight=70))
        self.whowinlb.setStyleSheet("""color: #A0E4A5;
                                    text-align: center;""")        
        
        self.innerwin = InnerWidget(self)
        self.innerwin.setGeometry(68, 70, 561, 561)
        self.innerwin.setStyleSheet("border-radius: 10px;")

        self.btn1 = QPushButton(self.innerwin)
        self.btn1.setGeometry(0, 0, 170, 170)
        self.btn1.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn1.clicked.connect(lambda : self.textPlacer(self.btn1, 1))

        self.btn2 = QPushButton(self.innerwin)
        self.btn2.setGeometry(195, 0, 170, 170)
        self.btn2.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn2.clicked.connect(lambda : self.textPlacer(self.btn2, 2))        

        self.btn3 = QPushButton(self.innerwin)
        self.btn3.setGeometry(390, 0, 170, 170)
        self.btn3.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn3.clicked.connect(lambda : self.textPlacer(self.btn3, 3))

        self.btn4 = QPushButton(self.innerwin)
        self.btn4.setGeometry(0, 195, 170, 170)
        self.btn4.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn4.clicked.connect(lambda : self.textPlacer(self.btn4, 4))

        self.btn5 = QPushButton(self.innerwin)
        self.btn5.setGeometry(195, 195, 170, 170)
        self.btn5.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn5.clicked.connect(lambda : self.textPlacer(self.btn5, 5))

        self.btn6 = QPushButton(self.innerwin)
        self.btn6.setGeometry(385, 195, 170, 170)
        self.btn6.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn6.clicked.connect(lambda : self.textPlacer(self.btn6, 6))

        self.btn7 = QPushButton(self.innerwin)
        self.btn7.setGeometry(0, 390, 170, 170)
        self.btn7.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn7.clicked.connect(lambda : self.textPlacer(self.btn7, 7))

        self.btn8 = QPushButton(self.innerwin)
        self.btn8.setGeometry(194, 390, 170, 170)
        self.btn8.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn8.clicked.connect(lambda : self.textPlacer(self.btn8, 8))

        self.btn9 = QPushButton(self.innerwin)
        self.btn9.setGeometry(390, 390, 170, 170)
        self.btn9.setStyleSheet("border-radius: 0px; border: 0px solid #000000;")
        self.btn9.clicked.connect(lambda : self.textPlacer(self.btn9, 9))

        new_game = QPushButton("New Game", self)
        new_game.setGeometry(65, 660, 250, 60)
        new_game.setFont(QFont("Montserrat", 15, weight=70))
        new_game.setStyleSheet("border-radius: 20px; background-color: #BED4FF")
        new_game.clicked.connect(self.newGame)

        quit_game = QPushButton("Quit Game", self)
        quit_game.setGeometry(380, 660, 250, 60)
        quit_game.setFont(QFont("Montserrat", 15, weight=70))
        quit_game.setStyleSheet("border-radius: 20px; background-color: #BED4FF")
        quit_game.clicked.connect(self.quitGame)
        
        
        self.show()
        
        TicTacToe.__buttonsls = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        
    def textPlacer(self, btn, bp):
        if btn.text() == "":
            symbol = "O" if self.count % 2 else "X"
            btn.setFont(QFont("Montserrat", 80))
            btn.setText(symbol)
            self.count += 1
            
            self.check()
    
    def check(self):
        btnvalues = []
        for i in TicTacToe.__buttonsls:
            btnvalues.append(i.text())
            
        if (btnvalues[0] == btnvalues[1] == btnvalues[2]) and not (btnvalues[0] == "" or btnvalues[1] == "" or btnvalues[2] == ""):
            self.whowinlb.setText(f"{TicTacToe.__buttonsls[0].text()} player won")
            TicTacToe.__buttonsls[0].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[1].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[2].setStyleSheet("background-color: #A0E4A5")
            self.disable()
            
            
        elif (btnvalues[3] == btnvalues[4] == btnvalues[5]) and not (btnvalues[3] == "" or btnvalues[4] == "" or btnvalues[5] == ""):
            self.whowinlb.setText(f"{TicTacToe.__buttonsls[3].text()} player won")
            TicTacToe.__buttonsls[3].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[4].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[5].setStyleSheet("background-color: #A0E4A5")
            self.disable()
            
            
        elif (btnvalues[6] == btnvalues[7] == btnvalues[8]) and not (btnvalues[6] == "" or btnvalues[7] == "" or btnvalues[8] == ""):
            self.whowinlb.setText(f"{TicTacToe.__buttonsls[6].text()} player won")
            TicTacToe.__buttonsls[6].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[7].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[8].setStyleSheet("background-color: #A0E4A5")
            self.disable()
            
            
        elif (btnvalues[0] == btnvalues[3] == btnvalues[6]) and not (btnvalues[0] == "" or btnvalues[3] == "" or btnvalues[6] == ""):
            self.whowinlb.setText(f"{TicTacToe.__buttonsls[6].text()} player won")
            TicTacToe.__buttonsls[0].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[3].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[6].setStyleSheet("background-color: #A0E4A5")
            self.disable()
            
            
        elif (btnvalues[1] == btnvalues[4] == btnvalues[7]) and not (btnvalues[1] == "" or btnvalues[4] == "" or btnvalues[7] == ""):
            self.whowinlb.setText(f"{TicTacToe.__buttonsls[1].text()} player won")
            TicTacToe.__buttonsls[1].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[4].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[7].setStyleSheet("background-color: #A0E4A5")
            self.disable()
            
            
        elif (btnvalues[2] == btnvalues[5] == btnvalues[8]) and not (btnvalues[2] == "" or btnvalues[5] == "" or btnvalues[8] == ""):
            self.whowinlb.setText(f"{TicTacToe.__buttonsls[2].text()} player won")
            TicTacToe.__buttonsls[2].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[5].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[8].setStyleSheet("background-color: #A0E4A5")
            self.disable()
            
        
        elif (btnvalues[2] == btnvalues[4] == btnvalues[6]) and not (btnvalues[2] == "" or btnvalues[4] == "" or btnvalues[6] == ""):
            self.whowinlb.setText(f"{TicTacToe.__buttonsls[4].text()} player won")
            TicTacToe.__buttonsls[2].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[4].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[6].setStyleSheet("background-color: #A0E4A5")
            self.disable()
            
            
        elif (btnvalues[0] == btnvalues[4] == btnvalues[8]) and not (btnvalues[0] == "" or btnvalues[4] == "" or btnvalues[8] == ""):
            self.whowinlb.setText(f"{TicTacToe.__buttonsls[0].text()} player won")
            TicTacToe.__buttonsls[0].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[4].setStyleSheet("background-color: #A0E4A5")
            TicTacToe.__buttonsls[8].setStyleSheet("background-color: #A0E4A5")
            self.disable()
            
        else:
            c = 1
            for i in TicTacToe.__buttonsls:
                if i.text() == "":
                    c = 0
            if c:
                for i in TicTacToe.__buttonsls:
                    if i.text() == "O":
                        i.setStyleSheet("background-color: #01AA8F")
                    else:
                        i.setStyleSheet("background-color: #9D9EA0")
                        
                self.whowinlb.setText("DRAW")
                
    
    def disable(self):
        
        for i in TicTacToe.__buttonsls:
            i.setEnabled(False)           
     
    def newGame(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("New Game")
        msg.setText("Do you really wat to start a new game")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.buttonClicked.connect(self.check_new_game)
        msg.show()
        
    def check_new_game(self, x):
        if x.text() == "&Yes":
            self.whowinlb.setText("")
            self.count = 0
            for btn in TicTacToe.__buttonsls:
                btn.setEnabled(True)           
                btn.setText("")
                btn.setStyleSheet("background-color: #DFECFF")
            
    def quitGame(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Quit Game")
        msg.setText("Do you really want to quit the game")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.buttonClicked.connect(self.check_quit_game)
        msg.show()
    
    def check_quit_game(self, x):
        if x.text() == "&Yes":
            exit()
        


app = QApplication(sys.argv)
main = TicTacToe()
sys.exit(app.exec_())
