# import numpy
# #
# # print('hello, world')

import time
import random

count = 0
begin = time.time()
while time.time() - begin < 1:
    a = random.random()
    b = random.random()
    c = a * b
    count += 1

print(count)