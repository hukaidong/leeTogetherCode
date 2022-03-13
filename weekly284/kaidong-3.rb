# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_top(nums, k, max_out_of_pile=nil)
    return -1 if nums.length == 0
    return -1 if nums.length == 1 and k.odd? and max_out_of_pile.nil?
    if k == 0
        return nums[0]
    elsif k == 1 
        if max_out_of_pile.nil? 
            if nums.length > 1
                return nums[1]
            else 
                return -1
            end
        else
            puts "#{nums[1]}, #{max_out_of_pile}"
            return [nums[1], max_out_of_pile].compact.max
        end
    elsif k <= nums.length
        return maximum_top(nums.drop(k-1), 1, nums.take(k-1).max)
    else
        return nums.max
    end
end
