import tkinter as tk
import pyjokes
import random

# Create the main window
root = tk.Tk()
root.title("JokeBot 5000")
root.geometry("400x200")  # Set the size of the window

# Create a text box for displaying jokes
joke_textbox = tk.Text(root, height=5, width=40)
joke_textbox.pack(pady=20)

# to fetch jokes from pyjokes package
def get_joke():
    joke = pyjokes.get_joke()
    joke_textbox.delete("1.0", tk.END) #to display blank textbox first, after every run
    joke_textbox.insert(tk.END, joke)


# Create a button to trigger the joke display
joke_button = tk.Button(root, text="Get a Joke", command=get_joke)
joke_button.pack(pady=10)

# Run the application
root.mainloop()

