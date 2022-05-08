MAGICNUM = 10 ** 9 + 7


KEYTYPE = "xx33333434"
def count_texts(pressed_keys)
  memory_4 = [1, 1, 2, 4, 8]
  count_rec_4 = lambda do |x|
    if memory_4.size < x
      memory_4.fill(nil, memory_4.size...x)
    end
    memory_4[x] ||= ( 
      count_rec_4[x-1] + count_rec_4[x-2] + count_rec_4[x-3] + count_rec_4[x-4]
                    ) % MAGICNUM
  end


  memory_3 = [1, 1, 2, 4, 7]
  count_rec_3 = lambda do |x|
    if memory_3.size < x
      memory_3.fill(nil, memory_3.size...x)
    end
    memory_3[x] ||= (count_rec_3[x-1] + count_rec_3[x-2] + count_rec_3[x-3]) % MAGICNUM
  end

  pressed_keys.chars.chunk {|x| x}.map do |(t, a)| 
    puts a.inspect
    puts "size #{a.size}"
    if KEYTYPE[t.to_i] == "3"
      count_rec_3.call(a.size)
    else
      count_rec_4.call(a.size)
    end
  end.reduce(1) do |s, i|
    puts "possible #{i}"
    (s * i) % MAGICNUM
  end
end
