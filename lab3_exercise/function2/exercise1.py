def main(movie):
    return movie.get("imdb", 0) > 5.5

example_movie = {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}
print(main(example_movie))  
