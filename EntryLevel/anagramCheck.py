## To find out if 2 strings are anagrams or not
## "Tom Marvolo Riddle "="I am Lord Voldemort"
## "spar" = "rasp"
## ignores cases of strings, special charcters, spaces etc
from collections import Counter
import re
def checkAngrm(str1,str2):
    chrCount1=getCharCount(str1)
    print (chrCount1)
    chrCount2=getCharCount(str2)
    print (chrCount2)
    # Now if both strings length are different, then not an anagram
    if len(chrCount1) != len(chrCount2):
        return False;

    # if each character is different, then not an anagram
    for i in chrCount1:
        #print (i,chrCount1[i],chrCount2[i])
        if chrCount1[i] != chrCount2[i]:
            return False;
    return True;

def getCharCount(str):
    # Remove extra characters like space, numbers, !@#%$^ etc
    removeChrs = re.compile('[^A-Za-z]')
    str = removeChrs.sub('',str)
    str = str.upper()
    #print (str)
    ###Using Counter method from collections##
    #count=Counter(str)

    ##Another method using dictionary get method##
    count = {}
    for keys in str:
        count.get(keys,0)
        count[keys] = count.get(keys,0)+1
    return count


#starting with main function
if __name__=="__main__": 
    #Asking for user entry
    firstStr = input ("Please enter first string : ")#"Hello World!!"

    secondStr = input ("Please enter second string : ")#"Hello World!!"
    
    print ("=====================================\n")
    result = checkAngrm(firstStr,secondStr)
    #print (result)

    if (result):
        print ("Entered strings are anagrams!!")
    else:
        print ("Entered strings are NOT anagrams!!")

