#brute force method (TC = O(n^2))
# def maxSum(arr,n,k):
#     max_sum = 0
#     for i in range(n-k+1):
#         current_sum = 0
#         for j in range(k):
#             current_sum += arr[i+j]
#         max_sum = max(current_sum , max_sum)
#     return max_sum
# if __name__ == "__main__":
#     arr =[5,2,-1,0,3]
#     k = 3
#     n = len(arr)
#     print(maxSum(arr,n,k))


#optimized method(TC = O(n))
def maxSubarray(arr,k):
    n = len(arr)
    if n < k:
        return -1
    
    ws = sum(arr[:k])
    maxsum = ws

    for i in range(k,n):
        ws += arr[i] - arr[i-k]
        maxsum = max(maxsum,ws)
    return maxsum

if __name__ == "__main__":
    arr =[5,2,-1,0,3]
    k = 3
    print(maxSubarray(arr,k))