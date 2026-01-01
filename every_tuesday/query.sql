-- identify high-risk heart attack patients by state and gender who meet all of the following conditions:
-- Diagnosed with a heart attack
-- Age > 45
-- Blood pressure ≥ 140
-- Cholesterol > 200
-- Wearable device slope = 2
-- Have undergone at least one X-ray
-- Have recorded at least one symptom
-- For each state and gender, return:
-- Number of high-risk patients
-- Average age
-- Average blood pressure
-- Average cholesterol
 
-- Pattern and approach to writing an SQL Statement
 
-- 1. What do you need - Columns that you need as part of the output
-- 2. Where do you have the information that you need - Tables
-- 3. Connections - Joins - How do you join the tables to get the information
-- 4. Join Conditions
-- 5. Other conditions apart from join
-- 6. Aggregate function to be used
-- 7. Group, Having
-- 8. SubQuery and/or any other predicates
-- 9. Order in which the information has to be displayed
 

SELECT a.state, m.gender,COUNT(m.member_id) as high_risk_patient, ROUND(AVG(m.age),2) AS avg_age, ROUND(AVG(bt.bloodpressure),2) as avg_bp, ROUND(AVG(bt.serumcholesterol),2) as avg_cholestrol
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis cd ON m.member_id = cd.memberinfo_member_id
JOIN wearabledevicedata wd ON cd.cardio_id = wd.cardiodiagnosis_cardio_id
JOIN xray x ON cd.cardio_id = x.cardiodiagnosis_cardio_id
JOIN symptom s ON cd.cardio_id = s.cardiodiagnosis_cardio_id
JOIN bloodtest bt ON cd.cardio_id = bt.cardiodiagnosis_cardio_id
WHERE cd.cardioarrestdetected = '1' and age>45 and bt.bloodpressure>=140 and bt.serumcholesterol>200 and wd.slope=2
GROUP BY a.state, m.gender
ORDER BY a.state, m.gender;