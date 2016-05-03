PlayerId = 0
Points = 1
Flipped = 2
Unflipped = 3

round, id, global, *players = ARGV[0].split(';')
round = round.to_i
id = id.to_i
global = global.to_i

if(round == 1)
    print '3FF'
    exit
end

players.map!{ |s| s.split('_').map(&:to_i) }

nplayers = players.size

my_pos = players.find_index { |a| a[PlayerId] == id }

coin_vals = players.map{|a| a[Flipped]*2 - a[Unflipped]}

move = [-1,1].max_by{|s|
    swap_gain = coin_vals.rotate(s)
    scores = (0...nplayers).map{|i|
        swap_gain[i]+players[i][Points]
    }
    scores.delete_at(my_pos)-scores.max
}
if move == 1
    print 'R'
else
    print 'T'
end

print ['1F', 'FF'][rand 2]