# Utwórz słownik filmów. Niech  kluczem będzie nazwa filmu, a parą wartości dwie liczby: kryteria wiekowe oraz liczba dostępnych biletów

movies = {"Bee Movie":[4,3], "Batman":[6,3], "Avengers":[13,7], "Spongebob-Film":[10,4]}

# Utwórz pętlę, która będzie działać w nieskończoność

while True:
    
    # Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca a następnie zamień frazę na format tytułowy (pierwsza litera każdego słowa jest wielka)

    movie = input("Podaj tytuł filmu: ").strip().title()
    
    # Stwórz instrukcję warunkową if. Jeśli wybrany film jest odostępny w słowniku, kontynuuj

    if movie in movies:
        
        # Zapytaj użytkownika o wiek

        age = int(input("Podaj swój wiek: "))
        
        # Sprawdź użytkownika pod kątem kwalifikowalności

        if age >= movies[movie][0]:
            
            # Jeśli użytkownik znajduje się w grupie docelowej, sprawdź dostępność miejsc

            if movies[movie][1] > 0:
                
                # Jeśli liczba dostępnych miejsc jest wartością dodatnią, zmiejsz pulę dostępnych miejsc o 1

                movies[movie][1] -= 1
                print("Sukces rezerwacji!")
                print("Pozostała liczba biletów:", movies[movie][1])
            else:
                print("Brak dostępnych biletów.")
        else:
            print("Za niski wiek.")
    else:

        print("Film nie jest dostępny.")
