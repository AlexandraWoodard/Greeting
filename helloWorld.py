# Alexandra Woodard
# March 2024 - Task 23

print("Hello World")

print("Git is awesome!")

# Ask the user for his/her/their name 

name = input("Enter your name ")

print(f'Hello {name}! Welcome to the program!')

# Ask about the weather 

weather = input("How is the weather today? [Sunny/Cloudy/Rainy/Snowy] ")

# Put the input into lower case and remove whitespace / beginning or trailing characters

weather = weather.lower().strip()

# Create comments for the weather options 

if weather == "sunny":
    print("Sunny days are great for picnics!")
elif weather == "cloudy":
    print("At least you won't get a sunburn today.")
elif weather == "rainy":
    print("Rainy days are great for reading and watching movies.")
elif weather == "snowy":
    print("I hope you can stay home from work or school today!")
else:
    print("Your input does not match the available options [Sunny/Cloudy/Rainy/Snowy]")

print("Thank you for telling me about the weather today.")