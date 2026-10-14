import tkinter as tk
from backEnd.databaseModel import singIn

usernameWarning = None
passwordWarning = None

def submit(username, password, root, passwordInput):
    global usernameWarning, passwordWarning

    cleanUsername = username.get()
    cleanPassword = password.get()
    if not cleanUsername.strip():
        usernameWarning = tk.Label(root, text = 'No username Inputted', font=('calibre',8, 'bold'))
        usernameWarning.grid(row=2,column=0)
    elif not cleanPassword.strip():
        passwordWarning = tk.Label(root, text = 'No password Inputted', font=('calibre',8, 'bold'))
        passwordWarning.grid(row=5,column=0)

    else:
        success = singIn(cleanUsername, cleanPassword)
        if success:
            print(123)
        else:
            incorrectDetails = tk.Label(root, text = 'Username or password Incorrect', font=('calibre',8, 'bold'))
            incorrectDetails.grid(row=5,column=0)
            password.set("")




def removeWarnings(inputEntered):
    if inputEntered == 0:
        if usernameWarning is not None and usernameWarning.winfo_manager():
            usernameWarning.grid_remove()

    if inputEntered == 1:
        if passwordWarning is not None and passwordWarning.winfo_manager():
            passwordWarning.grid_remove()