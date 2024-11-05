#exercise 5:
def difference(a, b):
    return a - b

def produit(a, b):
    return a * b

print(difference(7, 3)) 
print(produit(4, 5))    
##exercise 6:
def est_isocele(a, b, c):
    return a == b or a == c or b == c

def est_rectangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2

print(est_isocele(5, 5, 8))   
print(est_rectangle(3, 4, 5)) 
##exercise 7:
def lpp(a, b):
    return a if a < b else b

print(lpp(3, 7)) 
##exercise 8:
def valeur_absolue(x):
    return abs(x)

print(valeur_absolue(-10))  
##exercise 9:
def est_entier(x):
    return x == int(x)

print(est_entier(3))    
print(est_entier(3.0))  
print(est_entier(4.23)) 
##exercise 10:
def est_pair(n):
    return n % 2 == 0

print(est_pair(4))
print(est_pair(7))
##exercise 11:
def intervalle1(x):
    return -2 < x <= 3

def intervalle2(x):
    return x <= -3 or x >= 5

def intervalle3(x):
    return (-5 < x <= -3) or (0 <= x < 2)

def intervalle4(x):
    return (x > 0 and x != 1) or (x < 0 and x != -1)

print(intervalle1(2))   
print(intervalle2(-4))  
print(intervalle3(1))   
print(intervalle4(-2)) 
#exercise 12:
def signe(x):
    if x > 0:
        print("positif")
    elif x < 0:
        print("négatif")
    else:
        print("nul")

signe(3)  
signe(0)   
signe(-5) 
#exercise 13:
def est_bissextile(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print("bissextile")
    else:
        print("non bissextile")

est_bissextile(2024)  
est_bissextile(2100)  
#exercise 14
def somme_carres():
    S = 0
    for i in range(1, 11):
        S += i ** 2
    return S

print(somme_carres()) 
#exercise 15:
def somme_puissance_trois(n):
    S = 0
    for j in range(4, n + 1):
        S += 3 ** j
    return S

print(somme_puissance_trois(5))  
#exercise 16:
def somme_puissances(n, p):
    S = 0
    for k in range(1, n + 1):
        S += k ** p
    return S

print(somme_puissances(3, 2))
#exercise 17:
def mult_7(n):
    count = 0
    for i in range(1, n + 1):
        if i % 7 == 0:
            count += 1
    return count

def mult_7_pas_3_5(n):
    count = 0
    for i in range(1, n + 1):
        if i % 7 == 0 and i % 3 != 0 and i % 5 != 0:
            count += 1
    return count

print(mult_7(50))          
print(mult_7_pas_3_5(50))
#exercise 18:
def est_parfait(n):
    def somme_diviseurs(x):
        return sum(i for i in range(1, x) if x % i == 0)

    count = 0
    for i in range(1, n + 1):
        if somme_diviseurs(i) == i:
            count += 1
    return count

print(est_parfait(1000))  
#exercise 19:
def factorielle(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorielle(5))  
#exercise 20:
def suite_u(n):
    u = 4
    for _ in range(n):
        u = 2 - u / 2
    return u

def suite_F(n):
    F0, F1 = 0, 1
    for _ in range(n):
        F0, F1 = F1, F0 + F1
    return F0

print(suite_u(5))  
print(suite_F(5))  
#exercise 21:
def affichage():
    A = 1
    while A < 10:
        print(A)
        A += 2

# Exemple d'utilisation :
affichage()  # Affiche 1, 3, 5, 7, 9
#exercise 22:
def premier_entier():
    k = 0
    while k ** 2 < 1000:
        k += 1
    return k

print(premier_entier()) 
##exercise 23:
def somme_impairs(n):
    k = 1
    S = 0
    while k < n:
        S += k
        k += 2
    return S

print(somme_impairs(10))  
#exercise 24:
def nb_années(P):
    montant = 1000
    années = 0
    while montant <= P:
        montant *= 1.02
        années += 1
    return années

print(nb_années(2000))
#exercise 25:
def plus_gd_carré(n):
    i = 1
    while i ** 2 <= n:
        i += 1
    return (i - 1) ** 2

print(plus_gd_carré(20))  
#exercise 26:
def comptage(n):
    k = 1
    count = 0
    while k ** k <= n:
        count += 1
        k += 1
    return count

print(comptage(10)) 
#exercise 27:
def somme_diff_abs(n):
    S = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            S += abs(i - j)
    return S

print(somme_diff_abs(3))  
#exercise 28:
def mystere(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def nb_chiffres(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print(mystere(1234))    
print(nb_chiffres(1234))  
#exercise 29:
from math import sqrt

def carre_parfait(n):
    return int(sqrt(n)) ** 2 == n

def somme_carrés(n):
    S = 0
    for i in range(1, n + 1):
        if carre_parfait(i):
            S += i
    return S

print(carre_parfait(16))  
print(somme_carrés(10)) 
#exercise 30:
from random import choice

def pile_ou_Face():
    return choice(["pile", "face"])

print(pile_ou_Face()) 
#exercise 31:
from random import randint

def lancer_de_dé():
    return randint(1, 6)

print(lancer_de_dé()) 
#exercise 32:
from random import randint

def lancer_de_dé():
    return randint(1, 6)

def tirage_Monopoly():
    return lancer_de_dé() + lancer_de_dé()

print("Tirage Monopoly :", tirage_Monopoly()) 
#exercise 33:
from random import randint

def lancer_de_dé():
    return randint(1, 6)

def simulation(n):
    count = 0
    for _ in range(n):
        if lancer_de_dé() == 6:
            count += 1
    return count / n if n > 0 else 0  

print("Fréquence d'apparition de 6 sur 100 lancers :", simulation(100)) 
#exercise 35:
def est_pair(n):
    return n % 2 == 0

def syracuse(n, a):
    u = a
    for _ in range(n):
        if est_pair(u):
            u //= 2
        else:
            u = 3 * u + 1
    return u

def vol(a):
    valeurs = []
    while a != 1:
        valeurs.append(a)
        if est_pair(a):
            a //= 2
        else:
            a = 3 * a + 1
    valeurs.append(1)
    return valeurs

def temps_vol(a):
    count = 0
    while a != 1:
        a = 3 * a + 1 if not est_pair(a) else a // 2
        count += 1
    return count

def altitude_max(a):
    max_altitude = a
    while a != 1:
        a = 3 * a + 1 if not est_pair(a) else a // 2
        max_altitude = max(max_altitude, a)
    return max_altitude

print(syracuse(10, 7))      
print(vol(7))               
print(temps_vol(7))        
print(altitude_max(7))      