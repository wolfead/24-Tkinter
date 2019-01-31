"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Alex Wolfe.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    window = tkinter.Tk()
    # -------------------------------------------------------------------------
    # done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame = ttk.Frame(window,padding=100,relief='raised')
    frame.grid()
    # -------------------------------------------------------------------------
    # done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    button1 = ttk.Button(frame, text='Hello')
    button1.grid(row=0,column=0)
    # -------------------------------------------------------------------------
    # TODO: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    button1['command'] = (lambda : print('Hello'))
    # -------------------------------------------------------------------------
    # done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    entrybox = ttk.Entry(frame)
    entrybox.grid(row=1,column=2)
    entryboxbutton = ttk.Button(frame,text='If ok typed, print Hello')
    entryboxbutton.grid(row=0,column=2)
    entryboxbutton['command'] = (lambda : print_contents(entrybox))
    # -------------------------------------------------------------------------
    # done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    intentry = ttk.Entry(frame)
    intentry.grid(row=4,column=2)
    button3 = ttk.Button(frame,text='Print String')
    button3.grid(row=3,column=2)
    button3['command'] = (lambda : print_many_contents(intentry,entrybox))
    # -------------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------






    window.mainloop()
def print_contents(entrybox):
    if entrybox.get() == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def print_many_contents(intentry, entrybox):
    for k in range(int(intentry.get())):
        print(entrybox.get())
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
