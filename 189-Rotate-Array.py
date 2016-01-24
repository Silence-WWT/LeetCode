class Solution(object):
    def rotate(self, nums, k):
        """
        :param nums: list[int]
        :param k: int, num of steps
        :return nothing, modify nums in-place instead.
        """
        length = len(nums)
        offset = k % length
        if offset:
            nums.extend(nums[:-offset])
            for i in range(length - offset):
                nums.pop(0)


if __name__ == '__main__':
    nums = [1, 2]
    Solution().rotate(nums, 1)
    print(nums)
