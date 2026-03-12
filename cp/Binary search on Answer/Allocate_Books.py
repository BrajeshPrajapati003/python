'''
Given books[] where each value is the number of pages in a book & k students.
Books must be assigned contiguously.
Minimize the maximum pages assigned to any student.
'''
def allocate_books(books, k):
    # impossible if students exceeded books
    if k > len(books):
        return -1

    low, high = max(books), sum(books)
    ans = high

    while low <= high:
        mid = (low+high)//2
        if can_allocate(books, k, mid):
            ans = mid # feasible allocation
            high = mid-1 # try reducing pages
        else:
            low = mid+1

    return ans

def can_allocate(books, k, max_pages):
    students = 1 # first student
    pages = 0 # pages assigned so far

    for b in books:
        pages += b

        # if current student exceeds allowed pages
        if pages > max_pages:
            students += 1
            pages = b # assign book to next student

        # if students exceed limit allocation impossible
        if students > k:
            return False

    return True