
BASE_URL = 'http://127.0.0.1:8000/movies/'

# movies
path('', views.movie_list),  # 영화들
path('<int:movie_pk>/', views.movie_detail),  # 상세 영화
path('<int:movie_pk>/wish/', views.wish_movie),  #  보고싶어요 기능(보고싶어요 영화 추가)

# 특정 영화들
path('<int:genre_id>/', views.genre_movie),  #  장르 영화
path('<int:tag_id>/', views.tag_movie),  #  특성 영화

# 나의 보고싶어요 영화 보내주기
path('wished/', views.wished_movie),  # 보고싶어요한 영화 보내주기

# 나의 평가한 영화 보내주기
path('evaluated/', views.evaluated_movie),  # 평가한 영화 보내주기





# comments
path('<int:movie_pk>/comments/', views.create_comment),
path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete)