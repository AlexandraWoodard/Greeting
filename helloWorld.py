# Alexandra Woodard
# March 2024 - Task 23

print("Hello World")

print("Git is awesome!")

# Ask the user for his/her/their name 

name = input("Enter your first and last name ")

print(f'Hello {name}! Welcome to the program! Thank you for your time.')

# Ask the user's preferred name

nickname = input("Do you have a different name that you would like me to use? (Y/N) ")

nickname = nickname.lower().strip()

while True: 
    if nickname == "y":
        updated_name = input("What name would you like me to use? ")
        break
    elif nickname == "n":
        print("Ok, I will use your full name.")
        break
    else:
        print("You have not chosen between the options Y or N")
        print(" ")
        nickname = input("Do you have a different name that you would like me to use? (Y/N)")
        nickname = nickname.lower().strip()
    
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

if nickname == "y":
    print(f'Thank you for telling me about the weather today, {updated_name}.')
else:
    print(f'Thank you for telling me about the weather today, {name}.')

