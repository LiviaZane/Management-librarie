# utils file

import random

# Node of a single linked book's list
class Node_book:
    def __init__(book, title=None, authors = None, next=None):
        book.title = title
        book.authors = authors
        book.next = next

# Linked List class with a single head node for books
class LinkedList_books:
    def __init__(book):
        book.head = None


# Node of a single linked author's list
class Node_author:
    def __init__(author, id_author=None, author_name=None, author_given_name=None, next=None):
        author.id_author = id_author
        author.author_name = author_name
        author.author_given_name = author_given_name
        author.next = next

    # Linked List class with a single head node for books
class LinkedList_authors:
    def __init__(author):
        author.head = None


# Push beginning in the book's linked list
def add_book(book, title, authors):
    new_node = Node_book(title, authors)
    new_node.next = book.head
    book.head = new_node


# Push beginning in the author's linked list
def add_author(author, id_author, author_name, author_given_name):
    new_node = Node_author(id_author, author_name, author_given_name)
    new_node.next = author.head
    author.head = new_node



# List the book's list
def list_books(book):
   iterator = book.head
   while (iterator):
      print("\n", iterator.title)
      for i in range(10):
         if (iterator.authors[i] > 0):
            print("", iterator.authors[i])
      iterator = iterator.next

# List the author's list
def list_authors(author):
   iterator = author.head
   while (iterator):
      print("", iterator.author_name,iterator.author_given_name, "id =", iterator.id_author)
      iterator = iterator.next


# Find id_author in author's list end return name and given_name of that author
def find_author_id(author, id_author):
    iterator = author.head
    while (iterator):
        if (iterator.id_author == id_author):
            return iterator.author_name + ' ' + iterator.author_given_name
        iterator = iterator.next

# List all the books, each with his author(s)
def list_library(book, author):
    iterator_book = book.head
    iterator_author = author.head
    while (iterator_book):
        print("\n", iterator_book.title, "has autor(s):")
        for i in range(10):
            if (iterator_book.authors[i] > 0):
                print("      ", find_author_id(author, iterator_book.authors[i]))
        iterator_book = iterator_book.next


# Find a book in the book's list and return 1 if founded or 0 if not
def find_book(book, title):
    iterator = book.head
    while (iterator):
        if (iterator.title == title):
            return 1
        iterator = iterator.next
    return 0

def find_author(author, name, given_name):
    iterator = author.head
    while (iterator):
        if (iterator.author_name == name and iterator.author_given_name == given_name):
            return iterator.id_author
        iterator = iterator.next
    return 0


# List the author(s) of a given book
def list_book_authors(book, author, title):
    iterator_book = book.head
    iterator_author = author.head
    while (iterator_book):
        if(iterator_book.title == title):
            print("\n", title, "has autor(s):")
            for i in range(10):
                if (iterator_book.authors[i] > 0):
                    print("      ", find_author_id(author, iterator_book.authors[i]))
            break
        iterator_book = iterator_book.next

# List the author(s) of a given book - without print()
def list_book_authors_nodisplay(book, author, title):
    iterator_book = book.head
    iterator_author = author.head
    while (iterator_book):
        if(iterator_book.title == title):
#            print("\n", title, "has autor(s):")
            for i in range(10):
                if (iterator_book.authors[i] > 0):
                    continue
#                    print("      ", find_author_id(author, iterator_book.authors[i]))
#            break
        iterator_book = iterator_book.next


# List the b00k(s) of a given author
def list_author_books(book, id):
    iterator_book = book.head
    while (iterator_book):
        for i in range(10):
            if (iterator_book.authors[i] == id):
                print("", iterator_book.title)
        iterator_book = iterator_book.next

# List the b00k(s) of a given author - without print()
def list_author_books_nodisplay(book, id):
    iterator_book = book.head
    while (iterator_book.next):
        for i in range(10):
            if (iterator_book.authors[i] == id):
                continue
#                print("", iterator_book.title)
        iterator_book = iterator_book.next



def random_string(size):
    ASCII_START = 32
    ASCII_END = 126
    rand_string = ''
    for i in range(size):
        rand_string += chr(random.randint(ASCII_START, ASCII_END))

    return rand_string