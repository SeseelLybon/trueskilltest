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
team2 = [AI.HD.easy, AI.HD.easy, AI.HD.easy, AI.HD.easy]

(P1, P2), (AI.HD.easy, x, y, z) = trueskill.rate( [team1, team2], ranks=[0, 1] )



#match on ice oasis
team1 = [P1, P2]
team2 = [AI.Res.easy, AI.Res.easy]

(P1, P2), (AI.Res.easy, dummy) = trueskill.rate([team1, team2], ranks=[1, 0])

#match on islands
team1 = [P1, P2]
team2 = [AI.Res.standard]

(P1, P2), [AI.Res.standard] = trueskill.rate( [team1, team2], ranks=[0, 1] )

#Water border on my side, ai = chineese
team1 = [P1, P2]
team2 = [AI.Res.standard]

(P1, P2), [AI.Res.standard] = trueskill.rate( [team1, team2], ranks=[0, 1] )

#
team1 = [P1, P2]
team2 = [AI.Res.standard]

(P1, P2), [AI.Res.standard] = trueskill.rate( [team1, team2], ranks=[0, 1] )

#
team1 = [P1, P2]
team2 = [AI.Res.standard]

(P1, P2), [AI.Res.standard] = trueskill.rate( [team1, team2], ranks=[0, 1] )


print("post match 4")
print_ai_ratings()
print()
print("P1\t", sub_print_rating(P1))
print("P2\t", sub_print_rating(P2))

print("")
team1 = [P1, P2]




print("")

# Make list to sort by mu
ratings = []
for v in [AI.CD, AI.HD, AI.Res]:
    for d in [v.easy,v.standard,v.moderate,v.hard,v.hardest]:
        ratings.append()

print(ratings)
sorted(ratings, key=lambda x: x.mu)



'''
    print("AI." + v.version + ".easy", sub_print_rating(v.easy))
    print("drawchance:",round(trueskill.quality([team1, team2]),2))
    print("winchance:",round(win_probability(team1, team2),2))

team2 = [AI.CD.hardest,AI.CD.hardest]
print("CD Hardest,CD Hardest")
print("drawchance:",round(trueskill.quality([team1, team2]),2))
print("winchance:",round(win_probability(team1, team2),2))
print("")
'''