-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
from member_profile
where month(date_of_birth) = '3' and TLNO != 'NULL' and gender = 'w'
order by member_id asc; 
