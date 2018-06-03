SELECT H.hacker_id, h.name FROM Submissions S 
INNER JOIN Challenges C ON S.challenge_id = C.challenge_id
INNER JOIN Difficulty D ON C.difficulty_level = D.difficulty_level
INNER JOIN Hackers H ON S.hacker_id = H.hacker_id
WHERE S.score = D.score GROUP BY H.hacker_id, H.name HAVING COUNT(S.hacker_id) > 1
ORDER BY COUNT(S.hacker_id) DESC, S.hacker_id
