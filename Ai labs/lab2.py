# print("Qno:01 Make a program that lists the countries in the set")

clist = ['Canada','USA','Mexico','Australia']
# cset = {'Canada','USA','Mexico','Australia'}
for i in range(len(clist)):
    print(clist[i])

# print("Qno:02 reate a loop that counts from 0 to 100 ")
# for i in range(0,100):
#     print(i)

# tableInput= int(input("Enter a number to print a table of "))
# for i in range(1,11):
#     result = tableInput * i
#     print(tableInput, "X", i ,"=",result)


# print("Qno:03 Output the numbers 1 to 10 backwards using a loop")
# for i in range(10,0,-1):
#     print(i)


# print("Qno:04 Create a loop that counts all even numbers to 10")
# for i in range(2,10,2):
#     print(i)
    
print("Qno:05 Create a loop that sums the numbers from 100 to 200")
sum=0
for i in range(100,201):
    sum+=i

print("Sum of all num from 100 to 200",sum)  

print("Qno:03 Make a program that lists the countries in the set below using a while loop.")
    
clist2 = ["Canada","USA","Mexico"]
index=0
while index<len(clist2):
    print(clist2[index])
    index+=1