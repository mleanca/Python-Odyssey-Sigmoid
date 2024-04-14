phone_book = {
    "My": "078179905",
    "Tati": "079023513",
    "Mia": "1941848141"
}
#dictionary, with key and value

Set = {"New-York", "Chicago", "Chisinau"}
#unchangeable, unordered, unique items, only value

person = {
    "Mia": 5,
    "Mom": 65,
    "Tata": 70 
}

person2 = {
    "My": 32,
    "Tati": 40,
    "Zina": 41
}

list_persons = [person, person2]
print(list_persons)
print(len(list_persons))
print(len(person))
print(person.keys())
print(person.values())
# [{'Mia': 5, 'Mom': 65, 'Tata': 70}, {'My': 32, 'Tati': 40, 'Zina': 41}]
# 2
# 3
# dict_keys(['Mia', 'Mom', 'Tata'])
# dict_values([5, 65, 70])

# Hashing
# Hash function
# intersection function
# difference function
help(hash)