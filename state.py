#ahuva avihay
import copy


# l is a list of the crossing times. the init. state is a list of crossing times
# + 0 for the flashlight (all initially on the left side),
# and empty list=pers on the right and another empty list=moves so far.
def create(l):
    return [l + [0], [], []]


# Returns a list of states one cross away from state x (the children of x)
# Answer to question 1:
def get_next(x):
    ns = []
    if 0 in x[0]:  # if the light is in the first side of the river
        for index,a in enumerate(x[0][:-1]):
            for b in x[0][index+1:-1]:
                tmpOFx2 = x[2].copy()
                tmpOFx2.append([a, b])
                temp = [[i for i in x[0] if i not in [a, b, 0]], x[1] + [a, b, 0], tmpOFx2]
                ns.append(temp)

    else:  # if the light is in the second side of the river
        for b in x[1]:
            if (b != 0):
                tmpOFx2 = x[2].copy()
                tmpOFx2.append([b])
                temp = [x[0] + [b, 0], [i for i in x[1] if i not in [b, 0]], tmpOFx2]
                ns.append(temp)
    return ns


# Gets x (a state) and returns the length of the path to that state.
def path_len(x):
    pl = 0  # pl sums the path length
    for i in x[2]:  # for all the moves:
        pl += max(i)  # sum into pl the max. crossing time of the 1 or 2 pers. crossing
    return pl


# returns True iff state x is the target.
# x is the target iff no one is on the left side.
def is_target(x):
    return x[0] == []


# Answer to question 2:
# The heuristic is acceptable because it supposedly creates couples who cross the river together,
# When the slowest of the two couples is the next couple in pace and so on. Then he sums up the times of the highest of each pair.
# The result is always low or equal to true, because that way you get the minimum time for the group of people to pass
# (When combining people with transition times as close as possible - this is most effective). There is no faster way.
# And this is also a logical method because it is indeed a possible way to cross the river according to the rules.
# Conclusion: the heuristic is acceptable

def hdistance(s):  # The heuristic sums up all the members (crossing times) in the list of people who could not have crossed the river, in skips of 2
    if s[0] == []:
        return 0  # the heuristic value of s
    h = 0
    x = sorted(s[0])
    if x[0] == 0:
        x = x[1:]
    for i in range(len(x) - 1, -1, -2):
        h += x[i]
    return h
