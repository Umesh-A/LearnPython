#Create a function called middle_element that has one parameter named lst.
#If there are an odd number of elements in lst, the function should return the middle element. 
#If there are an even number of elements, the function should return the average of the middle two elements.


def middle_element(lst) :
  n = len(lst)
  if n%2 == 1:
    return lst[n//2]
  else :
    return (lst[n//2] + lst[n//2-1])/ 2


print(middle_element([5, 2, -10, -4, 4, 5]))