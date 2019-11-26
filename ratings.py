
import trueskill

# AI are sorted by difficulty because you cannot select difficulty per AI, only per match.
# e.i AI_CD_hard will never be able to play against AI_res_easy

AI = {"CD":{"easy":trueskill.Rating(),
            "standard":trueskill.Rating(),
            "moderate":trueskill.Rating(),
            "hard":trueskill.Rating(),
            "hardest":trueskill.Rating()},

      "HD":{"easy":trueskill.Rating(),
            "standard":trueskill.Rating(),
            "moderate":trueskill.Rating(),
            "hard":trueskill.Rating(),
            "hardest":trueskill.Rating()},

      "Res":{"easy":trueskill.Rating(),
            "standard":trueskill.Rating(),
            "moderate":trueskill.Rating(),
            "hard":trueskill.Rating(),
            "hardest":trueskill.Rating()}
      }

AI_CD_easy = trueskill.Rating()
AI_HD_easy = trueskill.Rating()
AI_Res_easy = trueskill.Rating()

AI_CD_standard = trueskill.Rating()
AI_HD_standard = trueskill.Rating()
AI_Res_standard = trueskill.Rating()

AI_CD_moderate = trueskill.Rating()
AI_HD_moderate = trueskill.Rating()
AI_Res_moderate = trueskill.Rating()

AI_CD_hard = trueskill.Rating()
AI_HD_hard = trueskill.Rating()
AI_Res_hard = trueskill.Rating()

AI_CD_hardest = trueskill.Rating()
AI_HD_hardest = trueskill.Rating()
AI_Res_hardest = trueskill.Rating()


P1 = trueskill.Rating()
P2 = trueskill.Rating()


def run_matches(loser, winner):
    for dummy in range(4):
        (winner,),(loser,) = trueskill.rate( [(winner,), (loser,)], ranks=[0,1])
    return loser, winner

def self_compare(easy, standard, moderate, hard, hardest):
    easy,standard = run_matches(easy, standard)
    standard,moderate = run_matches(standard, moderate)
    moderate,hard = run_matches(moderate, hard)
    hard,hardest = run_matches(hard, hardest)
    return easy, standard, moderate, hard, hardest


# AI CD
AI_CD_easy,AI_CD_standard ,AI_CD_moderate ,AI_CD_hard ,AI_CD_hardest = self_compare(AI_CD_easy,
                                                                                    AI_CD_standard,
                                                                                    AI_CD_moderate,
                                                                                    AI_CD_hard,
                                                                                    AI_CD_hardest)

# AI HD
AI_HD_easy,AI_HD_standard ,AI_HD_moderate ,AI_HD_hard ,AI_HD_hardest = self_compare(AI_HD_easy,
                                                                                    AI_HD_standard,
                                                                                    AI_HD_moderate,
                                                                                    AI_HD_hard,
                                                                                    AI_HD_hardest)

# AI Res
AI_Res_easy,AI_Res_standard ,AI_Res_moderate ,AI_Res_hard ,AI_Res_hardest = self_compare(AI_Res_easy,
                                                                                         AI_Res_standard,
                                                                                         AI_Res_moderate,
                                                                                         AI_Res_hard,
                                                                                         AI_Res_hardest)

# Easy difficulty
AI_CD_easy, AI_HD_easy = run_matches(AI_CD_easy, AI_HD_easy)
AI_CD_easy, AI_Res_easy = run_matches(AI_CD_easy, AI_Res_easy)
AI_HD_easy, AI_Res_easy = run_matches(AI_HD_easy, AI_Res_easy)


# Standard
AI_CD_standard,AI_HD_standard = run_matches(AI_CD_standard, AI_HD_standard)
AI_CD_standard,AI_Res_standard = run_matches(AI_CD_standard, AI_Res_standard)
AI_HD_standard,AI_Res_standard = run_matches(AI_HD_standard, AI_Res_standard)


# Moderate
AI_CD_moderate,AI_HD_moderate = run_matches(AI_CD_moderate, AI_HD_moderate)
AI_CD_moderate,AI_Res_moderate = run_matches(AI_CD_moderate, AI_Res_moderate)
AI_HD_moderate,AI_Res_moderate = run_matches(AI_HD_moderate, AI_Res_moderate)


# Hard
AI_CD_hard,AI_HD_hard = run_matches(AI_CD_hard, AI_HD_hard)
AI_CD_hard,AI_Res_hard = run_matches(AI_CD_hard, AI_Res_hard)
AI_HD_hard,AI_Res_hard = run_matches(AI_HD_hard, AI_Res_hard)


# Hardest
AI_CD_hardest,AI_HD_hardest = run_matches(AI_CD_hardest, AI_HD_hardest)
AI_CD_hardest,AI_Res_hardest = run_matches(AI_CD_hardest, AI_Res_hardest)
AI_HD_hardest,AI_Res_hardest = run_matches(AI_HD_hardest, AI_Res_hardest)