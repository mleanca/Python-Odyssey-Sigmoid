surname = ['Smith', 'Drew', 'Lee', 'Vishna']
name = ['Chris', 'Sadie', 'Enya', 'Lola']

dictionary_comprehension = {name:surname for surname, name in zip(surname, name)}
print(dictionary_comprehension)
# {'Chris': 'Smith', 'Sadie': 'Drew', 'Enya': 'Lee', 'Lola': 'Vishna'}

dictionary_comprehension2 = {surname:name for surname, name in zip(surname, name)}
print(dictionary_comprehension2)
# {'Smith': 'Chris', 'Drew': 'Sadie', 'Lee': 'Enya', 'Vishna': 'Lola'}

dictionary_comprehension3 = {surname:name for name, surname in zip(surname, name)}
print(dictionary_comprehension3)

dictionary_comprehension4 = {surname:name for name, surname in zip(name, surname)}
print(dictionary_comprehension4)

list = [i for j in range(9) for g in range(7) for i in range(18) if j == 5]
print(list)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

for j in range(5):
    for i in range(5):
        print(i + 1, end = " ")