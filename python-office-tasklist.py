tasklist = []

def task_input():
    task = input("Welche Aufgabe möchtest du erledigen: ")
    date = input("Fälligkeitsdatum: ")

    tasklist.append((task, date))
    

def show_tasks():
    if tasklist == '':
        print("Die Liste ist leer.")
    else:
        for item in tasklist:
            print(item)

def menu():
    while True:
        choice = input("Aufgaben hinzufügen (1), Aufgaben anzeigen (2), Beenden (3): ")

        if choice == '1':
            task_input()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            quit()
        else:
            "Falsche Eingabe!"
            continue
    
if __name__ == '__main__':
    menu()