# Prosty program kalkulatora

# Utwórz funkcję dodawania dwóch liczb
def add(a, b):
    return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    if b == 0:
        return "Blad: dzielenie przez zero!"
    return a / b


# Wyświetl listę operacji
print("Wybierz operacje.")
print("a. Dodawanie")
print("b. Odejmowanie")
print("c. Mnozenie")
print("d. Dzielenie")

# Pozwól użytkownikowi wybrać żądane działanie
op = input("Wybierz: (a/ b/ c/ d): ")

# Przechwyć 2 liczby wprowadzone przez użytkownika
num1 = float(input("Pierwsza liczba: "))
num2 = float(input("Druga liczba: "))

# Logika do wykonywania określonej operacji
if op == 'a':
    print("Wynik:", add(num1, num2))

elif op == 'b':
    print("Wynik:", subtract(num1, num2))

elif op == 'c':
    print("Wynik:", multiply(num1, num2))

elif op == 'd':
    print("Wynik:", divide(num1, num2))

# Jeśli użytkownik wybierze operację, która nie jest dostępna
else:
    print("Nieprawidlowa operacja!!!")