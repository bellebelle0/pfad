# tarot card dataset : https://github.com/metabismuth/tarot-json/releases/tag/v0

# TODO: map a value to tartot card names and lifepath desc
#TODO: function to add birthdates
def calculateLifePath(birthDate):
    #split birthdays by every two digits
    #add digits
    #check if final number is within available tarot values
    #if not reduce again
    #else return value
    #return secondary values
    pass

def getCard(lifePath):
    #use map to get tarot card and desc
    pass

def showResult():
    #show the card and its desc in a popup window
    pass


#TODO: Main
if __name__ == '__main__':
    while True:
        print('Please input your birthday in the form DDMMYY. For example: January 1st, 1999 would be 01011999')
        birthDate = input()

        restart = input('Ask another birthday? y/n \n')
        if restart.lower() == 'y':
            continue
        else:
            break


#return corresponding card and display it

#TODO: add keyword inputs such as favorite animal to customize a tarot card?