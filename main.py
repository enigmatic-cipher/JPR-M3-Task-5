"""
Given an array of integers as input, create a new array which contains the sum of elements appearing next to each other in the original array. Note that the size of the new array will be 1 less than that of the input array.
Input-> [1,2,3,4,5,6]
Output-> [3,5,7,9,11]
"""

ls = [1,2,3,4,5,6]
ln = len(ls)
nw_ls = []
el = 0
index = 0
for i in range(0,ln-1):
  e = ls[i]
  el = ls[i]+ls[i+1]
  nw_ls.append(el)
  index = index + 1
print(nw_ls)
