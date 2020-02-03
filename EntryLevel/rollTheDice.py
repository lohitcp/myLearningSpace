# Lets start with another simple program, rolling the dice
import random as r
#Added function to reverse the string
def rockNroll(resp):
    
    if resp == "Y":
        randNum = r.randint(1,6)
        dispTxt = "You have rolled the number {}"
        print (dispTxt.format(randNum))
        print ("=====================================")
        resp = input("Do you want to play again (Y/N) : ")
        rockNroll(resp.upper())
    elif resp == "N":
        print("Thank you for playing the game!!")
    else:
        print("Sorry, I didn't understand your entry. Please enter Y/N only")
        resp = input("Do you want to roll again (Y/N) : ")
        rockNroll(resp.upper())

#starting with main function
if __name__=="__main__": 
    #Asking for user entry
    resp = input ("Lets the roll the dice. Are you ready (Y/N) : ")
    
    rockNroll(resp.upper())
