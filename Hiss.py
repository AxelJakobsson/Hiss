import pyinputplus as pyip # pip install pyinputplus
import time
import random

totalFloors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
currentFloor = 0
pickUpFloor = []
targetFloors = []
sleepTimer = 1

time.sleep(sleepTimer)
print(totalFloors)
time.sleep(sleepTimer) # Pause for 1 second
print(f"Currently on floor: {currentFloor}")


targetFloors.append(pyip.inputInt(prompt="Which floor do you want to go to? ", min=1, max=10)) # Input which floor you want to go to, only ints between 1-10


if (targetFloors[0] > currentFloor): # Select your direction
    direction = 'UP'
else:
    direction = 'DOWN'

print(f"Elevator is currently on floor: {currentFloor}") 
print(f"The elevator is going to {targetFloors[0]}")
time.sleep(sleepTimer) # Pause for 1 second



while True: # Someone getting on the elevator
    onFloor = random.randint(1,10) # Generate a random number for the npc to be at
    
    totalFloorsCopy = totalFloors # Make sure they don't choose to go to the same floor that they are already on
    totalFloorsCopy.remove(onFloor) # ^
    
    goToFloor = random.choice(totalFloorsCopy) # Choose a floor to go to
    
    
    
    if (goToFloor > onFloor): # Select the directions
        newDirection = 'UP'
    else: 
        newDirection = 'DOWN'
        
    print(f"A person on floor {onFloor} wants to go to floor {goToFloor}. Their direction = {newDirection}, your direction = {direction}")
    break
time.sleep(sleepTimer) # Pause for 1 second
    
if (onFloor >= currentFloor and newDirection == direction):
    pickUpFloor.append(onFloor)
    targetFloors.append(goToFloor)
    
while targetFloors or pickUpFloor:
    
    if direction == 'UP':
        currentFloor += 1
    else:
        currentFloor -= 1
        
    if currentFloor in targetFloors:
        time.sleep(sleepTimer) # Pause for 1 second
        print(f"Elevator reached floor {currentFloor}. Staying to let passengers ut.")
        targetFloors.remove(currentFloor)

    if currentFloor in pickUpFloor:
        time.sleep(sleepTimer) # Pause for 1 second
        print(f"Elevator reached floor {currentFloor}. Staying to let passengers in.")
        pickUpFloor.remove(currentFloor)
        
    else:
        time.sleep(sleepTimer) # Pause for 1 second
        print(f"The elevator is currently on floor {currentFloor}")


time.sleep(sleepTimer) # Pause for 1 second
# print("All passengers have reached their destinations.")

# if (onFloor <= currentFloor and newDirection != direction):
#     direction = 'DOWN'
#     pickUpFloor.append(onFloor)
#     targetFloors.append(goToFloor)
#     while targetFloors or pickUpFloor:
#         if currentFloor in targetFloors:
#             time.sleep(sleepTimer) # Pause for 1 second
#             print(f"Elevator reached floor {currentFloor}. Staying to let passengers out.")
#             targetFloors.remove(currentFloor)

#         elif currentFloor in pickUpFloor:
#             time.sleep(sleepTimer) # Pause for 1 second
#             print(f"Elevator reached floor {currentFloor}. Staying to let passengers in.")
#             pickUpFloor.remove(currentFloor)
#         else:
#             time.sleep(sleepTimer) # Pause for 1 second
#             print(f"The elevator is currently on floor {currentFloor}")

#         if direction == 'UP':
#             currentFloor += 1
#         else:
#             currentFloor -= 1
#     time.sleep(sleepTimer) # Pause for 1 second
#     print("All passengers have reached their destinations.")
# # Programmet slutar ifall npcn vill neråt istället för upp