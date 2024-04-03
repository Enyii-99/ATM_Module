from cardHolder import cardHolder

def print_menu():
    print("Please choose from the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")


def deposit(cardHolder):
    try:
      deposit = float(input("How much $$ would you like to deposit: "))
      cardHolder.set_balance(cardHolder.get_balance() + deposit)
      print("Thank you for your deposit. Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid Input")   

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw: "))
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient Funds.")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("Thank you for banking with us!")    
    except:
        print("Invalid Input.")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("", "", "", "", "")
    ### Created user repo
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("12097648795432108", 3069, "Jane", "Ochokwu", 2654000.75)) 
    list_of_cardHolders.append(cardHolder("28765490987878765", 1279, "Mark", "Nonso", 657200.5)) 
    list_of_cardHolders.append(cardHolder("87978766906453234", 2225, "Obiora", "Ochokwu", 89706580000.00)) 
    list_of_cardHolders.append(cardHolder("90876542321127865", 6969, "Enyichukwu", "Ochokwu", 980769000.95)) 
    list_of_cardHolders.append(cardHolder("77876549980654674", 8903, "Segun", "Imah", 92249850000.78)) 

    debitCardNum = ""
    while True:
        try:
           debitCardNum = input("Please insert your debit card: ")
           ### Check against repo
           debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
           if(len(debitMatch) > 0):
               current_user = debitMatch[0]
               break
           else:
               print("card number not recognized, please try again.")
        except:
            print("card number not recognized, please try again.")   

while True:
    try:
        userPin = int(input("Please enter your pin: ").strip())
        if(current_user.get_pin() == userPin):
            break
        else:
            print("Invalid PIN, please try again.")
    except:
        print("Invalid PIN, please try again.")    

print("Welcome ", current_user.get_firstName()) 
option = 0
while (True):  
    print_menu()           
    try:
        option = int(input())
    except:
        print("Invalid input, please try again.")

    if(option == 1):
        deposit(current_user)
    elif(option == 2):
        withdraw(current_user)
    elif(option == 3):
        check_balance(current_user)
    elif(option == 4):
        break
    else:
        option == 0            

print("Thank you for banking with us.\n Have a nice day.")                  