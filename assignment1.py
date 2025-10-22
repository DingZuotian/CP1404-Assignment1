"""
CP1404 Assignment 1 - Books to Read
Name:DingZuotian
Date Started:10/19/2025
GitHub URL:https://github.com/DingZuotian/CP1404-Assignment1.git
"""
COMPLETED_STATUS = 'c'
UNREAD_STATUS = 'u'
FILENAME = "books.csv"


def main():
    print("Books to Read 1.0 by DingZuotian")
    books = load_books(FILENAME)

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "Q":
            save_books(books, FILENAME)
            print(f"{len(books)} books saved to {FILENAME}")
            print("\"So many books, so little time. Frank Zappa\"")
            break
        elif choice == "D":
            display_books(books)
        elif choice == "A":
            add_book(books)
        elif choice == "C":
            complete_book(books)


def load_books(filename):
    books = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    title, author, pages, status = parts
                    books.append([title, author, int(pages), status])
        print(f"{len(books)} books loaded.")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty book list.")
    except Exception as e:
        print(f"Error loading books: {e}")

    return books


def save_books(books, filename):
    try:
        with open(filename, 'w') as file:
            for book in books:
                file.write(f"{book[0]},{book[1]},{book[2]},{book[3]}\n")
    except Exception as e:
        print(f"Error saving books: {e}")


def display_menu():
    print("\nMenu:")
    print("D - Display books")
    print("A - Add a new book")
    print("C - Complete a book")
    print("Q - Quit")


def get_menu_choice():
    while True:
        choice = input(">>> ").upper()
        if choice in ['D', 'A', 'C', 'Q']:
            return choice
        print("Invalid menu choice")


def display_books(books):
    if not books:
        print("No books in list.")
        return

    sorted_books = sorted(books, key=lambda x: (x[1].lower(), x[0].lower()))

    max_title_len = max(len(book[0]) for book in sorted_books)
    max_author_len = max(len(book[1]) for book in sorted_books)

    unread_count = 0
    unread_pages = 0

    for i, book in enumerate(sorted_books, 1):
        title, author, pages, status = book
        marker = "*" if status == UNREAD_STATUS else " "

        if status == UNREAD_STATUS:
            unread_count += 1
            unread_pages += pages

        print(f"{marker}{i}. {title:<{max_title_len}} by {author:<{max_author_len}} {pages:>4} pages")

    if unread_count == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still need to read {unread_pages} pages in {unread_count} books.")


def add_book(books):
    print("Title:")
    title = get_non_empty_input("Input can not be blank")

    print("Author:")
    author = get_non_empty_input("Input can not be blank")

    print("Number of Pages:")
    pages = get_positive_integer()

    books.append([title, author, pages, UNREAD_STATUS])
    print(f"{title} by {author} ({pages} pages) added.")


def complete_book(books):
    unread_books = [book for book in books if book[3] == UNREAD_STATUS]
    if not unread_books:
        print("No unread books - well done!")
        return

    display_books(books)

    print("Enter the number of a book to mark as completed")
    selected_number = get_positive_integer("Invalid book number", 1, len(books))

    selected_index = selected_number - 1
    selected_book = books[selected_index]

    if selected_book[3] == COMPLETED_STATUS:
        print("That book is already completed")
    else:
        selected_book[3] = COMPLETED_STATUS
        print(f"{selected_book[0]} by {selected_book[1]} completed!")


def get_non_empty_input(error_message):
    while True:
        user_input = input().strip()
        if user_input:
            return user_input
        print(error_message)


def get_positive_integer(invalid_message="Invalid input - please enter a valid number",
                         min_value=1, max_value=None):
    while True:
        try:
            user_input = input()
            if not user_input:
                print(invalid_message)
                continue

            number = int(user_input)

            if number < min_value:
                print(f"Number must be > {min_value - 1}")
            elif max_value and number > max_value:
                print(invalid_message)
            else:
                return number

        except ValueError:
            print(invalid_message)


if __name__ == "__main__":
    main()
