round, id, global, *players = ARGV[0].split(';')
round = round.to_i
id = id.to_i
global = global.to_i

players.map!{ |s| s.split('_').map(&:to_i) }

nplayers = players.size

my_pos = players.find_index { |i, p, f, u| i == id }

prev_p = players[my_pos-1]
next_p = players[(my_pos+1)%nplayers]

prev_score = 2*prev_p[2] - prev_p[3]
next_score = 2*next_p[2] - next_p[3]

take_from = prev_p

$><< '3'
if prev_score > next_score || prev_score == next_score && prev_p[3] > next_p[3]
    $><< 'T'
else
    $><< 'R'
    take_from = next_p
end

if take_from[3] >= 3
    $><< 'C'
elsif take_from[3] >= 1
    $><< 'F'
else
    $><< 'N'
end