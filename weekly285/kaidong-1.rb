# @param {Integer[]} nums
# @return {Integer}
def count_hill_valley(nums)
    def sign(nump)
       [:eql, :pos, :neg][nump[0] <=> nump[1]] 
    end
    
    def signaggr(before, after) 
       if after == :eql
           before
       else
           after
       end
    end
    
    def signInverted?(before, after)
        if before == :eql or after == :eql
            return false
        end
        return before != after
    end
    
    count_num = 0 
    nums.each_cons(2)
    .map(&method(:sign))
    .reduce :eql do |last, curr|
        count_num += 1 if signInverted?(last, curr)
        signaggr(last, curr)
    end
    count_num
end
