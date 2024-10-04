tasklist = []

priority_order = {
    "gering": 1,
    "mittel": 2,
    "hoch": 3
}

def task_input():
    task = input("Welche Aufgabe möchtest du erledigen: ")
    date = input("Fälligkeitsdatum: ")
    prio = input("Priorität (gering, mittel, hoch): ")

    tasklist.append((task, date, prio))

def sorted_prio():
    sorted_list = sorted(tasklist, key=lambda x: priority_order[x[2]], reverse=True) # Sortiert nach prio und vergleicht die dritte Stelle mit priority_order
    for task in sorted_list:
        print(task)
    

def show_tasks():
    if tasklist == []:
        print("Die Liste ist leer.")
    else:
        for item in tasklist:
            print(item)

def menu():
    while True:
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