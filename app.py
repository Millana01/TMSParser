from parser.tms import TMS


def main():
    # Games page
    games = TMS("https://play.google.com/store/games")
    games.parse()
    games.save("games.json")

    # Movies page
    movies = TMS("https://play.google.com/store/movies")
    movies.parse()
    movies.save("movies.json")

    # Books page
    books = TMS("https://play.google.com/store/books")
    books.parse()
    books.save("books.json")

    # Family page
    family = TMS("https://play.google.com/store/apps/category/FAMILY")
    family.parse()
    family.save("family.json")


if __name__ == "__main__":
    main()
