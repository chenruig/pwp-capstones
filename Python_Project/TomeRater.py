class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        #if self == self.User:

        return self.email

        #else:
        #    return "User is NOT found!"

    def change_email(self, address):
        #if self == self.User:

        self.email = address
        print("This user's email has been updated.")
        
        #return "{}'s email has been updated.".format(self.User)
        #else:
        #    return "User is NOT found!"

    def __repr__(self):
        #if self == self.User:

        return "User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))

        #number_of_book = len(self.books)
        #return "User {0}, email: {1}, books read: {2}".format(0=self.name, 1=self.email, 2=number_of_book)
        #else:
        #    return "User is NOT found!"

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return self.User == other_user
        else:
            pass
    
    def read_book(self, book, rating = None):
        if book not in self.books:
            self.books.update({book: rating})
        else:
            pass

    def get_average_rating(self):
        total_rating = 0
        total_book = len(self.books)
        average_rating = total_rating / total_book
        for rating in self.books.values():
            total_rating += rating
        return averge_rating          
            
                
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return str(self.isbn)

    def set_isbn(self, new_isbn):
        #if self.Book == self.title:

        self.isbn = new_isbn
        print("This book's ISBN has been updated.")

        #return "The book of " + self.title + "'s ISBN had been updated."

    def add_rating(self, rating):
        if rating >= 0 and rating <=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_books.title and self.isbn == other_books.isbn:
            return self.Book == other_book
        else:
            pass

    def __hash_(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        number_rating = len(self.ratings)
        sum_rating = 0
        average = sum_rating / number_rating
        for rating in self.ratings:
            sum_rating += rating
        return average


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject
    

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def creat_book(self, title, isbn):
        Book.title = title
        Book.isbn = isbn
        return self.Book

    def creat_novel(self, title, author, isbn):
        Fiction.title = title
        Fiction.author = author
        Fiction.isbn = isbn
        return self.Fiction

    def create_non_fiction(self, title, subject, level, isbn):
        Non_Fiction.title = title
        Non_Fiction.subject = subject
        Non_Fiction.level = level
        Non_Fiction.isbn = isbn
        return self.Non_Fiction

    def add_book_to_user(self, book, email, rating = None):
        for email in self.users.keys():
            if email not in self.users:
                return "No user with email {}!".format(self.email)
            elif eamil in self.users:
                User.read_book(book, rating)
                Book.add_rating(rating)
        for book in self.books.keys():
            if book not in self.books:
                self.books[book] = 1
            elif book in self.books:
                self.books[book] += 1

    def add_user(self, name, email, user_book = None):
        User.name = name
        User.email = email
        if user_book != None:
            for book in user_books:
                TomeRater.add_book_to_user(book)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.user.values():
            print(value)

    def most_read_book(self):
        most_read_book = str(book)
        most_read_value = int(rating)
        for key, value in self.books.items():
            if value > most_read_value:
                most_read_value = value
                most_read_book = key
        return most_read_book

    def highest_rated_book(self):
        all_books = {}
        for book in self.books:
            if book in self.Book:
                all_books.update({book: book.get_average_rating()})

        most_rated_book = str(book)
        highest_rated_book = int(rating)
        for key, value in all_books.items():
            if value > highest_rated_book:
                highest_rated_book = value
                most_rated_book = key
        return most_rated_book

    def most_positive_user(self):
        all_users = {}
        for user in self.users:
            if user in self.User:
                all_users.update({user: user.get_average_rating()})

        most_positive_user = str(user)
        highest_rated_user = int(rating)
        for key, value in all_users.items():
            if value > highest_rated_user:
                highest_rated_user = value
                most_positive_use = key
        return most_positive_use
            
        
            
            
            
        


        
                
            

            
            

    
        
        
        


        
            








































    

    
