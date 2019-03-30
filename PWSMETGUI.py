from tkinter import *
import json
from itertools import permutations
from sympy import *
import time
import sys

file = "SituatiesJSON.json"

start_time = time.time()

# FUNCTIIES

def Expressionist(VergelijkingString, Vergelijkingen):
    for i in range(len(VergelijkingString)):
        iii = sympify(VergelijkingString[i])
        if iii not in Vergelijkingen:
            Vergelijkingen.append(iii)

def alphabet(word):
    if word[0] < word[-1]: return word
    else: return word[::-1]

def Thales(Punten, Cirkels, Relaties, Vergelijkingen, Symbolen):
    aP = 4
    permp = permutations(Punten,aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P4 = i[3]
        permc = permutations(Cirkels)
        for l in permc:
            c1 = l[0]
            L1 = Symbol(alphabet(str(P2)+str(P1)))
            L2 = Symbol(alphabet(str(P3)+str(P1)))
            RelatiesT = [
                [c1,P1,"0"],
                [c1,P2,"|"],
                [c1,P3,"|"],
                [c1,P4,"|"],
                [P1,[P2,P3],"|"],
                ]
            ExprsT = [L1-L2]
            hoek = P4
            result = all(elem in Relaties for elem in RelatiesT)
            resultexprs = all(elem in Vergelijkingen for elem in ExprsT)
            if result and resultexprs:
                hoekvar = alphabet(str(P2) + str(P4) + str(P3))
                hoekvar = Symbol(hoekvar)
                f = (hoekvar - 90)
                if f not in Vergelijkingen:
                    Vergelijkingen.append(f)
                    if hoekvar not in Symbolen: Symbolen.append(hoekvar)
                    print(f"Thales {f}")                    
                continue

def Pythagoras(Punten, Vergelijkingen, Symbolen):
    aP = 3
    permp = permutations(Punten,aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        hoek2 = Symbol(str(P1) + str(P2) + str(P3))
        hoek3 = hoek2 - 90
        if hoek3 in Vergelijkingen:
            AC = alphabet(str(P1) + str(P2))
            BC = alphabet(str(P3) + str(P2))
            AB = alphabet(str(P1) + str(P3))
            AC = Symbol(AC)
            BC = Symbol(BC)
            AB = Symbol(AB)
            f = AC**2 + BC**2 - AB**2
            if f not in Vergelijkingen:
                Vergelijkingen.append(f)
                if AC not in Symbolen: Symbolen.append(AC)
                if BC not in Symbolen: Symbolen.append(BC)
                if AB not in Symbolen: Symbolen.append(AB)
                print(f"Pythagoras {f}")

def somhoek(Punten, Vergelijkingen, Relaties, Symbolen):
    aP = 4
    permp = permutations(Punten,aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P4 = i[3]
        hoek1 = Symbol(alphabet(P3 + P2 + P1))
        hoek2 = Symbol(alphabet(P3 + P2 + P4))
        hoekcheck1 = hoek1 - 90
        hoekcheck2 = hoek2 - 90
        if (hoekcheck2 in Vergelijkingen) and (hoekcheck1 in Vergelijkingen):
            f = [P2,[P1,P4],"|"]
            if f not in Relaties:
                Relaties.append(f)
                if hoek1 not in Symbolen: Symbolen.append(hoek1)
                if hoek2 not in Symbolen: Symbolen.append(hoek2)
                print(f"Somhoek {f}")

def somlengte(Punten, Relaties, Vergelijkingen, Symbolen):
    aP = 3
    permp = permutations(Punten,aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        check = [P2,[P1,P3],"|"]
        if check in Relaties:
            L1 = Symbol(alphabet(str(P1) + str(P2)))
            L2 = Symbol(alphabet(str(P2) + str(P3)))
            L3 = Symbol(alphabet(str(P1) + str(P3)))
            f = L1 + L2 - L3
            if f not in Vergelijkingen:
                Vergelijkingen.append(f)
                if L1 not in Symbolen: Symbolen.append(L1)
                if L2 not in Symbolen: Symbolen.append(L2)
                if L3 not in Symbolen: Symbolen.append(L3)
                print(f"Somlengte {f}")

def gelijkbeendrieh(Punten, Vergelijkingen, Symbolen):
    aP = 3
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P1P2 = Symbol(alphabet(str(P1) + str(P2)))
        P1P3 = Symbol(alphabet(str(P1) + str(P3)))
        check = P1P2 - P1P3
        if check in Vergelijkingen:
            P1P2P3 = Symbol(alphabet(str(P1) + str(P2) + str(P3)))
            P1P3P2 = Symbol(alphabet(str(P1) + str(P3) + str(P2)))
            f = P1P2P3 - P1P3P2
            if f not in Vergelijkingen:
                Vergelijkingen.append(f)
                if P1P2P3 not in Symbolen: Symbolen.append(P1P2P3)
                if P1P3P2 not in Symbolen: Symbolen.append(P1P3P2)
                print(f"Gelijkbenige driehoeken: {P1P2P3} en {P1P3P2}")

def overstaandehoeken(Punten, Relaties, Vergelijkingen, Symbolen):
    aP = 5
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P4 = i[3]
        P5 = i[4]
        checka = [P1, [P2, P3], "|"]
        checkb = [P1, [P4, P5], "|"]
        if checka in Relaties and checkb in Relaties:
            P2P1P4 = Symbol(alphabet(str(P2) + str(P1) + str(P4)))
            P3P1P5 = Symbol(alphabet(str(P3) + str(P1) + str(P5)))
            f = P2P1P4 - P3P1P5
            if f not in Vergelijkingen:
                Vergelijkingen.append(f)
                if P2P1P4 not in Symbolen: Symbolen.append(P2P1P4)
                if P3P1P5 not in Symbolen: Symbolen.append(P3P1P5)
                print(f"Overstaande hoeken {P2P1P4} en {P3P1P5}")

def LHoeken(Punten, Relaties, Vergelijkingen, Symbolen):
    aP = 4
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P4 = i[3]
        check = [P3, [P2, P4], "|"]
        if check in Relaties:
            P1P2P3 = Symbol(alphabet(str(P1) + str(P2) + str(P3)))
            P1P2P4 = Symbol(alphabet(str(P1) + str(P2) + str(P4)))
            f = P1P2P3 - P1P2P4
            if f not in Vergelijkingen:
                Vergelijkingen.append(f)
                if P1P2P3 not in Symbolen: Symbolen.append(P1P2P3)
                if P1P2P4 not in Symbolen: Symbolen.append(P1P2P4)
                print(f"L-hoeken {P1P2P3}, {P1P2P4}")

def gestrektehoek(Punten, Relaties, Vergelijkingen, Symbolen):
    aP = 3
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        check = [P2, [P1, P3], "|"]
        if check in Relaties:
            P1P2P3 = Symbol(alphabet(str(P1) + str(P2) + str(P3)))
            f = P1P2P3 - 180
            if f not in Vergelijkingen:
                Vergelijkingen.append(f)
                if P1P2P3 not in Symbolen: Symbolen.append(P1P2P3)
                print(f"Gestrekte hoek {P1P2P3}")

def straalCirkel(Punten, Relaties, Vergelijkingen, Symbolen, Cirkels):
    aP = 3
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        permc = permutations(Cirkels)
        for l in permc:
            c = l[0]
            checka = [c, P1, "0"]
            checkb = [c, P2, "|"]
            checkc = [c, P3, "|"]
            if checka in Relaties and checkb in Relaties and checkc in Relaties:
                P1P2 = Symbol(alphabet(str(P1) + str(P2)))
                P1P3 = Symbol(alphabet(str(P1) + str(P3)))
                f = P1P2 - P1P3
                if f not in Vergelijkingen:
                    Vergelijkingen.append(f)
                    if P1P2 not in Symbolen: Symbolen.append(P1P2)
                    if P1P3 not in Symbolen: Symbolen.append(P1P3)
                    print(f"Straalcirkel {P1P2} = {P1P3}")

def FHoeken(Punten, Relaties, Vergelijkingen, Symbolen):
    aP = 5
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P4 = i[3]
        P5 = i[4]
        checka = [[P1, P2], [P3, P4], "//"]
        checkb = [P3, [P1, P5], "|"]
        if checka in Relaties and checkb in Relaties:
            P2P1P5 = Symbol(alphabet(str(P2) + str(P1) + str(P5)))
            P4P3P5 = Symbol(alphabet(str(P4) + str(P3) + str(P5)))
            f = P2P1P5 - P4P3P5
            if f not in Vergelijkingen:
                Vergelijkingen.append(f)
                if P2P1P5 not in Symbolen: Symbolen.append(P2P1P5)
                if P4P3P5 not in Symbolen: Symbolen.append(P4P3P5)
                print(f"Fhoeken {P2P1P5} en {P4P3P5}")

def gelijkvormdrieh(Punten, Relaties, Vergelijkingen, Symbolen):
    aP = 3
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        perma = permutations(Punten, aP)
        for ii in perma:
            P4 = ii[0]
            P5 = ii[1]
            P6 = ii[2]
            P1P2P3 = Symbol(alphabet(str(P1) + str(P2) + str(P3)))
            P4P5P6 = Symbol(alphabet(str(P4) + str(P5) + str(P6)))
            check = [[P1, P2, P3], [P4, P5, P6], "~"]
            if check in Relaties:
                P1P2 = Symbol(alphabet(str(P1) + str(P2)))
                P4P5 = Symbol(alphabet(str(P4) + str(P5)))
                P2P3 = Symbol(alphabet(str(P2) + str(P3)))
                P5P6 = Symbol(alphabet(str(P5) + str(P6)))
                f = (P1P2 / P4P5) - (P2P3 / P5P6)
                if f not in Vergelijkingen:
                    Vergelijkingen.append(f)
                    if P1P2 not in Symbolen: Symbolen.append(P1P2)
                    if P4P5 not in Symbolen: Symbolen.append(P4P5)
                    if P2P3 not in Symbolen: Symbolen.append(P2P3)
                    if P5P6 not in Symbolen: Symbolen.append(P5P6)
                    print(f"gelijkvormige driehoek: {f}")
    
def gelijkvormdriehhhh(Punten, Vergelijkingen, Relaties, Symbolen):
    """??????????????"""
    aP = 3
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        perma = permutations(Punten, aP)
        for ii in perma:
            P4 = ii[0]
            P5 = ii[1]
            P6 = ii[2]
            P1P2P3 = Symbol(alphabet(str(P1) + str(P2) + str(P3)))
            P1P3P2 = Symbol(alphabet(str(P1) + str(P3) + str(P2)))
            P4P5P6 = Symbol(alphabet(str(P4) + str(P5) + str(P6)))
            P4P6P5 = Symbol(alphabet(str(P4) + str(P6) + str(P5)))
            checka = P1P2P3 - P4P5P6
            checkb = P1P3P2 - P4P6P5
            if checka in Vergelijkingen and checkb in Vergelijkingen:
                f = [[P1, P2, P3], [P4, P5, P6], "~"]
                if f not in Relaties:
                    Relaties.append(f)
                    if P1P2P3 not in Symbolen: Symbolen.append(P1P2P3)
                    if P4P5P6 not in Symbolen: Symbolen.append(P4P5P6)
                    print(f"Driehoeken {P1P2P3} en {P4P5P6} zijn gelijkvormig volgens HHH")
            

def deellijnen(Punten, Relaties):
    aP = 4
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P4 = i[3]
        checka = [P3, [P1, P2], "|"]
        checkb = [P4, [P1, P3], "|"]
        if checka in Relaties and checkb in Relaties:
            f = [P3, [P1, P4], "|"]
            if f not in Relaties:
                Relaties.append(f)
                print(f"deellijnen {f}")

def evenwijdiglijn(Punten, Relaties):
    aP = 5
    permp = permutations(Punten, aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P4 = i[3]
        P5 = i[4]
        checka = [[P1, P2], [P3, P4], "//"]
        checkb = [P5, [P3, P4], "|"]
        if checka in Relaties and checkb in Relaties:
            f = [[P1, P2], [P3, P5], "//"]
            if f not in Relaties:
                Relaties.append(f)
                print(f"Lijnen {P1+P2} en {P3+P5} zijn evenwijdig")

def hoekensomdriehoek(Punten, Symbolen, Vergelijkingen):
    begintijdhoek = time.time()
    aP = 3
    permp = permutations(Punten,aP)
    for i in permp:
        P1 = i[0]
        P2 = i[1]
        P3 = i[2]
        P1P2P3 = Symbol(alphabet(str(P1) + str(P2) + str(P3)))
        P2P3P1 = Symbol(alphabet(str(P2) + str(P3) + str(P1)))
        P3P1P2 = Symbol(alphabet(str(P3) + str(P1) + str(P2)))
        f = P1P2P3 + P2P3P1 + P3P1P2 - 180
        if f not in Vergelijkingen:
            Vergelijkingen.append(f)
            if P1P2P3 not in Symbolen: Symbolen.append(P1P2P3)
            if P2P3P1 not in Symbolen: Symbolen.append(P2P3P1)
            if P3P1P2 not in Symbolen: Symbolen.append(P3P1P2)
    tijdd = (time.time() - begintijdhoek)
    print(f"{tijdd} seconds driehoekensom")
    print(len(Vergelijkingen))
    print(Vergelijkingen)


def antidoeler(Symbolen, DoelSymbool, antidoel):
    for e in Symbolen:
        if e not in DoelSymbool:
            if e not in antidoel:
                antidoel.append(e)

def algebra(Vergelijkingen, antidoel, OplosSymbool):
    print("Begonnen aan algebra")
    Exprstemp = Vergelijkingen.copy()
    subalgebra = []
    for x in antidoel:
        for ee in Exprstemp:
            a = solve(ee,x)
            if a:
                print(".", end="")
                Exprstemp.remove(ee)
                if len(a) == 1:
                    for i in range(len(Exprstemp)):
                        p = Exprstemp[i].subs(x, a[0])     
                        if p != 0:
                            subalgebra.append(p)
                elif len(a) == 2:
                    for i in range(len(Exprstemp)):
                        p = Exprstemp[i].subs(x, a[1])
                        if p != 0:
                            subalgebra.append(p)
                Exprstemp = subalgebra
                subalgebra = []
                break
            elif not a:
                continue 
    for e in Exprstemp:
        b = solve(e, OplosSymbool)
        if b:
            print(".", end="\n")
            print("Antwoord gevonden: ", end="")
            if len(b) == 1:
                print(f"{str(OplosSymbool)} = " + str(b[0]), end="")
            elif len(b) == 2:
                print(f"{str(OplosSymbool)} = " + str(b[1]), end="")
            stop()

def repeat(Punten, Vergelijkingen, Symbolen, Cirkels, Relaties, DoelSymbool, antidoel, OplosSymbool):
    print("...")
    Pythagoras(Punten, Vergelijkingen, Symbolen)
    Thales(Punten, Cirkels, Relaties, Vergelijkingen, Symbolen)
    somhoek(Punten, Vergelijkingen, Relaties, Symbolen)
    somlengte(Punten, Relaties, Vergelijkingen, Symbolen)
    gelijkbeendrieh(Punten, Vergelijkingen, Symbolen)
    overstaandehoeken(Punten, Relaties, Vergelijkingen, Symbolen)
    LHoeken(Punten, Relaties, Vergelijkingen, Symbolen)
    gestrektehoek(Punten, Relaties, Vergelijkingen, Symbolen)
    straalCirkel(Punten, Relaties, Vergelijkingen, Symbolen, Cirkels)
    FHoeken(Punten, Relaties, Vergelijkingen, Symbolen)
    gelijkvormdrieh(Punten, Relaties, Vergelijkingen, Symbolen)
    gelijkvormdriehhhh(Punten, Vergelijkingen, Relaties, Symbolen)
    deellijnen(Punten, Relaties)
    evenwijdiglijn(Punten, Relaties)
    hoekensomdriehoek(Punten, Symbolen, Vergelijkingen)
    antidoeler(Symbolen, DoelSymbool, antidoel)
    algebra(Vergelijkingen, antidoel, OplosSymbool)

def stop():
    tijd = (time.time() - start_time)
    print(f" in {tijd:.1f} seconden")
    sys.exit()

def jsonreader(filename, n):
    totaal = {}
    with open(filename, encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
    situatie = data[n]
    return situatie

def algoritme(n):
    start_time = time.time()
    Vergelijkingen = []
    antidoel = []
    subalgebra = []
    situatie = jsonreader(file, n)
    Punten = situatie["Punten"]
    Cirkels = situatie["Cirkels"]
    Relaties = situatie["Relaties"]
    VergelijkingString = situatie["VergelijkingString"]
    Symbolen = situatie["Symbolen"]
    for i in range(len(Symbolen)):
        Symbolen[i] = sympify(Symbolen[i])
    DoelSymbool = situatie["DoelSymbool"]
    for i in range(len(DoelSymbool)):
        DoelSymbool[i] = sympify(DoelSymbool[i])
    OplosSymbool = sympify(situatie["OplosSymbool"])
    Expressionist(VergelijkingString, Vergelijkingen)
    hoekensomdriehoek(Punten, Symbolen, Vergelijkingen)
    while True: repeat(Punten, Vergelijkingen, Symbolen, Cirkels, Relaties, DoelSymbool, antidoel, OplosSymbool)

def nverander():
    n = str(var.get())
    label1.configure(text=f"Situatie is nu {n}")
    return n

def uitvoer():
    algoritme(nverander())

window = Tk()
var = IntVar()

window.title("HOI")
window.geometry("350x200")

label1 = Label(window, text="Label 1", font=("Arial Bold", 14))
label1.grid(column=1, row=0)

rad1 = Radiobutton(window, text="Situatie 1", value=1, padx=10, variable=var, command=nverander, font=("Arial Bold", 14), indicatoron=0)
rad2 = Radiobutton(window, text="Situatie 2", value=2, padx=10, variable=var, command=nverander, font=("Arial Bold", 14), indicatoron=0)
rad3 = Radiobutton(window, text="Situatie 3", value=3, padx=10, variable=var, command=nverander, font=("Arial Bold", 14), indicatoron=0)
btn1 = Button(window, text="Klik hier om het algoritme te starten", command=uitvoer)

rad1.grid(column=0, row=0)
rad2.grid(column=0, row=1)
rad3.grid(column=0, row=2)
btn1.grid(column=0, row=3)

window.mainloop()
