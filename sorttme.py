def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right =arr[mid:]

    left=merge_sort(left)    #dividing into single element by storing data(recursive)
    right=merge_sort(right)  # into left and right

    i=j=k=0

    while i<len(left)and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1


    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

    return arr                  #returning the element of an array              
arr = [38,27,43,3,9,82,10]
merge_sort(arr)
print(f"the sorted array is:{arr}")
