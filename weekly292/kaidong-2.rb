# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def average_of_subtree(root)
  hitnum = 0
  evaltree = lambda do |t|
    if t.nil?
      return 0, 0
    else
      ls, ln = evaltree[t.left]
      rs, rn = evaltree[t.right]
      sum = t.val + ls + rs
      sacc = 1 + ln + rn
      hitnum += 1 if t.val == sum/sacc
      return [sum, sacc]
    end
  end
  evaltree[root]
  hitnum
end
