# Attributes
# Name
# year
# rating
# Methods
# pause
# play
# forward
# class is blueprint of Movie
# keyword: __init__ , use instead of function name with (Parameters)

class Movie:   # constructor: Movie
    def __init__(self,name,year,rating):
        #self: reference of object
        # self.key = parameter (value)
        self.name = name   #ATTRIBUTES : self.name - name is key
        self.year_of_release = year
        self.rating = rating

    def pause(self):
        print("Pause Movie"+ self.name)  #Methods

    def play(self):
        print("playing movie"+ self.name)
        
    def compare(self, other):
        if self.rating > other.rating:
            print(self.name + "has higher rating")
        else:
            print(other.name + "has higher rating")

#! printing parameters
Movie1 = Movie("3 idiots", 2009, 4.8)
print(Movie1.name)
print(Movie1.year_of_release) #we call with key of self not with parameters

#! how to call
# Variable = class_name(parameters)

#* Single parameter
Movie1 = Movie("3 idiots", 2009, 4.8)
Movie.pause(Movie1) #way 1 to print
Movie1.pause() #way 2 to print

#* with multiple parameters
Movie2 = Movie("Tare", 2007, 4.5)

# Way1 to print
Movie.compare(Movie1,Movie2) # par1: Movie1 and par2: Movie 2

# Way2 to print
Movie1.compare(Movie2) # first par: Movie1 and sec par: Movie 2
Movie2.compare(Movie1) # first par: Movie2 and sec par: Movie 1
