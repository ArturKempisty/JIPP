import random
# Stwórz listę "questions" składającą się z 3 pytań, które często zadają dzieci

questions = ["Czemu czekolada jest brazowa?\n","Co ma piernik do wiatraka?\n","Czy slonce spi w nocy?\n"]
answer = ""
# Wybierz losowe pytanie z danej listy za pomocą instrukcji warunkowej
while answer != "to wszystko":
    question = random.choice(questions)
# Zadaj wybrane pytanie za pomocą funkcji input()
# Pytania muszą zachować jednolite formatowanie
# Aby to uzyskać, przekonwertuje wszystkie odpowiedzi na małe litery i usuń wszelkie nadmiarowe spacje

    answer = input(question).strip().lower()

# Poczekaj do czasu, aż użytkownik wprowadzi hasło „To wszystko”

# Wyświetl wiadomość

print("Gituwa, brak pytan")