from trueskill import *

from ratings import *


#print_ai_ratings()

# 2v2v2
# 2v2
# 2v1
# 2v1
# 2v1
# 2v1

team1 = [P1, P2]
team2 = [AI["HD"]["easy"], AI["HD"]["easy"], AI["HD"]["easy"], AI["HD"]["easy"]]

(P1, P2), (AI["HD"]["easy"], x, y, z) = trueskill.rate( [team1, team2], ranks=[0, 1] )



#match on ice oasis
team1 = [P1, P2]
team2 = [AI["Res"]["easy"], AI["Res"]["easy"]]

(P1, P2), (AI["Res"]["easy"], dummy) = trueskill.rate([team1, team2], ranks=[1, 0])

#match on islands
team1 = [P1, P2]
team2 = [AI["Res"]["standard"]]

(P1, P2), [AI["Res"]["standard"]] = trueskill.rate( [team1, team2], ranks=[0, 1] )

#Water border on my side, ai = chineese
team1 = [P1, P2]
team2 = [AI["Res"]["standard"]]

(P1, P2), [AI["Res"]["standard"]] = trueskill.rate( [team1, team2], ranks=[0, 1] )

#
team1 = [P1, P2]
team2 = [AI["Res"]["standard"]]

(P1, P2), [AI["Res"]["standard"]] = trueskill.rate( [team1, team2], ranks=[0, 1] )

#
team1 = [P1, P2]
team2 = [AI["Res"]["standard"]]

(P1, P2), [AI["Res"]["standard"]] = trueskill.rate( [team1, team2], ranks=[0, 1] )


#print("post match 4")
#print_ai_ratings()
#print()
#print("P1\t", sub_print_rating(P1))
#print("P2\t", sub_print_rating(P2))

print("")
team1 = [P1, P2]




print("")
#print_ai_sorted_mu()

#TODO: somehow figure out how to run winchance against team1 vs x or x+y AI



# Attempt at using itertools.combinations
# failed; trueskill.Rating() can't be hashed?
all_AI = []
for vk, vv in AI.items():
    for dk, dv in AI[vk].items():
        all_AI.append((vk,dk))

all_team2 = list(all_AI)

all_easy = [(vk, "easy") for vk in AI.keys()]
all_standard = [(vk, "standard") for vk in AI.keys()]
all_moderate = [(vk, "moderate") for vk in AI.keys()]
all_hard = [(vk, "hard") for vk in AI.keys()]
all_hardest = [(vk, "hardest") for vk in AI.keys()]

#for s_team2 in all_team21:
#    print(s_team2)

all_team2 += list(itertools.combinations_with_replacement(all_easy, 2)) +\
             list(itertools.combinations_with_replacement(all_standard, 2)) +\
             list(itertools.combinations_with_replacement(all_moderate, 2)) +\
             list(itertools.combinations_with_replacement(all_hard, 2)) +\
             list(itertools.combinations_with_replacement(all_hardest, 2))

all_team2 += list(itertools.combinations_with_replacement(all_easy, 3)) +\
             list(itertools.combinations_with_replacement(all_standard, 3)) +\
             list(itertools.combinations_with_replacement(all_moderate, 3)) +\
             list(itertools.combinations_with_replacement(all_hard, 3)) +\
             list(itertools.combinations_with_replacement(all_hardest, 3))

all_team2 += list(itertools.combinations_with_replacement(all_easy, 4)) +\
             list(itertools.combinations_with_replacement(all_standard, 4)) +\
             list(itertools.combinations_with_replacement(all_moderate, 4)) +\
             list(itertools.combinations_with_replacement(all_hard, 4)) +\
             list(itertools.combinations_with_replacement(all_hardest, 4))

all_team2 += list(itertools.combinations_with_replacement(all_easy, 5)) +\
             list(itertools.combinations_with_replacement(all_standard, 5)) +\
             list(itertools.combinations_with_replacement(all_moderate, 5)) +\
             list(itertools.combinations_with_replacement(all_hard, 5)) +\
             list(itertools.combinations_with_replacement(all_hardest, 5))

all_team2 += list(itertools.combinations_with_replacement(all_easy, 6)) +\
             list(itertools.combinations_with_replacement(all_standard, 6)) +\
             list(itertools.combinations_with_replacement(all_moderate, 6)) +\
             list(itertools.combinations_with_replacement(all_hard, 6)) +\
             list(itertools.combinations_with_replacement(all_hardest, 6))


winchances = []
for s_team2 in all_team2:
    iter_teamkeys = []
    iter_team2 = []

    if isinstance(s_team2[0], str):
        iter_teamkeys.append((s_team2[0],s_team2[1]))
        iter_team2= [AI[s_team2[0]][s_team2[1]]]
    else:
        for player in s_team2:
            iter_team2.append( AI[player[0]][player[1]] )
            iter_teamkeys.append(player)

    winchances.append( (iter_teamkeys, win_probability(team1, iter_team2)) )



#winchances = []
#for v in [AI.CD, AI.HD, AI.Res]:
#    for d in [v.easy, v.standard, v.moderate, v.hard, v.hardest]:
#        team2 = [d]
#        winchance = win_probability(team1, team2)
#        winchances.append((v, d, winchance))
#
winchances = sorted(winchances, key=lambda x: x[1])

for game in winchances:

    for player_i in range(len(game[0])-1):
        print(game[0][player_i][0], game[0][player_i][1])

    print(game[0][-1][0], game[0][-1][1], "\t", str(round(game[1], 2)) + "%")


    #if len(game[0]) == 1:
    #    print(game[0][0][0], game[0][0][1], "\t", str(round(game[1],2))+"%")
    #elif len(game[0]) == 2:
    #    print(game[0][0][0], game[0][0][1])
    #    print(game[0][1][0], game[0][1][1], "\t", str(round(game[1],2))+"%")
    #elif len(game[0]) == 3:
    #    print(game[0][0][0], game[0][0][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][2][0], game[0][2][1], "\t", str(round(game[1],2))+"%")
    #elif len(game[0]) == 4:
    #    print(game[0][0][0], game[0][0][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][2][0], game[0][2][1], "\t", str(round(game[1],2))+"%")
    #elif len(game[0]) == 5:
    #    print(game[0][0][0], game[0][0][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][2][0], game[0][2][1], "\t", str(round(game[1],2))+"%")
    #elif len(game[0]) == 6:
    #    print(game[0][0][0], game[0][0][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][1][0], game[0][1][1])
    #    print(game[0][2][0], game[0][2][1], "\t", str(round(game[1],2))+"%")


#winchances = []
#for v1 in [AI.CD, AI.HD, AI.Res]:
#    for d1 in [v.easy, v.standard, v.moderate, v.hard, v.hardest]:
#        for v2 in [AI.CD, AI.HD, AI.Res]:
#            for d2 in [v.easy, v.standard, v.moderate, v.hard, v.hardest]:
#                team2 = [d1, d2]
#                winchance = win_probability(team1, team2)
#                winchances.append(((v1, d1),
#                                   (v2, d2),
#                                   winchance))
#
#print("")
#winchances = sorted(winchances, key=lambda x: x[2])
#
#for game in winchances:
#    print(game[0][0],game[0][1].name, round(game[0][1].mu,1))
#    print(game[1][0],game[1][1].name, round(game[1][1].mu,1), "\t", str(round(game[2],2))+"%")
#
#
'''
    print("AI." + v.name + ".easy", sub_print_rating(v.easy))
    print("drawchance:",round(trueskill.quality([team1, team2]),2))
    print("winchance:",round(win_probability(team1, team2),2))

team2 = [AI.CD.hardest,AI.CD.hardest]
print("CD Hardest,CD Hardest")
print("drawchance:",round(trueskill.quality([team1, team2]),2))
print("winchance:",round(win_probability(team1, team2),2))
print("")
'''