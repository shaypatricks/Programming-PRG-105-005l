import tkinter
import tkinter.messagebox

class MarketGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create two frames, one for radio buttons and one for regular buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create an IntVar object to use with the radio buttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()
        self.cb_var9 = tkinter.IntVar()
        self.cb_var0 = tkinter.IntVar()

        #set the variables to zero
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)
        self.cb_var9.set(0)
        self.cb_var0.set(0)

        # create three checkbutton widgets in the top frame
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Apples', variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Wine', variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Shirt', variable = self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='shoes', variable = self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='swords', variable = self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='rifles', variable = self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='horses', variable = self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.top_frame, text='sails', variable = self.cb_var8)
        self.cb9 = tkinter.Checkbutton(self.top_frame, text='furniture', variable = self.cb_var9)
        self.cb0 = tkinter.Checkbutton(self.top_frame, text='tea', variable = self.cb_var0)
        # pack the checkbuttons

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()
        self.cb9.pack()
        self.cb0.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text='ok', command=self.total)
        self.quit_button = tkinter.Button(self.bottom_frame, text='quit', command=self.main_window.destroy)

        # pack the bottom widget buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    # show choice


    def total(self):
        # create message string
        self.message = 'you total is:\n'
        self.total = 0.0

        if self.cb_var1.get() == 1:
            self.total += 300.0
            # self.message = self.message + '$300\n'
        if self.cb_var2.get() == 1:
            self.total += 150.0
            # self.message = self.message + '$150\n'
        if self.cb_var3.get() == 1:
            self.total += 710.0
            # self.message = self.message + '$710\n'
        if self.cb_var4.get() == 1:
            self.total += 400.0
            # self.message = self.message + '$400\n'
        if self.cb_var5.get() == 1:
            self.total += 500.0
            # self.message = self.message + '$500\n'
        if self.cb_var6.get() == 1:
            self.total += 1500.0
            # self.message = self.message + '$1500\n'
        if self.cb_var7.get() == 1:
            self.total += 900.0
            # self.message = self.message + '$900\n'
        if self.cb_var8.get() == 1:
            self.total += 1000.0
            # self.message = self.message + '$1000\n'
        if self.cb_var9.get() == 1:
            self.total += 2500.0
            # self.message = self.message + '$2500\n'
        if self.cb_var0.get() == 1:
            self.total += 1000.0
            # self.message = self.message + '$1000\n'

        tkinter.messagebox.showinfo('selection', self.total)



button = MarketGui()


