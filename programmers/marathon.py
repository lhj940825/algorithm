'''
 * User: Hojun Lim
 * Date: 2020-11-07
'''

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        else:
            continue

    return participant[-1]