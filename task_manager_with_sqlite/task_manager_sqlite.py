import sqlite3

conn = sqlite3.connect('task_manager.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL
    )
 ''')

def list_tasks():
    print("\n")
    print("*"*60)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if not tasks:
        print("No task Available")
    else:
        for task in tasks:
            print(task)
    print("\n")
    print("*"*60)  
def add_task(title,description):
    cursor.execute("INSERT INTO tasks(title,description) VALUES (?,?)",(title,description))
    conn.commit()

def update_task(taskID,newTitle,newDescription):
    
    cursor.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?",(newTitle,newDescription,taskID))
    conn.commit()

def delete_task(taskID):
    
    cursor.execute("DELETE FROM tasks WHERE id = ?",(taskID,))
    conn.commit()



def main():
    while True:
        print("\n Task manager app with DB")
        print("1. List Task")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit The App")
        choice = input("Enter Your Choice: ")

        if choice =="1":
            list_tasks()
        elif choice == "2":
            title = input("Enter the Task Title: ")
            desc = input("Enter the Task Description: ")
            add_task(title,desc)
        elif choice == "3":
            list_tasks()
            taskId = input("Enter the Task ID to Update: ")
            title = input("Enter the Task Title: ")
            desc = input("Enter the Task Description: ")
            update_task(taskId,title,desc)
        elif choice == "4":
            list_tasks()
            taskId = int(input("Enter the Task ID to Delete: "))
            delete_task(taskId)
        elif choice == "5":
            break
        else:
            print("Invalid number ")

    conn.close()
if __name__ == "__main__":
    main()