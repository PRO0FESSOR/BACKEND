
#loop 

    # Code to find the sum of squares of each element of the list using for loop  
      
    # creating the list of numbers  
    numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]  
      
    # initializing a variable that will store the sum  
    sum_ = 0  
      
    # using for loop to iterate over the list  
    for num in numbers:  
         
    sum_ = sum_ + num ** 2   
      
    print("The sum of squares is: ", sum_)


# range function

my_list = [3, 5, 6, 8, 4]  
for iter_var in range( len( my_list ) ):  
    my_list.append(my_list[iter_var] + 2)  

print( my_list )
