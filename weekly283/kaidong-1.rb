# @param {String} s
# @return {String[]}
def cells_in_range(s)
    result = []
    (s[0]..s[3]).each do |a|
        (s[1]..s[4]).each do |b|
            result << a+b
        end
    end
    result
end
