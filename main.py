from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QCheckBox, QFileDialog, QLabel, QVBoxLayout
from PySide6.QtGui import QCloseEvent, QIntValidator
import os
import random
import pandas as pd


class Okno(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1080, 720)
        self.setWindowTitle('Turniej Szachowy by Jakub Pawlowski')

        self.setup()

    def setup(self):
        layout = QVBoxLayout(self)

        self.line = QLineEdit(self)
        self.line.setPlaceholderText('Wybierz sciezke pliku za pomoca przycisku Importuj')
        self.line.setEnabled(False)
        layout.addWidget(self.line)

        self.rank_button = QPushButton(self)
        self.rank_button.setText('Ranking')
        layout.addWidget(self.rank_button)
        self.rank_button.hide()
        self.rank_button.clicked.connect(self.show_rank)

        self.kolejka = 0



        self.button_Import = QPushButton(self)
        
        #self.button_Import.move(490, 310)
        self.button_Import.setText('Importuj')
        layout.addWidget(self.button_Import)
        self.button_Import.clicked.connect(self.Import)

        self.generate_button = QPushButton(self)
        self.generate_button.setText('Generuj kolejke')
        self.generate_button.hide()
        layout.addWidget(self.generate_button)
        self.generate_button.clicked.connect(self.Generacja)

        


        




        self.button_quit = QPushButton(self)
        self.button_quit.setText('Zamknij')
        self.button_quit.move(490, 300)
        layout.addWidget(self.button_quit)
        
        



        self.show()

    


    def Import(self):

        self.lista = False
        response = QFileDialog.getOpenFileName(parent=self, caption='Wybierz plik')
        self.line.setText(str(response[0]))       
        self.data = pd.read_csv(response[0], delimiter=',')
        self.lista = self.data.values.tolist()
        self.variable = self.lista
        

        if self.lista:
            self.lista.sort(key=lambda x: x[2], reverse=True)
            self.show_rank(self.lista)
            self.generate_button.show()
            self.rank_button.show()

    def Generacja(self):
        self.kolejka += 1
        self.edit = EditRank(self.lista, self.kolejka)
        self.edit.show()

            
    def show_rank(self, list):
        self.ranking = Ranking(self.lista)
        self.ranking.show()
        


    
class Ranking(QWidget):
    def __init__(self, lista):
        super().__init__()
        self.setWindowTitle('Ranking')
        self.setFixedSize(800, 600)

        self.setup(lista)
    
    def setup(self, lista):
        layout = QVBoxLayout(self)
        i = 0

        for zawodnik in lista:
            i += 1
            zawodnik_label = QLabel(f"{i}. {zawodnik[0]} - {zawodnik[1]} - {zawodnik[2]}")  # Załóżmy, że zawodnik ma dwa atrybuty (np. ID i nazwisko)
            layout.addWidget(zawodnik_label)

        self.setLayout(layout)
      
class EditRank(QWidget):
    def __init__(self, lista, kolejka):
        super().__init__()

        self.setWindowTitle('Turniej')
        self.setFixedSize(1080, 720)

        self.setup(lista, kolejka)

    def setup(self, lista, kolejka):
        layout = QVBoxLayout(self)
        
        
        self.ID = []
        for zawodnik in lista:
            self.ID.append(zawodnik[0])
        while self.ID:
            self.color = ['Bialym', 'Czarnym']
            choice = random.choice(self.color)
            self.color.remove(choice)
            label = QLabel(f'{self.ID[0]} kolorem {choice} gra przeciwko {self.ID[-1]}')
            layout.addWidget(label)
            self.ID.pop(0)
            self.ID.pop(-1)
        self.actual = QPushButton(self)
        self.actual.setText('Aktualizuj ranking')
        layout.addWidget(self.actual)
        self.actual.clicked.connect(self.Edit)
    
    def Edit(self):
        self.edit = Edit()
        self.edit.show()

class Edit(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aktualizacja rankingu')
        self.setFixedSize(1080, 720)

        self.setup()
    
    def setup(self):
        layout = QVBoxLayout(self)
        self.ok_button = QPushButton(self)
        self.ok_button.setText('Praca')
        layout.addWidget(self.ok_button)


            



        

       
       


    








app = QApplication([])
login = Okno()
app.exec()

        