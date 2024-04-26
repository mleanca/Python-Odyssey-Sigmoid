
# Înainte de a începe, trebuie să instalați librarie `sigmoid_check` rulând comanda `pip install sigmoid_check==0.0.3` în terminal

# Task: Creați o funcție cu numele "task_1" care va returna o listă cu numerele de la 1 la 10
def task_1():
    numbers = [i for i in range(1,6)]
    return numbers

print(task_1())
# [1, 2, 3, 4, 5]

#print(session.check_task_1(task_1))

# Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
# Utilizați list comprehension în proces
def task_2():
    squares = [i**2 for i in range(1, 11)]
    return squares

print(task_2())
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(session.check_task_2(task_2))

# Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
def task_3():
    odd_numbers = [i for i in range(1, 11) if (i % 2 != 0)]
    return odd_numbers

print(task_3())
# [1, 3, 5, 7, 9]
# print(session.check_task_3(task_3))

# Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
# va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
number_dictionary = [[1, 2], [3, 4], [5, 6]]

def task_4(argument):
    flattened = [num for row in argument for num in row]
    return flattened

print(task_4(number_dictionary))
# [1, 2, 3, 4, 5, 6]
# print(session.check_task_4(task_4))

# Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până la 10.
# Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
# Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
def task_5(n):
    result = [
        "par" if (i % 2 == 0) 
        else "impar"
        for i in range(1, n + 1)]
    return result

print(task_5(10))
# ['impar', 'par', 'impar', 'par', 'impar', 'par', 'impar', 'par', 'impar', 'par']
print(task_5(4))
#['impar', 'par', 'impar', 'par']
# print(session.check_task_5(task_5))

# Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care mappează fiecare număr de la 1 la 5 la cubul său.
# Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
# Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
def task_6(n):
    result = {i: i**3 for i in range(1, n + 1)}
    return result

print(task_6(5))
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
print(task_6(10))
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}  
# print(session.check_task_6(task_6))

# Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii de 3 de la 1 la n, unde n este un argument al funcției.
# Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
# Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
def task_7(n):
    result = {i for i in range(1, n + 1) if i % 3 == 0}
    return sorted(list(result))

print(task_7(50))
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
# print session.check_task_7(task_7))

# Task: Creați o funcție cu numele "task_8" care are ca argument o listă de numere și va returna media aritmetică a numerelor din listă.
# Exemplu: Pentru lista [1, 2, 3, 4, 5] rezultatul va fi 3.0
def task_8(list_argument):
    sum_of_numbers = sum(list_argument)
    avg_of_numbers = sum_of_numbers / len(list_argument)
    return avg_of_numbers

number_list1 = [5,6,7,8,9,10]
print(task_8(number_list1))
# 7.5
# print(session.check_task_8(task_8))

# Task: Creați o funcție cu numele "task_9" care are ca argument un număr și va returna `True` dacă numărul este par, altfel `False`.
# Exemplu: Pentru numărul 4 rezultatul va fi `True`, iar pentru numărul 5 rezultatul va fi `False`.
def task_9(n):
    if (n % 2 == 0):
        return True
    else:
        return False

print(task_9(3))
# False
print(task_9(8))
# True
# print(session.check_task_9(task_9))

# Task: Creați o funcție cu numele "task_10" care are ca argument numele și vârsta unei persoane ca argumente poziționale și orașul ca un argument opțional,
# apoi returnează o descriere a persoanei în forma "Nume: *nume*, Varsta: *varsta*, Oras: *oras*".
# Exemplu: Pentru numele "Ana", vârsta 32 și orașul "București" rezultatul va fi "Nume: Ana, Varsta: 32, Oras: București"
def task_10(name, age, city="Null"):
    print(f"Nume: {name}, Varsta: {age}, Oras: {city}")

task_10("Mihai", 23, "Chisinau")
# Nume: Mihai, Varsta: 23, Oras: Chisinau
task_10("Elena", 19)
# Nume: Elena, Varsta: 19, Oras: Null
# print(session.check_task_10(task_10))

# Task: Creați o funcție cu numele "task_11" care acceptă o listă variabilă de numere și returnează valoarea maximă.
# Exemplu: Pentru lista [10, 20, 30, 40, 50] rezultatul va fi 50
def task_11(list):
    print(max(list))
    
number_list2 = [55, 12, 39, 214, 210, 2314, 557]
task_11(number_list2)
# 2314
# print(session.check_task_11(task_11))

# Task: Creați o funcție cu numele "task_12" care acceptă un număr și returnează factorialul său.
# Exemplu: Pentru numărul 5 rezultatul va fi 120
def task_12(n):
    if n == 0:
        return 1
    else:
        return n * task_12(n - 1)
    
print(task_12(10))
# 3628800
# print(session.check_task_12(task_12))

# Task: Creați o funcție cu numele "task_13" care acceptă două numere și returnează suma și produsul lor.
# Exemplu: Pentru numerele 3 și 4 rezultatul va fi (7, 12)
def task_13(i, j):
    sum = i + j
    product = i * j
    return f"({sum}, {product})"

print(task_13(5, 10))
# (15, 50)
# print(session.check_task_13(task_13))

# Task: Creați o funcție cu numele "task_14" care acceptă un număr ce reprezintă vârsta unei persoane și returnează textul "minor" dacă vârsta este sub 18 ani, "adult" dacă vârsta este între 18 și 65 ani și "senior" dacă vârsta este peste 65 de ani.
# Exemplu: Pentru vârsta 32 rezultatul va fi "adult"
def task_14(age):
    if (age < 18):
        print("minor")
    elif (age == 18):
        print("adult")
    elif (age < 65):
        print("adult")
    else:
        print("senior")

task_14(32)
# adult
# print(session.check_task_14(task_14))

# Task: Creați o funcție cu numele "task_15" care acceptă un string și returnează `True` dacă string-ul este un palindrom, altfel `False`.
# Exemplu: Pentru string-ul "ana" rezultatul va fi `True`, iar pentru string-ul "test" rezultatul va fi `False`.
def task_15(s):
    invers = s[::-1] #python slicing technique to reverse order of elements in a sequence, a string in this case
    return invers == s

print(task_15("nursesrun"))
# True
print(task_15("check"))
# False
# print(session.check_task_15(task_15))

# Task: Creați o funcție cu numele "task_16" care acceptă un string și returnează același string cu literele inversate.
# Exemplu: Pentru string-ul "test" rezultatul va fi "tset"
def task_16(s):
    inversed = s[::-1]
    return inversed

print(task_16("coding"))
# gnidoc
# print(session.check_task_16(task_16))

# Task: Creați o funcție cu numele "task_17" care acceptă un string și returnează numărul de cuvinte din string.
# Exemplu: Pentru string-ul "Hello, World!" rezultatul va fi 2
def task_17(s):
    list_of_words = s.split()
    return len(list_of_words)

print(task_17("Happy birthday to you!"))
# 4
# print(session.check_task_17(task_17))

# Task: Creați o funcție cu numele "task_18" care acceptă un număr ce reprezintă temperatura în grade Celsius și returnează temperatura în grade Fahrenheit.
# Exemplu: Pentru temperatura 0 rezultatul va fi 32.0
def task_18(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"{temp_fahrenheit} degrees Fahreinheit")

task_18(0)
task_18(25)
# 32.0 degrees Fahreinheit
# 77.0 degrees Fahreinheit
# print(session.check_task_18(task_18))

# Task: Creați o funcție cu numele "task_19" care acceptă un număr și returnează `True` dacă numărul este prim, altfel `False`.
# Exemplu: Pentru numărul 7 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
def task_19(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1): #ensuring base range is the square root of the number itself, not anything less than itself
        if num % i == 0:
            return False
    return True

print(task_19(10))
# False
# print(session.check_task_19(task_19))

# Task: Creați o funcție cu numele "task_20" care acceptă un număr și returnează `True` dacă numărul este un număr perfect, altfel `False`.
# Un număr perfect este un număr întreg pozitiv care este egal cu suma divizorilor săi, excluzând numărul însuși.
# Exemplu: Pentru numărul 28 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
def task_20(num):
    pass
# print(session.check_task_20(task_20))

# Task: Creați o funcție cu numele "task_21" care acceptă un număr și returnează `True` dacă numărul este un număr Armstrong, altfel `False`.
# Un număr Armstrong este un număr care este egal cu suma puterilor sale de cifre.
# Exemplu: Pentru numărul 153 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.

# print(session.check_task_21(task_21))

# Task: Creați o funcție cu numele "task_22" care acceptă un număr și returnează `True` dacă numărul este un număr Harshad, altfel `False`.
# Un număr Harshad este un număr care este divizibil cu suma cifrelor sale.
# Exemplu: Pentru numărul 18 rezultatul va fi `True`, iar pentru numărul 14 rezultatul va fi `False`.

# print(session.check_task_22(task_22))

# Task: Creați o funcție cu numele "task_23" care primește ca argument un număr și returneaeză o listă cu primele n numere ale seriei Fibonacci.
# Exemplu: Pentru numărul 5 rezultatul va fi [0, 1, 1, 2, 3]

# print(session.check_task_23(task_23))

# Task: Creați o funcție cu numele "task_24" care primește ca argument un număr și returnează o listă cu divizorii numărului respectiv.
# Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]

# print(session.check_task_24(task_24))
# print(session.get_completion_percentage())