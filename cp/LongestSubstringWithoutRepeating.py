# length of longest substring without repeating chars
def longest_substring(s: str) -> int:
    l = maxLen = 0
    st = set()
    for r in range(len(s)):
        while s[r] in st:
            st.remove(s[l])
            l += 1
        st.add(s[r])
        maxLen = max(r-l+1, maxLen)

    return maxLen
