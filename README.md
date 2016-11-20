# Twórcy:
	Krzysztof Benirowski
	Hubert Stanik


# Projekt nr 1:
	Firma kurierska - prosty system śledzenia przesyłek
	

# Technologia wykonania projektu:
	Python 3.5.2
	Django 1.10.3
	SQLite
	
	
# Struktura folderów:
* kurierproject - główny folder django
* tracking - główny folder aplikacji
 * migrations - folder z migracjami SQLite
 * static
     + tracking - folder z plikami css
 * templates
     + tracking - folder z szablonami stron
	
	
# Działanie:
1. Przejść do głównego folderu, który zawiera manage.py
2. Uruchomić serwer poleceniem "python manage.py runserver"
3. Otworzyć stronę "http://127.0.0.1:8000/tracking/" w przeglądarce
4. Wybrać jedną z opcji, "a" - śledzić przesylke, "b" - dodać nowy event do bazy
 	- opcja a)
		1. W polu Package id podać numer przesyłki (np: 1200, 1)
		2. Wcisnąć przycisk "Track"
		3. W przypadku nie odnalezienia w bazie niczego dla danego numery wyświetlony zostanie komunikat
		4. W przypadku podania prawidłowego numeru w tabeli poniżej pokaże się historia
	- opcja b)
		1. Uzupełnić wszystkie pola
		2. Wcisnąć przycisk "Create new entry"
		3. W przpadku podania danych w złym formacie formularz zostanie wyczyszczony
		4. W przypadku podania prawidłowych danych nastąpi przekierowanie na główną strone aplikacji
		5. Po dodaniu danych można je wyszukać korzystając z opcji "a"
		

# Known issues:
	- CSS nie działa jak powinien w przypadku opcji "b"
