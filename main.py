#  As a developer, I want to make at least three commits with descriptive messages.

#  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.

#  As a user, I want a destination to be randomly selected for my day trip.

#  As a user, I want a restaurant to be randomly selected for my day trip.

#  As a user, I want a mode of transportation to be randomly selected for my day trip.

#  As a user, I want a form of entertainment to be randomly selected for my day trip.

#  As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

#  As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

#  As a user, I want to display my completed trip in the console.

#  As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


destinations = ["Paris", "London", "Bali", "Rome", "Dubai"]
resturants = ["Pizza", "Chinese", "Mexican", "Native", "Italian"]
trasnportation = ["Car", "Boat", "Train", "Walking"]
entertainment = ["Skydiving", "Movies", "Swimming", "Sightseeing"]
import random



def greeting():
    print("Hello and welcome to the Ramon Day Trip Generator. Today we will choose a trip and everything that entails to your trip ")


greeting()


condition = True

while condition is True:
    random_destination = random.choice(destinations)
    user_input = input(f"Hello we have selected the destination {random_destination} for you. Is this okay. Y/N ?  ")
    if user_input == "N":
        print("Im sorry, we will select another destination for you!! ")
    elif user_input == "Y":
        print("I am glad we could provide a great destination for you")
        break 


while condition is True:
    random_resturants = random.choice(resturants)
    user_input = input(f"We have also selected {random_resturants} for you to eat. Will this fill your belly. Y/N ? ")
    if user_input == "N":
        print("Aw man im sorry to hear that, we will select a better option for you! ")
    elif user_input =="Y":
        print("I knew you would love that option. ")
        break


while condition is True:
    random_transportaion = random.choice(trasnportation)
    user_input = input(f'{random_transportaion} is the form of transportation we have selected for your trip. Is this okay. Y/N ? ')
    if user_input == "N":
        print("Don't worry we got you covered, We will find a better choice of transportation for you!!! ")
    elif user_input == "Y":
        print("That is an amazing choice. ")
        break


while condition is True:
    random_entertainment = random.choice(entertainment)
    user_input = input(f'{random_entertainment} is the form of entertainment you will have on this trip. Do you agree Y/N ? ')
    if user_input == "N":
        print("That's okay. We have plenty of other options to choose from")
    elif user_input == "Y":
        print("You will truly enjoy this activity. ")
        break

while condition is True:
    user_input = input(f"Your trip entails {random_destination} as your destination, {random_resturants} is the choice food you will eating, {random_transportaion} is the form of transportaion you will be using, and {random_entertainment} will be your entertaiment for the trip. Is this okay. Y/N ?  ")
    if user_input == "N":
        print("We will find a better trip for you!!!!!! ")
        break
    elif user_input == "Y":
        print("Thank you for choosing Ramon Inc for your trip details. We hope you have a wonderful trip and stay safe!!!!!!!!!!!!")
        break



# Add a change for commit/push testing

