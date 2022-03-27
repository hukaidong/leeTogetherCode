# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[][]}
require 'set'
def find_difference(nums1, nums2)
    n1 = Set.new(nums1)
    n2 = Set.new(nums2)
    return (n1-n2).to_a, (n2-n1).to_a
end
