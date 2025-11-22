
# S (SR-Code, Last name, First name) 
# #tropa ibahin niyo 'yung mga sr code wag pare-parehas para gumana
sections = {
    "BSIT-1109":[
        ("25-2314", "Adajar", "Jimuel"),
        ("25-src41ode", "Marfil", "Era"),
        ("25-sr4245code", "Tenorio", "Karl Max"),
    ],
    "BSIT-1108": [
        ("26-3234sr", "Coronel", "Jairus"),
        ("26-s3532r", "Osmillo", "Jorie"),
        ("26-sr352", "Umali", "Welington"),
    ],
    "BSIT-1103": [
        ("27-sr32545", "sample", "sample"),
        ("27-s4245r", "sample", "sample"),
    ],
}

attendance = {} #for storing

def mark_attendance(section_name):
    global attendance
    attendance = {}   # Reset every session

    students = sections[section_name]
    print(f"\n Attendance ({section_name})") 

    for sid, last, first in students:
        while True:
            status = input(f"{sid} | {last}, {first} (P/A): ").strip().lower()

            if status in ("p", "a"):
                attendance[sid] = "present" if status == "p" else "absent"
                break
            else:
                print("Invalid input. Enter 'p' or 'a'.")


    present_count = sum(1 for s in attendance.values() if len(s) == 7)
    absent_count  = sum(1 for s in attendance.values() if len(s) == 6)

    print("\n--- Summary ---")
    print(f"Present: {present_count}")
    print(f"Absent : {absent_count}")

    # Options after attendance
    while True:
        print("\n1.) SAVE THE FILE\n2.) BACK\n3.) END")
        choice = input("Enter choice: ")

        if choice == "1":
            filename = f"{section_name}_attendance.txt"
            with open(filename, "w") as f:
                f.write(f"ATTENDANCE: {section_name}\n\n")
                for sid, status in attendance.items():
                    last = next(x[1] for x in students if x[0] == sid)
                    first = next(x[2] for x in students if x[0] == sid)
                    f.write(f"{sid} | {last}, {first} : {status}\n")
                    
                f.write("\nSUMMARY\n")
                f.write(f"Present: {present_count}\n")
                f.write(f"Absent : {absent_count}\n")
            print(f"Saved to {filename}\n")

        elif choice == "2":
            return  

        elif choice == "3":
            print("Goodbye!")
            exit()

        else:
            print("Invalid option.")

while True:
    print("\n============================")
    print("1.) Attendance")
    print("2.) END") #dagdag na lang dito ung sa student info kau na bahala 
    print("============================")

    menu = input("Select: ")

    if menu == "1":
        print("\nChoose section/block:")
        for i, sec in enumerate(sections.keys(), start=1):
            print(f"{i}.) {sec}")
        print(f"{len(sections) + 1}.) BACK")

        choice = input("Choose: ")

        if choice.isdigit() and 1 <= int(choice) <= len(sections):
            section_name = list(sections.keys())[int(choice) - 1]
            mark_attendance(section_name)

        elif choice == str(len(sections) + 1):
            continue  # back to main

        else:
            print("Invalid section.\n")

    elif menu == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")