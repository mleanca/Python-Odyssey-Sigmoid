# Creează un tuple numit `numbers` care să conțină numerele de la 1 la 5
numbers = (2,3,4,1,5)
# Acum afișează tuple `numbers`
print(numbers)
# (2, 3, 4, 1, 5)

# Acum adaugă numărul 6 la tuple `numbers`
numbers_list = list(numbers)
numbers_list.append(6)
numbers = tuple(numbers_list)
# Acum afișează tuple `numbers`
print(numbers)
# (2, 3, 5, 1, 5, 6)

# Afișați primul element din tuple `numbers`
print(numbers[0])
# 2

# Afișeați ultimul element din tuple `numbers`
print(numbers[-1])
# 6

# Afișeați primele două elemente din tuple `numbers`
print(numbers[:2])
# (2, 3)
print(numbers[-6:-4])
# (2, 3)

# Afișeați ultimele două elemente din tuple `numbers`
print(numbers[-2:])
# (5, 6)
print(numbers[4:])
# (5, 6)

# Afișați lungimea tuple `numbers`
print(len(numbers))
# 6

# Afișați suma elementelor din tuple `numbers`
print(sum(numbers))
# 21

# Schibați elementul de la poziția 2 din tuple `numbers` cu 10
numbers_list = list(numbers)
numbers_list[2] = 10
numbers = tuple(numbers_list)
# Afișați tuple `numbers`
print(numbers)
# (2, 3, 10, 1, 5, 6)

# Ștergeți tuple `numbers`
del numbers
