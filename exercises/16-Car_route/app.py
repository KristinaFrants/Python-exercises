#Complete the function to print the amount of days it will take to cover a route.
#HINT: You may need to import the math module for this exercise.
# def car_route(n,m):
N=int(700)
M=int(750)
O=M%N
if O != 0:
  p = int((M/N)+1)
  print("Number of days to cover Mkms is:",p)

  
# else:
#   P=int(M/N)
#   print("Number of days to cover Mkms is:",P)


#Invoke the function with two intergers.
