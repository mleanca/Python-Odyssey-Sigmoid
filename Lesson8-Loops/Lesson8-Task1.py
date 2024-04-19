# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().
numbers_list = []

for number in range(1, 11):
    numbers_list.append(number)
    
print(numbers_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.
for number in numbers_list:
    if number % 2 == 0:
        print(number)
# 2
# 4
# 6
# 8
# 10

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.
i = 1

while i < 6:
    print(i)
    i += 1
# 1
# 2
# 3
# 4
# 5

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.
person = {
    'name': 'Max',
    'age': 30,
    'city': 'Chisinau'
}

for key, value in person.items():
    print(key, ":", value)
# name : Max
# age : 30
# city : Chisinau

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.
matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]

for row in matrix:
    print(f"Row:  {row}")
    for numbers in row:
        print(f"Number: {numbers}")
        
# Row:  [1, 2, 3, 4, 5]
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
# Row:  [6, 7, 8, 9, 10]
# Number: 6
# Number: 7
# Number: 8
# Number: 9
# Number: 10
# Row:  [11, 12, 13, 14, 15]
# Number: 11
# Number: 12
# Number: 13
# Number: 14
# Number: 15

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.
for i in range(1, 10):
    if i > 10:
        break
    print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.
numbers_list2 = [23,42,56,18,99,37]

for i, numbers in enumerate(numbers_list2):
    print(i, ":", numbers)
# 0 : 23
# 1 : 42
# 2 : 56
# 3 : 18
# 4 : 99
# 5 : 37

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.
capitals = ["Chisinau", "Bucharest", "Belgrade", "Kiev"]
countries = ["Moldova", "Romania", "Serbia", "Ukraine"]

for capital, country in zip(capitals, countries):
    print(capital, ":", country)
# Chisinau : Moldova
# Bucharest : Romania
# Belgrade : Serbia
# Kiev : Ukraine

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().
numbers_list3 = []

for i in range(1, 11):
    numbers_list3.append(i)
    
print(numbers_list3)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.
first_element = numbers_list3[0]

while first_element <= 50:
    for i in range(len(numbers_list3)):
        numbers_list3[i] *= 2
    first_element = numbers_list3[0]
    
if first_element > 50:
    print("First element", numbers_list3[0], "is greater than 50.")
    
print(numbers_list3)
# First element 64 is greater than 50.
# [64, 128, 192, 256, 320, 384, 448, 512, 576, 640]

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].
square_numbers_list = []

for number in range(len(numbers_list3)):
    square_number = number ** 2
    if square_number <= 100:
        square_numbers_list.append(square_number)
        
print(square_numbers_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.
product_numbers_list = []
multiplier = 7

for number in range(len(numbers_list3)):
    number *= multiplier
    product_numbers_list.append(number)
    
print(product_numbers_list)
# [0, 7, 14, 21, 28, 35, 42, 49, 56, 63]

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.
i = [1,2,3,4,5]
j = [5,4,3,2,1]
numbers_list4 = []

for numbers_i, numbers_j in zip(i, j):
    numbers_list4.append((numbers_i, numbers_j))

print(numbers_list4)
[(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .
for numbers_i, numbers_j in numbers_list4:
    if numbers_i < numbers_j:
        print(numbers_i, ":", numbers_j)
# 1 : 5
# 2 : 4

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".
for number in square_numbers_list:
    if number > 10:
        print("First number that is greater than 10:", number)
        break
    
if number <= 10:
    print("There are no values greater than 10")
# First number that is greater than 10: 16

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
for i in range(5):
    print("*  *  *  *  *")
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *

# Folosind for sau while loops realizați afișările de mai jos
i = 1 
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")  
        j += 1
    print()
    i += 1      
# 1
# 12
# 123
# 1234
# 12345



# 54321
# 5432
# 543
# 54
# 5



# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g



# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+


# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243



# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.