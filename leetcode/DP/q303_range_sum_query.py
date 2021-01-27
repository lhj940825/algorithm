class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            return
        self.nums = nums
        self.cum_sum = [0]*(len(nums)+1)

        for i, num in enumerate(nums, start=1):
            self.cum_sum[i] = self.cum_sum[i-1] + num


    def sumRange(self, i: int, j: int) -> int:
        return self.cum_sum[j+1] - self.cum_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# test