from genre_type import get_genre_type
from ready_books_collections import books_collection


def add_book(library):
    book_id: str = input("Enter Book Id : ")
    title: str = input("Enter Book Title : ")
    author: str = input("Enter Name of the Author : ")
    genre = get_genre_type()
    copies: str = input("Enter number of copies: ")

    library[book_id] = {'Title': title, 'Author': author, 'Genre': genre, 'Copies': int(copies)}
    print(f"Book {title} is added successfully.!!")
    print("**************************************************** \n")


def search_book(library):
    # collection = books_collection()
    book_id = input("Enter book id to search: ")

    book_details = library.get(book_id)
    if book_details:
        print(f"Details of book Id {book_id} : {book_details}")

    else:
        print("Book not found..!")
    print("**************************************************** \n")


def update_book(library):
    # collection = books_collection()
    book_id = input("Enter book ID to update book details : ")

    if book_id in library:
        print("Enter new details in the field or Press Enter to skip : ")
        new_title = input(f"1. Edit Title : Existing Title is {library[book_id]['Title']}, Enter New Title : ")
        new_genre = input(f"2. Edit Genre : Existing Genre is {library[book_id]['Genre']}, press Enter to get "
                          f"Genre Menu "), get_genre_type()
        new_author = input(f"3. Edit Author: Existing Autor is {library[book_id]['Author']}, Enter New Author : ")
        new_copies_count = input("3. Edit Copies : ")

        if new_title:
            library[book_id]['Title'] = new_title

        if new_genre:
            library[book_id]['Genre'] = new_genre

        if new_author:
            library[book_id]['Author'] = new_author

        if new_copies_count:
            library[book_id]['Copies'] = int(new_copies_count)

        else:
            print("No book found to update.. Please try again..!!!")

    print(f"Details of book ID {book_id} updated successfully..!!")

    print("**************************************************** \n")


def remove_book(library):
    book_id = input("Enter book_id which is to be removed from the library : ")
    if book_id in library.keys():
        library.pop(book_id)
        print("*" * 50)
        print(f"The book with id {book_id} is removed from the library")
        print("*" * 50)


def filter_book(library):
    print("Press Enter to select Genre Type...")
    genre_type = get_genre_type()
    genre_books = {}
    print("****************************************************")

    print(f"Following are the books of genre {genre_type} -")
    for bookid, details in library.items():
        if details['Genre'] == genre_type:
            genre_books['Title'] = library[bookid]['Title']
            print("-", genre_books['Title'])

    print("**************************************************** \n")


def count_books(library):
    print(library.values())
    total_books = sum(book["Copies"] for book in library.values())

    genre_type = get_genre_type()
    genre_book_count = sum(genre_books['Copies']for genre_books in library.values() if genre_books['Genre'] == genre_type)

    print("*" * 50)
    print(f"Total number of books in the library is {total_books}")
    print("*" * 50)
    print("*" * 50)
    print(f"Total number of books in the library of genre {genre_type} is {genre_book_count}")
    print("*" * 50)


def display_main_menu():
    print(
        "Main Menu - \n"
        "1. Add Book \n"
        "2. Search Book \n"
        "3. Update Book \n"
        "4. Remove Book \n"
        "5. Filter Books by Genre \n"
        "6. Count Books \n"

    )


def main():
    # library = {}
    library = books_collection()

    while True:
        display_main_menu()
        choice = int(input("Enter menu number of you choice: "))

        match choice:
            case 1:
                add_book(library)

            case 2:
                search_book(library)

            case 3:
                update_book(library)

            case 4:
                remove_book(library)

            case 5:
                filter_book(library)

            case 6:
                count_books(library)

            case 0:
                print("Enter 0 to exit the application..!!")

            case _:
                print("Invalid option..!! try again")


if __name__ == "__main__":
    main()
