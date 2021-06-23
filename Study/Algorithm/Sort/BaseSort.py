import timeit
from typing import List
import collections

# 2021.05.23 | gomip | created


class Sorting:
    def bubble(self, input: List[int]) -> List[int]:
        for i in range(1, len(input)):
            for j in range(0, len(input) - 1):
                if input[j] > input[j+1]:
                    input[j], input[j+1] = input[j+1], input[j]
        return input

    def select(self, input: List[int]) -> List[int]:
        for i in range(len(input)):
            min_index = i
            for j in range(i+1, len(input)):
                if input[j] < input[min_index]:
                    min_index = j
            input[i], input[min_index] = input[min_index], input[i]

        return input

    def insertion(self, input: List[int]) -> List[int]:
        for i in range(1, len(input)):
            val = input[i]
            j = i
            while j > 0 and input[j-1] > val:
                input[j] = input[j-1]
                j -= 1
            input[j] = val
        return input

    def merge(self, input: List[int]) -> List[int]:
        if len(input) <= 1:
            return input
        mid = len(input)//2
        left = self.merge(input[:mid])
        right = self.merge(input[mid:])

        merged_input = []
        left_index = right_index = 0
        i = 0
        while left_index < len(left) and right_index < len(right):
            print("======================= i : ", i, "=======================")
            print("left", left, left_index, left[left_index])
            print("right", right, right_index, right[right_index])
            if left[left_index] < right[right_index]:
                merged_input.append(left[left_index])
                left_index += 1
            else:
                merged_input.append(right[right_index])
                right_index += 1
            print("merged", merged_input)
            i+=1

        print("======================= after =======================")
        print("merged", merged_input)
        merged_input += left[left_index:]
        merged_input += right[right_index:]
        return merged_input

    def quick(self, input: List[int], low: int, high: int) -> List[int]:
        print("low", low, "high", high)

        def partition(low, high):
            pivot = input[high]
            print("pivot", pivot)
            left = low
            for right in range(low, high):
                if input[right] < pivot:
                    input[left], input[right] = input[right], input[left]
                    print("input in loop", input)
                    left += 1
            input[left], input[high] = input[high], input[left]
            print("input in return", input)
            print("left", left)
            return left

        if low < high:
            pivot = partition(low, high)
            print("pivot", pivot)
            self.quick(input, low, pivot - 1)
            self.quick(input, pivot + 1, high)
        return input


if __name__ == '__main__':
    input = [4, 3, 5, 1, 2]
    print(input)

    temp = Sorting()

    # start1 = timeit.timeit()
    # ans1 = temp.bubble(input)
    # end1 = timeit.timeit()
    # print("bubble sort in ", end1 - start1, "result : ", ans1)
    #
    # start2 = timeit.timeit()
    # ans2 = temp.select(input)
    # end2 = timeit.timeit()
    # print("select sort in ", end2 - start2, "result : ", ans2)
    #
    # start3 = timeit.timeit()
    # ans3 = temp.insertion(input)
    # end3 = timeit.timeit()
    # print("insertion sort in ", end3 - start3, "result : ", ans3)

    # start4 = timeit.timeit()
    # ans4 = temp.merge(input)
    # end4 = timeit.timeit()
    # print("merge sort in ", end4 - start4, "result : ", ans4)
    #
    start5 = timeit.timeit()
    ans5 = temp.quick(input, 0, len(input)-1)
    end5 = timeit.timeit()
    print("quick sort in ", end5 - start5, "result : ", ans5)


