from file_manager import write_to_json, read_from_json


def menu():
    print("""
        1. Malumot qoshish
        2. Malumotlarni korish
        3. Chiqish
          """)

    choice = input("choice: ")
    if choice == "1":
        name = input("Ismingizni kiriting: ")
        data = [{"ism": name}]
        write_to_json("data.json", data)

    elif choice == "2":
        data = read_from_json("data.json")
        print(data)

    elif choice == "3":
        exit()
    else:
        print("Hato tanlangan 1 dan 3 gacha")

if __name__ == "__main__":
    menu()
