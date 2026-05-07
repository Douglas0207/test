
def prefix_sum(arr):
    prefix_array = []
    total =0
    for num in arr:
        total = total+num
        prefix_array.append(total)
    return prefix_array

def rangeSumQuery(arr,l,r):
    l=l-1
    r=r-1
    prefix_array = prefix_sum(arr)
    if l==0:
        rangeSum = prefix_array[r]
    else:    
        rangeSum = prefix_array[r] - prefix_array[l-1]
    return rangeSum

def equillibriumSum(arr):
    prefix_array = prefix_sum(arr)
    left_sum = 0
    right_sum = 0
    total_sum = sum(arr)
    for i in range(len(arr)):
        if i ==0:
            left_sum =0
            right_sum = total_sum - prefix_array[i]
        else:
            left_sum = prefix_array[i-1]
            right_sum = total_sum - prefix_array[i]
        if left_sum == right_sum:
            return i
    return -1

def equillibriumSumOpt(arr):
    left_sum =0
    total = sum(arr)
    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1
    
def freqOfArray(arr):
    my_map = {}
    for num in arr:
        if num in my_map:
            my_map[num] +=1
        else:
            my_map[num] =1
    return my_map

def maximumFrequency(arr):
    my_map = {}
    max_count=0
    number=None
    for num in arr:
        my_map[num] = my_map.get(num,0)+1
    for num in my_map:
        if my_map[num] > max_count:
            max_count = my_map[num]
            number = num
    return number

def maxSubArray(arr,k):
    my_map = {}
    max_length =0
    curr_sum =0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == k:
            max_length = i+1

        previous_sum = curr_sum - k
        if previous_sum in my_map:
            length = i - my_map[previous_sum]
            if max_length < length:
                max_length = length

        if curr_sum not in my_map:
            my_map[curr_sum] = i

    return max_length

def maxSubArrayCount(arr,k):
    my_map = {}
    curr_sum = 0
    count = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == k:
            count+=1
        previous_sum = curr_sum - k
        if previous_sum in my_map:
            count+= my_map[previous_sum]
        my_map[curr_sum] = my_map.get(curr_sum,0) +1
    return count

def maxSubArrayPrac(arr,k):
    my_map = {}
    curr_sum = 0
    max_length = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == k:
            max_length = i+1
        prev_sum = curr_sum - k
        if prev_sum in my_map:
            length = i - my_map[prev_sum]
            if max_length < length:
                max_length = length
        if curr_sum not in my_map:
            my_map[curr_sum] = i
    return max_length


def runningSum(arr):
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i-1]
    return arr


arr1 = [1,2,3,4,5]
ans1 = prefix_sum(arr1)
print(ans1)
arr2 = [1,2,3,4,5,6,7]
l=3
r=6
ans2 = rangeSumQuery(arr2,l,r)
print(ans2)
arr3= [1, -1, 0]
ans3 = equillibriumSum(arr3)
print("Found at index ",ans3)
arr4 = [1,2,3,2,1]
ans4 = freqOfArray(arr4)
print(ans4)
arr5 = [1,2,3,2,1,2,3]
ans5 = maximumFrequency(arr5)
print(ans5)
arr6 = [1,-1,5,-2,3]
k=3
ans6 = maxSubArray(arr6,k)
print(ans6)
arr7 = [1,2,3]
ans7 = maxSubArrayCount(arr7,k)
print(ans7)
arr8 = [1,2,3,4,5]
runningSum(arr8)
print(arr8)