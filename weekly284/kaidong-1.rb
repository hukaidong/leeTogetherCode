# @param {Integer[]} nums
# @param {Integer} key
# @param {Integer} k
# @return {Integer[]}
def find_k_distant_indices(nums, key, k)
    idxs = nums.map.with_index do |x, i|
        if x == key
            i
        else
            nil
        end
    end.compact
    idxs.map do |x|
        startIdx = x - k
        startIdx = startIdx > 0 ? startIdx : 0
        eIdx = x + k
        eIdx = eIdx < nums.length ? eIdx : nums.length - 1
        (startIdx..eIdx).to_a
    end.flatten.uniq
end
