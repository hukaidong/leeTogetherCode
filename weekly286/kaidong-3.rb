# @param {Integer[]} queries
# @param {Integer} int_length
# @return {Integer[]}
def kth_palindrome(queries, int_length)
    halfceil = (int_length / 2.0).ceil
    halffloor = (int_length / 2.0).floor
    firstnum = 10 ** (halfceil - 1)
    max_idx = firstnum * 10 - 1
    pp firstnum, max_idx
    queries.map do |x|
        lnum = (firstnum + x - 1)
        next -1 if lnum > max_idx 
        rnum = lnum.digits.drop(halfceil-halffloor)
        (lnum.digits.reverse + rnum).join.to_i
    end
end
