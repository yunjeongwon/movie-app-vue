최종 프로젝트를 위한 데이터 베이스 모델링과 요청 URL 구성 및 응답 JSON설계

홈페이지 ( 추천페이지 )
/home

```json
{
  "popularMovies": [
    {
      "id": 1,
      "poster_url": "https://poster.com/poster/1",
    }
  ],
  "actionMovies": [
    {
      "id": 2,
      "poster_url": "https://poster.com/poster/2",
    }
  ]
}
```

검색페이지
/search
```json
{
  "movies": [
    {
      "id": 1,
      "poster_url": "https://poster.com/poster/1",
    }
  ]
}
```

평가페이지 
/evaluate
```json
{
  "movies": [
    {
      "id": 1,
      "poster_url": "https://poster.com/poster/1",
    }
  ]
}
```

디테일 
/movies/<int:pk>
```json
{
  "id": 1,
  "poster_url": "https://poster.com/poster/1",
}
```

좋아요한 영화목록 페이지
/likes
```json
{
  "likeMovies": [
    {
      "id": 1,
      "poster_url": "https://poster.com/poster/1",
    }
  ]
}
```

평가했던 목록 페이지
/evaulated_list
```json
{
  "evaulatedMovies": [
    {
      "id": 1,
      "poster_url": "https://poster.com/poster/1",
    }
  ]
}
```

개인취향분석 ( 미정 )
/analysis/<int:pk>
```json
{
  "username": "jw",
  "evaulatedMoviesCount": 10,
  "likeTag": [
    "colorful",
    "sad"
  ],
  "likeNation": "ko",
  "likeGerne": [
    "drama",
    "action"
  ],
  "totalRunningTime": 13
}
```