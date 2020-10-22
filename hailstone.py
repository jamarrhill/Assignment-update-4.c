# Name: Jamar Hill
# Date: 10/21/20
# Description: Assignment 4.c

def hailstone(n): #Define the function
    """This function returns the amount of steps it takes for a Hailstone sequence to process a value to 1"""
    steps = 0 #Estiblish counter
    while n != 1: #Start loop with a number not equal to 1
        if n % 2 == 0: #Idendify if the number is even
            n = n // 2 #If so divide by 2
            steps += 1 #Count an addtional step in the loop
        else: #Else the number is odd by defalt
            n = n * 3 + 1 #Multipy by 3 and add 1
            steps += 1 #Count an addtional step in the loop
    return steps

answer = (hailstone(1000))
print(answer)
