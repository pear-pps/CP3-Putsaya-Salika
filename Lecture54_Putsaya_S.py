def login(): #first page show username and password for user to enter
    username = input("username: ")
    password = input("password: ")
    if username == "admin" and password == "admin": #user enter correct both username and password can get into menu
        return menu()
    else:
        return print("try again!") #if not correct need to try again

def menu(): #show menu for user to choose
    print("Welcome! Choose one")
    print("1. vat calculater")
    print("2. price calculator")
    return choose()

def choose(): #user choose menu1 or menu2 and will lead to each different page
    userSelected = int(input(">> "))

    if userSelected == 1: #user pick 1 from menu will lead to vat calculator page
        return vatCalculate(totalPrice = int(input("Cost of goods: ")))

    elif userSelected == 2: #user pick 2 from menu will lead to price calculator page
        return priceCalculate()

def vatCalculate(totalPrice): #only calculate vat if user choose 1 in menu previous page
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return print("Price Included Vat:",result,"THB")

def priceCalculate(): #calculate both price and vat if user choose 2 in menu previous page
    firstPiece = int(input("1stCost: "))
    secondPiece = int(input("2ndCost: "))
    totalPrice = firstPiece + secondPiece
    return vatCalculate(totalPrice)

login()
