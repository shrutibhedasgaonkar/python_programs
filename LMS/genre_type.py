def get_genre_type() -> str:
    print("Genre Type: ")
    print("1. World History")
    print("2. Philosophy")
    print("3. Science")
    print("4. Crime")
    print("5. Thriller")
    print("6. Programming")
    print("7. Mystery")
    print("8. Mythology")
    print("9. Comedy")
    print("10. Fantasy")

    genre: int = int(input("Select genre type :"))

    match genre:
        case 1:
            return "World History"

        case 2:
            return "Philosophy"

        case 3:
            return "Science"

        case 4:
            return "Crime"

        case 5:
            return "Thriller"

        case 6:
            return "Programming"

        case 7:
            return "Mystery"

        case 8:
            return "Mythology"

        case 9:
            return "Comedy"

        case 10:
            return "Fantasy"

        case _:
            print("Invalid option...! Try again!!!")

