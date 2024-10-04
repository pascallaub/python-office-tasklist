import csv
from datetime import datetime, timedelta

tasklist = []

priority_order = {
    "gering": 1,
    "mittel": 2,
    "hoch": 3
}

def check_due_dates():
    today = datetime.today().date() #Aktuelles Datum
    one_day_before = today + timedelta(days=1) #Ein Tag später

    for task, date, prio in tasklist:
        try:
            due_date = datetime.strptime(date.strip(), "%d.%m.%Y").date() #Fälligkeitsdatum umwandeln in Datumsformat
            if due_date == one_day_before:
                print(f"⚠️  Benachrichtigung! {task} ist morgen fällig!⚠️")
        except ValueError:
            print(f"Ungültiges Datum für Aufgabe {task}: {date}")

def load_tasks_from_csv():
    try:
        with open("tasklist.csv", "r", newline="") as datei:
            csv_reader = csv.reader(datei)
            for row in csv_reader:
                tasklist.append(tuple(row)) #Zeilen in Tupel umwandeln und Taskliste hinzufügen
    except FileNotFoundError:
        print("Datei nicht gefunden!")

def task_input():
    task = input("Welche Aufgabe möchtest du erledigen: ")
    date = input("Fälligkeitsdatum: ")
    prio = input("Priorität (gering, mittel, hoch): ")

    with open("tasklist.csv", "a", newline="") as datei:
        csv_writer = csv.writer(datei)
        csv_writer.writerow((task, date, prio))

def sorted_prio():
    sorted_list = sorted(tasklist, key=lambda x: priority_order[x[2]], reverse=True) # Sortiert nach prio und vergleicht die dritte Stelle mit priority_order
    for task in sorted_list:
        print(task)
    

def show_tasks():
    if not tasklist:
        print("Die Liste ist leer.")
    else:
        for item in tasklist:
            print(item)

def menu():
    while True:
        load_tasks_from_csv()
        check_due_dates()
        choice = input("Aufgaben hinzufügen (1), Aufgaben anzeigen (2), Aufgaben sortieren (3), Beenden (4): ")

        if choice == '1':
            task_input()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            sorted_prio()
        elif choice == '4':
            quit()
        else:
            "Falsche Eingabe!"
            continue
    
if __name__ == '__main__':
    menu()