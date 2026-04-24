users = []
movies = []

def login():
    print("Welcome to MRR!")
    username = input("Enter username: ")

    if username in users:
        print("User already exists")
    else:
        users.append(username)
        print("Welcome", username)
        return username
