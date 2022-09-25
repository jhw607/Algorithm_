def solution(survey, choices):
    question = {'RT':0, 'CF':0, 'JM':0, 'AN':0} # 지표별 점수
    type = ['RT', 'CF', 'JM', 'AN'] # 유형별 지표번호
    indicator = []  # 지표별 점수 저장할 배열
    answer = []
    
    for idx, case in enumerate(survey):
        if case in question.keys():
            question[case] += choices[idx]-4
            print('if:', question)
        else:
            question[''.join(case[1]+case[0])] -= choices[idx]-4
            print('else:', question)
    
    for i in range(4):
        if question[type[i]] > 0:
            answer.append(type[i][1])
        else:
            answer.append(type[i][0])

    return ''.join(answer)