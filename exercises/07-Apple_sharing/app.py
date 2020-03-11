#Complete the function to print:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: Import the math module 

N=int(input("enter the number of students:")) #6
K=int(input("enter the number of Apples:")) #50
z=K/N # This will gives the apples per each student
y=K%N # This will gives the apples remains in the basket.
print(z)
print(y)
 
    

#Print the two answer per the example output.
# apple_sharing(6,50)