def binary_search(arr, target):
  lo,hi=0,len(arr)-1
  
  while lo<=hi:
    mid = (lo+hi)//2
    print(arr[lo:hi])
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      hi = mid -1
    else:
      lo = mid +1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 3
result = binary_search(arr, target)
print(result)