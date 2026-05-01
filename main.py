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
        "Title": "Us",
        "Year": "2019",
        "Synopsis": "Being back at her childhood home for vacation with her family, Adelaide Wilson can't help but feel concerned about something related to her traumatic past.",
        "Cast": "Lupita Nyong'o, Winston Duke, Evan Alex, Shahadi Wright Joseph",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Send Help",
        "Year": "2026",
        "Synopsis": "Linda Liddle is a survival enthusiast who got deserted on an island with her boss, Bradley Preston, whome she has conflicts with.",
        "Cast": "Rachel McAdams, Dylan O'Brien",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Ready or Not",
        "Year": "2019",
        "Synopsis": "Grace just got married to Alex Le Domas. She was introduced to the family's tradition where the new spouse must draw a card that would determine what game they'd play that night. Upon everyone's shock, Grace drew the Hide and Seek card.",
        "Cast": "Samara Weaving, Adam Brody, Mark O'Brien",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "The Hunger Games",
        "Year": "2012",
        "Synopsis": "Set in Panem where the 12 districts are forced to send tributes consisting of one boy and girl during the reaping, Primrose Everdeen's name was called, leading Katniss Everdeen to volunteer in place of her sister.",
        "Cast": "Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "The Conjuring",
        "Year": "2013",
        "Synopsis": "The Perrons and their daughters moved into a house where they later experience paranormal activities, summoning Ed and Lorraine Warren to investigate.",
        "Cast": "Vera Farmiga, Patrick Wilson, Ron Livingston, Lili Taylor",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "I Am What I Am",
        "Year": "2021",
        "Synopsis": "Follows the journey of a young boy as he navigates through setbacks and his passion for traditional lion dancing.",
        "Cast": "Li Xun, Chen Yexiong, Guo Hao",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Despicable Me",
        "Year": "2010",
        "Synopsis": "Gru and his army of minions sets up a plan to steal the moon. As he brought in three orphan girls to help with his scheme, his bond with them turned into something more than what he had in mind.",
        "Cast": "Steve Carell, Miranda Cosgrove, Dana Gaier, Elsie Fisher, Jason Segel",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "The Road",
        "Year": "2009",
        "Synopsis": "A man and his son journeys through a post-apocalyptic world, doing their best to survive as they scavenge for food and necessities while trying to avoid desperate predators.",
        "Cast": "Viggo Mortensen, Kodi Smit-McPhee",
        "Reviews": [],
        "Ratings": []
    },
    {   
        "Title": "Better Days",
        "Year": "2019",
        "Synopsis": "Chen Nian who is being bullied at school and her relationship with a tough street kid, Xiao Bei, with whom she is implicated in the murder of a teenage girl.",
        "Cast": "Zhou Dong Yu, Jackson Yee, Wei Lai",
        "Reviews": [],
        "Ratings": []
    }, 
    {
        "Title": "Brave",
        "Year": "2012",
        "Synopsis": "Set in Scotland in a rugged and mythical time, this movie features Princess Merida, and aspiring archer and impetuous daughter of Queen Elinor. Merida makes a reckless choice that unleashes unintended peril and forces her to spring into action to set things right.",
        "Cast": "Kelly Macdonald, Billy Connolly, Emma Thompson",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Top Gun",
        "Year": "1986",
        "Synopsis": "The Top Gun Naval Fighter Weapons School is where the best of the best trains to refine their elite flying skills. When hotshot fighter pilot Maverick is sent to the school, his reckless attitude and cocky demeanor put him at odds with the other pilots, especially the cool and collected Iceman.",
        "Cast": "Tom Cruise, Val Kilmer, Anthony Edwards, Kelly McGillis",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "The Sound of Music",
        "Year": "1965",
        "Synopsis": "Maria, a young novice from an Abby, is sent to become the governess to the seven children of a widowed navel captain. Maria proves to be unlike the governess the Captaina and the children have had before.",
        "Cast": "Julie Ansdrews, Christopher Plummer",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Barbie 12 Dancing Princesses",
        "Year": "2006",
        "Synopsis": "A king to 12 daughters worries about their unfit character for royal duties due to the words of a visitor and calls upon his cousin, Dutchess Rowena, to aid in teaching the girls their duties and sharpening their behavior. Instead, Her arrival brings an oppressive new order, while the king grows increasingly ill. Seeking freedom, the princess discover a hidden world using their mother's last gift to them.",
        "Cast": "Kelly Sheridan, Catherine O'Hara, Shawn Macdonald, ",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "The Forbidden Kingdom",
        "Year": "2008",
        "Synopsis": "When a magical staff transport Jason to ancient China, he is tasked with returning the staff to the Monkey King told by the prophecy.",
        "Cast": "Jackie Chan, Jet Li, Michael Angarano",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "The Sixth Sense",
        "Year": "1999",
        "Synopsis": "Malcolm Crowe takes on a new case that reflect similar symptoms of a previous patient whom he was shot by. In helping his new patient, Cole Sear, a shocking discovery is amde.",
        "Cast": "Bruce Willis, Haley Joel Osment",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "The Hobbit",
        "Year": "2012",
        "Synopsis": "Biblo, upon being chosen by Gandalf for him and the dwarves quest, initially refuses but soon joins them in their quest in reclaiming the dwarves land from the dragon Smaug, playing the role of the burglar in their quest due to a hobbit's stealth ability and scent which are unfamiliar to Smaug.",
        "Cast": "Martin Freeman, Ian Mckellen, Richard Armitage",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Up",
        "Year": "2009",
        "Synopsis": "Faced with his house about to be taken down, Carl decides to fulfill a dream him and his late wife made when they were kids by lifting off with thousands of balloons, marking the start of his journey.",
        "Cast": "Edward Asner, Jordan Nagai",
        "Reviews": [],
        "Ratings": []
    },
    {
        "Title": "Nanny McPhee",
        "Year": "2005",
        "Synopsis": "After the children of Cedric Brown runs off another nanny, he seeks out a new nenny for his children. A voice tells him the nanny he needs is Nanny McPhee. Upon meeting Nanny McPhee, the childrens are met with a nanny unlike the others they've been able to run off. Nanny McPhee proves to be a challange for the children, especially Simon.",
        "Cast": "Emma Thompson, Colin Firth, Thomas brodi-Sangstere",
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
        print("\nWelcome", username)
    return username

# Main menu page
def main_menu(username):
    while True: #loops until user chooses to exit
        #display menu options
        print("\n1. Browse Movies")
        print("2. View profile")
        print("3. Exit")

        choice = input("Select a Menu option: ")
        if choice == "1":
            browse_movies(username)
        elif choice == "2": #shows the user their profile consisting of their username, and reviews and ratings they've made
            view_profile(username)
        elif choice == "3": #when users are done, they can choose to exit
            print("Goodbye," + username + "!")
            break
        else:
            print("Invalid Choice") #Display when users input non available menu options
        
# Display movie page and information such as reviews and ratings
def movie_page(username, movie):
    while True:
        # displays movie info
        print(movie["Title"])
        print("Year: ", movie["Year"])
        print("Synopsis: ", movie["Synopsis"])
        print("Main cast:", movie["Cast"])

        print("\nReviews:")
        if len(movie["Reviews"]) == 0:
            print("No reviews made")
        else:
            for review in movie["Reviews"]:
                print(review)

        print("\nRatings:")
        if len(movie["Ratings"]) == 0:
            print("No ratings made")
        else:
            # calculates average rating
            rating_avg = sum(movie["Ratings"]) / len(movie["Ratings"])
            #shows average rating of movie and number of ratings made
            print("Average rating: " + str(round(rating_avg, 1)) + "/5 (" + str(len(movie["Ratings"])) + " ratings made)")

        choice = input("\n1. Add review"
                        "\n2. Add rating"
                        "\n3. Go back to movie list: ")
        
        if choice == "1":
            add_review(username, movie)

        elif choice == "2":
            add_rating(username, movie)

        elif choice == "3":
            return

# Allows users to browse and select a movie
def browse_movies(username):
    while True:
        print("\n")
        for items in range(len(movies)):
            #Get position of movies and its title
            print(str(items + 1) + ". " + movies[items]["Title"])
        
        choice = input("\nOptions:"
                       "\n1. Select movie"
                       "\n2. Go back to main menu: ")
        
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
        movie["Reviews"].append(username + " | " + movie["Title"] + ": " + review)
        print("Review added")

# Allows users to add a rating
def add_rating(username, movie):
    rating = input("Enter rating (1-5): ")
    if rating.isdigit():
        rating = int(rating)
        movie["Ratings"].append(username + " | " + movie["Title"] + ": " + str(rating))
        print("Rating added")

# Allows users to interact with profile page
def view_profile(username): #display the user's profile
    print("\nPROFILE")
    print("Username: " + username)

    print("\nReviews: ")
    review_count = 0
    for movie in movies: #loops through each movie
        for review in movie["Reviews"]: #loops through the reviews in the movie area
            if username in review:
                print(review)
                review_count = review_count + 1 #adds a review count for every review the user has made 
    #print message if no reviews were found
    if review_count == 0:
        print("No Reviews Made") 
    #for ratings
    print("\nRatings: ")
    rating_count = 0
    for movie in movies: 
        for rating in movie["Ratings"]:
            if username in rating:
                print(rating)
                rating_count = rating_count + 1
    if rating_count == 0:
        print("No Ratings Made")
            
def main():
    main_menu(login())

main()
       



