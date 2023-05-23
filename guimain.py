import os
import tkinter as tk
from tkinter import messagebox


def generate_number_wordlist(n):
  numbers = [str(i) for i in range(10)]
  wordlist = []
  generate_wordlist_helper("", n, numbers, wordlist)
  return wordlist


def generate_wordlist_helper(prefix, n, numbers, wordlist):
  if n == 0:
    wordlist.append(prefix)
    return
  for num in numbers:
    generate_wordlist_helper(prefix + num, n - 1, numbers, wordlist)


def generate_wordlist():
  digit_entry = digit_entry_field.get()
  file_entry = file_entry_field.get()

  if not digit_entry or not file_entry:
    messagebox.showerror("Error",
                         "Digit field and file name field cannot be empty!")
    return

  try:
    n = int(digit_entry)
  except ValueError:
    messagebox.showerror("Error",
                         "Invalid digit input! Please enter a valid integer.")
    return

  filename = file_entry

  file_location = file_location_entry_field.get()
  if not file_location:
    file_location = os.getcwd()

  wordlist = generate_number_wordlist(n)
  file_path = os.path.join(file_location, filename)

  with open(file_path, "w") as file:
    for word in wordlist:
      file.write(word + "\n")

  messagebox.showinfo("Success", f"Wordlist saved to {file_path}")


# Create GUI window
window = tk.Tk()
window.title("Number Wordlist Generator")

# Create labels and entry fields
digit_label = tk.Label(window, text="Number of digits:")
digit_label.pack()
digit_entry_field = tk.Entry(window)
digit_entry_field.pack()

file_label = tk.Label(window, text="File name:")
file_label.pack()
file_entry_field = tk.Entry(window)
file_entry_field.pack()

file_location_label = tk.Label(
  window, text="File location (leave blank for current directory):")
file_location_label.pack()
file_location_entry_field = tk.Entry(window)
file_location_entry_field.pack()

generate_button = tk.Button(window,
                            text="Generate Wordlist",
                            command=generate_wordlist)
generate_button.pack()

# Run the GUI window
window.mainloop()
