# @param {Integer[]} nums
# @return {Integer}
def count_hill_valley(nums)
    nums.each_cons(2)
    .map {|a, b| a <=> b}
    .reject {|x| x == 0}
    .each_cons(2)
    .sum {|a, b| a == b ? 0 : 1}
end 
