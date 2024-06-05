                                                    # Question no 01
# num_cities = int(input("Enter the number of cities: "))
    
#     # Open a file in write mode to store city data
# with open("city_data.txt", "w") as file:
#         # Loop through each city to collect and store data
#         for _ in range(num_cities):
#             city_name = input("Enter city name: ")
#             population = input("Enter population: ")
#             mayor_name = input("Enter mayor's name: ")
            
#             # Write city data to the file
#             file.write(f"City = {city_name},Population = {population},Mayor = {mayor_name}\n")

    
# print("City data has been successfully saved to 'city_data.txt'.")
 
  
                                                      # Question no 02
message = "Now we are AI students\n"
    
    # Open the file in append mode ('a' mode)
with open("student.txt", "a") as file:
        # Append the message to the file
        file.write(message)
       
    
print("Message appended to 'student.txt'.")
