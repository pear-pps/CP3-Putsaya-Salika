costInput = int(input("Cost of goods: ")) # user enter cost of product
def vatCalculator(costInput):
    return costInput+(costInput*7/100)
print("Include VAT: ",vatCalculator(costInput),"THB")