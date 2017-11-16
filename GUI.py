# import our required library TK Interface
import tkinter
import random



"""
    # Create the main window from tkinter
    Main_window = tkinter.Tk()

    # enter the main loop of Tkinter

    tkinter.mainloop()


main()

"""


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create a label (widget) to contain 'Hello World'
        self.label_1 = tkinter.Label(self.main_window, text="Cheese for Everyone!")
        self.label_2 = tkinter.Label(self.main_window, text="Where are you hiding little mortal we were just starting to have fun!!")
        self.label_3 = tkinter.Label(self.main_window, text=input('Enter a comment: '))
        self.label_4 = tkinter.Label(self.main_window, text=int(input('Enter a comment: ')))

        # Packing label to make it referable to he main window
        self.label_1.pack(side='top')
        self.label_2.pack(side='left')
        self.label_3.pack(side='bottom')
        self.label_4.pack(side='right')

        # enter the main loop of Tk()
        tkinter.mainloop()


my_gui = MyGui()
