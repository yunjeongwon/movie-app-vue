모델링


# 
추천알고리즘 
1 - 메인 (미정)
2-  자신이 선택한 영화 장르 top3 장르 추천
3 - 자신과 비슷한 나이 혹은 취향인 사람 추천 목록

# 

홈페이지 ( 추천페이지 )
검색페이지
평가페이지 
디테일 
좋아요한 영화목록 페이지
평가했던 목록 페이지
개인취향분석 ( 미정 )


# 
모델 

user 
comment
movie

# 
DB (model-movie)
pk 제목 장르 시간 like_users(mtm) 설명 posterlink 연령가 관객수 
청불 감독 출연 hashtag( 화려한 같은 특성표시 ) comment(MtM)

#
comment 
pk user(1:N) score content movie(MtM) 

# 
user 
pk email age_range, gender like_movies(mtm) comments(1:N)




<!-- https://developers.kakao.com/tool/rest-api/open/get/v2-user-me -->


