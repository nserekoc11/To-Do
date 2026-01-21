
def main():
    running = True

    while running:
        #Choose an option from the menu
        print("\n === Menu ===")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            inp = input("Enter task to add: ")
            add_task()
        elif choice == '2':
            inp = input("Enter task to delete: ")
            del_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice!")

inp = input("input")
db = {"task1", "task2"}

def add_task():
    db.add(inp)

def del_task():
    db.remove(inp)

def view_tasks():
    for task in db:
        print(task)

if __name__ == "__main__":
    main()

#TODO: Implement the functions above

#while running:
#    print("\n=== Menu ===")
#    print("1. Do something")
#    print("2. Do something else")
#    print("3. Exit")
#    
#    choice = input("Choose an option: ")
#    
#    if choice == '1':
#        print("Doing something...")
#    elif choice == '2':
#        print("Doing something else...")
#    elif choice == '3':
#        print("Goodbye!")
#        running = False
#    else:
#        print("Invalid choice!")

