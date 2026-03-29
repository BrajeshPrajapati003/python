'''
You're given n jobs.
Each job has: id, deadline, profit
Each job takes 1 unit time
Goal: maximize total profit
You can do only one job at a time
'''
# for each job -> scan backwards to find free slot
# complexity: O(n*d) (d = max deadline)
# Worst case: O(n²)

# Optimized Approach: DSU (instead of scanning, we jump directly to next free slot)

def job_sequencing_dsu(jobs):
    # jobs = [(id, deadline, profit)]

    # step 1: sort by profit (desc)
    jobs.sort(key=lambda x:x[2], reverse=True)

    # step 2: find max deadline
    max_deadline = max(job[1] for job in jobs)

    # step 3: initialize DSU
    parent = list(range(max_deadline+1))

    # find with path compression
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    # union: mark slot as used
    def union(u, v):
        parent[u] = v

    total_profit = 0
    res = [-1]*(max_deadline+1)

    # step 4: process jobs
    for id, deadline, profit in jobs:

        # find available slot
        available_slot = find(deadline)

        if available_slot > 0:
            # assign job
            res[available_slot] = id
            total_profit += profit

            # mark slot as filled -> link to previous slot
            union(available_slot, available_slot-1)

    return total_profit, res[1:]

jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

print(job_sequencing_dsu(jobs)) # (142, ['C', 'A', 'E'])
