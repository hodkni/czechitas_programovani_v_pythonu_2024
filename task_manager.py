"""Správce úkolů
Cílem tohoto projektu je vytvořit jednoduchou aplikaci pro správu úkolů v Pythonu. Aplikace umožní uživatelům přidávat, odstraňovat a prohlížet úkoly."""

"""1. Inicializace projektu
Vytvořte nový Python soubor (např. task_manager.py).
Na začátek souboru přidejte import potřebného modulu datetime, který bude využit pro přidávání časových razítek k úkolům."""

import datetime
import uuid

"""2. Definice třídy Task
Definujte třídu Task, která bude reprezentovat jednotlivé úkoly.
Třída bude mít konstruktor __init__, který přijímá jeden parametr description (popis úkolu).
V konstruktoru nastavte atributy description a timestamp. Atribut timestamp bude automaticky nastaven na aktuální datum a čas."""

class Task:
    def __init__(self, description): #init je konstruktor = konstruuje tridu
        self.description = description
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') #v argumentu tridy nemusi byt jen povinne parametry, ale i logika

    def __str__(self):
        return f"Task: {self.description}, time: {self.timestamp}."
    
"""3. Vytvoření datové struktury pro ukládání úkolů
Použijte slovník tasks pro ukládání úkolů, kde klíče budou jedinečná ID úkolů a hodnoty budou instance třídy Task."""

tasks = {}

"""4. Implementace funkcí pro manipulaci s úkoly
add_task(description): Funkce pro přidání nového úkolu. Generuje unikátní ID pro každý úkol, přidává úkol do slovníku a vypisuje informaci o přidání."""


def add_task(description):
    task_id = str(uuid.uuid4()) #musi byt string?
    new_task = Task(description)
    tasks[task_id] = new_task #do slovniku tasks pridam ke konkretnimu klici task_id vzdy jeho popis
    print(f"Byl přidán úkol s ID: {task_id}. Popis úkolu: {description}")


"""remove_task(task_id): Funkce pro odstranění úkolu. Kontroluje, zda úkol s daným ID existuje, a pokud ano, odstraní ho.
show_tasks(): Funkce pro zobrazení všech aktuálně uložených úkolů společně s jejich popisem a časem přidání."""

def remove_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Úkol s ID {task_id} byl odstraněn.")
    else:
        print(f"Úkol s ID {task_id} neexistuje.")
    
def show_task():
    if tasks:
        print("Seznam úkolů:")
        for task_id, task_instance in tasks.items():
            print(f"ID úkolu: {task_id}")
            print(f"Název úkolu: {task_instance}")
            print(f"Popis úkolu: {task_instance.description}")
            print("Čas přidání úkolu:", datetime.datetime.now())
    else:
        print("Neexistují žádné úkoly.")


"""5. Hlavní smyčka programu
Napište funkci main(), která bude obsahovat nekonečnou smyčku, jež načítá příkazy od uživatele.
Umožněte uživateli zadat příkazy add, remove a show. Na základě vstupu volajte odpovídající funkce."""

def main():
    while True:
        print("\nMožnosti příkazů:")
        print("1. add - Přidat nový úkol")
        print("2. remove - Odstranit úkol")
        print("3. show - Zobrazit všechny úkoly")
        print("4. exit - Ukončit program")

        choice = input("Zadejte příkaz: ").lower()

        if choice == "add":
            description = input("Zadejte popis nového úkolu: ")
            add_task(description)
        elif choice == "remove":
            task_id = input("Zadejte ID úkolu k odstranění: ")
            remove_task(task_id)
        elif choice == "show":
            show_task()
        elif choice == "exit":
            print("Program byl ukončen.")
            break
        else:
            print("Neplatný příkaz. Zadejte 'add', 'remove', 'show' nebo 'exit'.")
    

"""6. Testování a spuštění aplikace
Ujistěte se, že skript správně zpracovává všechny typy příkazů a že úkoly jsou správně přidávány, odstraňovány a zobrazovány.
Spusťte skript v terminálu nebo příkazové řádce a otestujte jeho funkčnost."""


main()

"""7. Verzování kódu pomocí Git
Inicializujte Git repozitář v adresáři projektu.
Uložte změny (commit) a pushněte je na GitHub. Tento krok poskytne studentům základní praxi s verzováním kódu."""

