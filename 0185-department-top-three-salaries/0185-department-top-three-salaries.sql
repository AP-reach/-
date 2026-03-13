SELECT Department, Employee, Salary
FROM (
    SELECT
        s2.name AS Department,
        s1.name AS Employee,
        s1.salary AS Salary,
        dense_rank() OVER (
            PARTITION BY s2.id
            ORDER BY s1.salary DESC
        ) AS rk
    FROM Employee AS s1
    JOIN Department AS s2
        ON s1.departmentId = s2.id
) t
WHERE rk < 4;
