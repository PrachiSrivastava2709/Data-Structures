#Recursive Approach
def binary_search(arr: list[int], start: int, end: int, target: int) -> int:
    if end >= start:
        mid = (end + start)//2
    
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return binary_search(arr, mid + 1, end, target)
        if target < arr[mid]:
            return binary_search(arr, 0, mid - 1, target)
            
    else:
        return -1
        
if __name__ == "__main__":
    nums = [2,3,4,5,6,7,8,9,10,11]
    print(binary_search(nums, 0, len(nums)-1, 11))