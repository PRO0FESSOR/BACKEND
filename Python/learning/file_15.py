
# tuples

# Python program to show how to create a tuple      
# Creating an empty tuple      
emptyTuple = ()      
print("Empty tuple: ", emptyTuple)      
      
# Creating a tuple having integers      
integerTuple = (3, 6, 7, 10, 16, 23)  
print("Tuple with integers: ", integerTuple)      
      
# Creating a tuple having objects of different data types  
mixedTuple = (6, "Javatpoint", 14.3)      
print("Tuple with different data types: ", mixedTuple)      
      
# Creating a nested tuple      
nestedTuple = ("Javatpoint", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))      
print("A nested tuple: ", nestedTuple)         



 # Python program to show how negative indexing works in Python tuples  
      
# Creating a tuple  
sampleTuple = ("Apple", "Mango", "Banana", "Orange", "Guava", "Berries")  
      
# Printing elements using negative indices  
print("Element at -1 index: ", sampleTuple[-1])  
print("Element at -2 index: ", sampleTuple[-2])  
print("Element at -3 index: ", sampleTuple[-3])  
print("Element at -4 index: ", sampleTuple[-4])  
print("Element at -5 index: ", sampleTuple[-5])  
print("Element at -6 index: ", sampleTuple[-6])  
    
# Printing the range of elements using negative indices  
print("Elements between -6 and -1 are: ", sampleTuple[-6:-1])  

# Python program to show how to access tuple elements      
  
# Creating a tuple having six elements  
sampleTuple = ("Apple", "Mango", "Banana", "Orange", "Guava", "Berries")   
  
# accessing the elements of a tuple using indexing  
print("First Element of the Given Tuple:", sampleTuple[0])  
print("Second Element of the Given Tuple:", sampleTuple[1])  
print("Third Element of the Given Tuple:", sampleTuple[2])  
print("Forth Element of the Given Tuple:", sampleTuple[3])  
print("Fifth Element of the Given Tuple:", sampleTuple[4])  
print("Sixth Element of the Given Tuple:", sampleTuple[5])  


    # Python program to show how slicing works in Python tuples  
      
    # Creating a tuple  
    sampleTuple = ("Apple", "Mango", "Banana", "Orange", "Guava", "Berries")  
      
    # Using slicing to access elements of the tuple  
    print("Elements between indices 1 and 5: ", sampleTuple[1:5])  
      
    # Using negative indexing in slicing  
    print("Elements between indices 0 and -3: ", sampleTuple[:-3])  
      
    # Printing the entire tuple by using the default start and end values  
    print("Entire tuple: ", sampleTuple[:])      


    # Python program to show how to delete elements of a Python tuple  
      
    # Creating a tuple  
    sampleTuple = ("Apple", "Mango", "Banana", "Orange", "Guava", "Berries")  
    # printing the entire tuple for reference  
    print("Given Tuple:", sampleTuple)  
      
    # Deleting a particular element of the tuple using the del keyword  
    try:  
        del sampleTuple[3]  
        print(sampleTuple)  
    except Exception as e:  
        print(e)  
      
    # Deleting the variable from the global space of the program using the del keyword  
    del sampleTuple  
      
    # Trying accessing the tuple after deleting it  
    try:  
        print(sampleTuple)  
    except Exception as e:  
        print(e)  

        

# Python program to demonstrate an approach of unpacking a tuple  
  
# creating a tuple (Packing a Tuple)  
fruits_tuple = ("mango", "orange", "banana", "apple", "papaya")  
  
# printing the given tuple for reference  
print("Given Tuple :", fruits_tuple)  
  
# unpacking a tuple  
(varOne, varTwo, varThree, varFour, varFive) = fruits_tuple  
  
# printing the results  
print("First Variable :", varOne)  
print("Second Variable :", varTwo)  
print("Third Variable :", varThree)  
print("Fourth Variable :", varFour)  
print("Fifth Variable :", varFive)  

    # Python program to demonstrate an approach of unpacking a tuple  
      
    # creating a tuple (Packing a Tuple)  
    fruits_tuple = ("mango", "orange", "banana", "apple", "papaya")  
      
    # printing the given tuple for reference  
    print("Given Tuple :", fruits_tuple)  
      
    # unpacking a tuple  
    # here, we are using * to store the remaining elements of the tuple in a list  
    (varOne, varTwo, *varThree) = fruits_tuple  
      
    # printing the results  
    print("First Variable :", varOne)  
    print("Second Variable :", varTwo)  
    print("Third Variable :", varThree)



