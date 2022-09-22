#!/usr/bin/python3
from sys import argv
res = 0
count = 0
for arg in argv:
    if len(argv) == 0:
        pass
    elif len(argv) > 0 and count > 0:
        res += int(arg)
    count += 1
print(res)

#res = 0
#nums = [1]
#for i in nums:
#    if len(nums) == 1:
 #       break
  #  else:
   #     res += i
#print(res)
