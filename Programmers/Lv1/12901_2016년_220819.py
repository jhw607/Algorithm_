month = [31,29,31,30,31,30,31,31,30,31,30,31]
week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
def solution(a, b):
    answer = ''
    days = sum(month[:a-1])+b-1
    answer = week[days%7]
    
    return answer
    
### 시간 줄이기
def solution(a, b):
    days = sum(month[:a-1])+b-1
    return week[days%7]
    
### 코드 줄이기
def solution(a, b):
    return week[(sum(month[:a-1])+b-1)%7]

### 함수 활용
week2 = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
from datetime import date
def solution(a, b):
    day = date(2016,a,b)
    return week2[day.weekday()]
    