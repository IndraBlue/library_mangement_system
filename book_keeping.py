user_choice=0
  while(user_choice<5):
    print("Press 1 for Displaying Books")
    print("Press 2 for lending a book")
    print("Press 3 to add a book")
    print("Press 4 to return a book")
    print("Press 5 to Exit")

    user_choice=int(input("Enter the choice: "))

    if user_choice==1:
      obj.displayBooks()
    elif user_choice==2:
      Book=input("Enter book: ")
      user=input("Enter name: ")
      obj.lendBook(user,Book)
    elif user_choice==3:
      Book=input("Enter the book name: ")
      obj.addBook(Book)
    elif user_choice==4:
      Book=input("Enter the book to return: ")
      obj.returnBook(Book)
    else:
      print("Thank You!")
      break
    
