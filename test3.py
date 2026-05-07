# Challenge 1 — Balance Point in Load System

# A server processes loads:

# loads = [10, 5, 5, 10, 5, 5]

# System is balanced if:

# sum(left side) == sum(right side)
# 🎯 Task

# Return:

# index where system is balanced

# If multiple → return first
# If none → return -1


def processLoads(arr):
    # idea => right sum = total - running sum - arr[i]
    total = sum(arr)
    running_sum = 0
    for i in range(len(arr)):
        right_sum = total - running_sum - arr[i]
        if running_sum == right_sum:
            return i
        running_sum += arr[i]
    return -1


loads = [10,5,5,10,5,5]
ans = processLoads(loads)
if ans == -1:
    print("System is not balanced")
else:
    print("System is balanced at",ans)


# Challenge 2 — Fraud Detection System

# A bank tracks transactions:

# transactions = [3, 4, 7, 2, -3, 1, 4, 2]

# They suspect fraud patterns when:

# sum of transactions = K
# K = 7
# 🎯 Task

# Return:

# total number of subarrays with sum = K
# 💡 Hint
# prefix sum + hashmap (frequency)


def subArrayCount(arr,k):
    my_map = {}
    curr_sum = 0
    count =0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == k:
            count+=1
        prev_sum = curr_sum - k 
        if prev_sum in my_map:
            count += my_map[prev_sum]
        my_map[curr_sum] = my_map.get(curr_sum,0) +1
    return count



transactions = [3,4,7,2,-3,1,4,2]
sum_of_transactions = 7
print("The total number of subarrays with sum = k is ",subArrayCount(transactions,sum_of_transactions))


# Challenge 3 — Sales Streak Analysis

# A company tracks daily profit/loss in an array:

# profits = [2, -1, 2, 3, -2, 4, -1]

# The manager wants to know:

# 👉 What is the longest continuous period where total profit = K

# K = 5
# 🎯 Task

# Return:

# length of longest subarray with sum = K
# 💡 Hint (don’t ignore)
# prefix sum + hashmap (index)


def subArrayLength(arr,k):
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


profits = [2,-1,2,3,-2,4,-1]
longest_continours_period = 5
print("The longest continous period where total profit of 5 is ",subArrayLength(profits,longest_continours_period))