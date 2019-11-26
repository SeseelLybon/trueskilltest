from trueskill import *

from ratings import *



print("AI_CD_easy",AI_CD_easy)
print("AI_HD_easy",AI_HD_easy)
print("AI_res_easy",AI_Res_easy)
print("")
print("AI_CD_standard",AI_CD_standard)
print("AI_HD_standard",AI_HD_standard)
print("AI_res_standard",AI_Res_standard)
print("")
print("AI_CD_moderate",AI_CD_moderate)
print("AI_HD_moderate",AI_HD_moderate)
print("AI_res_moderate",AI_Res_moderate)
print("")
print("AI_CD_hard",AI_CD_hard)
print("AI_HD_hard",AI_HD_hard)
print("AI_res_hard",AI_Res_hard)
print("")
print("AI_CD_hardest",AI_CD_hardest)
print("AI_HD_hardest",AI_HD_hardest)
print("AI_res_hardest",AI_Res_hardest)



# 2v2v2
# 2v2
# 2v1
# 2v1
# 2v1
# 2v1




team1 = [P1, P2]


team2 = [AI_HD_easy, AI_HD_easy, AI_HD_easy, AI_HD_easy]

(P1, P2), (AI_HD_easy, AI_HD_easy, AI_HD_easy, AI_HD_easy) = trueskill.rate( [team1, team2], ranks=[1,0] )



#match on ice oasis
team2 = [AI_res_easy, AI_res_easy]

(P1, P2), (res_easy_1, res_easy_2) = trueskill.rate( [team1, team2], ranks=[0,1] )

#match on islands
team2 = [res_stan_1]

(P1, P2), (res_stan_1,) = trueskill.rate( [team1, [res_stan_1]], ranks=[1,0] )



#Water border on my side, ai = chineese
team2 = [res_stan_1]

(P1, P2), (res_stan_1,) = trueskill.rate( [team1, team2], ranks=[1,0] )

# 
team2 = [res_stan_1]

(P1, P2), (res_stan_1,) = trueskill.rate( [team1, team2], ranks=[1,0] )

# 
team2 = [res_stan_1]

(P1, P2), (res_stan_1,) = trueskill.rate( [team1, team2], ranks=[1,0] )


print("post match 4")
print("P1\t", P1)
print("P2\t", P2)

'''