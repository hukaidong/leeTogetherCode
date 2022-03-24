# @param {String} directions
# @return {Integer}
def count_collisions(directions)
    count = 0
    dirH= {
        "L"=> -1,
        "S"=> 0,
        "R"=> 1
    }
    print(dirH["S"])
    aggregate = lambda { |last, curr|        
        count_old = count
        #print "\n#{last} #{curr} #{count} "
        if last == -1
            return dirH[curr]
        else
            return last + 1 if curr == "R"
            count += last
            count += 1 if curr == "L"
            #print "#{count - count_old}"
            return 0
        end
    }
    directions.each_char.reduce(-1, &aggregate)
    
    count
end
