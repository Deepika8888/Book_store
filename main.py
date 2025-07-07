def main ():
   #creating a book list
   try:
       booksList = []
       infile = open("thebooksList.txt", "r")
       line = infile.readline()
       while line: 
           booksList.append(line.rstrip("\n").split(","))
           line = infile.readline()
       infile.close()
   except FileNotFoundError:
       print("the booksList.txt is not found.")
       print("Starting a new book list.")
       booksList = []
       

   choice = 0
   while choice != 4:
       print("***Book Manager***")
       print("1), Add a book")
       print("2), Look up a book")
       print("3), Display a book") 
       print("4), Quit")
       choice = int(input())

       if choice ==1:
           print("Adding a book...")
           nBook = input("Enter a name of the book>>>: ")
           nAuthor= input("Enter a name of the Author>>>: ")
           nPages = input("Enter the pages of a Book: ")
           booksList.append([nBook, nAuthor, nPages])
       elif choice ==2:
           print("Looking for a book....")
           keyword = input("Enter the search term: ")
           for book in booksList:
               if keyword in book:
                   print(book)
       elif choice ==3:
           print("Displaying all books....")
           for i in range(len(booksList)):
               print(booksList[i])

       elif choice ==4:
           print("Quitting Program....")
   print("Program Terminted")
         
# saving to text file    
   outfile = open("thebooksList.txt", "a")
   for book in booksList:
       outfile.write(",".join(book) + "\n")
   outfile.close()
           



if __name__ == "__main__":
    main()

