def miniMaxSum(arr):
    arr2=arr[:]
    minsum=0
    maxsum=0
    
    for i in range(0,4):
        minsum+=min(arr)
        arr.remove(min(arr))
    
    for i in range(0,4):
        maxsum+=max(arr2)
        arr2.remove(max(arr2))
    print(minsum,maxsum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
        
    miniMaxSum(arr)
