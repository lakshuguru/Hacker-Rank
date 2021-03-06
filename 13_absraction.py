'''Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these 3 parameters:
string title
string author
int price
Implements the Book class' abstract display() method so it prints these  lines:
, a space, and then the current instance's title.
, a space, and then the current instance's author.
, a space, and then the current instance's price.
Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.:public ) when declaring MyBook or your code will not execute.
Sample Input

The following input from stdin is handled by the locked stub code in your editor:

The Alchemist
Paulo Coelho
248
Sample Output

The following output is printed by your display() method:

Title: The Alchemist
Author: Paulo Coelho
Price: 248'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", title)
        print("Author:", author)
        print("Price:",price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()