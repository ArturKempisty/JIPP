# Zliczanie samogłosek i spółgłosek w tekście

tekst = "Programowanie Pythona"

samogloski = "aeiouyąę"
vowels = 0
consonants = 0

# Iteracja po tekście i wypisanie znaków
for znak in tekst:
    print(znak)

# Liczenie samogłosek i spółgłosek
for znak in tekst:
    znak = znak.lower()
    if znak.isalpha():
        if znak in samogloski:
            vowels += 1
        else:
            consonants += 1

# Wyniki
print("Liczba samogłosek:", vowels)
print("Liczba spółgłosek:", consonants)
