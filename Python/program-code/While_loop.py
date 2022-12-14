# -*- coding: utf-8 -*-
"""Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kgmxMppOf6Fdnsk0tgO0yIENtdDQntM4

# While loop
"""

x = 1
while x < 4:
  print(x)
  x += 1

"""### Let us understand what is happening in the above program.
-Value of x is assigned as 1
-The while loop starts with the condition that x must be less than 4
-The subsequent two statements have the same indentation and will be considered a part of the while loop
-The value of x is printed. Initially, x=1
-The value of x is then increased by 1. So now, x=2
-Control goes back to the condition line; x is less than 4 (2<4). This means that the following statements will be executed again
This continues until x is assigned a value of 4. Then, the condition fails as x is not less than 4
-The next two statements will not be executed, and the while loop will end.
"""