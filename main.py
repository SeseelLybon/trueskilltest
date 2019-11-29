from trueskill import *

from ratings import *




print_ai_ratings()

# 2v2v2
# 2v2
# 2v1
# 2v1
# 2v1
# 2v1




team1 = [P1, P2]


team2 = [AI_HD_easy, AI_HD_easy, AI_HD_easy, AI_HD_easy]

(P1, P2), (AI_HD_easy, x, y, z) = trueskill.rate( [team1, team2], ranks=[0, 1] )



#match on ice oasis
team2 = [AI_Res_easy, AI_Res_easy]

(P1, P2), (AI_CD_easy, dummy) = trueskill.rate([team1, team2], ranks=[1, 0])

#match on islands
team2 = [AI_Res_standard]

(P1, P2), [AI_Res_standard] = trueskill.rate( [team1, team2], ranks=[0, 1] )



#Water border on my side, ai = chineese
team2 = [AI_Res_standard]

(P1, P2), [AI_Res_standard] = trueskill.rate( [team1, team2], ranks=[0, 1] )

# 
team2 = [AI_Res_standard]

(P1, P2), [AI_Res_standard] = trueskill.rate( [team1, team2], ranks=[0, 1] )

# 
team2 = [AI_Res_standard]

(P1, P2), [AI_Res_standard] = trueskill.rate( [team1, team2], ranks=[0, 1] )


print("post match 4")
print_ai_ratings()
print()
print("P1\t", sub_print_rating(P1))
print("P2\t", sub_print_rating(P2))