####Trying out new program to calculate the tax to be paid####

def validateEntry(resp):
    while True:
        try:
            numValue=float(input(resp))
           # print(numValue);
        except ValueError:
            print("Please enter valid amount")
            continue
        if (numValue<0):
            print("Please enter the amount greater than zero")
            continue
        else:
            #return numValue
            break

    return numValue        
            

####Starting with main function####
if __name__ == "__main__":

    print("--------------------------------------------------")
    print("\tLet's see how much tax you are paying")
    print("--------------------------------------------------")

    salary = validateEntry("Please enter your salary in Indian rupees - ")
    sav_80c = validateEntry("Please enter the amount invested in Section 80C - ")
    sav_80d = validateEntry("Please enter the amount invested in Section 80D - ")
