# Tema PA, Zane Livia, CR1.3B, ACE-UCV

from utils import *
import time

print("\n=====================================================")
print("\nHomework: Library Management System")
print("Author: Zane Livia, ACE-UCV, CR1.3B")

# Book's single linked list with push beginning
head_book = LinkedList_books()
authors = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]
add_book(head_book, "Carte 3", authors)
authors = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
add_book(head_book,"Carte 2", authors)
authors = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
add_book(head_book,"Carte 1", authors)

# List the book's list
print("\n=====================================================")
print("\nList the book's single linked list")
list_books(head_book)


# Author's single linked list with push beginning
head_author = LinkedList_authors()
name = "Zane"
given_name = "Livia"
add_author(head_author, 1, name, given_name)
name = "Zane"
given_name = "Madalina"
add_author(head_author, 2, name, given_name)
name = "Rebreanu"
given_name = "Liviu"
add_author(head_author, 3, name, given_name)

# List the author's list
print("\n=====================================================")
print("\nList the author's single linked list\n")
list_authors(head_author)


# List the library
print("\n=====================================================")
print("\nList the library\n")
list_library(head_book, head_author)

# List the author(s) of a given book
print("\n=====================================================")
print("\nList the author(s) of a given book")
title = "Carte 3"
if (find_book(head_book, title)):
    list_book_authors(head_book, head_author, title)
else:
    print("\n", title, "isn't in library")

title = "Carte 11"
if (find_book(head_book, title)):
    list_book_authors(head_book, head_author, title)
else:
    print("\n", title, "isn't in library")

title = "Carte 1"
if (find_book(head_book, title)):
    list_book_authors(head_book, head_author, title)
else:
    print("\n", title, "isn't in library")


# List the book(s) of a given author
print("\n=====================================================")
print("\nList the book(s) of a given author")
name = "Zane"
given_name = "Livia"
id = find_author(head_author, name, given_name)
if (id):
    print("\nAuthor", name, given_name, "co-authored following book(s):")
    list_author_books(head_book, id)
else:
    print("\nAuthor:", name, given_name, "isn't in library")

name = "Zane"
given_name = "Liviaaaaaaa"
id = find_author(head_author, name, given_name)
if (id):
    print("\nAuthor", name, given_name, "co-authored following book(s):")
    list_author_books(head_book, id)
else:
    print("\nAuthor:", name, given_name, "isn't in library")

name = "Zane"
given_name = "Madalina"
id = find_author(head_author, name, given_name)
if (id):
    print("\nAuthor", name, given_name, "co-authored following book(s):")
    list_author_books(head_book, id)
else:
    print("\nAuthor:", name, given_name, "isn't in library")

print("\n====================  END OF THE ALGHORITM EXAMPLES =======================\n")


#print("\nFor test run press 1 or something to exit \n")
val = input("\nFor test run press 1 or something to exit \n")
if (val == "1"):
    head_book = LinkedList_books()
    head_author = LinkedList_authors()
    random.seed()
    print("\nFill in the list of books and authors with 10.000 records")
    start = time.time()
    for i in range(10000):
        name = random_string(20)
        given_name = random_string(20)
        add_author(head_author, i, name, given_name)

    for i in range(10, 10000):
        title = random_string(40)
        for j in range(10):
            authors[j] = i - j
        add_book(head_book, title, authors)
    stop = time.time()
    print("Time [sec] =", stop - start)


  # List the author(s) for 10.000 of given books
    print("\n=====================================================")
    print("\nList the author(s) for 10.000 of given books")
    iterator_find_book = head_book
    iterator_find_author = head_author
    start = time.time()
    while(iterator_find_book.head):
        list_book_authors_nodisplay(iterator_find_book, iterator_find_author, iterator_find_book.head.title)
        iterator_find_book.head = iterator_find_book.head.next
    stop = time.time()
    print("Time [sec] =", stop - start)


    # List the book(s) for 10.000 of given authors
    head_book = LinkedList_books()
    head_author = LinkedList_authors()
    random.seed()
    for i in range(10000):
        name = random_string(20)
        given_name = random_string(20)
        add_author(head_author, i, name, given_name)
    for i in range(10, 10000):
        title = random_string(40)
        for j in range(10):
            authors[j] = i - j
        add_book(head_book, title, authors)

    print("\nList the author(s) for 10.000 of given book (each book with 10 authors)")
    print("Wait for 230 - 240 sec ........")
    iterator_find_book = head_book
    iterator_find_author = head_author
    start = time.time()
    while(iterator_find_author.head):
        list_author_books_nodisplay(head_book, iterator_find_author.head.id_author)
        iterator_find_author.head = iterator_find_author.head.next
    stop = time.time()
    print("Time [sec] =", stop - start)


    print("\n====================  END OF THE TEST =======================\n")

print("\n====================  END OF THE PROGRAM =======================\n")