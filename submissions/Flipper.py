import sys, random

# process input data (not used here):
args = sys.argv[1].split(';')
rounds, myid, coins = map(int, args[:3])
players = [map(int, data.split('_')) for data in args[3:]]

# implement strategy using multiples of 'N123ABCXYZRTFU':
options = '12333FFFFFFFFFFF'
print ''.join(random.choice(options) for i in range(3))