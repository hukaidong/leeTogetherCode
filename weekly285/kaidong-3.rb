# @param {Integer} num_arrows
# @param {Integer[]} alice_arrows
# @return {Integer[]}
def maximum_bob_points(num_arrows, alice_arrows)
    # arrow remain after i taken     num_arrow - alice_arrows[i] - 1
    # bob at i pos is max i+1 pos with 
    dp = proc do |pos, remain_arr| # return point, num_arrws
        if pos == alice_arrows.length
            point = 0
            num_arrws = []
        else
            h1 = dp[pos+1, remain_arr]
            if remain_arr <= alice_arrows[pos]
                point = h1[:point]
                num_arrws = [0] + h1[:num_arrws]
            else
                h2 = dp[pos+1, remain_arr - alice_arrows[pos] -1]
                if h1[:point] > h2[:point] + pos
                    point = h1[:point]
                    num_arrws = [0] + h1[:num_arrws]
                else
                    point = h2[:point] + pos
                    num_arrws = [alice_arrows[pos]+1] + h2[:num_arrws]
                end
            end
        end
        {point:, num_arrws:}
    end
    
    unfilled_arrws = dp[0, num_arrows][:num_arrws]
    arrow_left = num_arrows - unfilled_arrws.sum
    unfilled_arrws[0] += arrow_left
    unfilled_arrws

end
