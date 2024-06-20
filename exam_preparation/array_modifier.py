from typing import List


def swap(nums: List[int], index_one, index_two: int):
    nums[index_one], nums[index_two] = nums[index_two], nums[index_one]


def multiply(nums: List[int], index_one, index_two: int):
    nums[index_one] *= nums[index_two]


def decrease(nums: List[int]):
    return [num - 1 for num in nums]


def array_modifier(nums):
    while True:
        command = input()

        if command == 'end':
            print(', '.join(map(str, nums)))
            break

        parts = command.split()
        action = parts[0]

        if action == 'swap':
            swap(tuple(nums), int(parts[1]), int(parts[2]))

        elif action == 'multiply':
            multiply(nums, int(parts[1]), int(parts[2]))

        elif action == 'decrease':
            nums = decrease(nums)


numbers = list(map(int, input().split()))
array_modifier(numbers)

