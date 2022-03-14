# @param {Integer[]} nums
# @param {Integer} key
# @param {Integer} k
# @return {Integer[]}
def find_k_distant_indices(nums, key, k)
    idxs = nums.each_index.select {|x| nums[x] == key}
    idxs.flat_map {|x| (x-k..x+k).to_a}
        .uniq
        .select {|x| x.between?(0, nums.length-1)}
end
