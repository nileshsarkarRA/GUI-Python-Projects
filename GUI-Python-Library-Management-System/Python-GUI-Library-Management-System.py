## Library Management System by Team Achievers 

## Import all the relevant modules
import csv
from tkinter import *
from tkinter import messagebox


# Function to add a book to the library management System
def add_book():
    # Get the values from the entry boxes
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_author = book_author_entry.get()

    # Check if any field is empty error handling
    if book_id == "" or book_title == "" or book_author == "":
        messagebox.showerror("Error", "Please fill all the fields!")
    else:
        # Open the CSV file in append mode to add details
        with open("libraryDetailsData.csv", "a") as file:
            writer = csv.writer(file)
            # Write the values to the file
            writer.writerow([book_id, book_title, book_author])
        # Show a success message
        messagebox.showinfo("Success", "Book added successfully!")
        # Clear the entry boxes
        book_id_entry.delete(0, END)
        book_title_entry.delete(0, END)
        book_author_entry.delete(0, END)


# Function to search for a book in the library management system
def search_book():
    # Get the value to search from the entry box
    search_value = search_entry.get()

    # Open the CSV file in read mode using with to save file
    with open("libraryDetailsData.csv", "r") as file:
        reader = csv.reader(file)
        # Loop through the rows in the file
        for row in reader:
            # If the search value matches any of the fields
            if search_value in row:
                # Show the book details in a message box
                messagebox.showinfo("Book Details", f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor: {row[2]}")
                # Clear the search entry box
                search_entry.delete(0, END)
                return
        # If no match was found, show an error message
        messagebox.showerror("Error", "Book not found! Try to check libraryDetailsData.csv file")
        # Clear the search entry box
        search_entry.delete(0, END)


# Specifications of the GUI of the Library Management System
library_window = Tk()
library_window.title("Library Management System by Team Achievers")
library_window.geometry("450x180")

# Create the labels and entry boxes
Label(library_window, text="Book ID:").grid(row=0, column=0)
book_id_entry = Entry(library_window)
book_id_entry.grid(row=0, column=1)

Label(library_window, text="Title:").grid(row=1, column=0)
book_title_entry = Entry(library_window)
book_title_entry.grid(row=1, column=1)

Label(library_window, text="Author:").grid(row=2, column=0)
book_author_entry = Entry(library_window)
book_author_entry.grid(row=2, column=1)

Label(library_window, text="Search for book \nInclude either Name of book or Author or ID:").grid(row=3, column=0)
search_entry = Entry(library_window)
search_entry.grid(row=3, column=1)

# Create the buttons
add_button = Button(library_window, text="Add Book", command=add_book)
add_button.grid(row=5, column=0)

search_button = Button(library_window, text="Search Book", command=search_book)
search_button.grid(row=5, column=1)

library_window.mainloop()