def DeleteCustomer(name):
    i = 0
    for i in range(len(CStack)):
        if name == CStack[i]:
            CStack.pop(i)
        else:
            pass
name = input("Enter the name of customer")
DeleteCustomer(name)
print("Customer removed from list")
