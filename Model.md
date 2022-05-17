# 

|필드명|데이터 유형|역할|
|------|---|---|
|title|string|영화 제목|
|genre|foreign|영화 장르 |
|runnigtime|string|영화 상영시간|
|description|string|줄거리|
|age|string|연령가|
|adult|boolen|청불여부|
<!-- |director|string[]|감독|
|actors|string[]|배우| -->
|like_users|manytomany|라이크|
|hashtag|foreign|영화특성?| 
|poster_url|string|포스터 링크|
|trailer_url|string|예고편 링크|
|release_date|datetime|개봉일|



#
comment 
pk 
|필드명|데이터 유형|역할|
|------|---|---|
|user|string|유저 이름|
|score|string|평점|
|content|string|리뷰|
|movie|many to many|코멘트를 달 영화|

# 
user 
pk email age_range, gender like_movies(mtm) comments(1:N)

|필드명|데이터 유형|역할|
|------|---|---|
|email|string|유저 이메일|
|age_range|string|유저 나이대 (20,30,40)|
|gender |string|유저 성별|
|like_movies|many to many|유저가 좋아요한 영화|
|comments|1:N|유저가 작성한 코멘트|