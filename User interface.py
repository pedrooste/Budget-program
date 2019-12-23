import tkinter as tk
from tkinter import ttk #use this on labels and buttons for a nicer version
from arguments import *

LARGE_FONT = ("verdana",20)
SMALL_FONT = ("verdana",12)
BOTTOM_FRAME = '#f0f0f0'
TOP_FRAME = '#e8fdff'

class GUI(tk.Tk):
    def __init__ (self, *Args, **kwargs):
        
        tk.Tk.__init__ (self, *Args, **kwargs)
        
        #creating the window details
        '''tk.Tk.iconnitmap(self, default='enter address, must be icon')'''
        tk.Tk.wm_title(self,'eat my ass')
        
        #still need to figure out what this does, has been intergrated throughout the main class controller
        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        #creating top menubar
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label= 'exit', command =quit)
        '''other options
        filemenu,add_separator()
        #ilemenu.add_command(lable = 'my ass', command=quit)
        '''
        menubar.add_cascade(label= 'File', menu=filemenu)
        tk.Tk.config(self, menu= menubar)
        
        self.frames = {}
        
        #initialising all pages
        for F in (startPage, payPage, addPage, takePage):
            
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
        
        self.show_frame(startPage)
    
    #main control to determine which page to show
    def show_frame(self, cont):
        
        frame = self.frames[cont] #all frames are theoretically shown at once, however this line of code shows the current page at the top
        frame.tkraise()
    
    
class startPage(tk.Frame):
    
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        #creating frames
        topFrame = tk.Frame(self, bg = TOP_FRAME)
        topFrame.place(relwidth=1,relheight=0.8)

        bottomFrame = tk.Frame(self, bg = BOTTOM_FRAME)
        bottomFrame.place(relwidth=1,relheight=0.2,rely = 0.8)
        #creating labels
        titleLabel = ttk.Label(topFrame, font = LARGE_FONT, background =TOP_FRAME, text = 'Welcome!'  )
        titleLabel.pack(pady=10,padx=10)
        
        balanceLabel = ttk.Label(topFrame, font = SMALL_FONT, background =TOP_FRAME, text = displayBalance()  ) #creates the object and stores it in a variable
        balanceLabel.pack(pady=10,padx=10)
        #creating buttons
        payButton = ttk.Button(bottomFrame,text = "pay", command = lambda: controller.show_frame(payPage))
        payButton.pack()
        
        addButton = ttk.Button(bottomFrame,text = "add", command = lambda: controller.show_frame(addPage))
        addButton.pack()
        
        takeButton = ttk.Button(bottomFrame,text = "take", command = lambda: controller.show_frame(takePage))
        takeButton.pack()


        
        
        
        
class payPage(tk.Frame):
    
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        lable = ttk.Label(self,text="pay page", font = LARGE_FONT) #creates the object and stores it in a variable
        lable.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self,text = "home", command = lambda: controller.show_frame(startPage))
        button1.pack()


class addPage(tk.Frame):
    
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        lable = ttk.Label(self,text="add page", font = LARGE_FONT) #creates the object and stores it in a variable
        lable.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self,text = "home", command = lambda: controller.show_frame(startPage))
        button1.pack()
        
class takePage(tk.Frame):
    
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        lable = ttk.Label(self,text="take page", font = LARGE_FONT) #creates the object and stores it in a variable
        lable.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self,text = "home", command = lambda: controller.show_frame(startPage))
        button1.pack()


        
app = GUI()
app.geometry('640x480')
app.mainloop()