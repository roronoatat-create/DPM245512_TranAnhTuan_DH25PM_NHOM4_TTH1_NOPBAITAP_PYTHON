#Câu 10: Vẽ hình dùng Sleep
from time import sleep
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

shape1 = """
      *
    * * *
  * * * * *
    * * *
      *
"""

shape2 = """
        * *
      *
    * *
      * *
    * *
"""

shape3 = """
      * * *
      *
      * * *
      *
      *
    * * *
"""

shape4 = """
        * *
      *
        * *
      *
        *
      *
    * *
"""

clear_screen()
print(shape1)
sleep(5)

clear_screen()
print(shape2)
sleep(5)

clear_screen()
print(shape3)
sleep(5)

clear_screen()
print(shape4)