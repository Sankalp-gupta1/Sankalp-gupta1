def selection (arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini =j
                arr[i],arr[mini]=arr[mini],arr[i]
arr=[23,45,33,22,44,21]   
selection(arr)
print("your sorted array is",arr)
