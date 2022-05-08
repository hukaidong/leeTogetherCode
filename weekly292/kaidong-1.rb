# @param {String} num
# @return {String}
def largest_good_integer(num)
    num.chars.each_cons(3).map do |a|
      a.uniq.size == 1 ? a[0] : nil
    end.compact.max.yield_self do |x|
      x.nil? ? "" : x*3
    end
end
