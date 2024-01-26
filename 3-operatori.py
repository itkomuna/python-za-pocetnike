####### OPERATORI  #######

# Vrste operatora
    # Aritmeticki 
    # Operatori dodele
    # Opeatori poredjenja
    # Logicki operatori

### PRIMERI ###

#########################
# Aritmeticki operatori #
#########################

# Sabiranje  + 
print(10 + 20)
a = 10
b = 5
c = a + b
print(c)

a = 'Renault'
b = 4
print(a + " " + str(b))

# Oduzimanje   -
a = 100
b = 20
print(a - b)

# Mnozenje   *
a = 8
b = 5
b = 'Loop'
print(a * b)

# Deljenje  /
a = 25
b = 5
c = a / b
print(c)
print(type(c))

# Celobrojno deljenje   //
a = 100
b = 50
c = a // b
print(type(c))

# Ostatak pri deljenju   %
a = 15
b = 4
c = a % b
print(type(c))

# Eksponent **
print(4 ** 3)

# Redosled operacija
print(3 + 4 + 5 - 2 * 10)
print((2 * 5) + (10 // 3))

####################
# Operatori dodele #
####################

# =
a = 100
print(a)

# +=
a = 50
a += 30 # a = 50 + 30
print(a)

#  -=
a = 50
a -= 10 # a = 50 - 10
print(a)

# *=
a = 5
a *= 20 # a = 5 * 20
print(a)

# /=
a = 100
a /= 5  # a = 100 /5
print(a)

########################
# Operatori poredjenja #
########################
# == Jednako sa  a == b
print(4 == 4.0)
print('Python' == 'Python')
a = 5
b = 5
print(a == b)

# !=  Nije jednako
print(100 != 1000)

# > Vece od
print(100 > 1)

# < Manje od
print(20 < 200)

# >= Vece i jednako od
print(100 >= 100)

# <= Manje i jednako od
print(100 <= 10)

print(100 + 1 > 10 + 5)

#####################
# Logicki operatori #
#####################
# and
# or
# not
print(10 < 20 and 100 > 80)

a = 5
print(a == 5 or a == 10)

a = 100
b = 10
print(not(a == b))
print(not(200 > 10))

