# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Problem     Find a string
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-18, 11:24 p.m.
# ──────────────────────────────────────────────────

def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)
    #traverse through the string up to the point where the remaining legnth is less than substring 
    for i in range(len(string) - sub_len + 1):
        if string[i : i + sub_len] == sub_string:
            count +=1
    return count

