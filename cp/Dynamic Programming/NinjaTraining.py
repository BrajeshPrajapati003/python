'''
A ninja trains for N days. Each day, he can perform one of three activities:
- Running
- Fighting
- Learning new martial arts
Each activity gives a certain number of merit points per day.
Constraint: He cannot perform the same activity on two consecutive days.
Find the maximum merit points he can earn over N days.
'''

def ninjaTraining(points):
    # return ninjaTrainingForwardRecursion(points, -1, 0)

    # dp = [[-1]*4 for _ in range(len(points)+1)]
    # return ninjaTrainingForwardMemoization(points, -1, 0, dp)

    # return ninjaTrainingForwardTabulation(points)
    return ninjaTrainingBackwardTabulation(points)
    # return ninjaTrainingConstantSpace(points)


def ninjaTrainingForwardRecursion(points, last, d):

    # All training days have been completed
    if d == len(points):
        return 0

    maxPoints = float('-inf')

    # Try all three activities for the current day
    for j in range(3):
        if last != j:

            # Points earned today + max points obtainable from next day
            curr = points[d][j] + ninjaTrainingForwardRecursion(points, j, d+1)
            maxPoints = max(maxPoints, curr)

    return maxPoints


def ninjaTrainingForwardMemoization(points, last, d, dp):

    # No days remaining
    if d == len(points):
        return 0

    # Check whether this particular state was calculated.
    # last+1 converts the previous activity into a valid DP column index.
    if dp[d][last+1] != -1:
        return dp[d][last+1]

    maxPoints = float('-inf')

    for j in range(3):
        if last != j:
            curr = points[d][j] + ninjaTrainingForwardMemoization(points, j, d+1, dp)
            maxPoints = max(curr, maxPoints)

    # Store the maximum points for state (d, last)
    dp[d][last+1] = maxPoints
    return dp[d][last+1]

def ninjaTrainingForwardTabulation(points):
    n = len(points)

    # Rows:
    # 0 to n-1 -> Actual training days.
    # n -> Base case (all days completed).

    # Columns:
    # 0 -> No previous activity (last = -1).
    # 1 -> Previous activity = 0.
    # 2 -> Previous activity = 1.
    # 3 -> Previous activity = 2.

    dp = [[0]*4 for _ in range(n+1)]

    # Process days backwards because the transition
    # depends on dp[d+1].
    for d in range(n-1, -1, -1):

        # Consider every possible previous activity.
        for last in range(-1, 3):

            maxPoints = float('-inf')

            # Try all three activities for the current day.
            for j in range(3):
                if last != j:

                    # Current activity's points + best result from the next day
                    # j+1 shifts the selected activity into its corresponding DP column.
                    curr = points[d][j] + dp[d+1][j+1]
                    maxPoints = max(maxPoints, curr)

            # Store the answer for state (d, last).
            dp[d][last+1] = maxPoints

    # Start at Day 0 with no previous activity.
    return dp[0][0]

def ninjaTrainingBackwardTabulation(points):
    n = len(points)

    # Extra row for the base case (no days remaining)
    # Columns represent last = -1, 0, 1, 2.
    dp = [[0]*4 for _ in range(n+1)]

    # Start from the 1st day and build towards the last day
    for d in range(n):
        for last in range(-1, 3):
            maxPoints = float('-inf')

            for j in range(3):
                if j != last:
                    # try next activities on the same day
                    curr = points[d][j] + dp[d][j+1]
                    maxPoints = max(maxPoints, curr)

            dp[d+1][last+1] = maxPoints
    
    return dp[n][0]

# def ninjaTrainingConstantSpace(points):


days = 3 
points = list(list(map(int, input().split())) for _ in range(days))
print(ninjaTraining(points))

'''
===========================================================
1. RECURSIVE STATE
===========================================================

We define: f(d, last)
    d    -> Current day we are processing.
    last -> Activity performed on the previous day.

IMPORTANT:
'last' represents the previous day's activity, NOT the
activity we are currently selecting.

We use -1 for 'last' initially because no activity has
been performed before Day 0.

===========================================================
2. RECURSION TRANSITION [O(3^n)]
===========================================================

For the current day, try all three activities.

We cannot select activity j if:
    j == last

If activity j is selected:
    Current points = points[d][j]
    Remaining problem = f(d+1, j)

Why do we pass j?
Because activity j is now the activity performed on the
previous day from the perspective of the next day.

Therefore:
    f(d, last) = max(points[d][j] + f(d+1, j))
        for every j != last

===========================================================
3. BASE CASE
===========================================================

    if d == n:
        return 0
When d == n, all training days are completed.
No more points can be earned, so return 0.

===========================================================
4. MEMOIZATION / DP STATE [O(4n states * 3 choices] = O(12n) = O(n)
===========================================================

Our recursive state depends on TWO variables:
    d    -> Current day
    last -> Previous activity

Therefore, we need a 2D DP array.

    dp[d][last+1]

Why last+1?
The possible values of last are:
    -1, 0, 1, 2

But we want valid array column indices:
    0, 1, 2, 3

So we shift last by 1.
    last = -1  -> column 0
    last =  0  -> column 1
    last =  1  -> column 2
    last =  2  -> column 3

The extra column represents the initial state where
no previous activity exists.

We allocate:
    dp = [[-1]*4 for _ in range(n+1)]

Why n+1 rows?
Days range from 0 to n-1.

We allocate one additional row for the base case:
    d == n

That row contains zeros because all days are completed.

===========================================================
5. TABULATION
===========================================================

Our recurrence depends on: dp[d+1][j+1]

This means the current day's answer depends on the next
day's already calculated answer.

Therefore, we process days BACKWARDS:
    n-1, n-2, ..., 1, 0

For every day:
    1. Try every possible previous activity (last).
    2. Try every activity we can perform today (j).
    3. Skip j if j == last.
    4. Calculate today's points + next day's DP result.
    5. Store the maximum in dp[d][last+1].

Final answer: dp[0][0]

Why?
We start at Day 0 and initially have no previous activity.

Therefore:
    d = 0
    last = -1
    last + 1 = 0

Forward Approach:
    - Recursion starts at day 0 & moves towards n-1
    - Tabulation fills from day n-1 towards day 0

Backward Approach:
    - Recursion starts at day n-1 & moves towards day 0
    - Tabulation fills from day 0 towards day n-1

DP complexity:
    Time = No. of states * Work per state

'''
