#Suraya Malek
#CIS 261
#Date: November 11th, 2023
#Subject: Invoice Line Item Calculator

def get_price():
    while True:
        try:
            PRICE = float(input("Enter a price: "))
            return PRICE
        except ValueError:
            print("Invalid decimal number. Please try again.")
            
def get_quantity():
    while True:
        try:
            QUANTITY = int(input("Enter quantity: "))
            return QUANTITY
        except ValueError:
            print("invalid integer. Please try again: ")
            
if __name__ == "__main__":
    print("The Invoice Line Item Calculator")
    answer = "y"
    while answer.lower() == "y" :
          PRICE =get_price()
          QUANTITY = get_quantity()
          
          total = PRICE * QUANTITY
          
          print()
          print("Price: ", f"{PRICE: .2f}")
          print("Quantity: ", QUANTITY)
          print("Total: ",f"{total: .2f}")
          answer = input ("Enter another line item? (y/n): ")
          print()
          
    print("Bye!")
        
