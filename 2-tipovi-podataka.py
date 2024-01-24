### TIPOVI PODATAKA ###

### int ###
a = 3
b = 200
c = -200
print(a,b,c)
print(type(a))

### float ###
pi = 3.14
x = 4.7
y = -299.00
print(pi, x, y)
print(type(pi))

### complex ###
x = 2+3j
y = 1.5-4.8j
print(x)
print(y)
print(type(x))

### strings ###
a = 'Python je totalno ludilo, naucite ga'
print(a)
print(type(a))

### booleans ###
print(True)
print(False)
print(type(True))

### lists ###
liste  = [100, 'Python', 3.14, True, False, ['1', '2', '3']]
#          0       1       2     3      4          5 
#                                           [  0   1     2  ] 
print(liste)
print(type(liste))

### dictionaries (recnici) ###
kursevi = {'kurs':'python za pocetnike', 'predavac': 'Slobodan Miric'}
print(kursevi)
print(type(kursevi))

### tuples (torke) ###
kurs = ('python', 3, 'meseca')
#          0      1     2
print('Websites Worskhop ' + kurs[0] + ' kurs traje ' + str(kurs[1]) + " " + kurs[2])
print(type(kurs))

### sets (skupovi) ###
a = {'a', 'e' , 'i', 'o', 'u'}
print(type(a))
print(a)
