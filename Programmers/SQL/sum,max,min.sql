-- 최솟값 구하기
SELECT min(DATETIME) as '시간' from ANIMAL_INS

--!--!--!--!--!--!--!--!--!--!--

-- 동물 수 구하기
SELECT count(ANIMAL_TYPE) from animal_ins 
-- where ANIMAL_TYPE is not null

--!--!--!--!--!--!--!--!--!--!--

-- 중복 제거하기
SELECT count(distinct name) from animal_ins
where name is not null

