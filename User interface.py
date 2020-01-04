
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
        tk.Tk.wm_title(self,'Budget Program')
        
        #still need to figure out what this does, has been intergrated throughout the main class controller
        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        #creating top menubar
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label= 'exit', command =quit)
        filemenu.add_command(label= 'save and exit', command = lambda: popup())
        '''other options
        filemenu,add_separator()
        #ilemenu.add_command(lable = 'my ass', command=quit)
        '''
        menubar.add_cascade(label= 'File', menu=filemenu)
        tk.Tk.config(self, menu= menubar)
        

        #creating a dictionary where we will store our page objects, the key is the name of the class
        self.frames = {}
        
        #initialising all pages and storing objects within the dictionary
        for F in (startPage, payPage, addPage, takePage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
        self.show_frame(startPage)
        
        #starts off by showing the first page
        self.show_frame(startPage)
        
    #main control to determine which page to show
    def show_frame(self, cont):
        
        frame = self.frames[cont] #all frames are theoretically shown at once, however this line of code shows the current page at the top
        frame.tkraise()
        
    def uppinit(self):
        '''Runs a method in each class to update the main balance label screen'''
        self.frames[startPage].upp()
        self.frames[payPage].upp()
        self.frames[addPage].upp()
        self.frames[takePage].upp()
    
        
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
        
        #this has been used as a self. as we need to pass it to another method within the class. we should probably name all labels as self
        self.balanceLabel = ttk.Label(topFrame, font = SMALL_FONT, background =TOP_FRAME, text = displayBalance()  ) #creates the object and stores it in a variable
        self.balanceLabel.pack(pady=10,padx=10)
        
        #creating buttons
        payButton = ttk.Button(bottomFrame,text = "pay", command = lambda: controller.show_frame(payPage))
        payButton.pack()
        
        addButton = ttk.Button(bottomFrame,text = "add", command = lambda: controller.show_frame(addPage))
        addButton.pack()
        
        takeButton = ttk.Button(bottomFrame,text = "take", command = lambda: controller.show_frame(takePage))
        takeButton.pack()

    
    def upp(self):
        '''This method is called from the uppinit every time there is a balance change'''
        self.balanceLabel['text'] = displayBalance()
        
        
        
class payPage(tk.Frame):
    
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        #creating frames
        topFrame = tk.Frame(self, bg = TOP_FRAME)
        topFrame.place(relwidth=1,relheight=0.4)

        bottomFrame = tk.Frame(self, bg = BOTTOM_FRAME)
        bottomFrame.place(relwidth=1,relheight=0.6,rely = 0.4)
        
        #TOP FRAME
        titleLabel = ttk.Label(topFrame, font = LARGE_FONT, background =TOP_FRAME, text = 'Pay Page'  )
        titleLabel.pack(pady=10,padx=10)
        
        #this has been used as a self. as we need to pass it to another method within the class. we should probably name all labels as self
        self.balanceLabel = ttk.Label(topFrame, font = SMALL_FONT, background =TOP_FRAME, text = displayBalance()  )
        self.balanceLabel.pack(pady=10,padx=10)  
        
        #BOTTOM FRAME
        questionLabel = ttk.Label(bottomFrame, font = SMALL_FONT, background =BOTTOM_FRAME, text = 'How much have you been paid?'  ) #creates the object and stores it in a variable
        questionLabel.pack(pady=10,padx=10)
        
        questionEntry = ttk.Entry(bottomFrame, background = 'white')
        questionEntry.pack()
        
        payButton = ttk.Button(bottomFrame,text = "pay", command = lambda: pay(float(questionEntry.get())))
        payButton.pack()   
        
        homeButton = ttk.Button(bottomFrame,text = "home", command = lambda: controller.show_frame(startPage))
        homeButton.pack()        
        
        def pay(amount):
            '''small function that simpily calls two others, call it messy call it neat. I dont care'''
            payBalance(amount)
            controller.uppinit()
               
    def upp(self):
        self.balanceLabel['text'] = displayBalance()
        



class addPage(tk.Frame):
    
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        #creating frames
        topFrame = tk.Frame(self, bg = TOP_FRAME)
        topFrame.place(relwidth=1,relheight=0.4)

        bottomFrame = tk.Frame(self, bg = BOTTOM_FRAME)
        bottomFrame.place(relwidth=1,relheight=0.6,rely = 0.4)
        
        #TOP FRAME
        titleLabel = ttk.Label(topFrame, font = LARGE_FONT, background =TOP_FRAME, text = 'Add Page'  )
        titleLabel.pack(pady=10,padx=10)
        
        self.balanceLabel = ttk.Label(topFrame, font = SMALL_FONT, background =TOP_FRAME, text = displayBalance()  )
        self.balanceLabel.pack(pady=10,padx=10)  
        
        #BOTTOM FRAME

        questionLabel = ttk.Label(bottomFrame, font = SMALL_FONT, background =BOTTOM_FRAME, text = 'How much do you wish to add? Which account?'  ) #creates the object and stores it in a variable
        questionLabel.pack(pady=10,padx=10)
        
        questionEntry = ttk.Entry(bottomFrame, background = 'white')
        questionEntry.pack()
        
        self.account = tk.StringVar()
        accountChoose = ttk.Combobox(bottomFrame, textvariable=self.account, values=('leisure','pushbike','uni'))
        accountChoose.pack(pady=10,padx=10)
        
        addButton = ttk.Button(bottomFrame,text = "add", command = lambda: add(float(questionEntry.get())))
        addButton.pack()  
        
        homeButton = ttk.Button(bottomFrame,text = "home", command = lambda: controller.show_frame(startPage))
        homeButton.pack()
        
        def add(amount):
            addBalance(amount, self.account.get())
            controller.uppinit()
        
    def upp(self):
        self.balanceLabel['text'] = displayBalance()
        

            
        
class takePage(tk.Frame):
    
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        #creating frames
        topFrame = tk.Frame(self, bg = TOP_FRAME)
        topFrame.place(relwidth=1,relheight=0.4)

        bottomFrame = tk.Frame(self, bg = BOTTOM_FRAME)
        bottomFrame.place(relwidth=1,relheight=0.6,rely = 0.4)
        
        #TOP FRAME
        titleLabel = ttk.Label(topFrame, font = LARGE_FONT, background =TOP_FRAME, text = 'Take Page'  )
        titleLabel.pack(pady=10,padx=10)
        
        self.balanceLabel = ttk.Label(topFrame, font = SMALL_FONT, background =TOP_FRAME, text = displayBalance()  )
        self.balanceLabel.pack(pady=10,padx=10)  
        
        #BOTTOM FRAME

        questionLabel = ttk.Label(bottomFrame, font = SMALL_FONT, background =BOTTOM_FRAME, text = 'How much do you wish to take? Which account?'  ) #creates the object and stores it in a variable
        questionLabel.pack(pady=10,padx=10)
        
        questionEntry = ttk.Entry(bottomFrame, background = 'white')
        questionEntry.pack()
        
        self.account = tk.StringVar()
        accountChoose = ttk.Combobox(bottomFrame, textvariable=self.account, values=('leisure','pushbike','uni'))
        accountChoose.pack(pady=10,padx=10)
        
        addButton = ttk.Button(bottomFrame,text = "take", command = lambda: take(float(questionEntry.get())))
        addButton.pack()  
        
        homeButton = ttk.Button(bottomFrame,text = "home", command = lambda: controller.show_frame(startPage))
        homeButton.pack()
        
        def take(amount):
            takeBalance(amount, self.account.get())
            controller.uppinit()
        
    def upp(self):
        self.balanceLabel['text'] = displayBalance()

def popup():
    #creation/ settings
    popup = tk.Tk()
    popup.geometry('320x240')
    popup.wm_title('save and exit')
    
    #labels/buttons
    confirmationLabel = ttk.Label(popup, text = 'Are you sure you would like to exit?', font = SMALL_FONT)
    confirmationLabel.pack(pady=20,padx=10)
    
    yesButton = ttk.Button(popup, text = 'yes', command = lambda: save())
    yesButton.pack()
    
    noButton = ttk.Button(popup, text = 'no', command = popup.destroy)
    noButton.pack()
    #now we display the popup
    popup.mainloop()




#code officially starts here
app = GUI()    
app.geometry('640x480')
app.mainloop()

