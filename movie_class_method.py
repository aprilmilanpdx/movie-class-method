class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")

# <<movie_name>> by movie_director
# The movie_name and movie_director should be replaced by the according properties inside the object that calls the print_info() method.

my_movie = Movie('The Matrix', 'Wachowski')
my_movie.print_info()