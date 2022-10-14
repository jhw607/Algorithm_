-- 동명 동물 수 찾기
SELECT name, count(name)
FROM animal_ins
where name is not null
group by name having count(name)>1 
-- # having은 그룹화 한 후에 조건 적용
order by name

-- # 쿼리문의 실행 순서

-- # SELECT - 5순위 (필수)
-- # FROM - 1순위 (필수)
-- # WHERE - 2순위
-- # GROUP BY - 3순위
-- # HAVING - 4순위
-- # ORDER BY - 6순위

--!--!--!--!--!--!--!--!--!--!--

-- 고양이와 개는 몇마리 있을까
SELECT animal_type, count(animal_type)
from animal_ins
group by animal_type
order by animal_type

--!--!--!--!--!--!--!--!--!--!--

-- 입양 시각 구하기
SELECT hour(datetime), count(hour(datetime))
-- # count(datepart('hour',datetime))
from animal_outs
where 9 <= hour(datetime) and hour(datetime) <= 19
group by hour(datetime)
order by hour(datetime)

-- # hour(datetime) 이걸 안해봐서 시간함수 겁나 뒤짐..;;