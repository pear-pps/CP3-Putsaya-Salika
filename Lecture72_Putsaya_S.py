menuList = []

while True:
    menuInput = input("menu: ")
    if menuInput.lower() == "exit":
        break
    else:
        priceInput = input("price: ")
        menuList.append([menuInput,priceInput])
        for price in menuList:
            sum = 0
        sum+=int(price[1])

def showBill():
    print('-----Bill-----')
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
    print("--------------")
    print("Total",sum,"THB")

showBill()