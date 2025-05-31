import json

fileName = "task_manager.txt"
def load_data():
    try:
        with open(fileName,"r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def save_data_helper(tasks):
    with open(fileName,"w") as file:
        json.dump(tasks,file)

def list_all_task(tasks):
    print("\n")
    print("*"*60)

    for index,task in enumerate(tasks,start=1):
        print(f"{index}. title: {task['title']} desc: {task['description']}")
    print("\n")
    print("*"*60)
    
def add_task(tasks):
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    tasks.append({"title":title,"description":description})
    save_data_helper(tasks)

def update_task(tasks):
    list_all_task(tasks)
    index = int(input("Enter The Task Number To Update: "))
    if 1 <= index <= len(tasks):
            title = input("Enter Task Title: ")
            description = input("Enter Task Description: ")
            tasks[index-1] = {"title":title,"description":description}
            save_data_helper(tasks)
            print("Task Updated Successfully")
    else:
        print("Invalid Task Index Select")
        
def delete_task(tasks):
    list_all_task(tasks)
    index = int(input("Enter The Task Number To Delete: "))
    if 1 <= index <= len(tasks):
        del tasks[index-1]
        save_data_helper(tasks)
        print("Task Deleted Successfully")
    else:
        print("Invalid Task index")

def main():
    tasks = load_data()
    while True:
        print("\n TO-DO-LIST APPLICATION | CHOOSE AN OPTION ")
        print("1. List Your All Task ")
        print("2. Add Your Task ")
        print("3. Update Your Task ")
        print("4. Delete Your  Task ")
        print("5. Exit Your App ")
        choice =input("Enter Your Choise: ")
        
        match choice:
            case "1":
                list_all_task(tasks)
            case "2":
                add_task(tasks)
            case "3":
                update_task(tasks)
            case "4":
                delete_task(tasks)
            case "5":
                break
            case _:
                print("Invalid Choice")
    
if __name__ == "__main__":
    main()


