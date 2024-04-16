# Creați o variabilă numită number și atribuiți-i o valoare întreagă.
number = 18

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.
if number > 0:
    print("Numarul este pozitiv.")
# Numarul este pozitiv.

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.
if number % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul nu este par.")
# Numarul este par

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.
if number % 2 != 0:
    print("Numarul este impar.")
else:
    print("Numarul nu este impar.")
# Numarul nu este impar.

# Creați o variabilă text și atribuiți-i un șir de caractere.
text = """Clean Code book is about the best practices of writing elegant,
manageable, and readable code for developers. 
The book uses code examples in many programming languages,
like Java, C#, JavaScript, and many others."""
text_python = "Python"

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
if text_python in text:
    print("Textul contine cuvantul 'Python'.")
else:
    print("Textul nu contine cuvantul 'Python'.")
# Textul nu contine cuvantul 'Python'.

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.
text_java = "Java"
if text_java in text:
    print("Textul contine cuvantul 'Java'.")
else:
    print("Textul nu contine cuvantul 'Java'.")
# Textul contine cuvantul 'Java'.

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
if text_python in text:
    print("Textul contine cuvantul 'Python'.")
elif text_java in text:
    print("Textul contine cuvantul 'Java'.")
else:
    print("Textul nu conține niciunul dintre 'Python' sau 'Java'.")
# Textul contine cuvantul 'Java'.

# # Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# # În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# # Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
if text_python and text_java in text:
    print("Textul conține cuvantile 'Python' si 'Java'.")
else:
    print("Textul nu conține cuvantele 'Python' si 'Java'.")
# Textul conține cuvantile 'Python' si 'Java'.

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
number = int(input("Tastati un numar de la 1 la 5: ")) 
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
if number == 1:
    print("Unu")
# pentru 2 - printați "Doi"
elif number == 2:
    print("Doi")
# pentru 3 - printați "Trei"
elif number == 3:
    print("Trei")
# pentru 4 - printați "Patru"
elif number == 4:
    print("Patru")
# pentru 5 - printați "Cinci"
elif number == 5:
    print("Cinci")

