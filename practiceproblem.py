str = "(((abc))((d)))))"
solution = ["*"] * len(str)
# print solution

stack = []
itr = 0

for element in str:
    print "itr = ", itr
    print "stack = ", stack
    print "solution = ", solution
    if element == "(":
        solution[itr] = "-1"
        stack.append(itr)
    elif element == ")":


        if len(stack) > 0:
            solution[itr] = "1"
            stackelement = stack.pop()
            solution[stackelement] = "0"
        else:
            solution[itr] = "-1"
    else:
        solution[itr] = element
    itr += 1



print "solution = ", "".join(solution)
