import random
import math

#A basic plinko simulator based on probabilities for every chamber
"""
The chamber will selected based on rng.
As an example, if we are working with 4 chambers, a dropped coin has 8 different possible paths to follow
First and last chambers are only reachable by 1 path, second and third chambers are reachable by 3 paths each.
So a random selected number will decide if the coin dropped in a chamber by checking the range for that chamber 
which is decided by numbers of possible paths to that chamber.
For the example with 4 chambers:
Chamber 1 => 1
Chamber 2=> 2,3,4
Chamber 3 => 5,6,7
Chamber 4 => 8
If we get 5 as a random selected number, the value of 3rd element in the list chambers will be increased by 1.

Created by Yusuf Kagan Kizilarslan

"""

def main():
    global chambers
    global cols
    cols = int(input("Number of chambers: "))
    chambers = []
    for i in range(1,cols+1):
        chambers.append(0)
    while True:
        coin_num = 0
        action = input("Enter the number of coins you want to test. Type exit to exit. Type r to reset chambers: ")
        if action == "exit":
            break
        elif action == "r":
            main()
        else:
            coin_num = int(action)
        for i in range(1,coin_num+1):
            drop_coin()
        print(chambers)
def range_check(random_number):
    #Checks the range for randomly selected number
    #The range for current chamber will be calculated by function nextrow
    #If the number is smaller or equal to the range the coin is dropped to the current chamber
    cchamber = 0
    range = 0
    while True:
        range += nextrow(cchamber)
        if random_number <= range:
            return cchamber
        else:
            cchamber += 1
def nextrow(ccol):
    #Calculates the range for given chamber
    x = int((math.factorial(cols-1))/((math.factorial((cols-ccol-1)))*math.factorial(ccol)))
    return x
def drop_coin():
    current_number = random.randint(1,2**(cols-1)+1)
    chamber = range_check(current_number)
    #print(current_number, chamber) #For printing out the random number and its chamber for every roll
    chambers[chamber] += 1

main()

