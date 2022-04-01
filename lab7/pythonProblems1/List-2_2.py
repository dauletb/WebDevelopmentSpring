def centered_average(nums):
  nums.sort()
  nums.remove(nums[len(nums)-1])
  nums.remove(nums[0])
  s=0
  for x in nums:
      s=s+x
  return s/len(nums)