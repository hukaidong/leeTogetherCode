# @param {Integer[][]} piles
# @param {Integer} k
# @return {Integer}
def max_value_of_coins(piles, k)    
    dp_cache = piles.map do |p|
        Array.new(size=p.length+1)
    end
    
    dp = lambda do |idx, k|
        next 0 if idx == piles.length or k == 0
        dp_cache[idx][k] = dp_cache[idx][k] || proc do 
            sum = 0
            result_0 = dp.call(idx+1, k)
            result_1 = piles[idx].take(k).map.with_index do |p, i|
                sum += p
                sum + dp.call(idx+1, k-i-1)
            end.max
            [result_0, result_1].max
        end.call
    end
    dp.call(0, k)
end
