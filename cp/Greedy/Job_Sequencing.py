'''
You're given n jobs.
Each job has: id, deadline, profit
Each job takes 1 unit time
Goal: maximize total profit
You can do only one job at a time
'''

# Job Sequencing with Deadlines
def job_sequencing_deadline(jobs):
    # jobs: list of (id, deadline, profit)

    # sort jobs by profit in desc order
    # always try to take highest profit job first
    jobs.sort(key=lambda x:x[2], reverse=True)

    # find max deadline
    # to determine how many time slots we need
    max_deadline = max(job[1] for job in jobs)

    # track of occupied time slots
    # idx 0 is unused (1-based indexing for simplicity)
    # -1 means slot is free
    slots = [-1]*(max_deadline + 1)

    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job

        # schedule job in the latest possible free slot
        # go backwards from its deadline
        for t in range(deadline, 0, -1):
            
            # if slot free, assign this job
            if slots[t] == -1:
                slots[t] = job_id # mark occupied
                total_profit += profit
                break # move to next job

    # total profit, scheduled jobs (excluding idx 0)
    return total_profit, slots[1:]


jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

print(job_sequencing_deadline(jobs))
