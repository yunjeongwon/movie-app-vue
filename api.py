BASE_URL = 'http://127.0.0.1:8000/movies/'

# movies
path('', views.movie_list),  # 영화들
path('<int:movie_pk>/', views.movie_detail),  # 상세 영화
path('<int:movie_pk>/wish/', views.wish_movie),  #  보고싶어요 기능(보고싶어요 영화 추가)


# 나의 보고싶어요 영화 보내주기
path('wished/', views.wished_movie),  # 보고싶어요한 영화 보내주기


# 나의 평가한 영화 보내주기
path('evaluated/', views.evaluated_movie),  # 평가한 영화 보내주기


# 검색한 영화 보내주기
path('search/', views.search_movie),  # 검색한 결과 보내주기


# 평가하기
path('evaluate/', views.evaluate_movie),  # 영화 평가하기
# 평가할 때마다 연산해서 각 유저에 좋아하는 영화 장르, 특성을 저장


# 홈 추천 영화
# 남이 보고싶어요 or 좋게 평가한 영화들 추천
path('<int:user_id>/wish/', views.user_wished_movie),
path('<int:user_id>/evaluate/', views.user_evaluated_movie),


# 인기 top 10 (popularity)
path('popular/', views.popular_movie),  # top10 영화


# 장르 특성 추천 영화
path('<int:genre_id>/', views.genre_movie),  #  장르 영화
path('<int:tag_id>/', views.tag_movie),  #  특성 영화


#############################
# 개인이 평가한 영화의
# 장르나 특성과 비슷한 영화 추천
path('recommand/<int:user_id>/', views.recommand_movie),  # 영화 추천하기
# 개인의 유저의 좋아하는 장르, 특성에 맞는 영화 찾기
# 개인 평가한 영화, score
# 연산 후 영화들을 보내주기


# 000님을 위한 추천 장르
path('recommand/<int:user_id>/genreAndTag/', views.recommand_genreAndTag),  # 영화 추천하기
# 연산 후 장르나 특성들 리스트를 보내주기


# vote_average, vote_count 를 가공해서 2부분을 나누는데 
# 높높 => 대중
# 높낮 => 매니아
path('vote/', views.vote_movie),  # 영화 추천하기


# comments
path('<int:movie_pk>/comments/', views.create_comment),
path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete)
