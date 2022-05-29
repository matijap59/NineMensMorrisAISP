from State import *
import gameplay
def pobednickiraspored(tabla):
    brcr, brbl = tabla.brojcrnihibelih()
    a = tabla.razlikabrojablokiranihfigura1("B")
    b = tabla.razlikabrojablokiranihfigura1("W")
    if brbl == a or tabla.brojfigura("W") < 3:
        return 1
    if brcr == b or tabla.brojfigura("B") < 3:
        return -1
    else:
        return 0
def zatvoren(tabla):
    gameplay.BROJPOTEZA = gameplay.BROJPOTEZA - 1
    if gameplay.BROJPOTEZA%2==0:
        if gameplay.BROJPOTEZA in gameplay.LISTAMORISA:
            gameplay.BROJPOTEZA = gameplay.BROJPOTEZA + 1
            return 1
        else:
            gameplay.BROJPOTEZA = gameplay.BROJPOTEZA + 1
            return 0
    else:
        if gameplay.BROJPOTEZA in gameplay.LISTAMORISA:
            gameplay.BROJPOTEZA = gameplay.BROJPOTEZA + 1
            return -1
        else:
            gameplay.BROJPOTEZA = gameplay.BROJPOTEZA + 1
            return 0

def calculate_heuristic(tabla, faza):
    if faza == 1:
        vrednost =18*zatvoren(tabla)+26 * tabla.brojvezanihtrojki() + 9 * tabla.razlikabrojufigura() + 10 * (tabla.razlikabrojudvojkiunizu("B")-tabla.razlikabrojudvojkiunizu("W"))
        vrednost = vrednost+1 * (tabla.razlikabrojablokiranihfigura1("B") - tabla.razlikabrojablokiranihfigura1("W")) + 7 * tabla.razlikabrojutrojkidruginacin()
    if faza == 2:
        vrednost =14*zatvoren(tabla)+43 * tabla.brojvezanihtrojki() + 10 * (
                    tabla.razlikabrojablokiranihfigura1("B") - tabla.razlikabrojablokiranihfigura1("W")) + \
                   11 * tabla.razlikabrojufigura() +20*(tabla.razlikabrojudvojkiunizu("B")-tabla.razlikabrojudvojkiunizu("W"))+ 8 * tabla.razlikabrojuduplihtrojki() + 1086 * pobednickiraspored(tabla)
    return vrednost
