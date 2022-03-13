# @param {Integer} n
# @param {Integer[][]} artifacts
# @param {Integer[][]} dig
# @return {Integer}
def dig_artifacts(n, artifacts, dig)
    num_artifacts = artifacts.length
    dig_map = artifacts.each_with_object({}).with_index do |(a, h), idx|
       for i in a[0]..a[2] do
           for j in a[1]..a[3] do
               h[[i, j]] = idx
           end
       end 
    end
    dig.each {|x| dig_map.delete x}
    digged_artifacts = (0...num_artifacts).to_a - dig_map.values
    digged_artifacts.length
end
