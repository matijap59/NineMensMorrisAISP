from minimax import minimax
from minimax import pocetak
from minimax import kraj
from Tree import TreeNode
from Tree import Tree
from Hesmapa import *
from copy import deepcopy
from time import time
LISTAMORISA=[]
BROJPOTEZA=0
def play(game):
     global BROJPOTEZA
     global LISTAMORISA
     tabla = game.pozovistanje()
     game_root = TreeNode(deepcopy(tabla))
     hash_map=HashMap()
     game_tree = Tree(game_root)
     #game.konacanispis()
     for j in range(0,9,1):
         x1,x2=game.put_figure()
         BROJPOTEZA = BROJPOTEZA + 1
         if game.pozovitriunizu(x1, x2, "B"):
             LISTAMORISA.append(BROJPOTEZA)
             game.konacanispis()
             brisanje1(game,tabla)
             game.konacanispis()
         if tabla.razlikabrojudvojkiunizu("B")>0:
             start=time()
             red,kolona=tabla.razlikabrojudvojkiunizu1("B")
             end=time()
             razlika=end-start
             print(razlika)
             game.dodajfigurukonacno(red, kolona, "W")
             if game.pozovitriunizu(red, kolona, "W"):
                 LISTAMORISA.append(BROJPOTEZA)
                 faza5 = 1
                 a = brisanje2(game, tabla, faza5)
                 game.konacanispis()
             end=time()
         else:
             mozestu1=game.pozovidostupnamesta()
             for i in mozestu1:
                 xkor1=i[0]
                 ykor1=i[1]
                 pomocna=deepcopy(game.pozovistanje())
                 a=game.pozovidodajpolje(xkor1,ykor1,"W")
                 #print(a)
                 game_root.add_child(TreeNode(a))
                 game.pozoviponistipolje(xkor1,ykor1,"W")
             start=time()
             BROJPOTEZA=BROJPOTEZA+1
             red,kolona=kraj(game,tabla,game_tree.current,hash_map)
             game.dodajfigurukonacno(red,kolona,"W")
             if game.pozovitriunizu(red,kolona,"W"):
                 LISTAMORISA.append(BROJPOTEZA)
                 faza5=1
                 a=brisanje2(game,tabla,faza5)
                 game.konacanispis()
             end=time()
             razlika=end-start
             print(razlika)
     game.konacanispis()
     while game.traje():
        if game.potez()=="B":
            BROJPOTEZA=BROJPOTEZA+1
            brojac=0
            figurecrne, figurebele = game.pozicijefigura()
            figurecrne1 = []
            figurebele1 = []
            for crni in figurecrne:
                i=crni[0]
                j=crni[1]
                if game.pozovimozetu(i, j, "B"):
                    print(str(brojac) + " -> " + str(crni), end="   ")
                    brojac = brojac + 1
                    figurecrne1.append(crni)
            a=eval(input("Unesite 1 broj "))
            potez=figurecrne1[a]
            xkor=potez[0]
            ykor=potez[1]
            brojac1=0
            potezkrajni=game.pozovimozetu(xkor,ykor,"B")
            for p in potezkrajni:
                print(str(brojac1) + " -> " + str(p), end="   ")
                brojac1=brojac1+1
            a=eval(input("Unesite 1 broj "))
            potez1=potezkrajni[a]
            xkor1=potez1[0]
            ykor1=potez1[1]
            game.pozovizamenupolja(xkor, ykor, xkor1, ykor1, "B")
            if game.pozovitriunizu(xkor1,ykor1,"B"):
                LISTAMORISA.append(BROJPOTEZA)
                game.konacanispis()
                brisanje1(game,tabla)
                game.konacanispis()
        else:
            BROJPOTEZA=BROJPOTEZA+1
            figurecrne, figurebele = game.pozicijefigura()
            tabla=game.pozovistanje()
            game_root=TreeNode(deepcopy(tabla))
            hash_map=HashMap()
            game_tree=Tree(game_root)
            for k in figurebele:
                x=k[0]
                y=k[1]
                mozestu=game.pozovimozetu(x,y,"W")
                if len(mozestu)!=0:
                    for i in mozestu:
                        xkor1=i[0]
                        ykor1=i[1]
                        pomocna=deepcopy(game.pozovistanje())
                        a=game.pozovizamenupolja2(x,y,xkor1,ykor1,"W")
                        game_root.add_child(TreeNode(a))
                        game.pozovizamenupolja2(xkor1,ykor1,x,y,"W")
            start=time()
            red,kolona=pocetak(game,tabla,game_tree.current,hash_map)
            end=time()
            razlika=end-start
            print(razlika)
            figuraprvi,figuradrugi=tabla.prpolje(red,kolona,"W")
            game.pozovizamenupolja2(figuraprvi,figuradrugi,red,kolona,"W")
            game.konacanispis()
            if game.pozovitriunizu(red,kolona,"W"):
                LISTAMORISA.append(BROJPOTEZA)
                game.konacanispis()
                faza5=2
                a=brisanje2(game,tabla,faza5)
                game.konacanispis()

     pobednik = game.pobednik()
     if pobednik == "B":
         print("Pobedio je beli")
     if pobednik == "W":
         print("Pobedio je crni")

def brisanje1(game,tabla):
    x1=eval(input("Unesite x1 koje zelite da ponistite"))
    x2=eval(input("Unesite x2 koje zelite da ponistite"))
    a=1
    while a==1:
        if tabla.proveripolje(x1,x2,"W"):
            if game.pozovitriunizu(x1,x2,"W")==False:
                tabla.izmeni12(x1,x2)
                a=0
        else:
            x1 = eval(input("Unesite x1 koje zelite da ponistite"))
            x2 = eval(input("Unesite x2 koje zelite da ponistite"))

def brisanje2(game,tabla,faza5):
    if faza5==1:
        for i in range(0,7,1):
            for j in range(0,7,1):
                if tabla.proveripolje(i,j,"B"):
                    if game.pozovitriunizu(i,j,"B")==False:
                        tabla.izmeni12(i,j)
                        return False
    if faza5==2:
        brojac=0
        for i in range(0,7,1):
            for j in range(0,7,1):
                if tabla.proveripolje(i,j,"B"):
                    if game.pozovitriunizu(i,j,"B")==False:
                        tabla.izmeni12(i,j)
                        brojac=brojac+1
                        if brojac==1:
                            return False