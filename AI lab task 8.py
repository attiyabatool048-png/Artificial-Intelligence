import math [cite: 15]

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth): [cite: 16]
    # base case: targetDepth reached
    if (curDepth == targetDepth): [cite: 17]
        return scores[nodeIndex] [cite: 18]
    
    if (maxTurn): [cite: 19]
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)) [cite: 20]
    
    else: [cite: 21]
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth), 
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)) [cite: 22, 24]

# Driver code [cite: 23]
# The leaf nodes are represented by the scores array
scores = [3, 5, 2, 9, 3, 5, 2, 9] [cite: 25]
treeDepth = math.log(len(scores), 2) [cite: 26]

print("The optimal value is: ", end = "") [cite: 27]
print(minimax(0, 0, True, scores, treeDepth)) [cite: 28]