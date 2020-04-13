#Create a function named max_num() that takes a list of numbers named nums as a parameter.
#The function should return the largest number in nums

def max_num(nums):
  for num in nums:
    max_n = max(nums)
  return max_n

print(max_num([50, -10, 0, 75, 20]))