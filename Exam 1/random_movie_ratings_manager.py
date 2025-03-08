import random

def addMovie(movieName) :
    movielist = []
    movieName = input("Enter a movie: ")
    movielist.append(movieName)
    return movieName

def addRating(movieName,rating) :
    scores= { }
    movieName[addMovie()]= input("Select movie: ")
    if movieName is not None:
        return movieName
    if movieName is None:
        raise TypeError("Input must be entered into the sytem")
    rating[''] = input("Give rating: ")
    print (f'{movieName,rating}')

def generateRandomRating(movieName) :
    result = []
    for i in range(movieName):
        result.append(random.randint(1,5))
    return result

def displayMovieRatings() :
    round()

def main() :
    movieName = addMovie()
    rating = addRating()