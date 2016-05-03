def deep_copy(o)
  Marshal.load(Marshal.dump(o))
end

ID = 0
PTS = 1
FLP = 2
UFL = 3

round, id, global, *players = ARGV[0].split(';')
round = round.to_i
id = id.to_i
global = global.to_i

players.map!{ |s| s.split('_').map(&:to_i) }

nplayers = players.size

my_pos = players.find_index { |i, p, f, u| i == id }

state = {
    round: round,
    id: id,
    global: global,
    players: players,
    my_pos: my_pos,
    me: players[my_pos],
    prev_p: players[my_pos-1],
    next_p: players[(my_pos+1)%nplayers],
    ends_game: round == 50 && my_pos == nplayers-1,
    score: 0
}

moves = {
    'N' => ->s{deep_copy(s)},
    '1' => ->s{t = deep_copy(s); coins = [1, t[:global]].min; t[:global] -= coins; t[:me][UFL] += coins; t[:score] -= coins; t},
    '2' => ->s{t = deep_copy(s); coins = [2, t[:global]].min; t[:global] -= coins; t[:me][UFL] += coins; t[:score] -= coins; t},
    '3' => ->s{t = deep_copy(s); coins = [3, t[:global]].min; t[:global] -= coins; t[:me][UFL] += coins; t[:score] -= coins; t},
    'A' => ->s{t = deep_copy(s); coins = [1, t[:me][UFL]].min; t[:global] += coins; t[:me][UFL] -= coins; t[:score] += coins; t},
    'B' => ->s{t = deep_copy(s); coins = [2, t[:me][UFL]].min; t[:global] += coins; t[:me][UFL] -= coins; t[:score] += coins; t},
    'C' => ->s{t = deep_copy(s); coins = [3, t[:me][UFL]].min; t[:global] += coins; t[:me][UFL] -= coins; t[:score] += coins; t},
    'X' => ->s{t = deep_copy(s); coins = [1, t[:me][UFL]].min; t[:me][UFL] -= coins; t},
    'Y' => ->s{t = deep_copy(s); coins = [2, t[:me][UFL]].min; t[:me][UFL] -= coins; t},
    'Z' => ->s{t = deep_copy(s); coins = [3, t[:me][UFL]].min; t[:me][UFL] -= coins; t},
    'F' => ->s{t = deep_copy(s); coins = [1, t[:me][UFL]].min; t[:me][UFL] -= coins; t[:me][FLP] += coins; t[:score] += 2*coins; t},
    'U' => ->s{t = deep_copy(s); coins = [1, t[:me][FLP]].min; t[:me][FLP] -= coins; t[:me][UFL] += coins; t[:score] -= 2*coins; t},
    'R' => ->s{
        t = deep_copy(s)
        (-1...t[:players].size-1).each do |i|
            t[:players][i][FLP] = s[:players][i+1][FLP]
            t[:players][i][UFL] = s[:players][i+1][UFL]
        end
        t[:score] += 2*t[:me][FLP] - t[:me][UFL];
        t
    },
    'T' => ->s{
        t = deep_copy(s)
        (0...t[:players].size).each do |i|
            t[:players][i][FLP] = s[:players][i-1][FLP]
            t[:players][i][UFL] = s[:players][i-1][UFL]
        end
        t[:score] += 2*t[:me][FLP] - t[:me][UFL];
        t
    }
}


results = {}

'N123ABCXYZFURT'.each_char { |c1| 
    s1 = moves[c1][state]
    'N123ABCXYZFURT'.each_char { |c2| 
        s2 = moves[c2][s1]
        'N123ABCXYZFURT'.each_char { |c3| 
            s3 = moves[c3][s2]
            s3[:ends_game] ||= s3[:global] == 0
            results[c1+c2+c3] = s3
        }
    }
}

endingMoves = results.keys.select{|k| results[k][:ends_game]}

endingMoves.each{|k| results[k][:score] += 2*results[k][:me][FLP] - results[k][:me][UFL]}

$> << results.keys.shuffle.max_by {|k| results[k][:score]}