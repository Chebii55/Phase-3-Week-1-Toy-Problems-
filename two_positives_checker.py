
def num_checker():
    #input of the 3 values
    value_1=int(input("Enter the first value:"))
    value_2=int(input("Enter the second value:"))
    value_3=int(input("Enter the third value:"))
    #numbers input to a list
    num_list=[value_1,value_2,value_3]
    #sum of positive values
    total_greater_than_one = sum(1 for num in num_list if num > 1)
    #return of if True or False depending on the Input values
    if total_greater_than_one == 2:
        print(True)
    else:
        print(False)
     
    
num_checker()   






# if (value_1>1) and (value_2>1) and (value_3<1):
    #     print (True)
    # elif (value_1>1) and (value_2<1) and (value_3>1):
    #     print (True)
    # elif (value_1<1) and (value_2>1) and (value_3>1):
    #     print (True)
    # else:
    #     print (False)