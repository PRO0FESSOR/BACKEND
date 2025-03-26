
# python list 

    # a simple list   
    list1 = [1, 2, "Python", "Program", 15.9]      
    list2 = ["Amy", "Ryan", "Henry", "Emma"]   
      
    # printing the list  
    print(list1)  
    print(list2)  
      
    # printing the type of list  
    print(type(list1))  
    print(type(list2))

# sub list 

    list = [1,2,3,4,5,6,7]    
    print(list[0])    
    print(list[1])    
    print(list[2])    
    print(list[3])    
    # Slicing the elements    
    print(list[0:6])    
    # By default, the index value is 0 so its starts from the 0th element and go for index -1.    
    print(list[:])    
    print(list[2:5])    
    print(list[1:6:2])

# updating list values  
    list = [1, 2, 3, 4, 5, 6]       
    print(list)       
    # It will assign value to the value to the second index     
    list[2] = 10     
    print(list)      
    # Adding multiple-element     
    list[1:3] = [89, 78]       
    print(list)     
    # It will add value at the end of the list    
    list[-1] = 25    
    print(list)
