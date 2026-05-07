def leftRotate(arr):
    ele = arr[0]
    copy_arr = arr.copy()
    for i in range(len(arr)-1):
        copy_arr[i] = arr[i+1]
    copy_arr[len(arr)-1] = ele
    return copy_arr

def leftRotateByK(arr,k):
    res = []
    k = k % len(arr)
    for i in range(k,len(arr)):
        res.append(arr[i])
    for i in range(k):
        res.append(arr[i])
    return res

def leftRotateByKOpt(arr,k):
    k = k % len(arr)    
    reverse_arr(arr,0,k-1)
    reverse_arr(arr,k,len(arr)-1)
    reverse_arr(arr,0,len(arr)-1)
    return arr

def reverse_arr(arr,left,right):
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr

def leaderInArrayOpt(arr):
    res = []
    max_so_far = arr[len(arr)-1]
    res.append(max_so_far)
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > max_so_far:
            max_so_far = arr[i]
            res.append(arr[i])
    reverse_arr(res,0,len(res)-1)
    return res

def leaderInArray(arr):
    res = [arr[len(arr)-1]]
    for i in range(len(arr)-2,-1,-1):
        if checkLeader(res,arr[i]):
            res.append(arr[i])
    reverse_arr(res,0,len(res)-1)
    return res

def checkLeader(arr,k):
    for i in range(len(arr)):
        if arr[i]>k:
            return False
    return True

def findMissNo(arr):
    total = 0
    n = len(arr)+1
    total_sum = (n * (n+1))//2
    for i in range(len(arr)):
        total = total + arr[i]
    ans = total_sum - total
    return ans

def findMissNoXor(arr):
    xor_all =0
    xor_arr =0
    for i in range(1,len(arr)+2):
        xor_all = xor_all ^ i
    for num in arr:
        xor_arr = xor_arr ^ num
    missing = xor_all ^ xor_arr
    return missing
    
def maxConsecOnes(arr):
    count = 0
    max_streak =0
    for num in arr:
        if num == 1:
            count += 1
            if count > max_streak:
                max_streak = count
        else:
            count =0
    return max_streak


def singleNum(arr):
    xor =0
    for num in arr:
        xor = xor ^ num
    return xor
    

def maxSubArr(arr,k):
    max_len =0
    for i in range(len(arr)):
        sum =0
        for j in range(i,len(arr)):
            sum += arr[j]
            cur_len = j - i +1
            if sum == k:
                if cur_len> max_len:
                    max_len = cur_len
    return max_len


def majEle(arr):
    for i in range(len(arr)):
        count =0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                    count +=1
        if count > len(arr)/2:
            return arr[i]
    return None

   
                
        


arr1 = [1,2,3,4,5]
ans1 = leftRotate(arr1)
print(ans1)
k = 3
ans2 = leftRotateByK(arr1,k)
print(ans2)
ans3 = leftRotateByKOpt(arr1,k)
print(ans3)
arr2 = [16,17,4,3,5,2]
ans4 = leaderInArray(arr2)
print(ans4)
arr3 = [2,3,4,5,6,7]
ans5 = findMissNo(arr3)
print(ans5)
arr4 = [1,1,1,1,1,1,0,0,1,1,1]
ans6 = maxConsecOnes(arr4)
print(ans6)
arr5 = [1,1,2,2,3,4,4,5,5]
ans7 = singleNum(arr5)
print(ans7)
arr6 = [1,2,3,1,1,1,1]
m = 5
ans8 = maxSubArr(arr6,m)
print(ans8)
arr7 = [1,1,1,2,3,4,1]
ans9 = majEle(arr7)
print(ans9)