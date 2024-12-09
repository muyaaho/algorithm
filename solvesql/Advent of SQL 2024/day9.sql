-- https://solvesql.com/problems/predict-game-scores-1/
-- 게임 평점 예측하기1

with a as (
  select 
  genre_id,
  round(avg(critic_score), 3) as critic_score,
  ceiling(avg(critic_count)) as critic_count,
  round(avg(user_score), 3) as user_score,
  ceiling(avg(user_count)) as user_count
  from games
  group by genre_id
)

select 
g.game_id,
g.name,
coalesce(g.critic_score, a.critic_score) as critic_score,
coalesce(g.critic_count, a.critic_count) as critic_count,
coalesce(g.user_score, a.user_score) as user_score,
coalesce(g.user_count, a.user_count) as user_count
from games as g join a on g.genre_id = a.genre_id
where year >= 2015 and (g.critic_score is null or g.user_score is null)

-- select *
-- from a

-- select count(*)
-- from games
-- where year>=2015 and (user_count is null 
-- or critic_score is null)
-- 제출: 649개, 정답: 658개
