# 1. Find Maximum Element in Array

# 👉 Input: [3, 7, 2, 9, 5]
# 👉 Output: 9

# 💡 Hint:

# Start with first element as max
# Traverse and compare

# def findMaxFor(arr):
#     if(len(arr))==0:
#         return None
#     max_ele = float('-inf')
#     for i in range(len(arr)):
#         if max_ele < arr[i]:
#             max_ele = arr[i]
#     return max_ele # optimal for space

# 1. Find Maximum Element in Array

def findMax(arr):
    if(len(arr))==0:
        return None
    max_ele = arr[0]
    for nums in arr[1:]:
        if max_ele < nums:
            max_ele = nums
    return max_ele # extra space but iteration starts with first element

# 2. Find Minimum Element
def findMin(arr):
    if(len(arr))==0:
        return None
    min_ele = arr[0]
    for nums in arr[1:]:
        if min_ele > nums:
            min_ele = nums
    return min_ele
# 3. Reverse an Array

def reverseArr(arra):
    arr = arra
    left = 0
    right = len(arr)-1
    while left<right:
        # using temp variable
        # temp = arr[left]
        # arr[left] = arr[right]
        # arr[right] = temp
        # without using temp variable
        # right side is validated first. 
        # arr[left], arr[right] = 4,1
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1

    return arr

def findSecLar(arr):
    if len(arr)<2:
        return None
    lar = arr[0]
    sec_lar = float('-inf')
    for nums in arr:
        if lar < nums:
            sec_lar = lar
            lar = nums
        elif lar > nums and sec_lar < nums:
            sec_lar = nums
    if sec_lar == float('-inf'):
        return None
    return sec_lar    

def findArrSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
    
def removeDup(arr):
    dupArr = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            dupArr.append(arr[i])
    dupArr.append(arr[len(arr)-1])        
    return dupArr        

def moveZeros(arr):
    dupArr = []
    count =0
    for i in range(len(arr)):
        if arr[i]!= 0:
            dupArr.append(arr[i])
            count += 1
    for i in range(count,len(arr)):
        dupArr.append(0)
    return dupArr

def moveZerosOpt(arr):
    pos =0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos] = arr[i]
            pos +=1
    for i in range(pos, len(arr)):
        arr[i] = 0
    return arr            

def linearSearch(arr,tar):
    for i in range(len(arr)):
        if arr[i] == tar:
            return i
    return -1

def countEvenAndOdd(arr):
    even = 0
    odd = 0
    for num in arr:
        if num%2==0:
            even += 1
        else:
            odd += 1
    return even,odd

def sumOfArr(arr):
    total = 0
    for num in arr:
        total = total + num
    return total

def findPair(arr,k):
    if not arr:
        return "NO"
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[right] >= k:
            right -= 1
        if arr[left] + arr[right] > k:
            right -= 1
        if arr[left] + arr[right] < k:
            left +=1
        if arr[left] + arr[right] == k:
            return "YES"
        left += 1
    return "NO"

def findPairOpt(arr,k):
    if not arr:
        return "NO"
    left =0
    right = len(arr)-1
    while left<right:
        s = arr[left] + arr[right]
        if s == k:
            return left,right
        elif s < k:
            left +=1
        else:
            right -=1
    return "NO"













arr = [3,7,2,9,5]
arr1 = [1,1,2,2,3,3,4,4]
arr2 = [0,5,0,2,0,1,0,12,0,0,2]
ans1 = findMax(arr)
ans2 = findMin(arr)
ans3 = reverseArr(arr)
ans4 = findSecLar(arr)
ans5 = findArrSorted(arr)
ans6 = removeDup(arr1)
ans7 = moveZeros(arr2)
ans8 = moveZerosOpt(arr2)
tar = 9
ans9 = linearSearch(arr,tar)
arr3 = [1,2,3,4,5,4,3,2,1,0]
even,odd = countEvenAndOdd(arr3)
ans10 = sumOfArr(arr3)
arr4 = [-3, -1, 1, 2, 12, 13, 14, 18]
K = -4
ans11 = findPair(arr4,K)
ans12 = findPairOpt(arr4,K)
print(f"The maximum element is {ans1}")
print(f"The maximum element is {ans2}")
print(f"The Reverse of Array is {ans3}")
print(f"The Second largest element in the array is {ans4}")
if ans5 == False:
    print("The given array is not sorted")
else:
    print("The given array is Sorted")
print("Array after removing duplicates: ",ans6)
print("Array after moving zeros :",ans7)
print("Array after moving zeros :",ans8)
if ans9 == -1:
    print("The Number is not found")
else:
    print(f"The Number is found in the index : {ans9}")
print(f"Even: {even}, Odd: {odd}")
print("Sum of Array is : ",ans10)
print(ans11)
print(ans12)