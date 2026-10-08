# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-08, 11:24 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        s = list(input().split())
        if s[0]=='insert':
            l.insert(int(s[1]),int(s[2]))
        if s[0]=='remove':
            l.remove(int(s[1]))
        if s[0]=='append':
            l.append(int(s[1]))
        if s[0]=='sort':
            l.sort()
        if s[0]=='pop':
            l.pop()
        if s[0]=='reverse':
            l.reverse()     
        if s[0]=='print':
            print(l)
