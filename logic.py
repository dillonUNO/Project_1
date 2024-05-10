from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_win_Vote_Menu):
    def __init__(self) -> None:
        '''
        Initializes the program
        '''
        super().__init__()
        self.setupUi(self)
        self.lbl_Total.setHidden(True)
        self.lbl_Voted_For.setHidden(True)
        self.lbl_Bianca_Total.setHidden(True)
        self.lbl_Edward_Total.setHidden(True)
        self.lbl_Total.setHidden(True)
        self.lbl_Candidate_Menu.setHidden(True)
        self.lbl_Felicia_Total.setHidden(True)
        self.btn_Felicia.setHidden(True)
        self.btn_Edward.setHidden(True)
        self.btn_Back_2.setHidden(True)
        self.btn_Close.setHidden(True)
        self.btn_Bianca.setHidden(True)
        self.btn_Back_1.setHidden(True)
        self.btn_Vote.clicked.connect(lambda : self.vote())
        self.btn_Close.clicked.connect(lambda : self.close())
        self.btn_Bianca.clicked.connect(lambda : self.bianca())
        self.btn_Edward.clicked.connect(lambda : self.edward())
        self.btn_Felicia.clicked.connect(lambda : self.felicia())
        self.btn_Results.clicked.connect(lambda : self.results())
        self.btn_Back_1.clicked.connect(lambda : self.back1())
        self.btn_Back_2.clicked.connect(lambda : self.back2())
        self.total = 0
        self.bianca_total = 0
        self.edward_total = 0
        self.felicia_total = 0

    def vote(self) -> None:
        '''
        Prepares the program to enter the voting stage of the program
        '''
        self.lbl_Vote_Menu.setHidden(True)
        self.btn_Vote.setHidden(True)
        self.btn_Results.setHidden(True)
        self.lbl_Candidate_Menu.setHidden(False)
        self.btn_Bianca.setHidden(False)
        self.btn_Edward.setHidden(False)
        self.btn_Felicia.setHidden(False)

    def close(self) -> None:
        '''
        Closes the program
        '''
        self.close()

    def bianca(self) -> None:
        '''
        Logic to tally up votes for Bianca
        '''
        self.bianca_total += 1
        self.total += 1
        self.lbl_Voted_For.setText(f'Voted for Bianca')
        self.lbl_Voted_For.setHidden(False)
        self.btn_Back_2.setHidden(False)


    def edward(self) -> None:
        '''
        Logic to tally up votes for Edward
        '''
        self.edward_total += 1
        self.total += 1
        self.lbl_Voted_For.setText(f'Voted for Edward')
        self.lbl_Voted_For.setHidden(False)
        self.btn_Back_2.setHidden(False)

    def felicia(self) -> None:
        '''
        Logic to tally up voted for Felicia
        '''
        self.felicia_total += 1
        self.total += 1
        self.lbl_Voted_For.setText(f'Voted for Felicia')
        self.lbl_Voted_For.setHidden(False)
        self.btn_Back_2.setHidden(False)

    def results(self) -> None:
        '''
        Prepares the program to enter the results stage of the program
        '''
        self.btn_Back_1.setHidden(False)
        self.btn_Vote.setHidden(True)
        self.btn_Results.setHidden(True)
        self.btn_Close.setHidden(False)
        self.lbl_Felicia_Total.setHidden(False)
        self.lbl_Edward_Total.setHidden(False)
        self.lbl_Bianca_Total.setHidden(False)
        self.lbl_Total.setHidden(False)
        self.lbl_Bianca_Total.setText(f'Bianca - {self.bianca_total}')
        self.lbl_Edward_Total.setText(f'Edward - {self.edward_total}')
        self.lbl_Felicia_Total.setText(f'Felicia - {self.felicia_total}')
        self.lbl_Total.setText(f'Total - {self.total}')


    def back1(self) -> None:
        '''
        Logic to send the program back to the initial screen
        '''
        self.lbl_Vote_Menu.setHidden(False)
        self.btn_Vote.setHidden(False)
        self.btn_Results.setHidden(False)
        self.btn_Back_1.setHidden(True)
        self.btn_Close.setHidden(True)
        self.lbl_Felicia_Total.setHidden(True)
        self.lbl_Bianca_Total.setHidden(True)
        self.lbl_Edward_Total.setHidden(True)
        self.lbl_Total.setHidden(True)

    def back2(self) -> None:
        '''
        Logic to send the program back to the initial screen
        '''
        self.btn_Back_2.setHidden(True)
        self.btn_Bianca.setHidden(True)
        self.btn_Felicia.setHidden(True)
        self.btn_Edward.setHidden(True)
        self.lbl_Candidate_Menu.setHidden(True)
        self.lbl_Vote_Menu.setHidden(False)
        self.btn_Vote.setHidden(False)
        self.btn_Results.setHidden(False)
        self.lbl_Voted_For.setHidden(True)
