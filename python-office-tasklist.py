tasklist = []

def task_input():
    task = input("Welche Aufgabe möchtest du erledigen: ")
    date = input("Fälligkeitsdatum: ")

    tasklist.append((task, date))

    show_tasks()
    

def show_tasks():
    if tasklist == '':
        print("Die Liste ist leer.")
    else:
        for item in tasklist:
            print(item)

task_input()
