import tkinter


class Gui:
    def __init__(self):
        # create a window
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window,  width=300, height=300)
        self.pop = tkinter.Canvas(self.main_window)
        gif_1 = tkinter.PhotoImage(file='Car.gif')

        # create window frames and canvas image

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.canvas.create_image(150, 150, image=gif_1)

        # create some labels

        self.tank_label = tkinter.Label(self.top_frame, text='enter how many gallons your cars holds: ')
        self.tank_entry = tkinter.Entry(self.top_frame, width=10)
        self.miles_label = tkinter.Label(self.top_frame, text='How many miles have you traveled')
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        # pack button's

        self.canvas.pack()
        self.tank_label.pack(side='top')
        self.tank_entry.pack(side='top')
        self.miles_label.pack(side='top')
        self.miles_entry.pack(side='top')

        # create buttons
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='quit', command=self.main_window.destroy)

        self.describe_label = tkinter.Label(self.mid_frame, text='Converted to miles per gallons: ')

        self.value = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)

        self.describe_label.pack(side='left')
        self.miles_label.pack(side='left')

        # pack more buttons and frames
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Main loop time
        tkinter.mainloop()

    def convert(self):
        tanks = float(self.tank_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles/tanks

        self.value.set(format(mpg, ',.2f'))

# call the function


gui = Gui()
