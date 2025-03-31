# 평가점수가 가장 높은 사원의 정보

SELECT SUM(c.SCORE) as SCORE, b.EMP_NO, b.EMP_NAME, b.POSITION, b.EMAIL
FROM HR_EMPLOYEES as b 
    INNER JOIN HR_GRADE as c
    ON b.EMP_NO = c.EMP_NO
WHERE c.YEAR = 2022
GROUP BY b.EMP_NO
ORDER BY SCORE DESC
LIMIT 1