import tkinter as tk

# Create a new window
root = tk.Tk()


# Function to open a new window for entering data
def open_new_window():
    new_window = tk.Toplevel(root)

    # Create labels and entry fields
    number_label = tk.Label(new_window, text="Number:")
    number_label.pack()

    number_entry = tk.Entry(new_window)
    number_entry.pack()

    name_label = tk.Label(new_window, text="Name:")
    name_label.pack()

    name_entry = tk.Entry(new_window)
    name_entry.pack()

    # Function to add data to the list
    def add_to_list():
        number = number_entry.get()
        name = name_entry.get()

        # Add the data to the list or perform any other desired operation
        # You can also update the user interface to reflect the changes

        # Clear the entry fields after adding the data
        number_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)

    # Create a button to add the data to the list
    add_button = tk.Button(new_window, text="Add", command=add_to_list)
    add_button.pack()


# Function to clear the entry fields
def clear_entry():
    number_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)


# Create a button to open a new window
open_button = tk.Button(root, text="Open", command=open_new_window)
open_button.pack()

# Create a button to clear the entry fields
clear_button = tk.Button(root, text="Clear", command=clear_entry)
clear_button.pack()

# Run the main loop
root.mainloop()