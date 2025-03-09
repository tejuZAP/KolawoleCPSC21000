import random

movieName = {}
rating = {}

def addMovie(movieName) :
    #Asks for the users to add a movie title and adds it into the list called movieName
    title = input("Enter movie name: ") #Defines the input given by the users as title
    movieName[title] = [] #places title into the movieName list
    
def addRating(movieName, rating) :
    #Has the users select a movie in the list and assign a rating to it that is stored into the dictionary called rating
    movieName = input("Select a movie to rate: ") #defines the input given by the users as movieName
    if movieName in movieName: #if the input given by the users matches what is in the movieName list it ask the user to given a rating if not it prints an error
        while True:
            try:
                rating = int(input("Enter rating(1-5 stars): "))
                if 1 <= rating <= 5:
                    movieName[movieName] = rating
                    print(f"Rating for '{movieName}' updated to {rating} stars.")
                    break
                else:
                    print("Invalid rating")
            except ValueError:
                print(f"Movie is not in the manager")

def generateRandomRating(movieName) :
    #Adds a random rating to the movies in the list that gets stored to the dictionary 
    for title in movieName:
        movieName[title].append(random.randint(1, 5))

def displayMovieRatings() :
    #Takes the ratings stored in the dictionary and averages out the ratings added by the user and created by the random generator. The movie with the ratings get printed out
    for title, ratings in movieName.items():
        average_rating = round(sum(ratings) / len(ratings), 1)
        print(f"{title}: {average_rating} stars")
    
while True:
    print("1. Add Movie")
    print("2. Rate Movies")
    print("3. View Movies")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        addMovie(movieName) #calls the addMovie function
    elif choice == "2":
        addRating(movieName, rating) #calls the addRating function
    elif choice == "3":
        displayMovieRatings() #calls the displayMovieRatings function
    elif choice == "4":
        break
    else: 
        print("Invalid choice.")