# insertion sort algorithm, decreasing order
def insertionSort(nums):
    for i in range(len(nums)):
        j = i - 1
        val = nums[i]

        while j >= 0 and val > nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = val
    
