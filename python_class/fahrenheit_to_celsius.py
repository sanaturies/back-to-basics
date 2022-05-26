
#convert fahrenheit to celsius

flag=True
acceptable=['0','1','2','3','4','5','6','7','8','9','.']
while flag==True:
    fdegrees=(input("fahrenheit:"))
    for i in fdegrees:
        if i in acceptable:
            fdegrees = float(fdegrees)
            print((fdegrees-32)*(5/9))
            flag=False
            break
        else:
            print("please enter a numeric value")
            flag=True
            break