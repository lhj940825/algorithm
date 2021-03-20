'''
 * User: Hojun Lim
 * Date: 2021-03-20
'''

def solution(n, lost, reserve):
    pos_n = n - len(lost)
    _lost = []

    # when student with additional cloth got stollen
    for neg_n in lost:
        if neg_n in reserve:
            reserve.remove(neg_n)
            pos_n += 1
        else:
            _lost.append(neg_n)

    for neg_n in _lost:
        if neg_n - 1 in reserve:
            reserve.remove(neg_n - 1)
            pos_n += 1


        elif neg_n + 1 in reserve:
            reserve.remove(neg_n + 1)
            pos_n += 1


    print(reserve)
    return pos_n