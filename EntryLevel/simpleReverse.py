# "My first python program in many years!!"

#Added function to reverse the string
def reverseIt(strToRev):
    print ("=====================================\n")
    print ("Using Simple slice Method")
    print (strToRev[::-1])
    print ("=====================================\n")
    print ("Using For loop Method")
    revstrToRev = "";
    for loopVar in strToRev:
        revstrToRev = loopVar + revstrToRev;
    print (revstrToRev)
    print ("=====================================\n")
    print ("Using List method (copied from Internet)")
    revList = list(strToRev)
    revList.reverse();
    print (''.join(revList));


#starting with main function
if __name__=="__main__": 
    #Asking for user entry
    strToRev = input ("Please enter the string to be reversed : ")#"Hello World!!"
    print ("Sring Entered by you: " +strToRev)
    #print (type(strToRev))
    print ("=====================================\n")
    reverseIt(strToRev)
