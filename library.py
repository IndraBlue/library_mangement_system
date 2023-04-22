class Library:
  def __init__(self,list,name):
    self.bookList=list
    self.name=name
    self.lendDict={}
  def displayBooks(self):
    print("Following are the books in Library of",self.name)
    for book in self.bookList:
      print(book)
  def lendBook(self,user,Book):
    if Book not in self.bookList:
      print("Book you are searching is not available!")
    else:
      if Book not in self.lendDict.keys():
        self.lendDict.update({Book:user})
        print("Book has been sanctioned! you can take the book")
      else:
        print("Book is already lend to ",self.lendDict[Book])
  
  def addBook(self,Book):
    self.bookList.append(Book)
    print("Book has been added: ")
  
  def returnBook(self,Book):
    self.lendDict.pop(Book)
    print("Your book has been returned!")

if __name__=="__main__":
  a=[]
  n=int(input("Enter the number of book: "))
  for i in range(n):
    print("Enter book: ")
    a.append(input())
  obj=Library(a,"most dangerous books")
