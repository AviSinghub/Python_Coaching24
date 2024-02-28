def simple_interest(p,r,n):
    return p*r*n/100

def examine():
    prin_amt = float(input("Enter the principal amount: "))
    r= float(input("Enter the rate of interest: "))
    n= int(input("Enter the number of years: "))
    
    si = simple_interest(prin_amt,r ,n)
    print("The Simple Interset is: ", si)
examine()