menuDict = {'fried rice':65,'burger':45,'spaghetti':99,'noodle':55,'salad':60}
menuList = []
sum=0
while True:
    menuInput = input("MENU(type exit to finish): ")
    if menuInput.lower() == "exit":
        break
    else:
        menuList.append([menuInput,menuDict[menuInput]])
        for price in range(len(menuList)):
            sum
        sum+=menuList[price][1]

def showBill():
    print('-----Bill-----')
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
    print("--------------")
    print("Total price",sum,"THB")

showBill()
