import random

movieName = {}
rating = {}

def addMovie(movieName) :
    title = input("Enter movie name: ")
    movieName[title] = []
    
def addRating(movieName, rating) :
    movieName = input("Select a movie to rate: ")
    if movieName in movieName:
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
    for title in movieName:
        movieName[title].append(random.randint(1, 5))

def displayMovieRatings() :
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
        addMovie(movieName)
    elif choice == "2":
        addRating(movieName, rating)
    elif choice == "3":
        displayMovieRatings()
    elif choice == "4":
        break
    else: 
        print("Invalid choice.")