# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}

def minimal_k_sum(nums, k)
    nums.uniq!
    head_num = 1
    num_remain = k
    sum = 0
    while num_remain > 0
        collision_sum = nums.filter do |n|
            n >= head_num && n < head_num+num_remain
        end

        partial_sum = (2 * head_num + num_remain - 1) * num_remain / 2
        sum += partial_sum - collision_sum.sum
        
        head_num += num_remain
        num_remain = collision_sum.length
    end
    sum
end
