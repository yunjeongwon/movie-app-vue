최종 프로젝트를 위한 데이터 베이스 모델링과 요청 URL 구성 및 응답 JSON설계

홈페이지 ( 추천페이지 )
/home

```json
{
  "popularMovies": [
    {
      "id": 1,
      "poster_url": "https://poster.com/poster/1",
      "title": "아이언맨",
      "running_time": 100,
      "gerne": "액션",
      "tag": "감동",
    }
  ],
  "actionMovies": [],
  "성민님추천영화": [],
  "정원님추천영화": [],
  "시험 끝나면 이것부터 조진다": [],
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
      "title": "아이언맨",
      "running_time": 100,
      "gerne": "액션",
      "tag": "감동",
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
      "title": "아이언맨",
      "release_year": 2017,
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
  "title": "아이언맨",
  "running_time": 100,
  "gerne": [{
    1: "액션",
    2: "로맨스",
  }],
  "tag": [{
    1: "감동",
    2: "화려함",
  }],
  "release_year": 2017,
  "description": "줄거리줄거리줄거리",
  "trailer_url": "https://poster.com/trailer/1",
  "age_range": 15,
  "comments": [],
}
```

좋아요한 영화목록 페이지
/likes
```json
{
  "movies": [
    {
      "id": 1,
      "poster_url": "https://poster.com/poster/1",
      "title": "아이언맨",
      "running_time": 100,
      "gerne": "액션",
      "tag": "감동",
    }
  ]
}
```

평가했던 목록 페이지
/evaulated_list
```json
{
  "movies": [
    {
      "id": 1,
      "poster_url": "https://poster.com/poster/1",
      "title": "아이언맨",
      "running_time": 100,
      "gerne": "액션",
      "tag": "감동",
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