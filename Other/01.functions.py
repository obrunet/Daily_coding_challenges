"""
reimplementation of basic maths function on lists
such as max, mean_val, the result is checked with list methods
"""
from statistics import mean
lst_a = [1, 2, 0, 10, 6, 0]


def lst_mean(lst):
    """Returns the mean_val of a list of integers"""
    mean_val = 0
    for i, val in enumerate(lst):
        mean_val += val
    return mean_val / (i+1)


def lst_max(lst):
    """Returns the max of a list of integers"""
    max_val = 0
    for i in lst:
        if i > max_val: max_val = i
    return max_val
    

def main():
    print(f"Mean of list {lst_a}: {lst_mean(lst_a):.2f}, check: {round(mean(lst_a), 2)}")
    print(f"Max of list  {lst_a}: {lst_max(lst_a):.2f},  check: {round(max(lst_a), 2)}")


if __name__ == '__main__':
    main()