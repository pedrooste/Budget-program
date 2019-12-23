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
import shutil


#data

balance = [] #savings,pushbike,uni
percent = [0.25,0.25,0.50] #same

#trys to find the file and load it into a list
try:
    with open('media/balance.txt', 'r') as file: #with will automatically close the file
        for line in file.readlines(): 
            balance.append(float(line)) #creates a temp list of highscores

        #if it cant find the file...
except:
    print('there is no file specified') #debugging statement
    quit()


        
def addBalance():
    account = int(input('which account would you like to add too? \n spendings(0) \n pushbike(1) \n uni(2) \n '))
    amount = float(input('how much would you like to add? '))
    
    balance[account] = round((balance[account] + amount),2)
    total = balance[0] + balance[1] + balance[2]
    
    print("you now have",balance[account],"in that account \nThe total is now",total)

    cont = input('\n continue?')
    if cont == 'n':
        quit()

def takeBalance():
    account = int(input('which account would you like take away from? \n spendings(0) \n pushbike(1) \n uni(2) \n '))
    amount = float(input('how much would you like to add? '))
    
    balance[account] = round((balance[account] - amount),2)
    total = balance[0] + balance[1] + balance[2]
    
    print("you now have",balance[account],"in that account \n The total is now",total)

    cont = input('\n continue?')
    if cont == 'n':
        quit()

def displayBalance():
    total = balance[0] + balance[1] + balance[2]
    text = ('Your current balance is %s\nsavings: %s \npushbike: %s \nuni: %s' % (total,balance[0],balance[1],balance[2]))
    return (text)
        
def payBalance():
    amount = float(input('How much have you been paid?'))
    
    spend = round((amount*percent[0]),2)
    balance[0] = balance[0] + spend
    
    push = round((amount*percent[1]),2)
    balance[1] = balance[1] + push
    
    uni = round((amount*percent[2]),2)
    balance[2] = balance[2] + uni
    
    print(' savings:',balance[0],'\n pushbike:',balance[1],'\n uni:',balance[2])
    
    cont = input('\n continue?')
    if cont == 'n':
        quit()
        
        
        
def save():
    total = balance[0] + balance[1] + balance[2]
    print('the total is',total,'where each account is \n savings:',balance[0],'\n pushbike:',balance[1],'\n uni:',balance[2])
    match = input('Does this match? ')
    
    if match == 'y':
        print('\nmatch is correct')
        
        shutil.copy('media/balance.txt', 'media/balanceBackup.txt') #creates backup, first is file, second is destination
        
        with open('media/balance.txt','w') as file: #Will create a new file if there is not one there, use append to not overwrite data
            file.write(str(balance[0])+'\n'+str(balance[1])+'\n'+str(balance[2])) #writes to the file
            print('sucessfull')

    else:
        print('\nokay try again')
