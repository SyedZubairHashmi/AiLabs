print("Qno:01 a Python program to square and cube every number in a given list of integers using Lambda.")


print("square  a number by lambda")
number = [2,4,5,3,1]
square_numbers=list(map(lambda x:x*x ,number))
print(square_numbers)
print("cube  a number by lambda")
cube_numbers = list(map(lambda x:(x*x)*x , number))
print(cube_numbers)


print("Qno:02 a Python program to find if a given string starts with a given character using Lambda.")
character = input("Enter a charecter")

statrt_with = lambda x: True if x.startswith(character) else False 
print(statrt_with("zubair"))


