#imports for GUI
from tkinter import *
from tkinter import ttk

# imports for authentication need to be added in this form
from LoginHandlerClass import *
from activeUserClass import *

#datato test the login functions, more can be found in db_README.txt on GIT
#st78598
#1738977
#p@ssword

# Login gui done by Gary, please do not remove comments, and all changes must be commented
# in this file and through GIT commit message if happened
##################################################################################
# Start of login GUI with authentication calls and returns
#

# instantiate the user container class, to hold and pass
# the active user's info to subsequent functions
activeUser = activeUserClass()

#functions and methods
def callbackText():
    statusBar.config(text='Clicked')

def closeToplevel():
    login.destroy()

def callLoginHandlerClass(uid, upw):
    # instantiate LoginHandler Class
    authReturn = LoginHandler(uid, upw)
    if authReturn.loggedOn != False:
        #close window, set the User Class to hold user ID
        statusBar.config(text=authReturn.loginMessage)
        activeUser.setUID(authReturn.loggedOn)
        leftFrameLabel.config(text="Hi " + activeUser.userName)
        login.destroy()
    elif authReturn.loggedOn == False:
        # should limit the tries later (no. of cases when login class returns False)
        statusBar.config(text=authReturn.loginMessage)
    # consider to kill Login object (authreturn)

#GUI generators

root = Tk()
#Window header text / window name
root.wm_title("Login")
#set min size of the window
root.minsize(width=800, height=600)
#window status bar
statusBar = Label(root, text="", bd=1, relief=GROOVE, anchor=CENTER)
#relief is the simulated 3D effect: FLAT,RAISED,SUNKEN,GROOVE,RIDGE
#anchors are used to define where text is positioned relative to a reference point
statusBar.pack(side=BOTTOM, fill=X)

login = Toplevel(root)
login.wm_title("Login")

top1LabelUid = Label(login, text="User ID")
top1LabelUid.grid(row=1, pady=10, sticky=E)
top1LabelUpw = Label(login, text="Password")
top1LabelUpw.grid(row=2, pady=10, sticky=E)

top1EntryUid = ttk.Entry(login)
top1EntryUid.grid(row=1, column=1, columnspan=2, padx=5)
top1EntryUpw = ttk.Entry(login, show="*")
top1EntryUpw.grid(row=2, column=1, columnspan=2)

top1Button1 = ttk.Button(login, text="Cancel", command=closeToplevel)
top1Button1.grid(row=3, column=1, pady=10)
top1Button2 = ttk.Button(login, text="Login", command=lambda: callLoginHandlerClass(top1EntryUid.get(), top1EntryUpw.get()))
top1Button2.grid(row=3, column=2)

login.attributes('-topmost', True) #brings toplevel window to the top
login.focus_force()  #gives focus to toplevel window
login.grab_set() # disables main window until toplevel closed or given back by login.grab_release()

#
# login window code ends here.
##################################################################################
# Main window content starts here. This part of the code can be changed and reused freely.
#

leftFrame = Frame(root, width=200, background="red", padx=10, pady=10)
rightFrame = Frame(root, background="white")

leftFrameLabel = Label(leftFrame, text="")
leftFrameLabel.pack(pady=10)

button = ttk.Button(leftFrame, text='Click me')
button.config( command = callbackText )
button.pack()

# button.state( ["disabled"] )
# button.instate( ["disabled"] )  #returns true/false depends of the state of button widget
# button.state( ["!disabled"] )

#end of frames
leftFrame.pack(expand=False, side=LEFT, fill=Y)
rightFrame.pack(expand=True, side=RIGHT, fill=BOTH)

#hook main window to the event handler loop
root.mainloop()
