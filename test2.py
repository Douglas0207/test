# roblem: “Longest Stable Work Streak”

# A company tracks employee productivity for a week.

# You are given an array where:

# 1 → employee was productive that day
# 0 → employee was not productive

# However, the company allows at most one bad day (0) to be ignored (they assume it was due to external reasons).

# 👉 Task

# Find the maximum number of consecutive productive days, where you are allowed to treat at most one 0 as 1.

# [1,1,0,1,1,1,0,]


def findStreakTry(arr):
    count = 0
    max_consec = 0
    flag = False
    one_count = 0
    ones_before_zero = 0
    for num in arr:
        if num == 1:
            count += 1
            one_count +=1
        if num == 0 and flag == False:
            ones_before_zero = count
            count += 1
            flag = True
        elif num == 0 and flag == True:
            count = count - ones_before_zero
            one_count = one_count - ones_before_zero
        if max_consec < count:
            max_consec = count
    return max_consec

def findStreak(arr):
    zero_count =0
    curr_width =0
    left=0
    right=0
    max_width =0
    while right<len(arr):
        if arr[right] == 0:
            zero_count +=1
        while zero_count>1:
            if arr[left] ==0:
                zero_count -=1
            left +=1
        right+=1
        curr_width = right - left 
        if max_width<curr_width:
            max_width = curr_width
    return max_width




arr = [1,1,0,1,1,0,1,1,1,0,1]
ans = findStreak(arr)
print(ans)