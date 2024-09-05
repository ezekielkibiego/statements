def compound_interest(principal, rate, time):
    
    total_amount = principal * (1 + rate/100) ** time
    interest = total_amount - principal
    return interest

interest = compound_interest(int(input("Enter Principal: ")), int(input("Enter the rate: ")), int(input("Enter the time: ")))
print(f"Compound interest: {interest}")