"""
https://exercism.io/tracks/python/exercises/high-scores/solutions/7f661469ef3c49a391bbf1e4a44a4dd6

Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, one of the highest selling and
addictive games of all time, and a classic of the arcade era. Your task is to write methods that return
the highest score from the list, the last added score and the three highest scores.
"""

all_scores = [1, 2, 10, 4, 9, 6, 7]
 

def best_score(scores):
    """ Return the max/best score of a list"""
    return max(scores)


def last_score(scores):
    """Return the last score of a list"""
    return scores[-1]
 

def best_three_scores(scores):
    """Return the best three scores of a list"""
    return sorted(scores)[-3:]


def worst_three_scores(scores):
    """Return the worst three scores of a list"""
    return sorted(scores)[:3]

 
def main():
    print(f"""
        Best score: {best_score(all_scores)}
        Last score: {last_score(all_scores)}
        Best three scores: {best_three_scores(all_scores)}
        Worst three scores: {worst_three_scores(all_scores)}""")
 

if __name__ == "__main__":
    main()

