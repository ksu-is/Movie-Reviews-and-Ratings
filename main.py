users = []
movies = [
    {
        "Title": "...",
        "Year": "...",
        "Synopsis": "...",
        "Cast": "...",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "...",
        "Year": "...",
        "Synopsis": "...",
        "Cast": "...",
        "Reviews": [],
        "Ratings": []
    },
]

def login():
    print("Welcome to MRR!")
    username = input("Enter username: ")

    if username in users:
        print("User already exists")
    else:
        users.append(username)
        print("Welcome", username)
        return username
    
def add_review(username, movie):
    review = input("Enter review: ")
    if review != "":
        movie["reviews"].append(username + ": " + review)
        print("Review added")

def add_rating(movie):
    rating = input("Enter rating (1-5): ")
    if rating.isdigit():
        rating = int(rating)
        movie["ratings"].append(rating)
        print("Rating added")


       



