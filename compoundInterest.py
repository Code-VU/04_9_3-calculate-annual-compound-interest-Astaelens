def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
 n=0
 while n <3:
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
    
    amount=client_one_principal*(1+client_one_rate/100)**client_one_time
    intrest=amount-client_one_principal
    intrest_100=intrest*100
    intrest=round(intrest_100)/100
    print("Compound Interest: "+str(intrest))
    n=n+1
    if n<3:
        print("---")

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
