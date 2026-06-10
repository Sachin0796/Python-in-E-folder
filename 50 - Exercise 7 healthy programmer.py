#Healthy programmer
# Taking care of programmer so that he/she drinks water, look for their eyes and do some physical activity

import pygame
from datetime import datetime,timedelta

water_loop=False
eyes_loop=False
exercise_loop=False

now = datetime.now()
current_time=datetime.now()
water_time=current_time+timedelta(hours=1) # making user drink 500ml in 1 hour interval and excluding 2pm for lunch.
eyes_time = current_time+timedelta(minutes=30)
exercise_time=current_time+timedelta(minutes=45)

def water_function():
    pygame.mixer.init()
    pygame.mixer.music.load("kabhi_kabhi.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        water_input = input("Please drink two glasses of water(500ml). Enter 'Drank' once done:\n")
        while (True):
            if water_input.lower() == "drank":
                pygame.mixer.music.stop()
                # water_loop = True
                # break
                return
            else:
                water_input = input("Please enter 'Drank' to continue:\n")
        # if water_loop == True:
        #     water_loop == False
        #     break

def eyes_function():
    pygame.mixer.init()
    pygame.mixer.music.load("tu_hi_hai.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        eyes_input = input("Please take a break. Enter 'EyDone' once done:\n")
        while (True):
            if eyes_input.lower() == "eydone":
                pygame.mixer.music.stop()
                # eyes_loop = True
                return
            else:
                eyes_input = input("Please enter 'EyDone' to continue:\n")
        # if eyes_loop == True:
        #     eyes_loop == False
        #     break

def exercise_function():
    pygame.mixer.init()
    pygame.mixer.music.load("tarefoon_se.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        exercise_input = input("Please do some exercise. Enter 'ExDone' once done:\n")
        while (True):
            if exercise_input.lower() == "exdone":
                pygame.mixer.music.stop()
                # exercise_loop = True
                # break
                return
            else:
                exercise_input = input("Please enter 'ExDone' to continue:\n")
        # if exercise_loop == True:
        #     exercise_loop == False
        #     break


while(True):

    # Water, eyes and exercise:
    if (datetime.now().time().strftime('%H:%M')==water_time.time().strftime('%H:%M') and current_time.time().strftime('%H:%M')!='14:00') and \
            (water_time.time().strftime('%H:%M') == exercise_time.time().strftime('%H:%M')) and  \
            (water_time.time().strftime('%H:%M') == eyes_time.time().strftime('%H:%M')):
        print("Get ready to do all all activities")

        print("water time:", water_time)
        water_time = water_time + timedelta(hours=1)
        water_function()

        print("Eyes time:", eyes_time)
        eyes_time = eyes_time + timedelta(minutes=30)
        eyes_function()

        print("exercise_time:", exercise_time)
        exercise_time = exercise_time + timedelta(minutes=45)
        exercise_function()

    # water and exercise:
    elif (datetime.now().time().strftime('%H:%M')==water_time.time().strftime('%H:%M') and current_time.time().strftime('%H:%M')!='14:00') and \
            (water_time.time().strftime('%H:%M') == exercise_time.time().strftime('%H:%M')):
        print('Its time for drinking water and doing some exercise !!!')

        print("water time:", water_time)
        water_time = water_time + timedelta(hours=1)
        water_function()

        print("exercise_time:", exercise_time)
        exercise_time = exercise_time + timedelta(minutes=45)
        exercise_function()

    # water and eyes:
    elif (datetime.now().time().strftime('%H:%M') == water_time.time().strftime('%H:%M') and current_time.time().strftime('%H:%M') != '14:00') and \
            (water_time.time().strftime('%H:%M') == eyes_time.time().strftime('%H:%M')):
        print('Its time for drinking water and taking a break !!!')

        print("water time:", water_time)
        water_time = water_time + timedelta(hours=1)
        water_function()

        print("Eyes time:", eyes_time)
        eyes_time = eyes_time + timedelta(minutes=30)
        eyes_function()

    # exercise and eyes
    elif (datetime.now().time().strftime('%H:%M')==exercise_time.time().strftime('%H:%M')) and \
            (exercise_time.time().strftime('%H:%M') == eyes_time.time().strftime('%H:%M')):
        print('Its time for doing some exercise and taking a break !!!')

        print("exercise_time:", exercise_time)
        exercise_time = exercise_time + timedelta(minutes=45)
        exercise_function()

        print("Eyes time:", eyes_time)
        eyes_time = eyes_time + timedelta(minutes=30)
        eyes_function()

    # Only water
    elif datetime.now().time().strftime('%H:%M')==water_time.time().strftime('%H:%M') and current_time.time().strftime('%H:%M')!='14:00':
        print("water time:", water_time)
        water_time = water_time + timedelta(hours=1)
        water_function()

    # Only eyes
    elif datetime.now().time().strftime('%H:%M')==eyes_time.time().strftime('%H:%M'):
        print("Eyes time:", eyes_time)
        eyes_time = eyes_time + timedelta(minutes=30)
        eyes_function()

    # Only exercise
    elif datetime.now().time().strftime('%H:%M')==exercise_time.time().strftime('%H:%M'):
        print("exercise_time:", exercise_time)
        exercise_time = exercise_time + timedelta(minutes=45)
        exercise_function()

    # End of the day
    elif (datetime.now().time().strftime('%H:%M')>='18:00'):
        print("Its great to see that you took care of your health along with wealth. See you tomorrow. !!")
        exit(0)
    else:
        continue
