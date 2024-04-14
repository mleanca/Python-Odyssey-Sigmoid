# Creați un set gol numit `numbers_set`
numbers_set = {}

# Acum adăugați numerele de la 1 la 5 în setul `numbers_set`
numbers_set = {3, 5, 4, 1, 2}

# Acum afișați setul `numbers_set`
print(numbers_set)
#{1, 2, 3, 4, 5}

# Acum adăugați numărul 6 la setul `numbers_set`
numbers_set.add(6)

# Acum adaugă numerele de la 1 la 5 în setul `numbers_set` folosind metoda update()
numbers_set.update({1, 3, 5, 2, 4})
print(numbers_set)
# {1, 2, 3, 4, 5, 6}

# Extrageți numărul 3 din setul `numbers_set`
numbers_set.remove(3)

# Ștergeți un număr inexistent din setul `numbers_set` fără a genera o eroare
numbers_set.discard(8)

# Verificați dacă numărul 3 există în setul `numbers_set`
print(numbers_set)
# {1, 2, 4, 5, 6}

# Verificați elementele comune din setul `numbers_set` și setul {4, 5, 6, 7}
common_elements = numbers_set.intersection({4, 5, 6, 7})
print(common_elements)
# {4, 5, 6}

# Verificați dacă setul `numbers_set` este un subset al setului {1, 2, 3, 4, 5, 6, 7}
numbers_set2 = {1, 2, 3, 4, 5, 6, 7}
print(numbers_set.issubset(numbers_set2))
# True

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un subset al setului `numbers_set`
print(numbers_set2.issubset(numbers_set))
# False

# Verificați dacă setul `numbers_set` este un superset al setului {1, 2, 3, 4, 5, 6, 7}
print(numbers_set.issuperset(numbers_set2))
# False

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un superset al setului `numbers_set`
print(numbers_set2.issuperset(numbers_set))
# True

# Afișați lungimea setului `numbers_set`
print(len(numbers_set))
# 5

# Ștergeți toate elementele din setul `numbers_set`
numbers_set.clear()
# Afișați setul `numbers_set` pentru a verifica dacă a fost șters
print(numbers_set)
#set()