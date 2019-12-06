
import trueskill


# AI are sorted by difficulty because you cannot select difficulty per AI, only per match.
# e.i AI.CD.hard will never be able to play against AI.Res.easy


TS_env = trueskill.setup()



class difficulty: #difficulty
    def __init__(self,name=None):
        self.name = name
        self.easy = trueskill.Rating()
        self.standard = trueskill.Rating()
        self.moderate = trueskill.Rating()
        self.hard = trueskill.Rating()
        self.hardest = trueskill.Rating()

    def __repr__(self):
        return self.name

    def __iter__(self):
        pass
        
class AIc:
    CD = difficulty("CD ")
    HD = difficulty("HD ")
    Res = difficulty("Res")

AI = AIc()


AI_dict = {"CD":{"easy"     :AI.CD.easy,
                 "standard" :AI.CD.standard,
                 "moderate" :AI.CD.moderate,
                 "hard"     :AI.CD.hard,
                 "hardest"  :AI.CD.hardest},
           "HD":{"easy"     :AI.HD.easy,
                 "standard" :AI.HD.standard,
                 "moderate" :AI.HD.moderate,
                 "hard"     :AI.HD.hard,
                 "hardest"  :AI.HD.hardest},
           "Res":{"easy"    :AI.Res.easy,
                 "standard" :AI.Res.standard,
                 "moderate" :AI.Res.moderate,
                 "hard"     :AI.Res.hard,
                 "hardest"  :AI.Res.hardest}
           }


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

def sub_print_rating( rating:trueskill.Rating )->tuple:
    return round(rating.mu,1), round(rating.sigma,1)

def apply_names_to_ratings():
    for v in [AI.CD, AI.HD, AI.Res]:
        v.easy.name = "easy\t\t"
        v.standard.name = "standard\t"
        v.moderate.name = "moderate\t"
        v.hard.name = "hard\t\t"
        v.hardest.name = "hardest\t\t"

    for v in [AI_dict["CD"], AI_dict["HD"], AI_dict["Res"]]:
        v["easy"].name = "easy\t\t"
        v["standard"].name = "standard\t"
        v["moderate"].name = "moderate\t"
        v["hard"].name = "hard\t\t"
        v["hardest"].name = "hardest\t\t"

def apply_names_to_rating( rating ):
    for v in [rating.CD, rating.HD, rating.Res]:
        v.easy.name = "easy\t\t"
        v.standard.name = "standard\t"
        v.moderate.name = "moderate\t"
        v.hard.name = "hard\t\t"
        v.hardest.name = "hardest\t\t"

def print_ai_ratings():
    apply_names_to_rating()

    for v in [AI.CD, AI.HD, AI.Res]:
        for d in [v.easy, v.standard, v.moderate, v.standard,v.hard, v.hardest]:
            print(v.name, d.name, sub_print_rating(d))


# Make list to sort by mu
def print_ai_sorted_mu():
    ratings = []
    for v in [AI.CD, AI.HD, AI.Res]:
        for d in [v.easy, v.standard, v.moderate, v.hard, v.hardest]:
            ratings.append((v, d))

    ratings = sorted(ratings, key=lambda x: x[1].mu)

    print("")

    for v, d in ratings:
        print(v.name, d.name, sub_print_rating(d))


# AI CD
AI.CD.standard,AI.CD.standard ,AI.CD.moderate ,AI.CD.hard ,AI.CD.hardest = self_compare(AI.CD.easy,
                                                                                        AI.CD.standard,
                                                                                        AI.CD.moderate,
                                                                                        AI.CD.hard,
                                                                                        AI.CD.hardest)

# AI HD
AI.HD.easy,AI.HD.standard ,AI.HD.moderate ,AI.HD.hard ,AI.HD.hardest = self_compare(AI.HD.easy,
                                                                                    AI.HD.standard,
                                                                                    AI.HD.moderate,
                                                                                    AI.HD.hard,
                                                                                    AI.HD.hardest)

# AI Res
AI.Res.easy,AI.Res.standard ,AI.Res.moderate ,AI.Res.hard ,AI.Res.hardest = self_compare(AI.Res.easy,
                                                                                         AI.Res.standard,
                                                                                         AI.Res.moderate,
                                                                                         AI.Res.hard,
                                                                                         AI.Res.hardest)

# Easy difficulty
AI.CD.easy, AI.HD.easy = run_matches(AI.CD.easy, AI.HD.easy)
AI.CD.easy, AI.Res.easy = run_matches(AI.CD.easy, AI.Res.easy)
AI.HD.easy, AI.Res.easy = run_matches(AI.HD.easy, AI.Res.easy)


# Standard
AI.CD.standard,AI.HD.standard = run_matches(AI.CD.standard, AI.HD.standard)
AI.CD.standard,AI.Res.standard = run_matches(AI.CD.standard, AI.Res.standard)
AI.HD.standard,AI.Res.standard = run_matches(AI.HD.standard, AI.Res.standard)


# Moderate
AI.CD.moderate,AI.HD.moderate = run_matches(AI.CD.moderate, AI.HD.moderate)
AI.CD.moderate,AI.Res.moderate = run_matches(AI.CD.moderate, AI.Res.moderate)
AI.HD.moderate,AI.Res.moderate = run_matches(AI.HD.moderate, AI.Res.moderate)


# Hard
AI.CD.hard,AI.HD.hard = run_matches(AI.CD.hard, AI.HD.hard)
AI.CD.hard,AI.Res.hard = run_matches(AI.CD.hard, AI.Res.hard)
AI.HD.hard,AI.Res.hard = run_matches(AI.HD.hard, AI.Res.hard)


# Hardest
AI.CD.hardest,AI.HD.hardest = run_matches(AI.CD.hardest, AI.HD.hardest)
AI.CD.hardest,AI.Res.hardest = run_matches(AI.CD.hardest, AI.Res.hardest)
AI.HD.hardest,AI.Res.hardest = run_matches(AI.HD.hardest, AI.Res.hardest)






import itertools
import math


#Code of this function from snippet from Trueskill.org
def win_probability(team1, team2, BETA=TS_env.beta):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in itertools.chain(team1, team2))
    size = len(team1) + len(team2)
    denom = math.sqrt(size * (BETA * BETA) + sum_sigma)
    ts = trueskill.global_env()
    return ts.cdf(delta_mu / denom)





if __name__ == '__main__':
    print_ai_ratings()