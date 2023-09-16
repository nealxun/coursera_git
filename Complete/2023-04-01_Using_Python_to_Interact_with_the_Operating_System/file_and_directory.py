# working with directories
import os
os.chdir("2023-04-01_Using_Python_to_Interact_with_the_Operating_System")
print(os.getcwd())
print(os.path.getsize("guests.txt"))
print(os.path.getmtime("guests.txt"))

import datetime
timestamp = os.path.getmtime("guests.txt")
print(datetime.datetime.fromtimestamp(timestamp))