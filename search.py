#ahuva avihay
#search
import state
import frontier

def search(n):
    s=state.create(n)
    print(s)
    f=frontier.create(s)

#Answer to question 3:
#The problem was that in a loop that goes through all the members of the current state,
#If one of the boys is a target state, it immediately retrieves it and returns it as a solution.
#But he doesn't check if there might be a more efficient solution.
#(meaning there may be another son that the loop hasn't reached yet)
#To solve the problem, we eliminated the condition that checks for each child if it can be a target state,
#And now all the boys enter the priority queue and in the next iteration of the loop the most efficient state will be chosen,
#And there's already a check to see if it's a target state
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return s
        ns=state.get_next(s)
        for i in ns:
 #           if state.is_target(i):
 #               return i
            frontier.insert(f,i)
    return 0

print(search([1,2,5,10]))