def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    while True:
        marks = input("Enter marks: ").strip()
        if marks.isdigit():
            break
        else:
            print("Please enter a valid number for marks.")
    
    with open("students.txt", "a") as file:

        file.write(f"{name},{roll},{marks}\n")

        print("Student record added successfully!")
        
#add_student()

def view_student():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()
            if not records:
                print("No student record found")
                return
            print("\n Student Record:")
            print("--------------")
            for record in records:
             name,roll,marks = record.strip().split(",")
             print(f"Name:{name.strip()}, Roll no:{roll.strip()}, Marks:{marks.strip()}")
    except FileNotFoundError:
        print("No Student record file found.")

#view_student()

def search_student():
    try:
       search_name = input("Enter student name:").strip().lower()
       with open("students.txt", "r") as file:
        records = file.readlines()
        found = False
        for record in records:
            name,roll,marks = record.strip().split(",")
            if name.lower() == search_name:
                print(f"\n Student found:")
                print(f"Name:{name}, Roll no:{roll}, Marks:{marks}")
                found = True
                break
       if not found:
                print("\n Student not found")
    except FileNotFoundError:
     print("No Student record file found.")
#search_student()

def update_student():
 try:
     search_name = input("Enter student name:").strip().lower()
     with open("students.txt", "r") as file:
        records = file.readlines()
        updated_records=[]
        found = False
        for record in records:
            name,roll,marks = record.strip().split(",")
            if name.lower() == search_name:
                print(f"Current Marks for {name}:{marks}")
                new_marks = input("Enter new marks:").strip()
                updated_record = f"{name},{roll},{new_marks}\n"
                updated_records.append(updated_record)
                found = True
            else :
                updated_records.append(record)
     if found:
            with open("students.txt", "w") as file:
                file.writelines(updated_records)
          
                print("Marks updated successfully.")
     else: 
          print("Student not found")
 except FileNotFoundError:
           print("No Student record file found.")
#update_student()
def delete_student():
    try:
       search_name = input("Enter student name to delete:").strip().lower()
       found = False 
       updated_records=[]
       with open("students.txt", "r") as file:
        records = file.readlines()
        for record in records:
            name,roll,marks = record.strip().split(",") 
            if name.strip().lower() != search_name:
                updated_records.append(record)
            else:
                found = True
        if found:
            with open("students.txt", "w") as file:
                file.writelines(updated_records)
            print("Student record deleted successfully.")
        else:
           print("Student not found.")
    except FileNotFoundError:
           print("No Student record file found.")   
#delete_student()

def view_all_student_sorted():
   try:
      with open("students.txt", "r") as file:
        records = file.readlines()
        if not records:
            print("No student record found:")
            return
      sorted_records = sorted(records,key = lambda x: x.strip().split(",")[0].lower())
      print("\n---All student records(Sorted by name)---") 
      for record in sorted_records:
             name,roll,marks = record.strip().split(",")
             print(f"Name:{name.strip()}, Roll no:{roll.strip()}, Marks:{marks.strip()}")
   except FileNotFoundError:
           print("No Student record file found.")  

#view_all_student_sorted()

def find_topper():
    try:
       with open("students.txt", "r") as file:
        records = file.readlines()
        if not records:
            print("No student record found:")
            return 
        topper = None
        highest_marks = -1
        for record in records:
            name,roll,marks = record.strip().split(",") 
            if int(marks)>highest_marks:
             highest_marks = int(marks)
             topper=(name,roll,marks)
       print("\n TOPPER:")
       print(f"Name:{topper[0]},Roll no:{topper[1]},Marks:{topper[2]}")
    except FileNotFoundError:
           print("No Student record file found.")  
#find_topper() 

def show_statistics():
    try:
      with open("students.txt", "r") as file:
        records = file.readlines()
        if not records:
            print("No student record found:")
            return 
        total = len(records)
        marks_list=[]
        for record in records:
            name,roll,marks = record.strip().split(",")
            marks_list.append(int(marks))
        average = sum(marks_list) / total
        highest = max(marks_list)
        lowest = min(marks_list)
        print(f"\n Total Students:{total}")
        print(f"\n Average marks:{average}")
        print(f"\n Highest marks:{highest}")
        print(f"\n Lowest marks:{lowest}")
    except FileNotFoundError:
      print("No Student record file found.")  
#show_statistics() 

def menu():
    while True:
        print("\n====== Student Record System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. View All Sorted by Name")
        print("7. Find Topper")
        print("8. Show Statistics")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            view_all_student_sorted()
        elif choice == "7":
            find_topper()
        elif choice == "8":
            show_statistics()
        elif choice == "9":
            print("Exiting program")
            break
        else:
            print("Invalid choice! Please try again.")


menu()
