class Solution(object):
    def twoSum(self, nums, target):
        """

        :param nums: [list]
        :param target: [int]
        :return: [list]
        """

        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
