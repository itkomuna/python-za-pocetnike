# Tipovi podataka - mogu da ponesu jednu vrednost
    # integers
    # floats
    # bool
    # strings
# Strukture podataka - ako zelimo da u jednu promenljivu smestimo vise podataka i na taj nacim resavamo problem da nemamo samo jednu vrednost
    # liste
    # torke (tuples)
    # sets (skupovi)
    # dictionary (recnici)

#############
### LISTE ###
#############
vozac = 'Slobodan'
automobili = ['Renault', 'Peugeot', 'BMW', 'Mercedes', 'Audi']
#                 0          1        2         3         4
print(vozac + ' preferira u zadnjih 10ak godina ' + automobili[0])
print(len(automobili))

kurs = ['Backend', 3, 'Slobodan']
#           0      1       2 
print(kurs[0] + ' kurs traje ' + str(kurs[1]) + ' meseca i predavac je ' + kurs[2])

lista = [6, 'string neki', True, False, ['python', 'sql']]
print(type(lista))

#############
### TORKE ###
#############
program = ('html i css', 'python', 'django', 'sql')
print(program)
print(type(program))

ww_predavaci = ('sloba m.', 'boban', 'danijel', 'jovana', 'zoran', 'sloba z.')
print(ww_predavaci)
print(len(ww_predavaci))

termini = ('python i sql kurs', 3, True, 'Zoran', 'Slobodan')
print(termini)
print(termini[0] + ' traje ' + str(termini[1]) + ' meseca')

programski_jezici = 'python', 'sql', 'php', 'java', 'dart', 'php', 'c##'
print(type(programski_jezici))
print(programski_jezici[0] + ' je odlican izbor za bekend')

test = ('jedan',)
print(type(test))

############
### SETS ###
############
upis = {'februar', 'maj', 'septembar', 'decembar', 'februar', 'maj', 'septembar'}
print(upis)

test = {'stringovi', 3, 3.14, True}
print(test)

##################
### DICTIONARY ###
##################
#            key        value
kursevi = {'Sloba M': 'PHP i MySQL', 'Boban': 'HTML i CSS', 'Danijel': 'Javascript', 'Jovana': 'React', 'Zoran': 'Python i SQL', 'Sloba Z': 'Python i SQL'}
print(kursevi)
print(kursevi['Sloba M'])
print(kursevi['Sloba Z'])
print('Sloba Miric predaje ' + kursevi['Sloba M'] + ' a Sloba Zelic predeje ' + kursevi['Sloba Z'])

projekti = {'prvi projekat': 6, 'drugi projekat': [2,2,2]}
print('Prvi projekat traje ' + str(projekti['prvi projekat']) + ' meseci')
