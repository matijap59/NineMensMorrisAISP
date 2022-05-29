from math import inf
from Tree import TreeNode
from Tree import Tree
from heuristika import calculate_heuristic
from copy import deepcopy
from State import *

def pocetak(game,tabla,current_node,hash_map):
    dubina=4
    faza=2
    vr,redikolona=minimax(game,tabla,dubina,current_node,faza,hash_map)
    red=redikolona[0]
    kolona=redikolona[1]
    return red,kolona
def kraj(game,tabla,current_node,hash_map):
    dubina=3
    faza=1
    #vr,redikolona=minimax1(game,tabla,dubina,current_node,faza)
    vr,redikolona=minimax1(game, tabla, dubina, current_node, faza,hash_map)
    red=redikolona[0]
    kolona=redikolona[1]
    return red,kolona
def minimax(game,tabla,dubina,current_node,faza,hash_map,player="W",alpha=-float(inf),beta=float(inf)):
    if dubina==0:
        mogucipotezi = []
        figurecrne, figurebele = tabla.pozicijecrnihibelih()
        for beli in figurebele:
            x=beli[0]
            y=beli[1]
            if game.potez() == "B":
                mozetupotencijalno = tabla.mozetu(x, y, "B")
            if game.potez() == "W":
                mozetupotencijalno = tabla.mozetu(x, y, "W")
            if len(mozetupotencijalno)!=0:
                lista=[]
                lista.append(beli)
                lista.append(mozetupotencijalno)
                mogucipotezi.append(lista)
        for i in mogucipotezi:
            figura=i[0]
            figuradeo1=figura[0]
            figuradeo2=figura[1]
            potez=i[1:]
            for j in potez:
                for k in j:
                    potezdeo1=k[0]
                    potezdeo2=k[1]
                    pomocni=deepcopy(tabla)
                    if game.potez() == "B":
                        insertstanje = pomocni.zamenipolja2(figuradeo1, figuradeo2, potezdeo1, potezdeo2, "B")
                    if game.potez() == "W":
                        insertstanje = pomocni.zamenipolja2(figuradeo1, figuradeo2, potezdeo1, potezdeo2, "W")
        try:
            pomocni_state = pomocni.prebaciulistu()
            vrednost = hash_map[pomocni_state][0]
        except KeyError:
            pomocni_state=pomocni.prebaciulistu()
            vrednost = calculate_heuristic(tabla,faza)
            hash_map[pomocni_state] = vrednost, tabla
        return vrednost, (None, None)
    if player=="W":
        vrednost=-999999
        najboljipotez=None
        mogucipotezi=[]
        figurecrne,figurebele=tabla.pozicijecrnihibelih()
        for beli in figurebele:
            x=beli[0]
            y=beli[1]
            mozetupotencijalno=tabla.mozetu(x,y,"W")
            if len(mozetupotencijalno)!=0:
                lista=[]
                lista.append(beli)
                lista.append(mozetupotencijalno)
                mogucipotezi.append(lista)
        for i in mogucipotezi:
            #print(i)
            figura=i[0]
            figuradeo1=figura[0]
            figuradeo2=figura[1]
            potez=i[1:]
            for j in potez:
                for k in j:
                    potezdeo1=k[0]
                    potezdeo2=k[1]
                    pomocni=deepcopy(tabla)
                    pomocni.zamenipolja4(figuradeo1,figuradeo2,potezdeo1,potezdeo2,"W")
                    for current_child in current_node.children:
                        if pomocni==current_child.data:
                            new_node=current_child
                            break
                    else:
                        new_node=TreeNode(deepcopy(pomocni))
                        current_node.add_child(new_node)
                    try:
                        pomocni_state = pomocni.prebaciulistu()
                        new_value, new_state = hash_map[pomocni_state]
                    except KeyError:
                        pomocni_state = pomocni.prebaciulistu()
                        new_value, last_move = minimax(game, pomocni, dubina - 1, new_node, faza, hash_map, "B", alpha,beta)
                        hash_map[pomocni_state] = new_value, last_move
                    vrednost=max(vrednost,new_value)
                    alpha=max(alpha,vrednost)
                    if vrednost==new_value:
                        najboljipotez=(potezdeo1,potezdeo2)
                    if beta<=alpha:
                        break
        return vrednost, najboljipotez
    else:
        vrednost = 9999999
        najboljipotez = None
        mogucipotezi = []
        figurecrne, figurebele = tabla.pozicijecrnihibelih()
        for crne in figurecrne:
            x = crne[0]
            y = crne[1]
            mozetupotencijalno = tabla.mozetu(x, y, "B")
            if len(mozetupotencijalno) != 0:
                lista = []
                lista.append(crne)
                lista.append(mozetupotencijalno)
                mogucipotezi.append(lista)
        for i in mogucipotezi:
            figura = i[0]
            figuradeo1 = figura[0]
            figuradeo2 = figura[1]
            potez = i[1:]
            for j in potez:
                for k in j:
                    potezdeo1 = k[0]
                    potezdeo2 = k[1]
                    pomocni = deepcopy(tabla)
                    pomocni.zamenipolja4(figuradeo1, figuradeo2, potezdeo1, potezdeo2, "B")
                    for current_child in current_node.children:
                        if pomocni == current_child.data:
                            new_node = current_child
                            break
                    else:
                        new_node = TreeNode(deepcopy(pomocni))
                        current_node.add_child(new_node)
                    try:
                        pomocni_state = pomocni.prebaciulistu()
                        new_value, new_state = hash_map[pomocni_state]
                    except KeyError:
                        pomocni_state = pomocni.prebaciulistu()
                        new_value, last_move = minimax(game, pomocni, dubina - 1, new_node, faza, hash_map, "W", alpha,beta)
                        hash_map[pomocni_state] = new_value, last_move
                    vrednost = min(vrednost, new_value)
                    beta = min(beta, vrednost)
                    if vrednost == new_value:
                        najboljipotez = (potezdeo1, potezdeo2)
                    if beta <= alpha:
                        break
        return vrednost, najboljipotez
def minimax1(game,tabla,dubina,current_node,faza,hash_map,player="W",alpha=-float(inf),beta=float(inf)):
    if dubina==0:
        mogucipotezi=tabla.mogucepolje()
        for x,y in mogucipotezi:
            pomocni=deepcopy(tabla)
            if game.potez()=="B":
                pomocni.docrtaj(x,y,"B")
            if game.potez()=="W":
                pomocni.docrtaj(x,y,"W")
        a=game.potez()
        try:
            pomocni_state = pomocni.prebaciulistu()
            vrednost = hash_map[pomocni_state][0]
        except KeyError:
            pomocni_state = pomocni.prebaciulistu()
            vrednost = calculate_heuristic(tabla,faza)
            hash_map[pomocni_state] = vrednost, tabla                  #mzd ovo da sklonim
        return vrednost,(None,None)
    if player=="W":
        vrednost=-999999
        najboljipotez = None
        mogucipotezi=tabla.mogucepolje()
        for x,y in mogucipotezi:
            pomocni=deepcopy(tabla)
            pomocni.docrtaj(x,y,"W")
            for current_child in current_node.children:
                if pomocni==current_child.data:
                    new_node=current_child
                    break
            else:
                new_node=TreeNode(deepcopy(pomocni))
                current_node.add_child(new_node)
            try:
                pomocni_state=pomocni.prebaciulistu()
                new_value,new_state=hash_map[pomocni_state]
            except KeyError:
                pomocni_state = pomocni.prebaciulistu()
                new_value, last_move = minimax1(game, pomocni, dubina - 1, new_node, faza, hash_map, "B",alpha,beta)
                hash_map[pomocni_state]=new_value, last_move

            vrednost=max(vrednost,new_value)
            alpha=max(alpha,vrednost)
            if vrednost==new_value:
                najboljipotez=(x,y)
            if beta<=alpha:
                break
        return vrednost,najboljipotez
    else:
        vrednost=9999999
        najboljipotez = None
        mogucipotezi = tabla.mogucepolje()
        for x, y in mogucipotezi:
            pomocni = deepcopy(tabla)
            pomocni.docrtaj(x, y, "B")
            for current_child in current_node.children:
                if pomocni == current_child.data:
                    new_node = current_child
                    break
            else:
                new_node = TreeNode(deepcopy(pomocni))
                current_node.add_child(new_node)
            try:
                pomocni_state = pomocni.prebaciulistu()
                new_value, new_state = hash_map[pomocni_state]
            except KeyError:
                new_value, last_move = minimax1(game, pomocni, dubina - 1, new_node, faza, hash_map, "W",alpha,beta)
                hash_map[pomocni_state] = new_value, last_move

            vrednost = min(vrednost, new_value)
            beta = min(beta, vrednost)
            if vrednost == new_value:
                najboljipotez = (x, y)
            if beta <= alpha:
                break
        return vrednost, najboljipotez
