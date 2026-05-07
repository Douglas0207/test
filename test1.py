import random

# ✅ Your function (paste yours here)
def findPair_user(arr, k):
    if not arr:
        return "NO"
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[right] >= k:
            right -= 1
        if left < right and arr[left] + arr[right] > k:
            right -= 1
        if left < right and arr[left] + arr[right] < k:
            left += 1
        if left < right and arr[left] + arr[right] == k:
            return "YES"
        left += 1
    return "NO"


# ✅ Correct reference solution
def findPair_correct(arr, k):
    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == k:
            return "YES"
        elif s < k:
            left += 1
        else:
            right -= 1

    return "NO"


# 🔥 Random test generator
def generate_test():
    size = random.randint(0, 10)
    arr = sorted(random.randint(-10, 20) for _ in range(size))
    k = random.randint(-10, 30)
    return arr, k


# 🚀 Run multiple tests
for i in range(1000):
    arr, k = generate_test()

    out1 = findPair_user(arr, k)
    out2 = findPair_correct(arr, k)

    if out1 != out2:
        print("❌ MISMATCH FOUND!")
        print("Array:", arr)
        print("K:", k)
        print("Your Output:", out1)
        print("Correct Output:", out2)
        break
else:
    print("✅ All tests passed (for now 😏)")