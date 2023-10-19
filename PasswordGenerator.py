import tkinter as tk
import random
import string
root = tk.Tk()
root.title("Password Generator")


def generate_password1():
    password_length = int(passwordLength_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    result = password
    generate_password_entry.insert(0, result)



def accept_password():
    accepted_password = generate_password_entry.get()
    username = name_entry.get()
    result_label.config(text=f"Username: {username}\nPassword: {accepted_password}")



def reset_password():
    generate_password_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    result_label.config(text="")


enter_username = tk.Label(root, text="Enter User Name:", fg="green")
enter_username.grid(row=1, column=0, padx=10, pady=5, sticky='e')

enter_passwordLength = tk.Label(root, text="Enter Password Length:", fg="green")
enter_passwordLength.grid(row=2, column=0, padx=10, pady=5, sticky='e')

generate_password = tk.Label(root, text="Generated Password:", fg="green")
generate_password.grid(row=3, column=0, padx=10, pady=5, sticky='e')

name_entry = tk.Entry(root, borderwidth=3, relief="sunken", bg="light blue")
name_entry.grid(row=1, column=1, padx=10, pady=5)

passwordLength_entry = tk.Entry(root, borderwidth=3, relief="sunken", bg="light blue")
passwordLength_entry.grid(row=2, column=1, padx=10, pady=5)

generate_password_entry = tk.Entry(root, borderwidth=3, relief="sunken", bg="light blue")
generate_password_entry.grid(row=3, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password1, bg="yellow", fg="dark blue")
generate_button.grid(row=4, column=1, padx=10, pady=5)

accept_button = tk.Button(root, text="Accept", command=accept_password)
accept_button.grid(row=5, column=0, padx=10, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_password)
reset_button.grid(row=5, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="", fg="red")
result_label.grid(row=6, columnspan=2, padx=10, pady=10)

root.mainloop()
