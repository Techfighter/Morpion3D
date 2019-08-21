import random
ran = random.randint(1, 27)
player = ["X","O","+","/","|","-","@","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","U","V","W"]

#Amélioration des ligne possible sur le principe de Karnot. 50% moins partie Null.
#Il y a jusqu'a 9 joueurs en même temps sur la grille, plus de défi meilleur équilibré.

#IA pourait être encore plus améliorée en retirant les coup aléatoire...
#Par exemple, elle pourait fermé d'avance des trajectoire possible a son adversaire.
#Ou faire des 'fourchettes' jusqu'a [5 en 1] ?

def computer():
    global a, b, c, d, e, f, g, h, i, aa, bb, cc, dd, ee, ff, gg, hh, ii, aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii, key, valide, ran, xo, ox, ia, z, joueur, player, test
    #computer 3d
    if int(joueur) < 3:
        test = 1
    else:
        test = int(joueur)
    for z in range(0, test):
        ia = player[z]
        """if (z == 0):
            ia = ox
        else:
            ia = xo"""
        #IA alterne les verrifications [Retarder adversaire, Complété une ligne]
        if ((cc == ia and bbb == ia and a == " ") or (gg == ia and ddd == ia and a == " ") or (f == ia and h == ia and a == " ") or (fff == ia and hh == ia and a == " ") or (ff == ia and hhh == ia and a == " ") or (b == ia and c == ia and a == " ") or (d == ia and g == ia and a == " ") or (e == ia and i == ia and a == " ") or (aa == ia and aaa == ia and a == " ") or (bb == ia and ccc == ia and a == " ") or (dd == ia and ggg == ia and a == " ") or (ee == ia and iii == ia and a == " ") or (eee == ia and ii == ia and a == " ")):
            key = "1"
        if ((ggg == ia and ff == ia and b == " ") or (gg == ia and fff == ia and b == " ") or (cc == ia and aaa == ia and b == " ") or (ddd == ia and ii == ia and b == " ") or (dd == ia and iii == ia and b == " ") or (aa == ia and ccc == ia and b == " ") or (f == ia and g == ia and b == " ") or (d == ia and i == ia and b == " ") or (hh == ia and eee == ia and b == " ") or (a == ia and c == ia and b == " ") or (e == ia and h == ia and b == " ") or (bb == ia and bbb == ia and b == " ") or (ee == ia and hhh == ia and b == " ")):
            key = "2"
        if ((fff == ia and ii == ia and c == " ") or (ff == ia and iii == ia and c == " ") or (aaa == ia and bb == ia and c == " ") or (aa == ia and bbb == ia and c == " ") or (ddd == ia and hh == ia and c == " ") or (dd == ia and hhh == ia and c == " ") or (d == ia and h == ia and c == " ") or (a == ia and b == ia and c == " ") or (g == ia and e == ia and c == " ") or (f == ia and i == ia and c == " ") or (cc == ia and ccc == ia and c == " ") or (eee == ia and gg == ia and c == " ") or (ee == ia and ggg == ia and c == " ")):
            key = "3"
        if ((cc == ia and hhh == ia and d == " ") or (ccc == ia and hh == ia and d == " ") or (bbb == ia and ii == ia and d == " ") or (bb == ia and iii == ia and d == " ") or (aa == ia and ggg == ia and d == " ") or (aaa == ia and gg == ia and d == " ") or (c == ia and h == ia and d == " ") or (e == ia and f == ia and d == " ") or (dd == ia and ddd == ia and d == " ") or (ee == ia and fff == ia and d == " ") or (eee == ia and ff == ia and d == " ") or (a == ia and g == ia and d == " ") or (b == ia and i == ia and d == " ")):
            key = "4"
        if ((ccc == ia and gg == ia and e == " ") or (cc == ia and ggg == ia and e == " ") or (aaa == ia and ii == ia and e == " ") or (aa == ia and iii == ia and e == " ") or (bbb == ia and hh == ia and e == " ") or (bb == ia and hhh == ia and e == " ") or (fff == ia and dd == ia and e == " ") or (ff == ia and ddd == ia and e == " ") or (a == ia and i == ia and e == " ") or (d == ia and f == ia and e == " ") or (g == ia and c == ia and e == " ") or (b == ia and h == ia and e == " ") or (ee == ia and eee == ia and e == " ")):
            key = "5"
        if ((ii == ia and ccc == ia and f == " ") or (cc == ia and iii == ia and f == " ") or (dd == ia and eee == ia and f == " ") or (aa == ia and hhh == ia and f == " ") or (aaa == ia and hh == ia and f == " ") or (a == ia and h == ia and f == " ") or (bbb == ia and gg == ia and f == " ") or (bb == ia and ggg == ia and f == " ") or (b == ia and g == ia and f == " ") or (d == ia and e == ia and f == " ") or (c == ia and i == ia and f == " ") or (ff == ia and fff == ia and f == " ") or (ee == ia and ddd == ia and f == " ")):
            key = "6"
        if ((cc == ia and eee == ia and g == " ") or (aa == ia and ddd == ia and g == " ") or (ii == ia and hhh == ia and g == " ") or (bb == ia and fff == ia and g == " ") or (bbb == ia and ff == ia and g == " ") or (b == ia and f == ia and g == " ") or (a == ia and d == ia and g == " ") or (e == ia and c == ia and g == " ") or (h == ia and i == ia and g == " ") or (gg == ia and ggg == ia and g == " ") or (dd == ia and aaa == ia and g == " ") or (hh == ia and iii == ia and g == " ") or (ee == ia and ccc == ia and g == " ")):
            key = "7"
        if ((eee == ia and bb == ia and h == " ") or (ggg == ia and ii == ia and h == " ") or (gg == ia and iii == ia and h == " ") or (aa == ia and fff == ia and h == " ") or (aaa == ia and ff == ia and h == " ") or (a == ia and f == ia and h == " ") or (ddd == ia and cc == ia and h == " ") or (dd == ia and ccc == ia and h == " ") or (c == ia and d == ia and h == " ") or (g == ia and i == ia and h == " ") or (b == ia and e == ia and h == " ") or (hh == ia and hhh == ia and h == " ") or (ee == ia and bbb == ia and h == " ")):
            key = "8"
        if ((aaa == ia and ee == ia and i == " ") or (aa == ia and eee == ia and i == " ") or (cc == ia and fff == ia and i == " ") or (gg == ia and hhh == ia and i == " ") or (bbb == ia and dd == ia and i == " ") or (bb == ia and ddd == ia and i == " ") or (b == ia and d == ia and i == " ") or (a == ia and e == ia and i == " ") or (g == ia and h == ia and i == " ") or (c == ia and f == ia and i == " ") or (ii == ia and iii == ia and i == " ") or (hh == ia and ggg == ia and i == " ") or (ff == ia and ccc == ia and i == " ")):
            key = "9"
        if ((bb == ia and cc == ia and aa == " ") or (dd == ia and gg == ia and aa == " ") or (ee == ia and ii == ia and aa == " ") or (a == ia and aaa == ia and aa == " ") or (b == ia and ccc == ia and aa == " ") or (d == ia and ggg == ia and aa == " ") or (e == ia and iii == ia and aa == " ") or (bbb == ia and c == ia and aa == " ") or (ddd == ia and g == ia and aa == " ") or (eee == ia and i == ia and aa == " ") or (ff == ia and hh == ia and aa == " ") or (f == ia and hhh == ia and aa == " ") or (fff == ia and hh == ia and aa == " ")):
            key = "11"
        if ((aa == ia and cc == ia and bb == " ") or (ee == ia and hh == ia and bb == " ") or (b == ia and bbb == ia and bb == " ") or (e == ia and hhh == ia and bb == " ") or (a == ia and ccc == ia and bb == " ") or (aaa == ia and c == ia and bb == " ") or (eee == ia and h == ia and bb == " ") or (ff == ia and gg == ia and bb == " ") or (dd == ia and ii == ia and bb == " ") or (f == ia and ggg == ia and bb == " ") or (d == ia and iii == ia and bb == " ") or (ddd == ia and i == ia and bb == " ") or (fff == ia and g == ia and bb == " ")):
            key = "22"
        if ((aa == ia and bb == ia and cc == " ") or (gg == ia and ee == ia and cc == " ") or (ff == ia and ii == ia and cc == " ") or (c == ia and ccc == ia and cc == " ") or (b == ia and aaa == ia and cc == " ") or (f == ia and iii == ia and cc == " ") or (e == ia and ggg == ia and cc == " ") or (fff == ia and i == ia and cc == " ") or (a == ia and bbb == ia and cc == " ") or (g == ia and eee == ia and cc == " ") or (dd == ia and hh == ia and cc == " ") or (d == ia and hhh == ia and cc == " ") or (ddd == ia and h == ia and cc == " ")):
            key = "33"
        if ((aa == ia and gg == ia and dd == " ") or (ee == ia and ff == ia and dd == " ") or (d == ia and ddd == ia and dd == " ") or (e == ia and fff == ia and dd == " ") or (a == ia and ggg == ia and dd == " ") or (aaa == ia and g == ia and dd == " ") or (eee == ia and f == ia and dd == " ") or (bb == ia and ii == ia and dd == " ") or (hh == ia and cc == ia and dd == " ") or (b == ia and iii == ia and dd == " ") or (h == ia and ccc == ia and dd == " ") or (bbb == ia and i == ia and dd == " ") or (hhh == ia and c == ia and dd == " ")):
            key = "44"
        if ((aa == ia and ii == ia and ee == " ") or (dd == ia and ff == ia and ee == " ") or (gg == ia and cc == ia and ee == " ") or (bb == ia and hh == ia and ee == " ") or (e == ia and eee == ia and ee == " ") or (a == ia and iii == ia and ee == " ") or (d == ia and fff == ia and ee == " ") or (g == ia and ccc == ia and ee == " ") or (b == ia and hhh == ia and ee == " ") or (aaa == ia and i == ia and ee == " ") or (ddd == ia and f == ia and ee == " ") or (ggg == ia and c == ia and ee == " ") or (bbb == ia and h == ia and ee == " ")):
            key = "55"
        if ((dd == ia and ee == ia and ff == " ") or (cc == ia and ii == ia and ff == " ") or (f == ia and fff == ia and ff == " ") or (e == ia and ddd == ia and ff == " ") or (eee == ia and d == ia and ff == " ") or (c == ia and iii == ia and ff == " ") or (ccc == ia and i == ia and ff == " ") or (bb == ia and gg == ia and ff == " ") or (b == ia and ggg == ia and ff == " ") or (bbb == ia and g == ia and ff == " ") or (hh == ia and aa == ia and ff == " ") or (h == ia and aaa == ia and ff == " ") or (hhh == ia and a == ia and ff == " ")):
            key = "66"
        if ((aa == ia and dd == ia and gg == " ") or (ee == ia and cc == ia and gg == " ") or (hh == ia and ii == ia and gg == " ") or (g == ia and ggg == ia and gg == " ") or (d == ia and aaa == ia and gg == " ") or (h == ia and iii == ia and gg == " ") or (e == ia and ccc == ia and gg == " ") or (a == ia and ddd == ia and gg == " ") or (c == ia and eee == ia and gg == " ") or (i == ia and hhh == ia and gg == " ") or (bb == ia and ff == ia and gg == " ") or (b == ia and fff == ia and gg == " ") or (f == ia and bbb == ia and gg == " ")):
            key = "77"
        if ((gg == ia and ii == ia and hh == " ") or (bb == ia and ee == ia and hh == " ") or (h == ia and hhh == ia and hh == " ") or (e == ia and bbb == ia and hh == " ") or (c == ia and ddd == ia and hh == " ") or (b == ia and eee == ia and hh == " ") or (g == ia and iii == ia and hh == " ") or (i == ia and ggg == ia and hh == " ") or (aa == ia and ff == ia and hh == " ") or (a == ia and fff == ia and hh == " ") or (aaa == ia and f == ia and hh == " ") or (cc == ia and dd == ia and hh == " ") or (ccc == ia and d == ia and hh == " ")):
            key = "88"
        if ((aa == ia and ee == ia and ii == " ") or (gg == ia and hh == ia and ii == " ") or (cc == ia and ff == ia and ii == " ") or (i == ia and iii == ia and ii == " ") or (h == ia and ggg == ia and ii == " ") or (f == ia and ccc == ia and ii == " ") or (e == ia and aaa == ia and ii == " ") or (c == ia and fff == ia and ii == " ") or (g == ia and hhh == ia and ii == " ") or (a == ia and eee == ia and ii == " ") or (bb == ia and dd == ia and ii == " ") or (b == ia and ddd == ia and ii == " ") or (d == ia and bbb == ia and ii == " ")):
            key = "99" 
        if ((bbb == ia and ccc == ia and aaa == " ") or (ddd == ia and ggg == ia and aaa == " ") or (eee == ia and iii == ia and aaa == " ")or (aa == ia and a == ia and aaa == " ") or (bb == ia and c == ia and aaa == " ") or (dd == ia and g == ia and aaa == " ") or (ee == ia and i == ia and aaa == " ") or (fff == ia and hhh == ia and aaa == " ") or (ff == ia and h == ia and aaa == " ") or (f == ia and hh == ia and aaa == " ") or (b == ia and cc == ia and aaa == " ") or (d == ia and gg == ia and aaa == " ") or (e == ia and ii == ia and aaa == " ")):
            key = "111"
        if ((aaa == ia and ccc == ia and bbb == " ") or (eee == ia and hhh == ia and bbb == " ") or (bb == ia and b == ia and bbb == " ") or (ee == ia and h == ia and bbb == " ") or (ddd == ia and iii == ia and bbb == " ") or (fff == ia and ggg == ia and bbb == " ") or (dd == ia and i == ia and bbb == " ") or (ff == ia and g == ia and bbb == " ") or (aa == ia and c == ia and bbb == " ") or (a == ia and cc == ia and bbb == " ") or (f == ia and gg == ia and bbb == " ") or (d == ia and ii == ia and bbb == " ") or (e == ia and hh == ia and bbb == " ")):
            key = "222"
        if ((aaa == ia and bbb == ia and ccc == " ") or (ggg == ia and eee == ia and ccc == " ") or (fff == ia and iii == ia and ccc == " ")or (cc == ia and c == ia and ccc == " ") or (bb == ia and a == ia and ccc == " ") or (ff == ia and i == ia and ccc == " ") or (ee == ia and g == ia and ccc == " ") or (ddd == ia and hhh == ia and ccc == " ") or (dd == ia and h == ia and ccc == " ") or (d == ia and hh == ia and ccc == " ") or (b == ia and aa == ia and ccc == " ") or (f == ia and ii == ia and ccc == " ") or (e == ia and gg == ia and ccc == " ")):
            key = "333"
        if ((aaa == ia and ggg == ia and ddd == " ") or (eee == ia and fff == ia and ddd == " ") or (dd == ia and d == ia and ddd == " ") or (ee == ia and f == ia and ddd == " ") or (bbb == ia and iii == ia and ddd == " ") or (hhh == ia and fff == ia and ddd == " ") or (bb == ia and i == ia and ddd == " ") or (hh == ia and f == ia and ddd == " ") or (b == ia and ii == ia and ddd == " ") or (h == ia and ff == ia and ddd == " ") or (e == ia and ff == ia and ddd == " ") or (aa == ia and g == ia and ddd == " ") or (a == ia and gg == ia and ddd == " ")):
            key = "444"
        if ((aaa == ia and iii == ia and eee == " ") or (ddd == ia and fff == ia and eee == " ") or (ggg == ia and ccc == ia and eee == " ") or (bbb == ia and hhh == ia and eee == " ") or (ee == ia and e == ia and eee == " ") or (hh == ia and b == ia and eee == " ") or (bb == ia and h == ia and eee == " ") or (gg == ia and c == ia and eee == " ") or (g == ia and cc == ia and eee == " ") or (dd == ia and f == ia and eee == " ") or (d == ia and ff == ia and eee == " ") or (aa == ia and i == ia and eee == " ") or (i == ia and aa == ia and eee == " ")):
            key = "555"
        if ((ddd == ia and eee == ia and fff == " ") or (ccc == ia and iii == ia and fff == " ") or (ff == ia and f == ia and fff == " ") or (ee == ia and d == ia and fff == " ") or (bbb == ia and ggg == ia and fff == " ") or (aaa == ia and hhh == ia and fff == " ") or (bb == ia and g == ia and fff == " ") or (aa == ia and h == ia and fff == " ") or (b == ia and gg == ia and fff == " ") or (a == ia and hh == ia and fff == " ") or (e == ia and dd == ia and fff == " ") or (cc == ia and i == ia and fff == " ") or (dd == ia and e == ia and fff == " ")):
            key = "666"
        if ((aaa == ia and ddd == ia and ggg == " ") or (eee == ia and ccc == ia and ggg == " ") or (hhh == ia and iii == ia and ggg == " ")or (gg == ia and g == ia and ggg == " ") or (dd == ia and a == ia and ggg == " ") or (hh == ia and i == ia and ggg == " ") or (ee == ia and c == ia and ggg == " ") or (aa == ia and d == ia and ggg == " ") or (cc == ia and e == ia and ggg == " ") or (h == ia and ii == ia and ggg == " ") or (bbb == ia and fff == ia and ggg == " ") or (bb == ia and f == ia and ggg == " ") or (b == ia and ff == ia and ggg == " ")):
            key = "777"
        if ((ggg == ia and iii == ia and hhh == " ") or (bbb == ia and eee == ia and hhh == " ") or (hh == ia and h == ia and hhh == " ") or (ee == ia and b == ia and hhh == " ") or (gg == ia and i == ia and hhh == " ") or (g == ia and ii == ia and hhh == " ") or (bb == ia and e == ia and hhh == " ") or (ddd == ia and ccc == ia and hhh == " ") or (dd == ia and c == ia and hhh == " ") or (d == ia and cc == ia and hhh == " ") or (aaa == ia and ff == ia and hhh == " ") or (aa == ia and f == ia and hhh == " ") or (a == ia and ff == ia and hhh == " ")):
            key = "888"
        if ((aaa == ia and eee == ia and iii == " ") or (ggg == ia and hhh == ia and iii == " ") or (ccc == ia and fff == ia and iii == " ") or (ii == ia and i == ia and iii == " ") or (hh == ia and g == ia and iii == " ") or (ff == ia and c == ia and iii == " ") or (ee == ia and a == ia and iii == " ") or (aa == ia and e == ia and iii == " ") or (cc == ia and f == ia and iii == " ") or (gg == ia and h == ia and iii == " ") or (bbb == ia and ddd == ia and iii == " ") or (bb == ia and d == ia and iii == " ") or (b == ia and dd == ia and iii == " ")):
            key = "999"
    #Si aucune case n'est encore remplit, Joue au hazard
    if (a == " " and b == " " and c == " " and d == " " and e == " " and f == " " and g == " " and h == " " and i == " " and aa == " " and bb == " " and cc == " " and dd == " " and ee == " " and ff == " " and gg == " " and hh == " " and ii == " " and aaa == " " and bbb == " " and ccc == " " and ddd == " " and eee == " " and fff == " " and ggg == " " and hhh == " " and iii == " "):
        print("coup au hazard!")
        if (ran == 1):
            key = "1"
        if (ran == 2):
            key = "2"
        if (ran == 3):
            key = "3"
        if (ran == 4):
            key = "4"
        if (ran == 5):
            key = "5"
        if (ran == 6):
            key = "6"
        if (ran == 7):
            key = "7"
        if (ran == 8):
            key = "8"
        if (ran == 9):
            key = "9"
        if (ran == 10):
            key = "11"
        if (ran == 11):
            key = "22"
        if (ran == 12):
            key = "33"
        if (ran == 13):
            key = "44"
        if (ran == 14):
            key = "55"
        if (ran == 15):
            key = "66"
        if (ran == 16):
            key = "77"
        if (ran == 17):
            key = "88"
        if (ran == 18):
            key = "99"
        if (ran == 19):
            key = "111"
        if (ran == 20):
            key = "222"
        if (ran == 21):
            key = "333"
        if (ran == 22):
            key = "444"
        if (ran == 23):
            key = "555"
        if (ran == 24):
            key = "666"
        if (ran == 25):
            key = "777"
        if (ran == 26):
            key = "888"
        if (ran == 27):
            key = "999"
    #Si au moins une case est occupé et qu'il n'y a rien a faire, Joue au hazard
    if (key == ""):
        valide = 0
        while (valide == 0):
            print("coup au hazard!")
            ran = random.randint(1, 27)
            if ((ran == 1 and a == " ") or (ran == 2 and b == " ") or (ran == 3 and c == " ") or (ran == 4 and d == " ") or (ran == 5 and e == " ") or (ran == 6 and f == " ") or (ran == 7 and g == " ") or (ran == 8 and h == " ") or (ran == 9 and i == " ") or (ran == 10 and aa == " ") or (ran == 11 and bb == " ") or (ran == 12 and cc == " ") or (ran == 13 and dd == " ") or (ran == 14 and ee == " ") or (ran == 15 and ff == " ") or (ran == 16 and gg == " ") or (ran == 17 and hh == " ") or (ran == 18 and ii == " ") or (ran == 19 and aaa == " ") or (ran == 20 and bbb == " ") or (ran == 21 and ccc == " ") or (ran == 22 and ddd == " ") or (ran == 23 and eee == " ") or (ran == 24 and fff == " ") or (ran == 25 and ggg == " ") or (ran == 26 and hhh == " ") or (ran == 27 and iii == " ")):
                if (ran == 1):
                    key = "1"
                if (ran == 2):
                   key = "2"
                if (ran == 3):
                    key = "3"
                if (ran == 4):
                    key = "4"
                if (ran == 5):
                    key = "5"
                if (ran == 6):
                    key = "6"
                if (ran == 7):
                    key = "7"
                if (ran == 8):
                    key = "8"
                if (ran == 9):
                    key = "9"
                if (ran == 10):
                    key = "11"
                if (ran == 11):
                    key = "22"
                if (ran == 12):
                    key = "33"
                if (ran == 13):
                    key = "44"
                if (ran == 14):
                    key = "55"
                if (ran == 15):
                    key = "66"
                if (ran == 16):
                    key = "77"
                if (ran == 17):
                    key = "88"
                if (ran == 18):
                    key = "99"
                if (ran == 19):
                    key = "111"
                if (ran == 20):
                    key = "222"
                if (ran == 21):
                    key = "333"
                if (ran == 22):
                    key = "444"
                if (ran == 23):
                    key = "555"
                if (ran == 24):
                    key = "666"
                if (ran == 25):
                    key = "777"
                if (ran == 26):
                    key = "888"
                if (ran == 27):
                    key = "999"
                valide = 1
    print("> ", key)

def display():
    global a, b, c, d, e, f, g, h, i, aa, bb, cc, dd, ee, ff, gg, hh, ii, aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii, key, valide, ran, xo, ox, ia, z, joueur, player, test
    print("STEP 1") 
    print(a,"|",b,"|",c,"   1|2|3") 
    print("- - - - -    - - -")
    print(d,"|",e,"|",f,"   4|5|6") 
    print("- - - - -    - - -")
    print(g,"|",h,"|",i,"   7|8|9") 
    print("")
    print("STEP 2")
    print(aa,"|",bb,"|",cc,"   11|22|33") 
    print("- - - - -    -- -- --")
    print(dd,"|",ee,"|",ff,"   44|55|66") 
    print("- - - - -    -- -- --")
    print(gg,"|",hh,"|",ii,"   77|88|99") 
    print("")    
    print("STEP 3")
    print(aaa,"|",bbb,"|",ccc,"   111|222|333") 
    print("- - - - -    --- --- ---")
    print(ddd,"|",eee,"|",fff,"   444|555|666") 
    print("- - - - -    --- --- ---")
    print(ggg,"|",hhh,"|",iii,"   777|888|999") 
    print("")

game = 0

print("TTTTTTT   AAA    SSS   SSS   EEEE  RRRR    AAA    CCC  TTTTTTT")
print("T  T  T  A   A  S     S      E     R   R  A   A  C     T  T  T")
print("   T     AAAAA   SSS   SSS   EE    RRRR   AAAAA  C        T   ")
print("   T     A   A      S     S  E     R  R   A   A  C        T   ")
print("  TTT    A   A   SSS   SSS   EEEE  R   R  A   A   CCC    TTT  ")
print("")
print("   M   M   OOO   RRRR   PPPP   III   OOO   N   N    333  DDD ")
print("   MM MM  O   O  R   R  P   P   I   O   O  NN  N       3 D  D")
print("   M M M  O   O  RRRR   PPPP    I   O   O  N N N ==  33  D  D")
print("   M   M  O   O  R  R   P       I   O   O  N  NN       3 D  D")
print("   M   M   OOO   R   R  P      III   OOO   N   N    333  DDD ")
print("")
print("JONATHAN BÉDARD 2018-2019")
print("")
print("ASTUCE:  ") 
print("  /      SERVEZ-VOUS DES DIAGONALS")
print(" X| |    SUR UNE BOUCLE ÉTENDUS.") 
print("/- - -/  CECI POUR TOUT LES ÉTAGES.")
print("  | |X   VOUS BLOQUEREZ PLUS D'UN") 
print(" - -/-   COUP AVEC CETTE FINTE.")
print("  |X|    ") 
print("")
    
while (game == 0):
    print("0 Joueur = CPU VS CPU.\n1 Joueur = YOU VS CPU.\n2 Joueur = YOU VS HIM.")
    joueur = input("Nombre de Joueur (0-9)? >")
    if (joueur == ""):
        joueur = 0
    print("")
    a = b = c = d  = e = f = g = h = i = aa = bb = cc = dd  = ee = ff = gg = hh = ii = aaa = bbb = ccc = ddd = eee = fff = ggg = hhh = iii = " "
    player = ["X","O","+","/","|","-","@","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","U","V","W"]
    xo = "X"
    ox = "O"
    coup = 27

    display()

    while (coup > 0):
        key = "" 
        print("Joueur", xo, "c'est a votre tour.")
        print("")
        
        if (xo == "X"): #player[27-coup]
            if (int(joueur) > 0):    
                key = input(">")
            else:
                computer()
        else:
            if (int(joueur) > 1):    
                key = input(">")
            else:
                computer()
                
        if (key == "1"):
            if (a == " "):
                a = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "2"):
            if (b == " "):
                b = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "3"):
            if (c == " "):
                c = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "4"):
            if (d == " "):
                d = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "5"):
            if (e == " "):
                e = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")            
        if (key == "6"):
            if (f == " "):
                f = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "7"):
            if (g == " "):
                g = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "8"):
            if (h == " "):
                h = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "9"):
            if (i == " "):
                i = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")

        if (key == "11"):
            if (aa == " "):
                aa = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "22"):
            if (bb == " "):
                bb = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "33"):
            if (cc == " "):
                cc = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "44"):
            if (dd == " "):
                dd = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "55"):
            if (ee == " "):
                ee = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")            
        if (key == "66"):
            if (ff == " "):
                ff = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "77"):
            if (gg == " "):
                gg = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "88"):
            if (hh == " "):
                hh = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "99"):
            if (ii == " "):
                ii = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "111"):
            if (aaa == " "):
                aaa = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "222"):
            if (bbb == " "):
                bbb = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "333"):
            if (ccc == " "):
                ccc = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "444"):
            if (ddd == " "):
                ddd = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "555"):
            if (eee == " "):
                eee = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")            
        if (key == "666"):
            if (fff == " "):
                fff = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "777"):
            if (ggg == " "):
                ggg = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "888"):
            if (hhh == " "):
                hhh = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "999"):
            if (iii == " "):
                iii = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        print("")
        display()
        
        if ((a == xo and b == xo and c == xo) or (a == xo and d == xo and g == xo) or (a == xo and e == xo and i == xo) or (g == xo and e == xo and c == xo) or (b == xo and e == xo and h == xo) or (c == xo and f == xo and i == xo) or (d == xo and e == xo and f == xo) or (g == xo and h == xo and i == xo) or (a == xo and aa == xo and aaa == xo) or (b == xo and bb == xo and bbb == xo) or (c == xo and cc == xo and ccc == xo) or (d == xo and dd == xo and ddd == xo) or (e == xo and ee == xo and eee == xo) or (f == xo and ff == xo and  fff == xo) or (g == xo and gg == xo and ggg == xo) or (h == xo and hh == xo and hhh == xo) or (i == xo and ii == xo and iii == xo) or (aa == xo and bb == xo and cc == xo) or (aa == xo and dd == xo and gg == xo) or (aa == xo and ee == xo and ii == xo) or (gg == xo and ee == xo and cc == xo) or (bb == xo and ee == xo and hh == xo) or (cc == xo and ff == xo and ii == xo) or (dd == xo and ee == xo and ff == xo) or (gg == xo and hh == xo and ii == xo) or (aaa == xo and bbb == xo and ccc == xo) or (aaa == xo and ddd == xo and ggg == xo) or (aaa == xo and eee == xo and iii == xo) or (ggg == xo and eee == xo and ccc == xo) or (bbb == xo and eee == xo and hhh == xo) or (ccc == xo and fff == xo and iii == xo) or (ddd == xo and eee == xo and fff == xo) or (ggg == xo and hhh == xo and iii == xo) or (a == xo and ee == xo and iii == xo) or (b == xo and ee == xo and hhh == xo) or (c == xo and ee == xo and ggg == xo) or (d == xo and ee == xo and fff == xo) or (f == xo and ee == xo and ddd == xo) or (g == xo and ee == xo and ccc == xo) or (h == xo and ee == xo and bbb == xo) or (i == xo and ee == xo and aaa == xo) or (a == xo and bb == xo and ccc == xo) or (c == xo and bb == xo and aaa == xo) or (d == xo and ee == xo and fff == xo) or (f == xo and ee == xo and ddd == xo) or (g == xo and hh == xo and iii == xo) or (i == xo and hh == xo and ggg == xo) or (a == xo and dd == xo and ggg == xo) or (g == xo and dd == xo and aaa == xo) or (b == xo and ee == xo and hhh == xo) or (h == xo and ee == xo and bbb == xo) or (c == xo and ff == xo and iii == xo) or (i == xo and ff == xo and ccc == xo) or (a == xo and f == xo and h == xo) or (c == xo and d == xo and h == xo) or (b == xo and f == xo and g == xo) or (b == xo and d == xo and i == xo) or (aa == xo and ff == xo and hh == xo) or (cc == xo and dd == xo and hh == xo) or (bb == xo and ff == xo and gg == xo) or (bb == xo and dd == xo and ii == xo) or (aaa == xo and fff == xo and hhh == xo) or (ccc == xo and ddd == xo and hhh == xo) or (bbb == xo and fff == xo and ggg == xo) or (bbb == xo and ddd == xo and iii == xo) or (a == xo and ff == xo and hhh == xo) or (c == xo and dd == xo and hhh == xo) or (b == xo and ff == xo and ggg == xo) or (b == xo and dd == xo and iii == xo) or (d == xo and ff == xo and eee == xo) or (f == xo and dd == xo and eee == xo) or (e == xo and dd == xo and fff == xo) or (e == xo and ff == xo and ddd == xo) or (a == xo and fff == xo and hh == xo) or (c == xo and ddd == xo and ii == xo) or (b == xo and eee == xo and ii == xo) or (b == xo and fff == xo and gg == xo) or (a == xo and cc == xo and bbb == xo) or (c == xo and aa == xo and ccc == xo) or (b == xo and aa == xo and ccc == xo) or (b == xo and c == xo and aaa == xo) or (g == xo and ii == xo and hhh == xo) or (i == xo and gg == xo and hhh == xo) or (h == xo and gg == xo and iii == xo) or (h == xo and ii == xo and ggg == xo) or (a == xo and gg == xo and ddd == xo) or (g == xo and aa == xo and ddd == xo) or (b == xo and aa == xo and ggg == xo) or (d == xo and gg == xo and aaa == xo) or (b == xo and hh == xo and eee == xo) or (h == xo and bb == xo and eee == xo) or (e == xo and bb == xo and hhh == xo) or (e == xo and hh == xo and bbb == xo) or (c == xo and ii == xo and fff == xo) or (i == xo and cc == xo and fff == xo) or (f == xo and cc == xo and iii == xo) or (f == xo and ii == xo and ccc == xo) or (a == xo and ii == xo and eee == xo) or (g == xo and cc == xo and eee == xo) or (e == xo and cc == xo and ggg == xo) or (e == xo and ii == xo and aaa == xo)):
            print(xo, "a Gagné!")
            print("")
            coup = 0
        else:
            if (coup == 0):
                print("Partie Null!")
                print("")
                
        if (int(joueur) == 9):#ok
            if (coup == 27 or coup == 18 or coup == 9 or coup == 0):
                xo = "X"
                ox = "O"
            if (coup == 26 or coup == 17 or coup == 8):
                xo = "O"
                ox = "+"
            if (coup == 25 or coup == 16 or coup == 7):
                xo = "+"
                ox = "/"
            if (coup == 24 or coup == 15 or coup == 6):
                xo = "/"
                ox = "|"
            if (coup == 23 or coup == 14 or coup == 5):
                xo = "|"
                ox = "-"
            if (coup == 22 or coup == 13 or coup == 4):
                xo = "-"
                ox = "@"
            if (coup == 21 or coup == 12 or coup == 3):
                xo = "@"
                ox = "Y"
            if (coup == 20 or coup == 11 or coup == 2):
                xo = "Y"
                ox = "Z"
            if (coup == 19 or coup == 10 or coup == 1):
                xo = "Z"
                ox = "X"
        
        if (int(joueur) == 8):#ok
            if (coup == 27 or coup == 19 or coup == 11 or coup == 3):
                xo = "X"
                ox = "O"
            if (coup == 26 or coup == 18 or coup == 10 or coup == 2):
                xo = "O"
                ox = "+"
            if (coup == 25 or coup == 17 or coup == 9 or coup == 1):
                xo = "+"
                ox = "/"
            if (coup == 24 or coup == 16 or coup == 8 or coup == 0):
                xo = "/"
                ox = "|"
            if (coup == 23 or coup == 15 or coup == 7):
                xo = "|"
                ox = "-"
            if (coup == 22 or coup == 14 or coup == 6):
                xo = "-"
                ox = "@"
            if (coup == 21 or coup == 13 or coup == 5):
                xo = "@"
                ox = "Y"
            if (coup == 20 or coup == 12 or coup == 4):
                xo = "Y"
                ox = "X"
        
        if (int(joueur) == 7):#ok
            if (coup == 27 or coup == 20 or coup == 13 or coup == 6):
                xo = "X"
                ox = "O"
            if (coup == 26 or coup == 19 or coup == 12 or coup == 5):
                xo = "O"
                ox = "+"
            if (coup == 25 or coup == 18 or coup == 11 or coup == 4):
                xo = "+"
                ox = "/"
            if (coup == 24 or coup == 17 or coup == 10 or coup == 3):
                xo = "/"
                ox = "|"
            if (coup == 23 or coup == 16 or coup == 9 or coup == 2):
                xo = "|"
                ox = "-"
            if (coup == 22 or coup == 15 or coup == 8 or coup == 1):
                xo = "-"
                ox = "@"
            if (coup == 21 or coup == 14 or coup == 7 or coup == 0):
                xo = "@"
                ox = "X"
        
        if (int(joueur) == 6):#ok
            if (coup == 27 or coup == 21 or coup == 15 or coup == 9 or coup == 3):
                xo = "X"
                ox = "O"
            if (coup == 26 or coup == 20 or coup == 14 or coup == 8 or coup == 2):
                xo = "O"
                ox = "+"
            if (coup == 25 or coup == 19 or coup == 13 or coup == 7 or coup == 1):
                xo = "+"
                ox = "/"
            if (coup == 24 or coup == 18 or coup == 12 or coup == 6 or coup == 0):
                xo = "/"
                ox = "|"
            if (coup == 23 or coup == 17 or coup == 11 or coup == 5):
                xo = "|"
                ox = "-"
            if (coup == 22 or coup == 16 or coup == 10 or coup == 4):
                xo = "-"
                ox = "X"
        
        if (int(joueur) == 5):#ok
            if (coup == 27 or coup == 22 or coup == 17 or coup == 12 or coup == 7 or coup == 2):
                xo = "X"
                ox = "O"
            if (coup == 26 or coup == 21 or coup == 16 or coup == 11 or coup == 6 or coup == 1):
                xo = "O"
                ox = "+"
            if (coup == 25 or coup == 20 or coup == 15 or coup == 10 or coup == 5 or coup == 0):
                xo = "+"
                ox = "/"
            if (coup == 24 or coup == 19 or coup == 14 or coup == 9 or coup == 4):
                xo = "/"
                ox = "|"
            if (coup == 23 or coup == 18 or coup == 13 or coup == 8 or coup == 3):
                xo = "|"
                ox = "X"
        
        if (int(joueur) == 4):#ok
            if (coup == 27 or coup == 23 or coup == 19 or coup == 15 or coup == 11 or coup == 7 or coup == 3):
                xo = "X"
                ox = "O"
            if (coup == 26 or coup == 22 or coup == 18 or coup == 14 or coup == 10 or coup == 6 or coup == 2):
                xo = "O"
                ox = "+"
            if (coup == 25 or coup == 21 or coup == 17 or coup == 13 or coup == 9 or coup == 5 or coup == 1):
                xo = "+"
                ox = "/"
            if (coup == 24 or coup == 20 or coup == 16 or coup == 12 or coup == 8 or coup == 4 or coup == 0):
                xo = "/"
                ox = "X"

        if (int(joueur) == 3):#ok
            if (coup == 27 or coup == 24 or coup == 21 or coup == 18 or coup == 15 or coup == 12 or coup == 9 or coup == 6 or coup == 3 or coup == 0):
                xo = "X"
                ox = "O"
            if (coup == 26 or coup == 23 or coup == 20 or coup == 17 or coup == 14 or coup == 11 or coup == 8 or coup == 5 or coup == 2):
                xo = "O"
                ox = "+"
            if (coup == 25 or coup == 22 or coup == 19 or coup == 16 or coup == 13 or coup == 10 or coup == 7 or coup == 4 or coup == 1):
                xo = "+"
                ox = "X"

        if (int(joueur) < 3):#ok
            if (coup == 26 or coup == 24 or coup == 22 or coup == 20 or coup == 18 or coup == 16 or coup == 14 or coup == 12 or coup == 10 or coup == 8 or coup == 6 or coup == 4 or coup == 2):
                xo = "O"
                ox = "X"
            else:
                xo = "X"
                ox = "O"
    
    print("Jouer une partie ?")
    key = input("[oui / non] >")
    if (key.upper() == "NON"):
        print("bye bye")
        exit()
    print("")
    
