class Exception(Exception):
    pass
from State import *
import time
class Game(object):
    __slots__ = ['_current_state', '_player_turn']
    def __init__(self):
        self._current_state=None
        self._player_turn="B"
        self.initialize_game()
    def initialize_game(self):
        self._current_state=State()
        self._player_turn="B"
    def put_figure(self):                   #DODATI DA SE UKLONI AKO SU 3 U REDU
        print(self._current_state)
        #if self._player_turn=="B":
        while True:
            #start=time.time()
            #(m,qx,qy)=self.min(alfa,beta)                 #predlaganje najboljeg poteza, m predstavlja vrednost
            #end=time.time()                          #qx,qy najbolji potez xdxdxdxdxdxdxdxdxdxdxd
            #print('Evaluation time: {}s'.format(round(end - start, 7)))
            #print('Recommended move: X = {}, Y = {}'.format(qx, qy))
            a=1
            px = int(input("Unesite px "))
            while a==1:
                if px>6 or px<0:
                    px = int(input("Unesite px "))
                else:
                    a=0
            a = 1
            py = int(input("Unesite py "))
            while a == 1:
                if py > 6 or py < 0:
                    py = int(input("Unesite py "))
                else:
                    a = 0
            if self._current_state.is_move_valid1(px,py,"B"):
                self._current_state.set_value(px,py,"B")
                self._player_turn="W"
                break
            else:
                print("Nije validan potez")
            if self._current_state.triunizu(px,py,"B"):
                self._current_state.pozovibrisanje("B")
                self._current_state.konacanispis()
        return px,py
    def nemadalje(self):
        if self._player_turn=="B":
            suprotno="W"
        if self._player_turn=="W":
            suprotno="B"
        brojac=0
        for i in range(0,7,1):
            for j in range(0,7,1):
                if self._current_state.nemadalje1(i,j,self._player_turn):
                    if self._current_state.proveritidalje(i,j,self._player_turn)==True:
                        brojac=brojac+1
                        break
        if brojac>0:
            return True
        else:
            return False

    def is_end1(self):                                                   #POSTAVLJANJE FIGURA        #KAD SE IZVRSI 9 PUTA TO
        for i in range(0,18,1):
            self.put_figure()
    def traje(self):                                                      #DODATI DA NEMA GDE DALJE DA SE IDE
        brojcrnih, brojbelih=self._current_state.brojcrnihibelih()
        #if brojcrnih<=2 or brojbelih<=2 or self._current_state.statenemadalje("B") or self._current_state.statenemadalje("W"):
        if brojcrnih <= 2 or brojbelih <= 2:
            return False
        return True
    # def nemadalje(self):
    #     if self._player_turn=="B":
    #         suprotno="W"
    #     if self._player_turn=="W":
    #         suprotno="B"
    #     brojac=0
    #     for i in range(0,7,1):
    #         for j in range(0,7,1):
    #             if self._current_state.nemadalje1(i,j,self._player_turn):
    #                 if self._current_state.proveritidalje(i,j,self._player_turn)==True:
    #                     brojac=brojac+1
    #                     break
    #     if brojac>0:
    #         return True
    #     else:
    #         return False
    def pobednik(self):
        brojcrnih, brojbelih = self._current_state.brojcrnihibelih()
        if brojcrnih<=2 or self._current_state.statenemadalje("B"):
            return "B"
        if brojbelih<=2 or self._current_state.statenemadalje("W"):
            return "W"
        #if self._current_state.nemadalje():                                    #DODATI OVO OBAVEZNO




    def potez(self):
        if self._player_turn=="B":
            self._player_turn="W"         #vljd ne treba izbrisati xdxdxdxdxdxd
            return "B"
        if self._player_turn=="W":
            self._player_turn = "B"
            return "W"
        else:
            raise Exception("Greska")
    def provera3unizu(self,i,j):                       #dodati ovo u end1 ili u put_figure
        if self._player_turn=="B":
            self._current_state.triunizu(i,j,"B")
        else:
            self._current_state.triunizu(i,j,"W")
    def brisi(self,i,j):
        if self._player_turn=="B":
            #self._current_state.izbrisi(i,j,"B")
            suprotno = "W"
            if not self._current_state.triunizu(i,j,"B"):
                self._current_state.izbrisi(i,j,"B")
        else:
            #self._current_state.izbrisi(i,j,"W")
            suprotno = "B"
            if not self._current_state.triunizu(i, j, "W"):
                self._current_state.izbrisi(i, j, "W")
    def pozicijefigura(self):
        figurecrne, figurebele=self._current_state.pozicijecrnihibelih()
        return figurecrne, figurebele
    def pozicijefigura1(self,tabla):
        figurecrne, figurebele=self._current_state.pozicijecrnihibelih1(tabla)
        return figurecrne, figurebele
    def pozovidalimoze(self,i,j,value):
        return self._current_state.proveritidalje1(i,j,value)
    def pozovimozetu(self,i,j,value):
        return self._current_state.mozetu(i,j,value)
    def pozovimozetu1(self,i,j,value):
        return self._current_state.mozetu1(i,j,value)
    def pozovizamenupolja(self,xkor,ykor,xkor1,ykor1,value):
        return self._current_state.zamenipolja(xkor,ykor,xkor1,ykor1,value)
    def pozovizamenupolja2(self,xkor,ykor,xkor1,ykor1,value):
        return self._current_state.zamenipolja2(xkor,ykor,xkor1,ykor1,value)
    def pozovizamenupolja1(self,xkor,ykor,xkor1,ykor1,value,state):
        print(state)
        return self._current_state.zamenipolja1(xkor,ykor,xkor1,ykor1,value,state)
    def pozovitriunizu(self,xkor1,ykor1,value):
        return self._current_state.triunizu(xkor1,ykor1,value)
    def pozovibrisanje(self,value):
        if value=="B":
            suprotno="W"
        if value=="W":
            suprotno="B"
        a = 1
        x1 = int(input("Unesite x1 "))
        while a == 1:
            if x1 > 6 or x1 < 0:
                x1 = int(input("Unesite x1 "))
            else:
                a = 0
        a = 1
        x2 = int(input("Unesite x2 "))
        while a == 1:
            if x2 > 6 or x2 < 0:
                x2 = int(input("Unesite x2 "))
            else:
                a = 0
        b=1
        while b==1:
            if self._current_state.is_move_valid2(x1, x2, suprotno):
                self._current_state.set_value(x1, x2, "*")
                b=0
            else:
                x1 = int(input("Unesite x1 "))
                while a == 1:
                    if x1 > 6 or x1 < 0:
                        px = int(input("Unesite x1 "))
                    else:
                        a = 0
                a = 1
                x2 = int(input("Unesite x2 "))
                while a == 1:
                    if x2 > 6 or x2 < 0:
                        x2 = int(input("Unesite py "))
                    else:
                        a = 0
    def konacanispis(self):
        self._current_state.ispis()

    def konacanispis1(self,state):
        self._current_state.ispis1(state)
    def board(self):
        return self._current_state.niz()
    def pozovipoljagdemozebitisve(self):
        return self._current_state.p
    def pozovimozetu2(self,i,j,value,state):
        return self._current_state.mozetu2(i,j,value,state)
    def pozovistanje(self):
        return self._current_state
    def pozicijefigura1(self,state):
        figurecrne, figurebele = self._current_state.pozicijecrnihibelih1(state)
        return figurecrne, figurebele
    def pozovimozetu3(self,i,j,value,state):
        return self._current_state.mozetu3(i,j,value,state)
    def pozovidostupnamesta(self):
        return self._current_state.dostupnamesta()
    def pozovidodajpolje(self,i,j,value):
        return self._current_state.dodajpolje(i,j,value)
    def pozoviponistipolje(self,i,j,value):
        return self._current_state.ponistipolje(i,j,value)
    def dodajfigurukonacno(self,i,j,value):
        return self._current_state.dodajfigurukonacn(i,j,value)
    def pozoviizbrisibot(self,value):
        return self._current_state.izbrisibot(value)
