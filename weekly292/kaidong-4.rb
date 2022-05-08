def has_valid_path(grid)
  return false if grid[0][0] == ")"
  m = grid.size
  n = grid[0].size
  grid.each {|x| x.map! {|y| y == "(" ? 1 : -1 } }
  candidate = Array.new(m) { Array.new(n) {Array.new} }
  candidate[0][0] = [grid[0][0]]
  for i in (0...m)
    for j in (0...n)
      thisval = grid.dig(i, j)
      addthis = proc {|x| x + thisval}
      next if i == 0 and j == 0
      candidate[i][j] = ((i == 0 ? [] : candidate.dig(i-1, j).map(&addthis)) +
                         (j == 0 ? [] : candidate.dig(i, j-1).map(&addthis)) )
                          .uniq.select {|x| x >= 0}
    end
  end
  candidate.dig(m-1, n-1).include? 0
end
