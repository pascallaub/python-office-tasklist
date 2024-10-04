tasklist = []

def task_input():
    task = input("Welche Aufgabe möchtest du erledigen: ")
    date = input("Fälligkeitsdatum: ")

    tasklist.append((task, date))
    
    print(tasklist)

task_input()