'''
LC 2140. Solving Questions with Brainpower
You are given a 2D array questions, where each question contains:
    points: Points earned by solving the question.
    brainpower: Number of subsequent questions you must skip after solving it.

For every question, you have two choices:
    1. Solve: Earn its points, but skip the next brainpower questions.
    2. Skip: Move to the next question without earning any points.

Find the maximum points you can earn.
'''

def mostPoints(questions) -> int:
    # return mostPointsForwardRecursion(questions, 0)

    # dp = [-1]*len(questions)
    # return mostPointsMemo(questions, dp, 0)
    return mostPointsTabulation(questions)

def mostPointsForwardRecursion(q, idx):
    if idx > len(q):
        return 0
    
    pick = q[idx][0] + mostPointsForwardRecursion(q, idx+q[idx][1]+1)
    
    skip = mostPointsForwardRecursion(q, idx+1)

    return max(pick, skip)

def mostPointsMemo(q, dp, idx):
    n = len(q)
    if idx >= n:
        return 0
    
    if dp[idx] != -1:
        return dp[idx]

    pick = q[idx][0] + mostPointsMemo(q, dp, idx+q[idx][1]+1)
    skip = mostPointsMemo(q, dp, idx+1)

    dp[idx] = max(pick, skip)

    return dp[idx]

def mostPointsTabulation(q):
    n = len(q)
    if n == 1:
        return q[0][0]
    
    dp = [0]*(n+1)
    for i in range(n-1, -1, -1):

        next_idx = i+q[i][1]+1
        take = q[i][0]
        if next_idx < n:
            take += dp[next_idx]
        skip = dp[i+1]

        dp[i] = max(take, skip)
    return dp[0]


# dp[i] depends on a potentially distant future state.
# Unlike Frog Jump or House Robber, where we only needed the previous one or two states,
# here we may need many different future states.
# So, constant-space optimization using the usual DP recurrence isn't straightforward.


'''
BACKWARD RECURSION:
-----------------------------
we face a problem:
If we solve question i, we must ensure that no previously solved question conflicts with it.

A previously solved question j conflicts with i if (j + brainpower[j] >= i).

This depends on the brainpower of previously selected questions, not just the current question's brainpower.

Therefore, knowing only i is insufficient to determine a simple take/skip transition.
-------------------------------

FORWARD RECURSION:
-------------------------------
Now the choices are straightforward:
    1. Take: Earn points[i] and jump to i + brainpower[i] + 1.
    2. Skip: Move to i + 1.
-------------------------------

Backward recursion is not inherently impossible, but it requires tracking additional information about previously selected questions. Forward recursion gives us a clean state with just one parameter (i), making memoization and tabulation straightforward.
'''
