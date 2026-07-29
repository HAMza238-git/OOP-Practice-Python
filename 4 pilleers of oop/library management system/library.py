class Books:
    def __init__(self, book_id, title, author, category, avalibility):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.avalibility = avalibility

    def display_info(self):
        print("book_id", self.book_id)
        print("title", self.title)
        print("author", self.author)
        print("category", self.category)
        print("avalibility", self.avalibility)
        print()

book1 = Books("B101", "pak_His", "Danyal", "Histroy", True)

book1.display_info()

class Member:
    def __init__(self, member_id, name, phone,  ):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.borrowed_books = []

    def display_info(self):
        print("Member id", self.member_id)
        print("Name", self.name)
        print("Phone no", self.phone)
        print ("Borrowed Books", self.borrowed_books)
        print()

member1 = Member("M101", "Danyal", "0920001",)

member1.display_info()

class Library:
    def __init__(self):
        self.books = []
        self.member = []

    def add_Books(self, books):
        self.books.append(books)

    def display_all_books(self):
        for books in self.books:
            books.display_info()

    def add_members(self, members):
        self.member.append(members)

    def display_all_member(self):
        for members in self.member:
            members.display_info()


    def search_books(self, books_id):
        for books in self.books:
            if books.book_id == books_id:
                books.display_info()
                return
        print("record not found")

    def search_member(self, member_id):
        for member in self.member:
            if member.member_id == member_id:
                member.display_info()
                print("member is found")
                return
                
        print("member not found")
                            

    def borrow_book(self, book_id, member_id):
        for member in self.member:
            if member.member_id == member_id:
                for books in self.books:
                    if books.book_id == book_id:
                        if books.avalibility:
                            member.borrowed_books.append(books)
                            books.avalibility = False
                            print("book borwoed successfully")
                            return
                        else:
                            print("Book already borrowed")
                            return
                    
                print("book not found")
                return
         
        print("member not found")



    def return_book(self, book_id, member_id):
        for member in self.member:
            if member.member_id == member_id:
                for books in member.borrowed_books:
                    if books.book_id == book_id:
                            member.borrowed_books.remove(books)
                            books.avalibility = True
                            print("book returned successfully")
                            return
                print("book not found")
                return
        print("member not found")

   




system = Library()

# system.add_Books(book1)
# system.add_members(member1)

# system.search_books("B101")
# system.search_member("M101")
# system.borrow_book("B101", "M101")
# system.return_book("B101", "M101")
while True:
    print("1. Add Books",)
    print("2. Add Member",)
    print("3. Display all Books",)
    print("4. Display all Member",)
    print("5. search Books",)
    print("6. search Member",)
    print("7. Borrowed Books",)
    print("8. Return Books",)
    print("9. Exit",) 

    choice = (input("Enter your Choice"))   

    if choice == "1":
        book_id = input("Enter book id")
        title = input("Enter title")
        author = input("Enter author name")
        category = input("Enter category")

        book = Books(book_id, title, author, category, True)
        system.add_Books(book)
        print("book added successfully")

    elif choice == "2":
        member_id = input("enter id of member")
        name = input("name")
        phone = input("phone no")

        member = Member(member_id, name, phone)
        system.add_members(member)
        print("member added successfully")

    elif choice == "3":
         system.display_all_books()

    elif choice == "4":
             system.display_all_member()

    elif choice == "5":
        book_id = input ("enter book id")
        system.search_books(book_id)

    elif choice == "6":
            member_id = input ("enter member id")
            system.search_member(member_id)

    elif choice == "7":
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        system.borrow_book(book_id, member_id)


    elif choice == "8":
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        system.return_book(book_id, member_id)

    elif choice == "9":
        print("thnakyou for using library management system")
        break

    else:
        print("invalid choice")







    