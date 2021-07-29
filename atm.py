#Code Chef Problem Code HS08TEST



#Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a
#multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank
#charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an
#attempted transaction.

print("Let's start the atm program")
print("Hello")
go = False
withdraw = iinput()

current = int(input(range(0, 2000)))

if withdraw % 5 == 0:
    go = True

if go == True:
    if withdraw < current:
        print("Withdrawing ' ' money for you")
        remaining = current - (withdraw + 0.50)
        print("Remaining balance is ' ' ")
        print(remaining)
    else:
        print("The amount entered is greater than the saving balance")
else:
    print("Please enter the sum in multiple of 5")

