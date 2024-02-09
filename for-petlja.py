# for <varijabla> in <niz>
    # <blok koda>

brojevi = list(range(0,5))
print(brojevi)

x = []
for i in range(1,6):
    y = i ** 2
    x.append(y)
print(x)
print(max(x))
print(min(x))

for i in range(1,10):
    print(i, end=" ")

print()

for i in range(5,15):
    print(i, end=" ")

print()

for i in range(0,10,3):
    print(i, end="")

print()

brojevi = [1,2,3,4,5,6,7,8,9,10]
for broj in brojevi:
    print(broj, end=",")

print()

for broj in brojevi:
    print(broj * 3)

print()

for x in brojevi:
    if x%2 == 0:
        print(f"Ispis parnog broja {x}")
    else:
        print(f"Ispis neparnog broja {x}")

print()

lista = [1,2,3,4,5]
zbir = 0
for broj in lista:
    zbir = zbir + broj
    print(zbir)

print()

neki_string = "Python je bonbonica, jako mi se svidja"
for i in neki_string:
    print(i, end="")

print()

band = ['james', 'lars', 'kirk', 'robert']
for member in band:
    print(f"{member.title()}, je clan benda Metallica")

print()
niz = [1,2,3,4,5,6,7,8,9,10]
broj = 15
pronadjen = False
for i in niz:
    if i == broj:
        pronadjen = True
        break
if pronadjen:
    print("Broj je pronadjen")
else:
    print("Broj nije pronadjen")

print()

predavaci = {
    'Boban': 'HTML i CSS',
    'Danijel': 'Javascript',
    'Jovana': 'React',
    'Sloba M': 'PHP i MySQL',
    'Zoran': 'Python i SQL',
    'Sloba Z': 'Python i SQL'
}
for predavac in predavaci:
    print(f"{predavac.title()} drago mi je da prenosis svoje znanje polaznicima")

print()

torka = ('python', 'php', 'java', 'dart', 'go')
for i in torka:
    print(i)

print()

putovanja = {'grcka', 'hrvatsku', 'italija', 'tajland'}
for put in putovanja:
    print(put)