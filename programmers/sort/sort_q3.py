'''
 * User: Hojun Lim
 * Date: 2021-03-23
'''

def solution(citations):
    sorted_citations = sorted(citations, reverse=True)
    for i in range(len(sorted_citations)):
        if sorted_citations[i] <= i:
            return i
    return len(sorted_citations)