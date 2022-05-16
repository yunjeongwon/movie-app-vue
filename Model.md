# 

|필드명|데이터 유형|역할|
|------|---|---|
|title|테스트2|테스트3|
|genre|테스트2|테스트3|
|runnigtime|테스트2|테스트3|
|description|테스트2|테스트3|
|age|테스트2|테스트3|
|청불|테스트2|테스트3|
|감독|테스트2|테스트3|
|출연|테스트2|테스트3|
|like_users|테스트2|테스트3|
|hashtag|테스트2|테스트3|


#
comment 
pk user(1:N) score content movie(MtM) 

# 
user 
pk email age_range, gender like_movies(mtm) comments(1:N)