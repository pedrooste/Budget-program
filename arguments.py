""" Keeps track of spending as also done with excel
This is an initial stage.
"""

__author__ = "Pedro oste"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "fuck that"
__status__ = "Prototype, Development or Production"


""" revision notes:


"""
#needed for copying files(backup)
import shutil

#global variables
balance = {}
percent = [0.25,0.25,0.50] #same


#Opens the balance file and loads it into a dictionary
try:
    with open('Media/balance.txt', 'r') as file:
        for line in file.readlines(): 
            list = line.split('\t') #spilts the original file into a list of three
            list1 = list[0] #creates an individual of each to create a final list later
            list2 = float(list[1]) #has to make an int otherwise it will sort it as if its an str 
            balance[list1] = list2
except:
    print('there is no file specified') #debugging statement
    quit()
    

   
   
def addBalance(amount, account):
    '''adds amount to the selected account'''
    balance[account] = round((balance[account] + amount),2)

def takeBalance(amount, account):
    '''takes amount from the selected account'''
    balance[account] = round((balance[account] - amount),2)

def displayBalance():
    '''returns a text to be displayed by the balance label'''
    total = round(balance['leisure'] + balance['pushbike'] + balance['uni'],2)
    text = ('Your current balance is $%s\nLeisure: $%s \nPushbike: $%s \nUni: $%s' % (total,balance['leisure'],balance['pushbike'],balance['uni']))
    #print(text)
    return (text)

def payBalance(amount):
    '''seperates pay into seperate amounts'''
    spend = round((amount*percent[0]),2)
    balance['leisure'] = balance['leisure'] + spend

    push = round((amount*percent[1]),2)
    balance['pushbike'] = balance['pushbike'] + push

    uni = round((amount*percent[2]),2)
    balance['uni'] = balance['uni'] + uni

        
       
def save():
    #makes a copy of the file before saving
    shutil.copy('media/balance.txt', 'media/balanceBackup.txt')
        
    with open('media/balance.txt','w') as file: #Will create a new file if there is not one there, use append to not overwrite data
        file.write('leisure\t'+str(balance['leisure'])+'\npushbike\t'+str(balance['pushbike'])+'\nuni\t'+str(balance['uni'])) #writes to the file
        print('sucessfull')
    quit()
