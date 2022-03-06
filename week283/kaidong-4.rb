# @param {Integer[]} nums
# @return {Integer[]}
def replace_non_coprimes(nums)
    ci = 0  # current index

    while ci + 1 < nums.length
        if nums[ci] == 1
            ci += 1
            next
        end   
        
        repeated_num = 0
        while nums[ci] == nums[ci+repeated_num+1]
            repeated_num += 1
        end
        if repeated_num < 50
            repeated_num.times { nums.delete_at(ci+1) }
        else
            nums = nums[0..ci] + nums[ci+repeated_num+1...nums.length]
        end
        
        if ci + 1 == nums.length
            break
        end
        
        gcd, lcm = nums[ci].gcdlcm(nums[ci+1])
        if gcd > 1
            nums[ci] = lcm
            nums.delete_at(ci+1)
            ci -= 1 if ci > 0
        else
            ci += 1
        end
    end
    nums
end
