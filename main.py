# insertion sort algorithm, decreasing order
def insertionSort(nums):
    for i in range(len(nums)):
        j = i - 1
        val = nums[i]

        while j >= 0 and val > nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = val
        # printing the array after each loop to visualize the process of insertion sort
        print(f'Loop {i + 1}:')
        print(nums)

# test cases
if __name__ == '__main__':
    nums = [1,3,5,4,2,6,7]
    insertionSort(nums)
