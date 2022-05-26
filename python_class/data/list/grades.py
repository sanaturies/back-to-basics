
# Create a program that keeps track of a list of grades
# The user can add, delete, display, and sort grades
grades=[]
choice=1

while choice!=0:
    print(''' 
        0:Exit
        1:Show grades
        2:Add a grade
        3:Delete a grade
        4:Sort grades
        5:Calculate average
        6:Find duplicates
        7:Delete duplicates
        8:Remove all grades above a specific value
        9:Remove all grades below a specific value
        10: add multiple grades at once
     ''')
    choice=int(input('please a enter a number from the choices above '))
    if choice==0:
        print('Thank you for visiting!')
    elif choice==1:
        print(grades)
    elif choice==2:
        new_grade=input('what grade do you want to add?')
        try:
            new_grade=int(new_grade)
        except:
            print('please enter a valid integer')
        else:
            grades.append(new_grade)
        print('new list of grades:',grades)
    elif choice==3:
        delete_grade=int(input('what grade do you want to delete?'))
        if delete_grade not in grades:
            print('sorry that value does not exist in the list')
        else:
            grades.remove(delete_grade)
            print('new list of grades:',grades)
    elif choice==4:
        sorted_grades=grades.sort()
        print('new list of grades:',grades)
    elif choice==5:
        running_sum=0
        for i in grades:
            running_sum+=i
        average=running_sum/len(grades)
        print('the average grade is:',average)
    elif choice==6:
        duplicates=[]
        for i in grades:
            ammount=grades.count(i)
            if ammount>=2:
                duplicates.append(i)
            #print(set(duplicates),'1')
        print(set(duplicates))
    elif choice==7:
        print(set(grades))
    elif choice==8:
        newgradelist=[]
        value=int(input('what is the specific value?'))
        for i in grades:
            if i<value:
                newgradelist.append(i)
        print('new list of grades:', newgradelist)
    elif choice==9:
        newgradelist=[]
        value=int(input('what is the specific value?'))
        grades.append(value)
        for i in grades:
            if i>value:
                newgradelist.append(i)
        print('new list of grades:', newgradelist)
    elif choice==10:
        values=input('what are the grades? (please enter seperated by commas)')
        values=values.split(',')
        for i in values:
            try:
                i=int(i)
            except:
                print('please enter a valid integer')
            else:
                grades.append(i)
        print(grades)
    else:
        print('sorry that is not a valid choice (enter 0 to exit)')
        

