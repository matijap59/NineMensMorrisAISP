class State(object):
    def __init__(self):
        self._board=[]
        """for i in range(0,8,1):                                  #Matrica 3x8
            self._board.append(3*['*'])"""
        #print(self._board)
        self._board.append(['*','-','-','*','-','-','*'])
        self._board.append(['-','*','-','*','-','*','-'])
        self._board.append(['-','-','*','*','*','-','-'])
        self._board.append(['*','*','*','-','*','*','*'])
        self._board.append(['-','-','*','*','*','-','-'])
        self._board.append(['-','*','-','*','-','*','-'])
        self._board.append(['*','-','-','*','-','-','*'])
        # self._board.append(['*','-','-','*','-','-','W'])
        # self._board.append(['-','*','-','B','-','*','-'])
        # self._board.append(['-','-','B','*','B','-','-'])
        # self._board.append(['B','W','B','-','*','B','W'])
        # self._board.append(['-','-','*','*','*','-','-'])
        # self._board.append(['-','*','-','B','-','B','-'])
        # self._board.append(['W','-','-','W','-','-','*'])
    #@property
    def get_value(self,i,j):
        return self._board[i][j]
    #@value.setter
    def set_value(self,i,j,value):
        self._board[i][j]=value
    def is_move_valid1(self,i,j,value):
        value=value.upper()
        if value!="W" and value!="B":
            return False
        if self._board[i][j]!="*":
            return False
        return True
    def is_move_valid2(self,i,j,value):
        value=value.upper()
        if self._board[i][j]!=value:
            return False
        return True
    def __str__(self):
        ret = ""
        """for i in range(0,3,1):
            for j in range(0,3,1):
                if i==j:
                    ret=ret+self._board[i][0]+" "
                else:
                    ret=ret+"- "
            ret=ret+self._board[i][1]+" "
            for k in range(2,-1,-1):
                if i==k:
                    ret=ret+self._board[i][2]+" "
                else:
                    ret=ret+"- "
            ret=ret+"\n"
        for i in range(0,3,1):
            ret=ret+self._board[3][i]+" "
        ret=ret+"- "
        for i in range(0,3,1):
            ret=ret+self._board[4][i]+" "
        ret=ret+"\n"
        for i in range(5,8,1):
            for j in range(2,-1,-1):
                if i-5==j:
                    ret=ret+self._board[i][0]+" "
                else:
                    ret=ret+"- "
            ret=ret+self._board[i][1]+" "
            for k in range(0,3,1):
                if i-5==k:
                    ret=ret+self._board[i][2]+" "
                else:
                    ret=ret+"- "
            ret=ret+"\n"
        return ret"""
        print("  0 1 2 3 4 5 6")
        for i in range(0,7,1):
            ret=ret+str(i)+" "
            for j in range(0,7,1):
                ret=ret+self._board[i][j]+" "
            ret=ret+"\n"
        return ret

    def brojcrnihibelih(self):                             #AKO BUDE SPORO DODAJ BROJACE ONDA VAMO I ODUZIMAJ
        brojcrnih=0
        brojbelih=0
        for i in range(0,7,1):
            for j in range(0,7,1):
                if self._board[i][j]=="B":
                    brojcrnih=brojcrnih+1
                if self._board[i][j]=="W":
                    brojbelih=brojbelih+1
        return brojcrnih, brojbelih
    def pozicijecrnihibelih(self):
        figurecrne=[]
        figurebele=[]
        listacrni = []
        listabeli=[]
        for i in range(0,7,1):
            for j in range(0,7,1):
                if self._board[i][j]=="B":
                    listacrni = []
                    listacrni.append(i)
                    listacrni.append(j)
                    figurecrne.append(listacrni)
                if self._board[i][j]=="W":
                    listabeli = []
                    listabeli.append(i)
                    listabeli.append(j)
                    figurebele.append(listabeli)
        return figurecrne,figurebele
    def pozicijecrnihibelih1(self,tabla):
        figurecrne=[]
        figurebele=[]
        listacrni = []
        listabeli=[]
        for i in range(0,7,1):
            for j in range(0,7,1):
                if tabla[i][j]=="B":
                    listacrni = []
                    listacrni.append(i)
                    listacrni.append(j)
                    figurecrne.append(listacrni)
                if tabla=="W":
                    listabeli = []
                    listabeli.append(i)
                    listabeli.append(j)
                    figurebele.append(listabeli)
        return figurecrne,figurebele
    def nemadalje1(self,i,j,value):
        if value=="B":
            suprotno="W"
        if value=="W":
            suprotno="B"
        if self._board[i][j]!=value:
            return False
        return True
    def proveritidalje(self,i,j,value):
        if value=="B":
            suprotno="W"
        if value=="W":
            suprotno="B"
        if i==0 and j==0:
            if self._board[0][3]==suprotno and self._board[3][0]==suprotno:
                return False
            return True
        if i==0 and j==6:
            if self._board[0][3]==suprotno and self._board[3][6]==suprotno:
                return False
            return True
        if i==6 and j==0:
            if self._board[3][0]==suprotno and self._board[6][3]==suprotno:
                return False
            return True
        if i==6 and j==6:
            if self._board[6][3]==suprotno and self._board[3][6]==suprotno:
                return False
            return True
        if i==1 and j==1:
            if self._board[1][3]==suprotno and self._board[3][1]==suprotno:
                return False
            return True
        if i==1 and j==5:
            if self._board[1][3]==suprotno and self._board[3][5]==suprotno:
                return False
            return True
        if i==5 and j==1:
            if self._board[5][3]==suprotno and self._board[3][1]==suprotno:
                return False
            return True
        if i==5 and j==5:
            if self._board[5][3]==suprotno and self._board[3][5]==suprotno:
                return False
            return True
        if i==2 and j==2:
            if self._board[2][3]==suprotno and self._board[3][2]==suprotno:
                return False
            return True
        if i==2 and j==4:
            if self._board[2][3]==suprotno and self._board[3][4]==suprotno:
                return False
            return True
        if i==4 and j==2:
            if self._board[3][2]==suprotno and self._board[4][3]==suprotno:
                return False
            return True
        if i==4 and j==4:
            if self._board[2][3]==suprotno and self._board[3][2]==suprotno:
                return False
            return True
        if i==0 and j==3:
            if self._board[0][0]==suprotno and self._board[0][6]==suprotno and self._board[1][3]==suprotno:
                return False
            return True
        if i==3 and j==0:
            if self._board[0][0]==suprotno and self._board[6][0]==suprotno and self._board[3][1]==suprotno:
                return False
            return True
        if i==3 and j==6:
            if self._board[0][6]==suprotno and self._board[6][6]==suprotno and self._board[3][5]==suprotno:
                return False
            return True
        if i==6 and j==3:
            if self._board[6][0]==suprotno and self._board[6][6]==suprotno and self._board[5][3]==suprotno:
                return False
            return True
        if i==2 and j==3:
            if self._board[2][2]==suprotno and self._board[2][4]==suprotno and self._board[1][3]==suprotno:
                return False
            return True
        if i==3 and j==2:
            if self._board[2][2]==suprotno and self._board[2][4]==suprotno and self._board[1][3]==suprotno:
                return False
            return True
        if i==3 and j==4:
            if self._board[2][4]==suprotno and self._board[4][4]==suprotno and self._board[3][5]==suprotno:
                return False
            return True
        if i==4 and j==3:
            if self._board[4][2]==suprotno and self._board[4][4]==suprotno and self._board[5][3]==suprotno:
                return False
            return True
        if i==1 and j==3:
            if self._board[0][3]==suprotno and self._board[1][1]==suprotno and self._board[1][5]==suprotno and self._board[2][3]==suprotno:
                return False
            return True
        if i==3 and j==1:
            if self._board[1][1]==suprotno and self._board[3][0]==suprotno and self._board[3][2]==suprotno and self._board[5][1]==suprotno:
                return False
            return True
        if i==3 and j==5:
            if self._board[1][5]==suprotno and self._board[3][4]==suprotno and self._board[3][6]==suprotno and self._board[5][5]==suprotno:
                return False
            return True
        if i==5 and j==3:
            if self._board[4][3]==suprotno and self._board[5][1]==suprotno and self._board[5][5]==suprotno and self._board[6][3]==suprotno:
                return False
            return True
    def proveritidalje1(self,i,j,value):           #True ako moze, False ako ne moze
        if value=="B":
            suprotno="B"
        if value=="W":
            suprotno="W"
        if i==0 and j==0:
            if self._board[0][3]==suprotno and self._board[3][0]==suprotno:
                return False
            return True
        if i==0 and j==6:
            if self._board[0][3]==suprotno and self._board[3][6]==suprotno:
                return False
            return True
        if i==6 and j==0:
            if self._board[3][0]==suprotno and self._board[6][3]==suprotno:
                return False
            return True
        if i==6 and j==6:
            if self._board[6][3]==suprotno and self._board[3][6]==suprotno:
                return False
            return True
        if i==1 and j==1:
            if self._board[1][3]==suprotno and self._board[3][1]==suprotno:
                return False
            return True
        if i==1 and j==5:
            if self._board[1][3]==suprotno and self._board[3][5]==suprotno:
                return False
            return True
        if i==5 and j==1:
            if self._board[5][3]==suprotno and self._board[3][1]==suprotno:
                return False
            return True
        if i==5 and j==5:
            if self._board[5][3]==suprotno and self._board[3][5]==suprotno:
                return False
            return True
        if i==2 and j==2:
            if self._board[2][3]==suprotno and self._board[3][2]==suprotno:
                return False
            return True
        if i==2 and j==4:
            if self._board[2][3]==suprotno and self._board[3][4]==suprotno:
                return False
            return True
        if i==4 and j==2:
            if self._board[3][2]==suprotno and self._board[4][3]==suprotno:
                return False
            return True
        if i==4 and j==4:
            if self._board[2][3]==suprotno and self._board[3][2]==suprotno:
                return False
            return True
        if i==0 and j==3:
            if self._board[0][0]==suprotno and self._board[0][6]==suprotno and self._board[1][3]==suprotno:
                return False
            return True
        if i==3 and j==0:
            if self._board[0][0]==suprotno and self._board[6][0]==suprotno and self._board[3][1]==suprotno:
                return False
            return True
        if i==3 and j==6:
            if self._board[0][6]==suprotno and self._board[6][6]==suprotno and self._board[3][5]==suprotno:
                return False
            return True
        if i==6 and j==3:
            if self._board[6][0]==suprotno and self._board[6][6]==suprotno and self._board[5][3]==suprotno:
                return False
            return True
        if i==2 and j==3:
            if self._board[2][2]==suprotno and self._board[2][4]==suprotno and self._board[1][3]==suprotno:
                return False
            return True
        if i==3 and j==2:
            if self._board[2][2]==suprotno and self._board[2][4]==suprotno and self._board[1][3]==suprotno:
                return False
            return True
        if i==3 and j==4:
            if self._board[2][4]==suprotno and self._board[4][4]==suprotno and self._board[3][5]==suprotno:
                return False
            return True
        if i==4 and j==3:
            if self._board[4][2]==suprotno and self._board[4][4]==suprotno and self._board[5][3]==suprotno:
                return False
            return True
        if i==1 and j==3:
            if self._board[0][3]==suprotno and self._board[1][1]==suprotno and self._board[1][5]==suprotno and self._board[2][3]==suprotno:
                return False
            return True
        if i==3 and j==1:
            if self._board[1][1]==suprotno and self._board[3][0]==suprotno and self._board[3][2]==suprotno and self._board[5][1]==suprotno:
                return False
            return True
        if i==3 and j==5:
            if self._board[1][5]==suprotno and self._board[3][4]==suprotno and self._board[3][6]==suprotno and self._board[5][5]==suprotno:
                return False
            return True
        if i==5 and j==3:
            if self._board[4][3]==suprotno and self._board[5][1]==suprotno and self._board[5][5]==suprotno and self._board[6][3]==suprotno:
                return False
            return True
    def mozetu(self,i,j,value):
        if value == "B":
            suprotno = "W"
        if value == "W":
            suprotno = "B"
        niz = []
        string = "(" + str(i) + " " + str(j) + ")"
        pomocna = []
        if i==0 and j==0:
            if self._board[0][3]=="*":
                pomocna = []
                pomocna.append(0)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][0]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(0)
                niz.append(pomocna)
        if i==0 and j==6:
            if self._board[0][3]=="*":
                pomocna = []
                pomocna.append(0)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][6]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(6)
                niz.append(pomocna)
        if i==6 and j==0:
            if self._board[3][0]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(0)
                niz.append(pomocna)
            if self._board[6][3]=="*":
                pomocna = []
                pomocna.append(6)
                pomocna.append(3)
                niz.append(pomocna)
        if i==6 and j==6:
            if self._board[6][3]=="*":
                pomocna = []
                pomocna.append(6)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][6]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(6)
                niz.append(pomocna)
        if i==1 and j==1:
            if self._board[1][3]=="*":
                pomocna = []
                pomocna.append(1)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][1]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(1)
                niz.append(pomocna)
        if i==1 and j==5:
            if self._board[1][3]=="*":
                pomocna = []
                pomocna.append(1)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][5]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(5)
                niz.append(pomocna)
        if i==5 and j==1:
            if self._board[5][3]=="*":
                pomocna = []
                pomocna.append(5)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][1]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(1)
                niz.append(pomocna)
        if i==5 and j==5:
            if self._board[5][3]=="*":
                pomocna = []
                pomocna.append(5)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][5]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(5)
                niz.append(pomocna)
        if i==2 and j==2:
            if self._board[2][3]=="*":
                pomocna = []
                pomocna.append(2)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][2]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(2)
                niz.append(pomocna)
        if i==2 and j==4:
            if self._board[2][3]=="*":
                pomocna = []
                pomocna.append(2)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[3][4]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(4)
                niz.append(pomocna)
        if i==4 and j==2:
            if self._board[3][2]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(2)
                niz.append(pomocna)
            if self._board[4][3]=="*":
                pomocna = []
                pomocna.append(4)
                pomocna.append(3)
                niz.append(pomocna)
        if i==4 and j==4:
            if self._board[3][4]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(4)
                niz.append(pomocna)
            if self._board[4][3]=="*":
                pomocna = []
                pomocna.append(4)
                pomocna.append(3)
                niz.append(pomocna)
        if i==0 and j==3:
            if self._board[0][0]=="*":
                pomocna = []
                pomocna.append(0)
                pomocna.append(0)
                niz.append(pomocna)
            if self._board[0][6]=="*":
                pomocna = []
                pomocna.append(0)
                pomocna.append(6)
                niz.append(pomocna)
            if self._board[1][3]=="*":
                pomocna = []
                pomocna.append(1)
                pomocna.append(3)
                niz.append(pomocna)
        if i==3 and j==0:
            if self._board[0][0]=="*":
                pomocna = []
                pomocna.append(0)
                pomocna.append(0)
                niz.append(pomocna)
            if self._board[6][0]=="*":
                pomocna = []
                pomocna.append(6)
                pomocna.append(0)
                niz.append(pomocna)
            if self._board[3][1]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(1)
                niz.append(pomocna)
        if i==3 and j==6:
            if self._board[0][6]=="*":
                pomocna = []
                pomocna.append(0)
                pomocna.append(6)
                niz.append(pomocna)
            if self._board[6][6]=="*":
                pomocna = []
                pomocna.append(6)
                pomocna.append(6)
                niz.append(pomocna)
            if self._board[3][5]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(5)
                niz.append(pomocna)
        if i==6 and j==3:
            if self._board[6][0]=="*":
                pomocna = []
                pomocna.append(6)
                pomocna.append(0)
                niz.append(pomocna)
            if self._board[6][6]=="*":
                pomocna = []
                pomocna.append(6)
                pomocna.append(6)
                niz.append(pomocna)
            if self._board[5][3]=="*":
                pomocna = []
                pomocna.append(5)
                pomocna.append(3)
                niz.append(pomocna)
        if i==2 and j==3:
            if self._board[2][2]=="*":
                pomocna = []
                pomocna.append(2)
                pomocna.append(2)
                niz.append(pomocna)
            if self._board[2][4]=="*":
                pomocna = []
                pomocna.append(2)
                pomocna.append(4)
                niz.append(pomocna)
            if self._board[1][3]=="*":
                pomocna = []
                pomocna.append(1)
                pomocna.append(3)
                niz.append(pomocna)         #OVDE
        if i==3 and j==2:
            if self._board[2][2]=="*":
                pomocna = []
                pomocna.append(2)
                pomocna.append(2)
                niz.append(pomocna)
            if self._board[4][2]=="*":
                pomocna = []
                pomocna.append(4)
                pomocna.append(2)
                niz.append(pomocna)
            if self._board[3][1]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(1)
                niz.append(pomocna)
        if i==3 and j==4:
            if self._board[2][4]=="*":
                pomocna = []
                pomocna.append(2)
                pomocna.append(4)
                niz.append(pomocna)
            if self._board[4][4]=="*":
                pomocna = []
                pomocna.append(4)
                pomocna.append(4)
                niz.append(pomocna)
            if self._board[3][5]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(5)
                niz.append(pomocna)
        if i==4 and j==3:
            if self._board[4][2]=="*":
                pomocna = []
                pomocna.append(4)
                pomocna.append(2)
                niz.append(pomocna)
            if self._board[4][4]=="*":
                pomocna = []
                pomocna.append(4)
                pomocna.append(4)
                niz.append(pomocna)
            if self._board[5][3]=="*":
                pomocna = []
                pomocna.append(5)
                pomocna.append(3)
                niz.append(pomocna)
        if i==1 and j==3:
            if self._board[0][3]=="*":
                pomocna = []
                pomocna.append(0)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[1][1]=="*":
                pomocna = []
                pomocna.append(1)
                pomocna.append(1)
                niz.append(pomocna)
            if self._board[1][5]=="*":
                pomocna = []
                pomocna.append(1)
                pomocna.append(5)
                niz.append(pomocna)
            if self._board[2][3]=="*":
                pomocna = []
                pomocna.append(2)
                pomocna.append(3)
                niz.append(pomocna)
        if i==3 and j==1:
            if self._board[1][1]=="*":
                pomocna = []
                pomocna.append(1)
                pomocna.append(1)
                niz.append(pomocna)
            if self._board[3][0]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(0)
                niz.append(pomocna)
            if self._board[3][2]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(2)
                niz.append(pomocna)
            if self._board[5][1]=="*":
                pomocna = []
                pomocna.append(5)
                pomocna.append(1)
                niz.append(pomocna)
        if i==3 and j==5:
            if self._board[1][5]=="*":
                pomocna = []
                pomocna.append(1)
                pomocna.append(5)
                niz.append(pomocna)
            if self._board[3][4]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(4)
                niz.append(pomocna)
            if self._board[3][6]=="*":
                pomocna = []
                pomocna.append(3)
                pomocna.append(6)
                niz.append(pomocna)
            if self._board[5][5]=="*":
                pomocna = []
                pomocna.append(5)
                pomocna.append(5)
                niz.append(pomocna)
        if i==5 and j==3:
            if self._board[4][3]=="*":
                pomocna = []
                pomocna.append(4)
                pomocna.append(3)
                niz.append(pomocna)
            if self._board[5][1]=="*":
                pomocna = []
                pomocna.append(5)
                pomocna.append(1)
                niz.append(pomocna)
            if self._board[5][5]=="*":
                pomocna = []
                pomocna.append(5)
                pomocna.append(5)
                niz.append(pomocna)
            if self._board[6][3]=="*":
                pomocna = []
                pomocna.append(6)
                pomocna.append(3)
                niz.append(pomocna)
        return niz
    def mozetu1(self,i,j,value):
        if value=="B":
            suprotno="W"
        if value=="W":
            suprotno="B"
        niz=[]
        #niz.append([int(x1), int(x2)])
        string="("+str(i)+" "+str(j)+")"
        if i==0 and j==0:
            if self._board[0][3]=="*":
                niz.append([int(0), int(3)])
            if self._board[3][0]=="*":
                niz.append([int(3), int(0)])
        if i==0 and j==6:
            if self._board[0][3]=="*":
                niz.append([int(0), int(3)])
            if self._board[3][6]=="*":
                niz.append([int(3), int(6)])
        if i==6 and j==0:
            if self._board[3][0]=="*":
                niz.append([int(3), int(0)])
            if self._board[6][3]=="*":
                niz.append([int(6), int(3)])
        if i==6 and j==6:
            if self._board[6][3]=="*":
                niz.append([int(6), int(3)])
            if self._board[3][6]=="*":
                niz.append([int(3), int(6)])
        if i==1 and j==1:
            if self._board[1][3]=="*":
                niz.append([int(1), int(3)])
            if self._board[3][1]=="*":
                niz.append([int(3), int(1)])
        if i==1 and j==5:
            if self._board[1][3]=="*":
                niz.append([int(1), int(5)])
            if self._board[3][5]=="*":
                niz.append([int(3), int(5)])
        if i==5 and j==1:
            if self._board[5][3]=="*":
                niz.append([int(5), int(3)])
            if self._board[3][1]=="*":
                niz.append([int(3), int(1)])
        if i==5 and j==5:
            if self._board[5][3]=="*":
                niz.append([int(5), int(5)])
            if self._board[3][5]=="*":
                niz.append([int(3), int(5)])
        if i==2 and j==2:
            if self._board[2][3]=="*":
                niz.append([int(2), int(3)])
            if self._board[3][2]=="*":
                niz.append([int(3), int(2)])
        if i==2 and j==4:
            if self._board[2][3]=="*":
                niz.append([int(2), int(3)])
            if self._board[3][4]=="*":
                niz.append([int(3), int(4)])
        if i==4 and j==2:
            if self._board[3][2]=="*":
                niz.append([int(3), int(2)])
            if self._board[4][3]=="*":
                niz.append([int(4), int(3)])
        if i==4 and j==4:
            if self._board[2][3]=="*":
                niz.append([int(2), int(3)])
            if self._board[3][2]=="*":
                niz.append([int(3), int(2)])
        if i==0 and j==3:
            if self._board[0][0]=="*":
                niz.append([int(0), int(0)])
            if self._board[0][6]=="*":
                niz.append([int(0), int(6)])
            if self._board[1][3]=="*":
                niz.append([int(1), int(3)])
        if i==3 and j==0:
            if self._board[0][0]=="*":
                niz.append([int(0), int(0)])
            if self._board[6][0]=="*":
                niz.append([int(6), int(0)])
            if self._board[3][1]=="*":
                niz.append([int(3), int(1)])
        if i==3 and j==6:
            if self._board[0][6]=="*":
                niz.append([int(0), int(6)])
            if self._board[6][6]=="*":
                niz.append([int(6), int(6)])
            if self._board[3][5]=="*":
                niz.append([int(3), int(5)])
        if i==6 and j==3:
            if self._board[6][0]=="*":
                niz.append([int(6), int(0)])
            if self._board[6][6]=="*":
                niz.append([int(6), int(6)])
            if self._board[5][3]=="*":
                niz.append([int(5), int(3)])
        if i==2 and j==3:
            if self._board[2][2]=="*":
                niz.append([int(2), int(2)])
            if self._board[2][4]=="*":
                niz.append([int(2), int(4)])
            if self._board[1][3]=="*":
                niz.append([int(1), int(3)])
        if i==3 and j==2:
            if self._board[2][2]=="*":
                niz.append([int(2), int(2)])
            if self._board[2][4]=="*":
                niz.append([int(2), int(4)])
            if self._board[1][3]=="*":
                niz.append([int(1), int(3)])
        if i==3 and j==4:
            if self._board[2][4]=="*":
                niz.append([int(2), int(4)])
            if self._board[4][4]=="*":
                niz.append([int(4), int(4)])
            if self._board[3][5]=="*":
                niz.append([int(3), int(5)])
        if i==4 and j==3:
            if self._board[4][2]=="*":
                niz.append([int(4), int(2)])
            if self._board[4][4]=="*":
                niz.append([int(4), int(4)])
            if self._board[5][3]=="*":
                niz.append([int(5), int(3)])
        if i==1 and j==3:
            if self._board[0][3]=="*":
                niz.append([int(0), int(3)])
            if self._board[1][1]=="*":
                niz.append([int(1), int(1)])
            if self._board[1][5]=="*":
                niz.append([int(1), int(5)])
            if self._board[2][3]=="*":
                niz.append([int(2), int(3)])
        if i==3 and j==1:
            if self._board[1][1]=="*":
                niz.append([int(1), int(1)])
            if self._board[3][0]=="*":
                niz.append([int(3), int(0)])
            if self._board[3][2]=="*":
                niz.append([int(3), int(2)])
            if self._board[5][1]=="*":
                niz.append([int(5), int(1)])
        if i==3 and j==5:
            if self._board[1][5]=="*":
                niz.append([int(1), int(5)])
            if self._board[3][4]=="*":
                niz.append([int(3), int(4)])
            if self._board[3][6]=="*":
                niz.append([int(3), int(6)])
            if self._board[5][5]=="*":
                niz.append([int(5), int(5)])
        if i==5 and j==3:
            if self._board[4][3]=="*":
                niz.append([int(4), int(3)])
            if self._board[5][1]=="*":
                niz.append([int(5), int(1)])
            if self._board[5][5]=="*":
                niz.append([int(5), int(5)])
            if self._board[6][3]=="*":
                niz.append([int(6), int(3)])
        return niz
    def mozetu2(self,i,j,value,state):
        if value=="B":
            suprotno="W"
        if value=="W":
            suprotno="B"
        niz=[]
        #niz.append([int(x1), int(x2)])
        string="("+str(i)+" "+str(j)+")"
        if i==0 and j==0:
            if state[0][3]=="*":
                niz.append([int(0), int(3)])
            if state[3][0]=="*":
                niz.append([int(3), int(0)])
        if i==0 and j==6:
            if state[0][3]=="*":
                niz.append([int(0), int(3)])
            if state[3][6]=="*":
                niz.append([int(3), int(6)])
        if i==6 and j==0:
            if state[3][0]=="*":
                niz.append([int(3), int(0)])
            if state[6][3]=="*":
                niz.append([int(6), int(3)])
        if i==6 and j==6:
            if state[6][3]=="*":
                niz.append([int(6), int(3)])
            if state[3][6]=="*":
                niz.append([int(3), int(6)])
        if i==1 and j==1:
            if state[1][3]=="*":
                niz.append([int(1), int(3)])
            if state[3][1]=="*":
                niz.append([int(3), int(1)])
        if i==1 and j==5:
            if state[1][3]=="*":
                niz.append([int(1), int(5)])
            if state[3][5]=="*":
                niz.append([int(3), int(5)])
        if i==5 and j==1:
            if state[5][3]=="*":
                niz.append([int(5), int(3)])
            if state[3][1]=="*":
                niz.append([int(3), int(1)])
        if i==5 and j==5:
            if state[5][3]=="*":
                niz.append([int(5), int(5)])
            if state[3][5]=="*":
                niz.append([int(3), int(5)])
        if i==2 and j==2:
            if state[2][3]=="*":
                niz.append([int(2), int(3)])
            if state[3][2]=="*":
                niz.append([int(3), int(2)])
        if i==2 and j==4:
            if state[2][3]=="*":
                niz.append([int(2), int(3)])
            if state[3][4]=="*":
                niz.append([int(3), int(4)])
        if i==4 and j==2:
            if state[3][2]=="*":
                niz.append([int(3), int(2)])
            if state[4][3]=="*":
                niz.append([int(4), int(3)])
        if i==4 and j==4:
            if state[2][3]=="*":
                niz.append([int(2), int(3)])
            if state[3][2]=="*":
                niz.append([int(3), int(2)])
        if i==0 and j==3:
            if state[0][0]=="*":
                niz.append([int(0), int(0)])
            if state[0][6]=="*":
                niz.append([int(0), int(6)])
            if state[1][3]=="*":
                niz.append([int(1), int(3)])
        if i==3 and j==0:
            if state[0][0]=="*":
                niz.append([int(0), int(0)])
            if state[6][0]=="*":
                niz.append([int(6), int(0)])
            if state[3][1]=="*":
                niz.append([int(3), int(1)])
        if i==3 and j==6:
            if state[0][6]=="*":
                niz.append([int(0), int(6)])
            if state[6][6]=="*":
                niz.append([int(6), int(6)])
            if state[3][5]=="*":
                niz.append([int(3), int(5)])
        if i==6 and j==3:
            if state[6][0]=="*":
                niz.append([int(6), int(0)])
            if state[6][6]=="*":
                niz.append([int(6), int(6)])
            if state[5][3]=="*":
                niz.append([int(5), int(3)])
        if i==2 and j==3:
            if state[2][2]=="*":
                niz.append([int(2), int(2)])
            if state[2][4]=="*":
                niz.append([int(2), int(4)])
            if state[1][3]=="*":
                niz.append([int(1), int(3)])
        if i==3 and j==2:
            if state[2][2]=="*":
                niz.append([int(2), int(2)])
            if state[2][4]=="*":
                niz.append([int(2), int(4)])
            if state[1][3]=="*":
                niz.append([int(1), int(3)])
        if i==3 and j==4:
            if state[2][4]=="*":
                niz.append([int(2), int(4)])
            if state[4][4]=="*":
                niz.append([int(4), int(4)])
            if state[3][5]=="*":
                niz.append([int(3), int(5)])
        if i==4 and j==3:
            if state[4][2]=="*":
                niz.append([int(4), int(2)])
            if state[4][4]=="*":
                niz.append([int(4), int(4)])
            if state[5][3]=="*":
                niz.append([int(5), int(3)])
        if i==1 and j==3:
            if state[0][3]=="*":
                niz.append([int(0), int(3)])
            if state[1][1]=="*":
                niz.append([int(1), int(1)])
            if state[1][5]=="*":
                niz.append([int(1), int(5)])
            if state[2][3]=="*":
                niz.append([int(2), int(3)])
        if i==3 and j==1:
            if state[1][1]=="*":
                niz.append([int(1), int(1)])
            if state[3][0]=="*":
                niz.append([int(3), int(0)])
            if state[3][2]=="*":
                niz.append([int(3), int(2)])
            if state[5][1]=="*":
                niz.append([int(5), int(1)])
        if i==3 and j==5:
            if state[1][5]=="*":
                niz.append([int(1), int(5)])
            if state[3][4]=="*":
                niz.append([int(3), int(4)])
            if state[3][6]=="*":
                niz.append([int(3), int(6)])
            if state[5][5]=="*":
                niz.append([int(5), int(5)])
        if i==5 and j==3:
            if state[4][3]=="*":
                niz.append([int(4), int(3)])
            if state[5][1]=="*":
                niz.append([int(5), int(1)])
            if state[5][5]=="*":
                niz.append([int(5), int(5)])
            if state[6][3]=="*":
                niz.append([int(6), int(3)])
        return niz

    def triunizu1(self,i,j,value):   #True ako jesu, False ako nisu   vljd je tako xdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxd
        if value=="B":
            suprotno="W"
        if value=="W":
            suprotno="B"
        brojac=0
        if i!=3 and j!=3:
            for k in range(0,7,1):
                if self._board[i][k]=="*" or self._board[i][k] == suprotno:
                    brojac=brojac+1
            if brojac==0:
                return True
            brojac=0
            for k in range(0,7,1):
                if self._board[k][j]=="*" or self._board[k][j]==suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                return True
        # if i<3 and j>3:
        #     pass
        # if i>3 and j<3:
        #     pass
        # if i>3 and j>3:
        #     pass
        if i==3 and j<3:
            brojac=0
            for k in range(0,3,1):
                if self._board[i][k]=="*" or self._board[i][k]==suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                    return True
            brojac=0
            for k in range(0,7,1):
                if self._board[k][j]=="*" or self._board[k][j]==suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                return True
        if i==3 and j>3:
            brojac=0
            for k in range(4,7,1):
                if self._board[i][k]=="*" or self._board[i][k]==suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                return True
            brojac=0
            for k in range(0, 7, 1):
                if self._board[k][j] == "*" or self._board[k][j] == suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                return True
        if j==3 and i<3:
            brojac=0
            for k in range(0,7,1):
                if self._board[i][k]=="*" or self._board[i][k] == suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                return True
            brojac=0
            for k in range(0,3,1):
                if self._board[k][j]=="*" or self._board[k][j]==suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                return True
        if j==3 and i>3:
            brojac=0
            for k in range(0,7,1):
                if self._board[i][k]=="*" or self._board[i][k] == suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                return True
            for k in range(4,7,1):
                brojac=0
                if self._board[k][j]=="*" or self._board[k][j]==suprotno:
                    brojac = brojac + 1
            if brojac == 0:
                return True
        return False

    def triunizu(self,i,j,value):
        if value == "B":
            suprotno = "W"
        if value == "W":
            suprotno = "B"
        b=1
        if i==0 and j==0:
            if self._board[0][0]==value and self._board[0][3]==value and self._board[0][6]==value:
                b=0
            if self._board[0][0]==value and self._board[3][0]==value and self._board[6][0]==value:
                b=0
        if i==0 and j==3:
            if self._board[0][0]==value and self._board[0][3]==value and self._board[0][6]==value:
                b=0
            if self._board[0][3]==value and self._board[1][3]==value and self._board[2][3]==value:
                b=0
        if i==0 and j==6:
            if self._board[0][0]==value and self._board[0][3]==value and self._board[0][6]==value:
                b=0
            if self._board[6][0]==value and self._board[3][6]==value and self._board[6][6]==value:
                b=0
        if i==1 and j==1:
            if self._board[1][1]==value and self._board[1][3]==value and self._board[1][5]==value:
                b=0
            if self._board[1][1]==value and self._board[3][1]==value and self._board[5][1]==value:
                b=0
        if i==1 and j==3:
            if self._board[1][1]==value and self._board[1][3]==value and self._board[1][5]==value:
                b=0
            if self._board[0][3]==value and self._board[1][3]==value and self._board[2][3]==value:
                b=0
        if i==1 and j==5:
            if self._board[1][1]==value and self._board[1][3]==value and self._board[1][5]==value:
                b=0
            if self._board[1][5]==value and self._board[3][5]==value and self._board[5][5]==value:
                b=0
        if i==2 and j==2:
            if self._board[2][2]==value and self._board[2][3]==value and self._board[2][4]==value:
                b=0
            if self._board[2][2]==value and self._board[3][2]==value and self._board[4][2]==value:
                b=0
        if i==2 and j==3:
            if self._board[2][2]==value and self._board[2][3]==value and self._board[2][4]==value:
                b=0
            if self._board[0][3]==value and self._board[1][3]==value and self._board[2][3]==value:
                b=0
        if i==2 and j==4:
            if self._board[2][4]==value and self._board[3][4]==value and self._board[4][4]==value:
                b=0
            if self._board[2][2]==value and self._board[2][3]==value and self._board[2][4]==value:
                b=0
        if i==3 and j==0:
            if self._board[0][0]==value and self._board[3][0]==value and self._board[6][0]==value:
                b=0
            if self._board[3][0]==value and self._board[3][1]==value and self._board[3][2]==value:
                b=0
        if i==3 and j==1:
            if self._board[1][1]==value and self._board[3][1]==value and self._board[5][1]==value:
                b=0
            if self._board[3][0]==value and self._board[3][1]==value and self._board[3][2]==value:
                b=0
        if i==3 and j==2:
            if self._board[2][2]==value and self._board[3][2]==value and self._board[4][2]==value:
                b=0
            if self._board[3][0]==value and self._board[3][1]==value and self._board[3][2]==value:
                b=0
        if i==3 and j==4:
            if self._board[2][4]==value and self._board[3][4]==value and self._board[4][4]==value:
                b=0
            if self._board[3][4]==value and self._board[3][5]==value and self._board[3][6]==value:
                b=0
        if i==3 and j==5:
            if self._board[1][5]==value and self._board[3][5]==value and self._board[5][5]==value:
                b=0
            if self._board[3][4]==value and self._board[3][5]==value and self._board[3][6]==value:
                b=0
        if i==3 and j==6:
            if self._board[0][6]==value and self._board[3][6]==value and self._board[6][6]==value:
                b=0
            if self._board[3][4]==value and self._board[3][5]==value and self._board[3][6]==value:
                b=0
        if i==4 and j==2:
            if self._board[2][2]==value and self._board[3][2]==value and self._board[4][2]==value:
                b=0
            if self._board[4][2]==value and self._board[4][3]==value and self._board[4][4]==value:
                b=0
        if i==4 and j==3:
            if self._board[4][2]==value and self._board[4][3]==value and self._board[4][4]==value:
                b=0
            if self._board[4][3]==value and self._board[5][3]==value and self._board[6][3]==value:
                b=0
        if i==4 and j==4:
            if self._board[2][4]==value and self._board[3][4]==value and self._board[4][4]==value:
                b=0
            if self._board[4][2]==value and self._board[4][3]==value and self._board[4][4]==value:
                b=0
        if i==5 and j==1:
            if self._board[1][1]==value and self._board[3][1]==value and self._board[5][1]==value:
                b=0
            if self._board[5][1]==value and self._board[5][3]==value and self._board[5][5]==value:
                b=0
        if i==5 and j==3:
            if self._board[5][1]==value and self._board[5][3]==value and self._board[5][5]==value:
                b=0
            if self._board[4][3]==value and self._board[5][3]==value and self._board[6][3]==value:
                b=0
        if i==5 and j==5:
            if self._board[1][5]==value and self._board[3][5]==value and self._board[5][5]==value:
                b=0
            if self._board[5][1]==value and self._board[5][3]==value and self._board[5][5]==value:
                b=0
        if i==6 and j==0:
            if self._board[0][0]==value and self._board[0][3]==value and self._board[0][6]==value:
                b=0
            if self._board[6][0]==value and self._board[6][3]==value and self._board[6][6]==value:
                b=0
        if i==6 and j==3:
            if self._board[6][0]==value and self._board[6][3]==value and self._board[6][6]==value:
                b=0
            if self._board[4][3]==value and self._board[5][3]==value and self._board[6][3]==value:
                b=0
        if i==6 and j==6:
            if self._board[6][0]==value and self._board[6][3]==value and self._board[6][6]==value:
                b=0
            if self._board[0][6]==value and self._board[3][6]==value and self._board[6][6]==value:
                b=0
        if b==0:
            return True
        else:
            return False

    def izbrisi(self,i,j,value):
        if value=="B":
            suprotno="W"
        if value=="W":
            suprotno="B"
        if self._board[i][j]==suprotno:
            self._board[i][j]="*"
        else:
            print("Pogresan potez")
    def zamenipolja(self,xkor,ykor,xkor1,ykor1,value):
        self._board[xkor][ykor]="*"
        if value == "B":
            self._board[xkor1][ykor1]="B"
        if value=="W":
            self._board[xkor1][ykor1]="W"
        string=""
        for i in range(0,7,1):
            for j in range(0,7,1):
                string=string+self._board[i][j]+" "
            string=string+"\n"
        print(string)

    def zamenipolja2(self, xkor, ykor, xkor1, ykor1, value):
        self._board[xkor][ykor] = "*"
        if value == "B":
            self._board[xkor1][ykor1] = "B"
        if value == "W":
            self._board[xkor1][ykor1] = "W"
        string = ""
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                string = string + self._board[i][j] + " "
            string = string + "\n"
        return string
    def zamenipolja3(self, xkor, ykor, xkor1, ykor1, value):
        self._board[xkor][ykor] = "*"
        if value == "B":
            self._board[xkor1][ykor1] = "B"
        if value == "W":
            self._board[xkor1][ykor1] = "W"
        matrica=[]
        for i in range(0,7,1):
            niz=[]
            for j in range(0,7,1):
                niz.append(self._board[i][j])
            matrica.append(niz)
        return matrica

    def zamenipolja1(self,xkor, ykor, xkor1, ykor1, value,state):
        state[xkor][ykor] = "*"
        if value == "B":
            state[xkor1][ykor1] = "B"
        if value == "W":
            state[xkor1][ykor1] = "W"
        string = ""
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                string = string + state[i][j] + " "
            string = string + "\n"
        return string
        #print(string)
    def zamenipolja4(self,xkor,ykor,xkor1,ykor1,value):
        self._board[xkor][ykor]="*"
        if value == "B":
            self._board[xkor1][ykor1]="B"
        if value=="W":
            self._board[xkor1][ykor1]="W"
    def ispis(self):
        print("  0 1 2 3 4 5 6")
        ret=""
        for i in range(0,7,1):
            ret=ret+str(i)+" "
            for j in range(0,7,1):
                ret=ret+self._board[i][j]+" "
            ret=ret+"\n"
        print(ret)
    def ispis2(self,matrica):
        ret = ""
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                ret = ret + matrica[i][j] + " "
            ret = ret + "\n"
        print(ret)
    def ispis1(self,state):
        ret=""
        for i in range(0,7,1):
            for j in range(0,7,1):
                ret=ret+state[i][j]+" "
            ret=ret+"\n"
        print(ret)

    def niz(self):
        return self._board

    def brojvezanihtrojki(self):
        brojac = 0
        brojac1 = 0
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                if i != 3:
                    if self._board[i][j] == "-" or self._board[i][j] == "B":
                        brojac1 = brojac1 + 1
            if i == 3:
                if self._board[i][0] == "B" and self._board[i][1] == "B" and self._board[i][2] == "B":
                    brojac = brojac + 1
            if i == 3:
                if self._board[i][4] == "B" and self._board[i][5] == "B" and self._board[i][6] == "B":
                    brojac = brojac + 1
            if brojac1 == 7:
                brojac = brojac + 1
            brojac1 = 0
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                if i != 3:
                    if self._board[j][i] == "-" or self._board[j][i] == "B":
                        brojac1 = brojac1 + 1
            if i == 3:
                if self._board[0][i] == "B" and self._board[1][i] == "B" and self._board[2][i] == "B":
                    brojac = brojac + 1
            if i == 3:
                if self._board[4][i] == "B" and self._board[5][i] == "B" and self._board[6][i] == "B":
                    brojac = brojac + 1
            if brojac1 == 7:
                brojac = brojac - 1
            brojac1 = 0
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                if i != 3:
                    if self._board[i][j] == "-" or self._board[i][j] == "W":
                        brojac1 = brojac1 + 1
            if i == 3:
                if self._board[i][0] == "W" and self._board[i][1] == "W" and self._board[i][2] == "W":
                    brojac = brojac - 1
            if i == 3:
                if self._board[i][4] == "W" and self._board[i][5] == "W" and self._board[i][6] == "W":
                    brojac = brojac + 1
            if brojac1 == 7:
                brojac = brojac - 1
            brojac1 = 0
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                if i != 3:
                    if self._board[j][i] == "-" or self._board[j][i] == "W":
                        brojac1 = brojac1 + 1
            if i == 3:
                if self._board[0][i] == "W" and self._board[1][i] == "W" and self._board[2][i] == "W":
                    brojac = brojac - 1
            if i == 3:
                if self._board[4][i] == "W" and self._board[5][i] == "W" and self._board[6][i] == "W":
                    brojac = brojac - 1
            if brojac1 == 7:
                brojac = brojac - 1
            brojac1 = 0
        return brojac

    def razlikabrojuvezanihtrojki(self):
        pass

    def razlikabrojublokiranihfigura(self):
        brojac = 0  # dodati do kraja ono
        suprotno = "W"
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                if self._board[i][j] == "B":
                    if i == 0 and j == 0:
                        if self._board[0][3] != "*" and self._board[3][0] != "*":
                            brojac = brojac + 1
                    if i == 0 and j == 6:
                        if self._board[0][3] != "*" and self._board[3][6] != "*":
                            brojac = brojac + 1
                    if i == 6 and j == 0:
                        if self._board[3][0] != "*" and self._board[6][3] != "*":
                            brojac = brojac + 1
                    if i == 6 and j == 6:
                        if self._board[6][3] != "*" and self._board[3][6] != "*":
                            brojac = brojac + 1
                    if i == 1 and j == 1:
                        if self._board[1][3] != "*" and self._board[3][1] != "*":
                            brojac = brojac + 1
                    if i == 1 and j == 5:
                        if self._board[1][3] != "*" and self._board[3][5] != "*":
                            brojac = brojac + 1
                    if i == 5 and j == 1:
                        if self._board[3][1] != "*" and self._board[5][3] != "*":
                            brojac = brojac + 1
                    if i == 5 and j == 5:
                        if self._board[5][3] != "*" and self._board[3][5] != "*":
                            brojac = brojac + 1
                    if i == 2 and j == 2:
                        if self._board[2][3] != "*" and self._board[3][2] != "*":
                            brojac = brojac + 1
                    if i == 2 and j == 4:
                        if self._board[2][3] != "*" and self._board[3][4] != "*":
                            brojac = brojac + 1
                    if i == 4 and j == 2:
                        if self._board[3][2] != "*" and self._board[4][3] != "*":
                            brojac = brojac + 1
                    if i == 4 and j == 4:
                        if self._board[4][3] != "*" and self._board[3][4] != "*":
                            brojac = brojac + 1
                    if i == 0 and j == 3:
                        if self._board[0][0] != "*" and self._board[1][3] != "*" and self._board[0][6] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 0:
                        if self._board[0][0] != "*" and self._board[3][1] != "*" and self._board[6][0] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 6:
                        if self._board[0][6] != "*" and self._board[3][5] != "*" and self._board[6][6] != "*":
                            brojac = brojac + 1
                    if i == 6 and j == 3:
                        if self._board[6][0] != "*" and self._board[5][3] != "*" and self._board[6][6] != "*":
                            brojac = brojac + 1
                    if i == 2 and j == 3:
                        if self._board[2][2] != "*" and self._board[1][3] != "*" and self._board[2][4] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 2:
                        if self._board[2][2] != "*" and self._board[3][1] != "*" and self._board[2][4] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 4:
                        if self._board[2][4] != "*" and self._board[3][5] != "*" and self._board[4][4] != "*":
                            brojac = brojac + 1
                    if i == 4 and j == 3:
                        if self._board[4][2] != "*" and self._board[5][3] != "*" and self._board[4][4] != "*":
                            brojac = brojac + 1
                    if i == 1 and j == 3:
                        if self._board[1][1] != "*" and self._board[0][3] != "*" and self._board[1][5] != "*" and self._board[2][3] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 1:
                        if self._board[1][1] != "*" and self._board[3][0] != "*" and self._board[3][2] != "*" and self._board[5][1] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 5:
                        if self._board[1][5] != "*" and self._board[3][4] != "*" and self._board[3][6] != "*" and self._board[5][5] != "*":
                            brojac = brojac + 1
                    if i == 5 and j == 3:
                        if self._board[5][1] != "*" and self._board[4][4] != "*" and self._board[4][6] != "*" and self._board[5][5] != "*":
                            brojac = brojac + 1
                else:
                    if self._board[i][j] == "B":
                        if i == 0 and j == 0:
                            if self._board[0][3] != "*" and self._board[3][0] != "*":
                                brojac = brojac + 1
                        if i == 0 and j == 6:
                            if self._board[0][3] != "*" and self._board[3][6] != "*":
                                brojac = brojac + 1
                        if i == 6 and j == 0:
                            if self._board[3][0] != "*" and self._board[6][3] != "*":
                                brojac = brojac + 1
                        if i == 6 and j == 6:
                            if self._board[6][3] != "*" and self._board[3][6] != "*":
                                brojac = brojac + 1
                        if i == 1 and j == 1:
                            if self._board[1][3] != "*" and self._board[3][1] != "*":
                                brojac = brojac + 1
                        if i == 1 and j == 5:
                            if self._board[1][3] != "*" and self._board[3][5] != "*":
                                brojac = brojac + 1
                        if i == 5 and j == 1:
                            if self._board[3][1] != "*" and self._board[5][3] != "*":
                                brojac = brojac + 1
                        if i == 5 and j == 5:
                            if self._board[5][3] != "*" and self._board[3][5] != "*":
                                brojac = brojac + 1
                        if i == 2 and j == 2:
                            if self._board[2][3] != "*" and self._board[3][2] != "*":
                                brojac = brojac + 1
                        if i == 2 and j == 4:
                            if self._board[2][3] != "*" and self._board[3][4] != "*":
                                brojac = brojac + 1
                        if i == 4 and j == 2:
                            if self._board[3][2] != "*" and self._board[4][3] != "*":
                                brojac = brojac + 1
                        if i == 4 and j == 4:
                            if self._board[4][3] != "*" and self._board[3][4] != "*":
                                brojac = brojac + 1
                        if i == 0 and j == 3:
                            if self._board[0][0] != "*" and self._board[1][3] != "*" and self._board[0][6] != "*":
                                brojac = brojac + 1
                        if i == 3 and j == 0:
                            if self._board[0][0] != "*" and self._board[3][1] != "*" and self._board[6][0] != "*":
                                brojac = brojac + 1
                        if i == 3 and j == 6:
                            if self._board[0][6] != "*" and self._board[3][5] != "*" and self._board[6][6] != "*":
                                brojac = brojac + 1
                        if i == 6 and j == 3:
                            if self._board[6][0] != "*" and self._board[5][3] != "*" and self._board[6][6] != "*":
                                brojac = brojac + 1
                        if i == 2 and j == 3:
                            if self._board[2][2] != "*" and self._board[1][3] != "*" and self._board[2][4] != "*":
                                brojac = brojac + 1
                        if i == 3 and j == 2:
                            if self._board[2][2] != "*" and self._board[3][1] != "*" and self._board[2][4] != "*":
                                brojac = brojac + 1
                        if i == 3 and j == 4:
                            if self._board[2][4] != "*" and self._board[3][5] != "*" and self._board[4][4] != "*":
                                brojac = brojac + 1
                        if i == 4 and j == 3:
                            if self._board[4][2] != "*" and self._board[5][3] != "*" and self._board[4][4] != "*":
                                brojac = brojac + 1
                        if i == 1 and j == 3:
                            if self._board[1][1] != "*" and self._board[0][3] != "*" and self._board[1][5] != "*" and \
                                    self._board[2][3] != "*":
                                brojac = brojac + 1
                        if i == 3 and j == 1:
                            if self._board[1][1] != "*" and self._board[3][0] != "*" and self._board[3][2] != "*" and \
                                    self._board[5][1] != "*":
                                brojac = brojac + 1
                        if i == 3 and j == 5:
                            if self._board[1][5] != "*" and self._board[3][4] != "*" and self._board[3][6] != "*" and \
                                    self._board[5][5] != "*":
                                brojac = brojac + 1
                        if i == 5 and j == 3:
                            if self._board[5][1] != "*" and self._board[4][4] != "*" and self._board[4][6] != "*" and self._board[5][5] != "*":
                                    brojac=brojac-1
        return brojac

    def razlikabrojablokiranihfigura1(self, value):
        brojac=0
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                if self._board[i][j] == value:
                    if i == 0 and j == 0:
                        if self._board[0][3] != "*" and self._board[3][0] != "*":
                            brojac = brojac + 1
                    if i == 0 and j == 6:
                        if self._board[0][3] != "*" and self._board[3][6] != "*":
                            brojac = brojac + 1
                    if i == 6 and j == 0:
                        if self._board[3][0] != "*" and self._board[6][3] != "*":
                            brojac = brojac + 1
                    if i == 6 and j == 6:
                        if self._board[6][3] != "*" and self._board[3][6] != "*":
                            brojac = brojac + 1
                    if i == 1 and j == 1:
                        if self._board[1][3] != "*" and self._board[3][1] != "*":
                            brojac = brojac + 1
                    if i == 1 and j == 5:
                        if self._board[1][3] != "*" and self._board[3][5] != "*":
                            brojac = brojac + 1
                    if i == 5 and j == 1:
                        if self._board[3][1] != "*" and self._board[5][3] != "*":
                            brojac = brojac + 1
                    if i == 5 and j == 5:
                        if self._board[5][3] != "*" and self._board[3][5] != "*":
                            brojac = brojac + 1
                    if i == 2 and j == 2:
                        if self._board[2][3] != "*" and self._board[3][2] != "*":
                            brojac = brojac + 1
                    if i == 2 and j == 4:
                        if self._board[2][3] != "*" and self._board[3][4] != "*":
                            brojac = brojac + 1
                    if i == 4 and j == 2:
                        if self._board[3][2] != "*" and self._board[4][3] != "*":
                            brojac = brojac + 1
                    if i == 4 and j == 4:
                        if self._board[4][3] != "*" and self._board[3][4] != "*":
                            brojac = brojac + 1
                    if i == 0 and j == 3:
                        if self._board[0][0] != "*" and self._board[1][3] != "*" and self._board[0][6] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 0:
                        if self._board[0][0] != "*" and self._board[3][1] != "*" and self._board[6][0] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 6:
                        if self._board[0][6] != "*" and self._board[3][5] != "*" and self._board[6][6] != "*":
                            brojac = brojac + 1
                    if i == 6 and j == 3:
                        if self._board[6][0] != "*" and self._board[5][3] != "*" and self._board[6][6] != "*":
                            brojac = brojac + 1
                    if i == 2 and j == 3:
                        if self._board[2][2] != "*" and self._board[1][3] != "*" and self._board[2][4] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 2:
                        if self._board[2][2] != "*" and self._board[3][1] != "*" and self._board[2][4] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 4:
                        if self._board[2][4] != "*" and self._board[3][5] != "*" and self._board[4][4] != "*":
                            brojac = brojac + 1
                    if i == 4 and j == 3:
                        if self._board[4][2] != "*" and self._board[5][3] != "*" and self._board[4][4] != "*":
                            brojac = brojac + 1
                    if i == 1 and j == 3:
                        if self._board[1][1] != "*" and self._board[0][3] != "*" and self._board[1][5] != "*" and self._board[2][3] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 1:
                        if self._board[1][1] != "*" and self._board[3][0] != "*" and self._board[3][2] != "*" and self._board[5][1] != "*":
                            brojac = brojac + 1
                    if i == 3 and j == 5:
                        if self._board[1][5] != "*" and self._board[3][4] != "*" and self._board[3][6] != "*" and self._board[5][5] != "*":
                            brojac = brojac + 1
                    if i == 5 and j == 3:
                        if self._board[5][1] != "*" and self._board[4][4] != "*" and self._board[4][6] != "*" and self._board[5][5] != "*":
                            brojac = brojac + 1
        return brojac

    def brojblokiranihfigura(self):
        pass

    def brojfigura(self,value):
        brojac = 0
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                if self._board[i][j] == value:
                    brojac = brojac + 1
        return brojac

    def razlikabrojufigura(self):
        brojac = 0
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                if self._board[i][j] == "B":
                    brojac = brojac + 1
                else:
                    if self._board[i][j] == "W":
                        brojac = brojac - 1
        return brojac

    def razlikabrojudvojkiunizu1(self,value):
        if self._board[0][0] == value and self._board[0][3] == value and self._board[0][6] == "*":
            return 0,6
        if self._board[0][0] == value and self._board[0][3] == "*" and self._board[0][6] == value:
            return 0,3
        if self._board[0][0] == "*" and self._board[0][3] == value and self._board[0][6] == value:
            return 0,0
        if self._board[1][1] == value and self._board[1][3] == value and self._board[1][5] == "*":
            return 1,5
        if self._board[1][1] == value and self._board[1][3] == "*" and self._board[1][5] == value:
            return 1,3
        if self._board[1][1] == "*" and self._board[1][3] == value and self._board[1][5] == value:
            return 1,1
        if self._board[2][2] == value and self._board[2][3] == value and self._board[2][4] == "*":
            return 2,4
        if self._board[2][2] == value and self._board[2][3] == "*" and self._board[2][4] == value:
            return 2,3
        if self._board[2][2] == "*" and self._board[2][3] == value and self._board[2][4] == value:
            return 2,2
        if self._board[3][0] == value and self._board[3][1] == value and self._board[3][2] == "*":
            return 3,2
        if self._board[3][0] == value and self._board[3][1] == "*" and self._board[3][2] == value:
            return 3,1
        if self._board[3][0] == "*" and self._board[3][1] == value and self._board[3][2] == value:
            return 3,0
        if self._board[3][4] == value and self._board[3][5] == value and self._board[3][6] == "*":
            return 3,6
        if self._board[3][4] == value and self._board[3][5] == "*" and self._board[3][6] == value:
            return 3,5
        if self._board[3][4] == "*" and self._board[3][5] == value and self._board[3][6] == value:
            return 3,4
        if self._board[4][2] == value and self._board[4][3] == value and self._board[4][4] == "*":
            return 4,4
        if self._board[4][2] == value and self._board[4][3] == "*" and self._board[4][4] == value:
            return 4,3
        if self._board[4][2] == "*" and self._board[4][3] == value and self._board[4][4] == value:
            return 4,2
        if self._board[5][1] == value and self._board[5][3] == value and self._board[5][5] == "*":
            return 5,1
        if self._board[5][1] == value and self._board[5][3] == "*" and self._board[5][5] == value:
            return 5,3
        if self._board[5][1] == "*" and self._board[5][3] == value and self._board[5][5] == value:
            return 5,1
        if self._board[6][0] == value and self._board[6][3] == value and self._board[6][6] == "*":
            return 6,6
        if self._board[6][0] == value and self._board[6][3] == "*" and self._board[6][6] == value:
            return 6,3
        if self._board[6][0] == "*" and self._board[6][3] == value and self._board[6][6] == value:
            return 6,0
        if self._board[0][0] == value and self._board[3][0] == value and self._board[6][0] == "*":
            return 6,0
        if self._board[0][0] == value and self._board[3][0] == "*" and self._board[6][0] == value:
            return 3,0
        if self._board[0][0] == "*" and self._board[3][0] == value and self._board[6][0] == value:
            return 0,0
        if self._board[1][1] == value and self._board[3][1] == value and self._board[5][1] == "*":
            return 5,1
        if self._board[1][1] == value and self._board[3][1] == "*" and self._board[5][1] == value:
            return 3,1
        if self._board[1][1] == "*" and self._board[3][1] == value and self._board[5][1] == value:
            return 1,1
        if self._board[2][2] == value and self._board[3][2] == value and self._board[4][2] == "*":
            return 4,2
        if self._board[2][2] == value and self._board[3][2] == "*" and self._board[4][2] == value:
            return 3,2
        if self._board[2][2] == "*" and self._board[3][2] == value and self._board[4][2] == value:
            return 2,2
        if self._board[0][3] == value and self._board[1][3] == value and self._board[2][3] == "*":
            return 2,3
        if self._board[0][3] == value and self._board[1][3] == "*" and self._board[2][3] == value:
            return 1,3
        if self._board[0][3] == "*" and self._board[1][3] == value and self._board[2][3] == value:
            return 0,3
        if self._board[4][3] == value and self._board[5][3] == value and self._board[6][3] == "*":
            return 6,3
        if self._board[4][3] == value and self._board[5][3] == "*" and self._board[6][3] == value:
            return 5,3
        if self._board[4][3] == "*" and self._board[5][3] == value and self._board[6][3] == value:
            return 4,3
        if self._board[2][4] == value and self._board[3][4] == value and self._board[4][4] == "*":
            return 4,4
        if self._board[2][4] == value and self._board[3][4] == "*" and self._board[4][4] == value:
            return 3,4
        if self._board[2][4] == "*" and self._board[3][4] == value and self._board[4][4] == value:
            return 2,4
        if self._board[1][5] == value and self._board[3][5] == value and self._board[5][5] == "*":
            return 5,5
        if self._board[1][5] == value and self._board[3][5] == "*" and self._board[5][5] == value:
            return 3,5
        if self._board[1][5] == "*" and self._board[3][5] == value and self._board[5][5] == value:
            return 1,5
        if self._board[0][6] == value and self._board[3][6] == value and self._board[6][6] == "*":
            return 6,6
        if self._board[0][6] == value and self._board[3][6] == "*" and self._board[6][6] == value:
            return 3,6
        if self._board[0][6] == "*" and self._board[3][6] == value and self._board[6][6] == value:
            return 0,6
    def razlikabrojudvojkiunizu(self,value):
        brojac=0
        if self._board[0][0]==value and self._board[0][3]==value and self._board[0][6]=="*":
            brojac=brojac+1
        if self._board[0][0]==value and self._board[0][3]=="*" and self._board[0][6]==value:
            brojac=brojac+1
        if self._board[0][0]=="*" and self._board[0][3]==value and self._board[0][6]==value:
            brojac=brojac+1
        if self._board[1][1]==value and self._board[1][3]==value and self._board[1][5]=="*":
            brojac=brojac+1
        if self._board[1][1]==value and self._board[1][3]=="*" and self._board[1][5]==value:
            brojac=brojac+1
        if self._board[1][1]=="*" and self._board[1][3]==value and self._board[1][5]==value:
            brojac=brojac+1
        if self._board[2][2]==value and self._board[2][3]==value and self._board[2][4]=="*":
            brojac=brojac+1
        if self._board[2][2]==value and self._board[2][3]=="*" and self._board[2][4]==value:
            brojac=brojac+1
        if self._board[2][2]=="*" and self._board[2][3]==value and self._board[2][4]==value:
            brojac=brojac+1
        if self._board[3][0]==value and self._board[3][1]==value and self._board[3][2]=="*":
            brojac=brojac+1
        if self._board[3][0]==value and self._board[3][1]=="*" and self._board[3][2]==value:
            brojac=brojac+1
        if self._board[3][0]=="*" and self._board[3][1]==value and self._board[3][2]==value:
            brojac=brojac+1
        if self._board[3][4]==value and self._board[3][5]==value and self._board[3][6]=="*":
            brojac=brojac+1
        if self._board[3][4]==value and self._board[3][5]=="*" and self._board[3][6]==value:
            brojac=brojac+1
        if self._board[3][4]=="*" and self._board[3][5]==value and self._board[3][6]==value:
            brojac=brojac+1
        if self._board[4][2]==value and self._board[4][3]==value and self._board[4][4]=="*":
            brojac=brojac+1
        if self._board[4][2]==value and self._board[4][3]=="*" and self._board[4][4]==value:
            brojac=brojac+1
        if self._board[4][2]=="*" and self._board[4][3]==value and self._board[4][4]==value:
            brojac=brojac+1
        if self._board[5][1]==value and self._board[5][3]==value and self._board[5][5]=="*":
            brojac=brojac+1
        if self._board[5][1]==value and self._board[5][3]=="*" and self._board[5][5]==value:
            brojac=brojac+1
        if self._board[5][1]=="*" and self._board[5][3]==value and self._board[5][5]==value:
            brojac=brojac+1
        if self._board[6][0]==value and self._board[6][3]==value and self._board[6][6]=="*":
            brojac=brojac+1
        if self._board[6][0]==value and self._board[6][3]=="*" and self._board[6][6]==value:
            brojac=brojac+1
        if self._board[6][0]=="*" and self._board[6][3]==value and self._board[6][6]==value:
            brojac=brojac+1
        if self._board[0][0]==value and self._board[3][0]==value and self._board[6][0]=="*":
            brojac=brojac+1
        if self._board[0][0]==value and self._board[3][0]=="*" and self._board[6][0]==value:
            brojac=brojac+1
        if self._board[0][0]=="*" and self._board[3][0]==value and self._board[6][0]==value:
            brojac=brojac+1
        if self._board[1][1]==value and self._board[3][1]==value and self._board[5][1]=="*":
            brojac=brojac+1
        if self._board[1][1]==value and self._board[3][1]=="*" and self._board[5][1]==value:
            brojac=brojac+1
        if self._board[1][1]=="*" and self._board[3][1]==value and self._board[5][1]==value:
            brojac=brojac+1
        if self._board[2][2]==value and self._board[3][2]==value and self._board[4][2]=="*":
            brojac=brojac+1
        if self._board[2][2]==value and self._board[3][2]=="*" and self._board[4][2]==value:
            brojac=brojac+1
        if self._board[2][2]=="*" and self._board[3][2]==value and self._board[4][2]==value:
            brojac=brojac+1
        if self._board[0][3]==value and self._board[1][3]==value and self._board[2][3]=="*":
            brojac=brojac+1
        if self._board[0][3]==value and self._board[1][3]=="*" and self._board[2][3]==value:
            brojac=brojac+1
        if self._board[0][3]=="*" and self._board[1][3]==value and self._board[2][3]==value:
            brojac=brojac+1
        if self._board[4][3]==value and self._board[5][3]==value and self._board[6][3]=="*":
            brojac=brojac+1
        if self._board[4][3]==value and self._board[5][3]=="*" and self._board[6][3]==value:
            brojac=brojac+1
        if self._board[4][3]=="*" and self._board[5][3]==value and self._board[6][3]==value:
            brojac=brojac+1
        if self._board[2][4]==value and self._board[3][4]==value and self._board[4][4]=="*":
            brojac=brojac+1
        if self._board[2][4]==value and self._board[3][4]=="*" and self._board[4][4]==value:
            brojac=brojac+1
        if self._board[2][4]=="*" and self._board[3][4]==value and self._board[4][4]==value:
            brojac=brojac+1
        if self._board[1][5]==value and self._board[3][5]==value and self._board[5][5]=="*":
            brojac=brojac+1
        if self._board[1][5]==value and self._board[3][5]=="*" and self._board[5][5]==value:
            brojac=brojac+1
        if self._board[1][5]=="*" and self._board[3][5]==value and self._board[5][5]==value:
            brojac=brojac+1
        if self._board[0][6]==value and self._board[3][6]==value and self._board[6][6]=="*":
            brojac=brojac+1
        if self._board[0][6]==value and self._board[3][6]=="*" and self._board[6][6]==value:
            brojac=brojac+1
        if self._board[0][6]=="*" and self._board[3][6]==value and self._board[6][6]==value:
            brojac=brojac+1
        return brojac
    def razlikabrojutrojkidruginacin(self):
        brojac = 0
        if self._board[0][0] == "B" and self._board[0][3] == "B" and self._board[3][0] == "B":
            brojac = brojac + 1
        if self._board[0][6] == "B" and self._board[0][3] == "B" and self._board[3][6] == "B":
            brojac = brojac + 1
        if self._board[6][0] == "B" and self._board[3][0] == "B" and self._board[6][3] == "B":
            brojac = brojac + 1
        if self._board[6][6] == "B" and self._board[6][3] == "B" and self._board[3][6] == "B":
            brojac = brojac + 1
        if self._board[1][1] == "B" and self._board[1][3] == "B" and self._board[3][1] == "B":
            brojac = brojac + 1
        if self._board[1][5] == "B" and self._board[1][3] == "B" and self._board[3][5] == "B":
            brojac = brojac + 1
        if self._board[5][1] == "B" and self._board[5][3] == "B" and self._board[3][1] == "B":
            brojac = brojac + 1
        if self._board[5][5] == "B" and self._board[5][3] == "B" and self._board[3][5] == "B":
            brojac = brojac + 1
        if self._board[2][2] == "B" and self._board[2][3] == "B" and self._board[3][2] == "B":
            brojac = brojac + 1
        if self._board[2][4] == "B" and self._board[2][3] == "B" and self._board[3][4] == "B":
            brojac = brojac + 1
        if self._board[4][2] == "B" and self._board[3][2] == "B" and self._board[4][3] == "B":
            brojac = brojac + 1
        if self._board[4][4] == "B" and self._board[4][3] == "B" and self._board[3][4] == "B":
            brojac = brojac + 1
        if self._board[0][0] == "W" and self._board[0][3] == "W" and self._board[3][0] == "W":
            brojac = brojac - 1
        if self._board[0][6] == "W" and self._board[0][3] == "W" and self._board[3][6] == "W":
            brojac = brojac - 1
        if self._board[6][0] == "W" and self._board[3][0] == "W" and self._board[6][3] == "W":
            brojac = brojac - 1
        if self._board[6][6] == "W" and self._board[6][3] == "W" and self._board[3][6] == "W":
            brojac = brojac - 1
        if self._board[1][1] == "W" and self._board[1][3] == "W" and self._board[3][1] == "W":
            brojac = brojac - 1
        if self._board[1][5] == "W" and self._board[1][3] == "W" and self._board[3][5] == "W":
            brojac = brojac - 1
        if self._board[5][1] == "W" and self._board[5][3] == "W" and self._board[3][1] == "W":
            brojac = brojac - 1
        if self._board[5][5] == "W" and self._board[5][3] == "W" and self._board[3][5] == "W":
            brojac = brojac - 1
        if self._board[2][2] == "W" and self._board[2][3] == "W" and self._board[3][2] == "W":
            brojac = brojac - 1
        if self._board[2][4] == "W" and self._board[2][3] == "W" and self._board[3][4] == "W":
            brojac = brojac - 1
        if self._board[4][2] == "W" and self._board[3][2] == "W" and self._board[4][3] == "W":
            brojac = brojac - 1
        if self._board[4][4] == "W" and self._board[4][3] == "W" and self._board[3][4] == "W":
            brojac = brojac - 1
        return brojac

    def razlikabrojuduplihtrojki(self):
        brojac = 0
        if self._board[0][0] == "B" and self._board[0][3] == "B" and self._board[0][6] == "B" and self._board[3][0] == "B" and self._board[6][
            0] == "B":
            brojac = brojac + 1
        if self._board[0][0] == "B" and self._board[0][3] == "B" and self._board[0][6] == "B" and self._board[3][6] == "B" and self._board[6][
            6] == "B":
            brojac = brojac + 1
        if self._board[0][0] == "B" and self._board[6][3] == "B" and self._board[6][6] == "B" and self._board[3][0] == "B" and self._boardself._board[6][
            0] == "B":
            brojac = brojac + 1
        if self._board[6][6] == "B" and self._board[6][3] == "B" and self._board[0][6] == "B" and self._board[3][6] == "B" and self._board[6][
            0] == "B":
            brojac = brojac + 1
        if self._board[1][1] == "B" and self._board[1][3] == "B" and self._board[1][5] == "B" and self._board[3][1] == "B" and self._board[5][
            1] == "B":
            brojac = brojac + 1
        if self._board[1][5] == "B" and self._board[1][3] == "B" and self._board[1][1] == "B" and self._board[3][5] == "B" and self._board[5][
            5] == "B":
            brojac = brojac + 1
        if self._board[5][1] == "B" and self._board[3][1] == "B" and self._board[1][1] == "B" and self._board[5][3] == "B" and self._board[5][
            5] == "B":
            brojac = brojac + 1
        if self._board[5][5] == "B" and self._board[5][3] == "B" and self._board[5][1] == "B" and self._board[3][5] == "B" and self._board[1][
            5] == "B":
            brojac = brojac + 1
        if self._board[2][2] == "B" and self._board[2][3] == "B" and self._board[2][4] == "B" and self._board[3][2] == "B" and self._board[4][
            2] == "B":
            brojac = brojac + 1
        if self._board[2][4] == "B" and self._board[2][3] == "B" and self._board[2][2] == "B" and self._board[3][4] == "B" and self._board[4][
            4] == "B":
            brojac = brojac + 1
        if self._board[4][2] == "B" and self._board[4][3] == "B" and self._board[4][4] == "B" and self._board[3][2] == "B" and self._board[2][
            2] == "B":
            brojac = brojac + 1
        if self._board[4][4] == "B" and self._board[4][3] == "B" and self._board[4][2] == "B" and self._board[3][4] == "B" and self._board[3][
            2] == "B":
            brojac = brojac + 1
        if self._board[0][0] == "W" and self._board[0][3] == "W" and self._board[0][6] == "W" and self._board[3][0] == "W" and self._board[6][
            0] == "W":
            brojac = brojac - 1
        if self._board[0][0] == "W" and self._board[0][3] == "W" and self._board[0][6] == "W" and self._board[3][6] == "W" and self._board[6][
            6] == "W":
            brojac = brojac - 1
        if self._board[0][0] == "W" and self._board[6][3] == "W" and self._board[6][6] == "W" and self._board[3][0] == "W" and self._board[6][
            0] == "W":
            brojac = brojac - 1
        if self._board[6][6] == "W" and self._board[6][3] == "W" and self._board[0][6] == "W" and self._board[3][6] == "W" and self._board[6][
            0] == "W":
            brojac = brojac - 1
        if self._board[1][1] == "W" and self._board[1][3] == "W" and self._board[1][5] == "W" and self._board[3][1] == "W" and self._board[5][
            1] == "W":
            brojac = brojac - 1
        if self._board[1][5] == "W" and self._board[1][3] == "W" and self._board[1][1] == "W" and self._board[3][5] == "W" and self._board[5][
            5] == "W":
            brojac = brojac - 1
        if self._board[5][1] == "W" and self._board[3][1] == "W" and self._board[1][1] == "W" and self._board[5][3] == "W" and self._board[5][
            5] == "W":
            brojac = brojac - 1
        if self._board[5][5] == "W" and self._board[5][3] == "W" and self._board[5][1] == "W" and self._board[3][5] == "W" and self._board[1][
            5] == "W":
            brojac = brojac - 1
        if self._board[2][2] == "W" and self._board[2][3] == "W" and self._board[2][4] == "W" and self._board[3][2] == "W" and self._board[4][
            2] == "W":
            brojac = brojac - 1
        if self._board[2][4] == "W" and self._board[2][3] == "W" and self._board[2][2] == "W" and self._board[3][4] == "W" and self._board[4][
            4] == "W":
            brojac = brojac - 1
        if self._board[4][2] == "W" and self._board[4][3] == "W" and self._board[4][4] == "W" and self._board[3][2] == "W" and self._board[2][
            2] == "W":
            brojac = brojac - 1
        if self._board[4][4] == "W" and self._board[4][3] == "W" and self._board[4][2] == "W" and self._board[3][4] == "W" and self._board[3][
            2] == "W":
            brojac = brojac - 1
        return brojac
    def dostupnamesta(self):
        matrica=[]
        lista=[]
        for i in range(0,7,1):
            for j in range(0,7,1):
                if self._board[i][j]=="*":
                    lista.append(i)
                    lista.append(j)
                    matrica.append(lista)
                    lista=[]
        return matrica
    def dodajpolje(self,i,j,value):
        self._board[i][j]=value
        string=""
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                string = string + self._board[i][j] + " "
            string = string + "\n"
        return string
    def ponistipolje(self,i,j,value):
        self._board[i][j] = "*"
        string = ""
        for i in range(0, 7, 1):
            for j in range(0, 7, 1):
                string = string + self._board[i][j] + " "
            string = string + "\n"
        return string
    def mogucepolje(self):
        lista=[]
        matrica=[]
        for i in range(0,7,1):
            for j in range(0,7,1):
                if self._board[i][j]=="*":
                    lista.append(i)
                    lista.append(j)
                    matrica.append(lista)
                    lista=[]
        return matrica
    def docrtaj(self,i,j,value):
        self._board[i][j]=value
    def dodajfigurukonacn(self,i,j,value):
        self._board[i][j]=value
    def prebaciulistu(self):
        matrica=[]
        lista=[]
        for i in range(0,7,1):
            for j in range(0,7,1):
                vr=self._board[i][j]
                lista.append(vr)
            matrica.append(lista)
            lista=[]
        return matrica
    def izbrisibot(self,value):
        if value=="B":
            suprotno="W"
        if value=="W":
            suprotno="B"
        for i in range(0,7,1):
            for j in range(0,7,1):
                if self._board[i][j]==suprotno:
                    print("1")
                    self._board[i][j]="*"
                    break
    def izmeni12(self,i,j):
        self._board[i][j]="*"
    def proveripolje(self,i,j,value):
        if self._board[i][j]==value:
            return True
        else:
            return False
    def statenemadalje(self,value):
        lista=[]
        matrica=[]
        for i in range(0,7,1):
            for j in range(0,7,1):
                if self._board[i][j]==value:
                    lista.append(i)
                    lista.append(j)
                    lista=[]
            matrica.append(lista)
        brojac=0
        for mat in matrica:
            i=mat[0]
            j=mat[1]
            if i == 0 and j == 0:
                if self._board[0][3] == "*" or self._board[3][0] == "*":
                    brojac = brojac + 1
            if i == 0 and j == 6:
                if self._board[0][3] == "*" or self._board[3][6] == "*":
                    brojac = brojac + 1
            if i == 6 and j == 0:
                if self._board[3][0] == "*" or self._board[6][3] == "*":
                    brojac = brojac + 1
            if i == 6 and j == 6:
                if self._board[6][3] == "*" or self._board[3][6] == "*":
                    brojac = brojac + 1
            if i == 1 and j == 1:
                if self._board[1][3] == "*" or self._board[3][1] == "*":
                    brojac = brojac + 1
            if i == 1 and j == 5:
                if self._board[1][3] == "*" or self._board[3][5] == "*":
                    brojac = brojac + 1
            if i == 5 and j == 1:
                if self._board[3][1] == "*" or self._board[5][3] == "*":
                    brojac = brojac + 1
            if i == 5 and j == 5:
                if self._board[5][3] == "*" or self._board[3][5] == "*":
                    brojac = brojac + 1
            if i == 2 and j == 2:
                if self._board[2][3] == "*" or self._board[3][2] == "*":
                    brojac = brojac + 1
            if i == 2 and j == 4:
                if self._board[2][3] == "*" or self._board[3][4] == "*":
                    brojac = brojac + 1
            if i == 4 and j == 2:
                if self._board[3][2] == "*" or self._board[4][3] == "*":
                    brojac = brojac + 1
            if i == 4 and j == 4:
                if self._board[4][3] == "*" or self._board[3][4] == "*":
                    brojac = brojac + 1
            if i == 0 and j == 3:
                if self._board[0][0] == "*" or self._board[1][3] == "*" or self._board[0][6] == "*":
                    brojac = brojac + 1
            if i == 3 and j == 0:
                if self._board[0][0] == "*" or self._board[3][1] == "*" or self._board[6][0] == "*":
                    brojac = brojac + 1
            if i == 3 and j == 6:
                if self._board[0][6] == "*" or self._board[3][5] == "*" or self._board[6][6] == "*":
                    brojac = brojac + 1
            if i == 6 and j == 3:
                if self._board[6][0] == "*" or self._board[5][3] == "*" or self._board[6][6] == "*":
                    brojac = brojac + 1
            if i == 2 and j == 3:
                if self._board[2][2] == "*" or self._board[1][3] == "*" or self._board[2][4] == "*":
                    brojac = brojac + 1
            if i == 3 and j == 2:
                if self._board[2][2] == "*" or self._board[3][1] == "*" or self._board[2][4] == "*":
                    brojac = brojac + 1
            if i == 3 and j == 4:
                if self._board[2][4] == "*" or self._board[3][5] == "*" or self._board[4][4] == "*":
                    brojac = brojac + 1
            if i == 4 and j == 3:
                if self._board[4][2] == "*" or self._board[5][3] == "*" or self._board[4][4] == "*":
                    brojac = brojac + 1
            if i == 1 and j == 3:
                if self._board[1][1] == "*" or self._board[0][3] == "*" or self._board[1][5] == "*" or \
                        self._board[2][3] == "*":
                    brojac = brojac + 1
            if i == 3 and j == 1:
                if self._board[1][1] == "*" or self._board[3][0] == "*" or self._board[3][2] == "*" or \
                        self._board[5][1] == "*":
                    brojac = brojac + 1
            if i == 3 and j == 5:
                if self._board[1][5] == "*" or self._board[3][4] == "*" or self._board[3][6] == "*" or \
                        self._board[5][5] == "*":
                    brojac = brojac + 1
            if i == 5 and j == 3:
                if self._board[5][1] == "*" or self._board[4][4] == "*" or self._board[4][6] == "*" or \
                        self._board[5][5] == "*":
                    brojac = brojac + 1
            if brojac==0:
                return False
            else:
                return True
    def prpolje(self,i,j,value):
        if i == 0 and j == 0:
            if self._board[0][3] == value:
                return 0,3
            if self._board[3][0] == value:
                return 3, 0
        if i == 0 and j == 6:
            if self._board[0][3] == value:
                return 0, 3
            if self._board[3][6] == value:
                return 3, 6
        if i == 6 and j == 0:
            if self._board[3][0] == value:
                return 3, 0
            if self._board[6][3] == value:
                return 6, 3
        if i == 6 and j == 6:
            if self._board[6][3] == value:
                return 6, 3
            if self._board[3][6] == value:
                return 3, 6
        if i == 1 and j == 1:
            if self._board[1][3] == value:
                return 1, 3
            if self._board[3][1] == value:
                return 3, 1
        if i == 1 and j == 5:
            if self._board[1][3] == value:
                return 1, 3
            if self._board[3][5] == value:
                return 3, 5
        if i == 5 and j == 1:
            if self._board[5][3] == value:
                return 5, 3
            if self._board[3][1] == value:
                return 3, 1
        if i == 5 and j == 5:
            if self._board[5][3] == value:
                return 5, 3
            if self._board[3][5] == value:
                return 3, 5
        if i == 2 and j == 2:
            if self._board[2][3] == value:
                return 2, 3
            if self._board[3][2] == value:
                return 3, 2
        if i == 2 and j == 4:
            if self._board[2][3] == value:
                return 2, 3
            if self._board[3][4] == value:
                return 3, 4
        if i == 4 and j == 2:
            if self._board[3][2] == value:
                return 3, 2
            if self._board[4][3] == value:
                return 4, 3
        if i == 4 and j == 4:
            if self._board[3][4] == value:
                return 3, 4
            if self._board[4][3] == value:
                return 4, 3
        if i == 0 and j == 3:
            if self._board[0][0] == value:
                return 0, 0
            if self._board[0][6] == value:
                return 0, 6
            if self._board[1][3] == value:
                return 1, 3
        if i == 3 and j == 0:
            if self._board[0][0] == value:
                return 0, 0
            if self._board[6][0] == value:
                return 6, 0
            if self._board[3][1] == value:
                return 3, 1
        if i == 3 and j == 6:
            if self._board[0][6] == value:
                return 0, 6
            if self._board[6][6] == value:
                return 6, 6
            if self._board[3][5] == value:
                return 3, 5
        if i == 6 and j == 3:
            if self._board[6][0] == value:
                return 6, 0
            if self._board[6][6] == value:
                return 6, 6
            if self._board[5][3] == value:
                return 5, 3
        if i == 2 and j == 3:
            if self._board[2][2] == value:
                return 2, 2
            if self._board[2][4] == value:
                return 2, 4
            if self._board[1][3] == value:
                return 1, 3
        if i == 3 and j == 2:
            if self._board[2][2] == value:
                return 2, 2
            if self._board[4][2] == value:
                return 4, 2
            if self._board[1][3] == value:
                return 1, 3
        if i == 3 and j == 4:
            if self._board[2][4] == value:
                return 2, 4
            if self._board[4][4] == value:
                return 4, 4
            if self._board[3][5] == value:
                return 3, 5
        if i == 4 and j == 3:
            if self._board[4][2] == value:
                return 4, 2
            if self._board[4][4] == value:
                return 4, 4
            if self._board[5][3] == value:
                return 5, 3
        if i == 1 and j == 3:
            if self._board[0][3] == value:
                return 0, 3
            if self._board[1][1] == value:
                return 1, 1
            if self._board[1][5] == value:
                return 1, 5
            if self._board[2][3] == value:
                return 2, 3
        if i == 3 and j == 1:
            if self._board[1][1] == value:
                return 1, 1
            if self._board[3][0] == value:
                return 3, 0
            if self._board[3][2] == value:
                return 3, 2
            if self._board[5][1] == value:
                return 5, 1
        if i == 3 and j== 5:
            if self._board[1][5] == value:
                return 1, 5
            if self._board[3][4] == value:
                return 3, 4
            if self._board[3][6] == value:
                return 3, 6
            if self._board[5][5] == value:
                return 5, 5
        if i == 5 and j == 3:
            if self._board[4][3] == value:
                return 4, 3
            if self._board[5][1] == value:
                return 5, 1
            if self._board[5][5] == value:
                return 5, 5
            if self._board[6][3] == value:
                return 6, 3
