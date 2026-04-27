#Setting up structure with empty list and list of movies
users = []
movies = [
    {
        "Title": "The Others",
        "Year": "2001",
        "Synopsis": "A mother and her children experience paranormal activities in the house they reside in, stirring confusion among them and their servants.",
        "Cast": "Nicole Kidman, Fionnula Flanagan, Christopher Eccleston, James Bentley, Elaine Cassidy, Alakina Mann, Eric Sykes",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Peter Rabbit",
        "Year": "2018",
        "Synopsis": "Peter Rabbit and his sisters comes in contact with Mr. McGregor's relative and they don't see eye to eye, leading to a battle of wills.",
        "Cast": "James Corden, Domhnall Gleeson, Rose Byrne, Margot Robbie, Daisy Ridley, Elizabeth Debicki",
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

# login system - adds new users and checks existing users
def login():
    print("Welcome to MRR!")
    username = input("Enter username: ")

    if username in users:
        print("Welcome back", username)
    else:
        users.append(username)
        print("Welcome", username)
        return username

# Main menu page
def main_menu(username):
    while True: #loops until user chooses to exit
        #display menu options
        print("1. Browse Movies")
        print("2. View profile")
        print("3. Exit")

        choice = input("Slect a Menu option: ") #user's input of choice they want to interact with
        if choice == "1": #shows the user the movie list
            browse_movies(username)
        elif choice == "2": #shows the user their profile consisting of their username, and reviews and ratings they've made
            view_profile(username)
        elif choice == "3": #when users are done, they can choose to exit
            print("Goodbye," + username + "!")
        else: 
            print("Invalid Choice") #displays if user inputs outside of the available menu options
        
# Display movie page and information such as reviews and ratings
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
            for review in movie["Reviews"]:
                print(review)

        print("\nRatings:")
        if len(movie["Ratings"]) == 0:
            print("No ratings made")
        else:
            # calculates average rating
            rating_avg = sum(movie["ratings"]) / len(movie["ratings"])
            #shows average rating of movie and number of ratings made
            print("Average rating: " + str(round(rating_avg, 1)) + "/5 (" + str(len(movie["ratings"])) + " rating made)")

        choice = input("\n1. Add review"
                        "\n2. Add rating"
                        "\n3. Go back to movie list")
        
        if choice == "1":
            add_review(username, movie)

        elif choice == "2":
            add_rating(movie)

        elif choice == "3":
            return

# Allows users to browse and select a movie
def browse_movies(username):
    while True:
        for items in range(len(movies)):
            #Get position of movies and its title
            print(str(items + 1) + ". " + movies[items]["Title"])
        
        choice = input("\n1. Select movie"
                       "\n2. Go back to main menu")
        
        if choice == "1":
            movie_name = input("Enter movie: ")
            for movie in movies:
                if movie["Title"].lower() == movie_name.lower():
                    # displays movie info
                    movie_page(username, movie)
                    break
                else: 
                    print("Movie not found")

        elif choice == "2":
            return
    
# Allows users to add a review
def add_review(username, movie):
    review = input("Enter review: ")
    if review != "":
        movie["reviews"].append(username + ": " + review)
        print("Review added")

# Allows users to add a rating
def add_rating(movie):
    rating = input("Enter rating (1-5): ")
    if rating.isdigit():
        rating = int(rating)
        movie["ratings"].append(rating)
        print("Rating added")

# Allows users to interact with profile page
def view_profile(username): #display the user's profile
    print("PROFILE")
    print("Username: " + username)
    print("Reviews Made: ")
    print("Ratings Made: ")

    print("Reviews: ")
    review_count = 0
    for review in movies["Reviews"]: #loops through the reviews in the movie area
        if username in review:
            print(review)
            review_count = review_count + 1 #adds a review count for every review present 
        else:
            print("No Reviews Made") #if no reviews are present for this user, will print this message
    
    print("Ratings: ")
    ratings = 0
    for ratings in movies["Ratings"]: #loops through the ratings in the movie area
        ratings = ratings + 1 # adds a rating count for every rating the user has made
        if ratings == 0:
            print("No Ratings Made") #present this message if user made no ratings
            
       



