-- 코드를 입력하세요
SELECT animal_id, name, sex_upon_intake
from animal_ins
-- Lucy, Ella, Pickle, Rogan, Sabrina, Mitty
where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by animal_id