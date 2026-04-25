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
    {
        "Title": "...",
        "Year": "...",
        "Synopsis": "...",
        "Cast": "...",
        "Reviews": [],
        "Ratings": []
    }

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

def main_menu(username):
    while True:
        print("1. Browse Movies")
        print("2. View profile")
        print("3. Exit")

        choice = input("Slect a Menu option: ")
        if choice == "1":
            browse_movies(username)
        elif choice == "2":
            view_profile(username)
        elif choice == "3":
            print("Goodbye," + username + "!")
        else:
            print("Invalid Choice")
        

def movie_page(username, movie):
    while True:
        # displays movie info
        print(movie["Title"])
        print("Year: ", movie["Year"])
        print("Synopsis: ", movie["Synopsis"])
        print("Main cast:", movie["Cast"])

        print("\nReviews:")
        if len(movie["reviews"]) == 0:
            print("No reviews made")
        else:
            for review in movie["reviews"]:
                print(review)

        print("\nRatings:")
        if len(movie["rating"]) == 0:
            print("No ratings made")
        else:
            # calculates average rating
            rating_avg = sum(movie["ratings"]) / len(movie["ratings"])
            #shows average rating of movie and number of ratings made
            print("Average rating: " + str(round(rating_avg, 1)) + "/5 (" + str(len(movie["ratings"])) + " rating made)")

        choice = input("\n1. Add review"
                            "2. Add rating"
                            "3. Go back to movie list")
        
        if choice == "1":
            add_review(username, movie)

        elif choice == "2":
            add_rating(movie)

        elif choice == "3":
            return

def browse_movies(username):
    while True:
        for items in range(len(movies)):
            #Get position of movies and its title
            print(str(items + 1) + ". " + movies[items]["title"])
        
        choice = input("\n1. Select movie\n2. Go back to main menu\n")
        
        if choice == "1":
            movie_name = input("Enter movie: ")
            for movie in movies:
                if movie["title"].lower() == movie_name.lower():
                    # displays movie info
                    movie_page(username, movie)
                    break
                else: 
                    print("Movie not found")

        elif choice == "2":
            return
    
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


       



