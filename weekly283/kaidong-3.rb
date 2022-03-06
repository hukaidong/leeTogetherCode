# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {Integer[][]} descriptions
# @return {TreeNode}

class TreeNode
    attr_accessor :isChild
end


def create_binary_tree(descriptions)
  tnHash = Hash.new do |h, k|
    return h[k] if h.has_key?(k)
    tn = TreeNode.new(k)
    tn.isChild = false
    h[k] = tn
  end

  descriptions.each do |parent, child, isleft|
    if isleft == 1
      tnHash[parent].left = tnHash[child]
    else
      tnHash[parent].right = tnHash[child]
    end
    tnHash[child].isChild = true
  end

  tnHash.each_value.filter {|v| !v.isChild}.first
end
