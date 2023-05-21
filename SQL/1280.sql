SELECT
    S1.student_id,
    S1.student_name,
    S2.subject_name,
    COUNT(C.subject_name) as attended_exams
FROM
    Students S1
    JOIN Subjects S2
    LEFT JOIN Examinations C
        ON S1.student_id = C.student_id 
            AND S2.subject_name = C.subject_name
GROUP BY
    S1.student_id,
    S2.subject_name
ORDER BY
    S1.student_id,
    S2.subject_name
