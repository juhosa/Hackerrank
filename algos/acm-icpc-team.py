# return tuple (max_num_topics, teams_max)
def work(n,topics,ms):
    max_topics = 0
    teams_max = 0
    
    peeps = {}

    for i in xrange(n):
        peeps[i] = ms[i]

    # create all 2-person team permutations
    team_perms = []
    for i in peeps.keys():
        for j in xrange(i,len(peeps.keys())):
            team_perms.append((i,j))

    # count permutation score
    team_scores = {}

    for teams in team_perms:
        
        tmp = str(bin(int(peeps[teams[0]],2) | int(peeps[teams[1]],2))[2:])

        count = 0

        count = tmp.count("1")
        
        team_scores[teams] = count

        if count > max_topics:
            max_topics = count
            
    for k,v in team_scores.iteritems():
        if v == max_topics:
            teams_max = teams_max + 1
    
    return (max_topics, teams_max)

first_line = "500 500" # test 5
#first_line = raw_input()

N = int(first_line.split(" ")[0])
M = int(first_line.split(" ")[1])

mstemp = []
with open('acm-icp-team-test5.txt') as f:
    mstemp = f.read().splitlines()
    
Ms = []
for i in xrange(0,len(mstemp)):
    tmp = mstemp[i]
    tmp2 = bin(int(tmp,2))
    Ms.append(tmp2)

answers = work(N,M,Ms)
max_num_topics = answers[0] # maximum number of topics a 2-person team can know
teams_max = answers[1] # num of 2-person teams that can know the maximum number of topics

print max_num_topics
print teams_max
