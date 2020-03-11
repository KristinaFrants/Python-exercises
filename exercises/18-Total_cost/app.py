#Complete the function to print the total cost in dollars and cents of N cupcakes. 
# def total_cost(d,c,n):

#     sum1=((d*100)+c)
#     sum2=(sum1*n)
#     dollar2=(sum2//100)
#     cent2=(sum2%100)
#     print("%i %i" % (dollar2,cent2))

N = int(10)
A = int(15)
B = int(2)
Total_cost_dollar= (N*A)
Total_cost_cents= (N*B)
print(Total_cost_dollar,Total_cost_cents)


#way nb 2
# totalcents= (100*N+A)*B
# print(str(totalcents//100)+ " " + str(totalcents%100))


