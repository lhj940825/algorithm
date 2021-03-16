'''
 * User: Hojun Lim
 * Date: 2021-03-16
'''

def solution(answers):
    students = [1,2,3]
    stu1_sol = [1,2,3,4,5]
    stu2_sol = [2,1,2,3,2,4,2,5]
    stu3_sol = [3,3,1,1,2,2,4,4,5,5]

    stu1_ans_cnt = 0
    stu2_ans_cnt = 0
    stu3_ans_cnt = 0

    len_stu1_pattern = 5
    len_stu2_pattern = 8
    len_stu3_pattern = 10

    num_answers = len(answers)
    i = 0

    while i< num_answers:
        cur_ans = answers[i]
        if stu1_sol[i%len_stu1_pattern] == cur_ans: stu1_ans_cnt += 1
        if stu2_sol[i%len_stu2_pattern] == cur_ans: stu2_ans_cnt += 1
        if stu3_sol[i%len_stu3_pattern] == cur_ans: stu3_ans_cnt += 1
        i += 1

    list_stu_ans_cnt = [stu1_ans_cnt, stu2_ans_cnt, stu3_ans_cnt]
    max_ans_cnt = max(list_stu_ans_cnt)

    answer = [i + 1 for i, cnt in enumerate(list_stu_ans_cnt) if cnt == max_ans_cnt]
    return answer