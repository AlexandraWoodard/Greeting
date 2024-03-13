# Alexandra Woodard
# March 2024 - Task 23

print("Hello World")

print("Git is awesome!")

# Ask the user for his/her/their name 

name = input("Enter your first and last name ")

print(f'Hello {name}! Welcome to the program! Thank you for your time.')

# Ask about the weather 

weather = input("How is the weather today? [Sunny/Cloudy/Rainy/Snowy/Other] ")

# Put the input into lower case and remove whitespace / beginning or trailing characters

weather = weather.lower().strip()

# Create comments for the weather options 
# Address error handling for user input

while True: 
    if weather == "sunny":
        print("Sunny days are great for picnics!")
        break
    elif weather == "cloudy":
        print("At least you won't get a sunburn today.")
        break
    elif weather == "rainy":
        print("Rainy days are great for reading and watching movies.")
        break
    elif weather == "snowy":
        print("I hope you can stay home from work or school today!")
        break
    elif weather == "other":
        print("Ok! That's unusual.")
        break
    else:
        print("Your input does not match the available options [Sunny/Cloudy/Rainy/Snowy]")
        print(" ")
        weather = input("How is the weather today? [Sunny/Cloudy/Rainy/Snowy] ")
        weather = weather.lower().strip()

print("Thank you for telling me about the weather today.")