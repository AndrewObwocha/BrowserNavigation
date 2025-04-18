# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 4 - Web Browser
#
# ~ Created by CMPUT 175 Team ~
# =================================================================

from stack import Stack

def getAction():
    '''
    takes action from user and checks if it is valid
    Inputs: none
    Returns: string
    '''
    userEntry = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
    assert userEntry in '=<>q', 'Invalid entry.'
    return userEntry
            

def goToNewSite(current, bck, fwd):
    '''
    This function prompts the user to enter a new website address, and returns the index to the current site
    Inputs: string
    Returns: string
    '''   
    newSite = input('URL: ')
    bck.push(current)
    fwd.clear()
    return newSite

    
def goBack(current, bck, fwd):
    '''
    This function is called when the user enters “<" during getAction() it checks if there is a webpage stored before current web page.
    Inputs: string
    Returns: string
    '''    
    try:
        website = bck.pop()
        fwd.push(current)
        return website
    except IndexError:
        print('Cannot go back.')
        return current

def goForward(current, bck, fwd):
    '''
    This function is called when the user enters “>” during getAction().it checks if there is a webpage stored after current web page.
    Inputs: string
    Returns: string
    '''    
    try:
        website = fwd.pop()
        bck.push(current)
        return website
    except IndexError:
        print('Cannot go forward.')
        return current

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True   
    
    print('Browser closing... Goodbye!')    
        
if __name__ == "__main__":
    main()