# Zapytaj użytkownika o nazwisko

name = input("Jakie masz imie?: ")

# Zapytaj użytkownika o wiek

age = input("Ile masz lat?: ")

# Zapytaj użytkownika o miasto
city = input("W jakim miescie mieszkasz?: ")

# Zapytaj użytkownika o jego zainteresowania
interest = input("Jakie sa twoje zainteresowania?: ")

# Utwórz tekst wyjściowy za pomocą formatowania ciągów

string = "Siemka {}, masz {} lat. Mieszkasz w  {} i kochasz {}!"

output = string.format(name,age,city,interest)

# Wydrukuj tekst wyjściowy
print(output)