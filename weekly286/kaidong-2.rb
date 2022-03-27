# @param {Integer[]} nums
# @return {Integer}
def min_deletion(nums)
    _, keep = nums.drop(1).reduce([nums[0], 1]) do |(last, keep), n|
       if keep.odd? and n == last
           [last, keep]
       else
           [n, keep + 1]
       end
    end
    if keep.even?
        nums.length - keep
    else
        nums.length - keep + 1
    end
end
