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
        "Title": "Better Days",
        "Year": "2019",
        "Synopsis": "Chen Nian who is being bullied at school and her relationship with a tough street kid, Jackson Yee, with whom she is implicated in the murder of a teenage girl.",
        "Cast": "Zhou Dong Yu, Jackson Yee, Wei Lai",
        "Reviews": [],
        "Ratings": []
    }, 
    {
        "Title": "Brave",
        "Year": "2012",
        "Synopsis": "Set in schotland in a rugged and mythical time, this movie features Princess Merida, and aspiring archer and impetuous daughter of Queen Elinor. Merida makes a reckless choice that unleashes unintended peril and forces her to spring into action to set things right.",
        "Cast": "Kelly Macdonald, Billy Connolly, Emma Thompson",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Top Gun",
        "Year": "1986",
        "Synopsis": "The Top Gun Navel Fighter Weapons School is where the best of the best trains to refine their elite flying skills. When hotshot fighter pilot Maverick is sent to the school, his reckless attitude and cocky demeanor put him at odds with the other pilots, especially the cool and collected Iceman.",
        "Cast": "Tom Cruise, Val Kilmer, Anthony Edwards, Kelly McGillis",
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

def view_profile(username):
    print("PROFILE")
    print("Username: " + username)
    print("Reviews Made: ")
    print("Ratings Made: ")

    print("Reviews: ")
    review_count = 0
    if review_count == 0:
        print("No Reviews Made")
    else:
        review_count = review_count + 1 
    
    print("Ratings: ")
    ratings = 0
    if ratings == 0:
        print("No Ratings Made")
    else:
        ratings = ratings + 1 

       



