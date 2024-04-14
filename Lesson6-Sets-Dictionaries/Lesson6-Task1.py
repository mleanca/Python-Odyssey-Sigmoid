# Creați un dicțioar gol
person = {}

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "name" și valoarea fiind "John"
# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "age" și valoarea fiind 30
person = {
    "name": "John",
    "age": 30
}

# Acum afișați dicționarul
print(person)
# {'name': 'John', 'age': 30}

# Acum ștergeți cheia "name" din dicționar
del person["name"]

# Acum afișați dicționarul
print(person)
# {'age': 30}

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "city" și valoarea fiind "New York" folosind metoda setdefault()
person.setdefault("city", "New York")

# Afișați toate cheile din dicționar
print(person.keys())
# dict_keys(['age', 'city'])

# Afișați toate valorile din dicționar
print(person.values())
# dict_values([30, 'New York'])

# Afișați toate perechile de cheie-valoare din dicționar folosind metoda items()
print(person.items())
# dict_items([('age', 30), ('city', 'New York')])

# Afișați numărul de perechi de cheie-valoare din dicționar
print(len(person))
# 2

# Extrageți valoarea unei chei inexistente fără a genera o eroare
print(person.get("name"))
# None

# Acum actualizați dicționarul cu un alt dicționar, folosind metoda update()
likes = {
    "pizza": "margarita",
    "movie": "Dune",
    "sport": "volleyball"
}
person.update(likes)
print(person)
# {'age': 30, 'city': 'New York', 'pizza': 'margarita', 'movie': 'Dune', 'sport': 'volleyball'}

# Setați valoarea cheii "pizza" la 10 folosind metoda setdefault()
likes.setdefault("pizza", 10)
# Afișați dicționarul
print(person)
# nu se schimba nimic, deoarece chieie "pizza" deja exista
# {'age': 30, 'city': 'New York', 'pizza': 'margarita', 'movie': 'Dune', 'sport': 'volleyball'}

# Ștergeți cheia "pizza" din dicționar folosind metoda pop()
person.pop("pizza")
# Afișați dicționarul
print(person)
# {'age': 30, 'city': 'New York', 'movie': 'Dune', 'sport': 'volleyball'}

# Ștergeți toate perechile de cheie-valoare din dicționar
person.clear()
# Afișați dicționarul
print(person)
# {}