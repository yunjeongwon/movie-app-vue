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


API(장고 drf)(서버) <==> Vue(사용자)


API 서버를 위한 데이터 요청
(모든 평가는 evaluate 페이지 or 디테일 페이지에서만, 코멘트 x)

---
(홈)
인기영화 보내주기

어떤 특성의 영화 보내주기

어떤 장르 영화 보내주기

어떤 유저의 보고싶어요 영화 보내주기

어떤 유저의 평가한 영화 보내주기


(검색)
검색한 결과 보내주기

인풋 submit
@submit => axios =>

api 그 검색어로 db에서 찾는다

/api/v1/search
data: {
  title: '화려'
}

data를 가지고 db에서 영화를 찾는다
data와 같은 영화제목을 찾고
장르 찾고
특성 찾고


{
  movies: [
    {
      title:,
      id:,
    }
  ]
}
응답해준다


요청으로 검색어


(평가하기)
랜덤 영화 50개 보내주기


(보관함)
나의 보고싶어요 영화 보내주기

나의 평가한 영화 보내주기


(디테일)
영화 디테일 보내주기

이미 평가한 영화면 그 평점을 보여줘라
(프로필에서 평가한 영화랑 같은지 판단, 같으면 그 평가한 평점을 선택)

**댓글 CRUD**


프로필(
  보고싶어요 영화 리스트
  평가한 영화 리스트
)

로그인 한 유저 정보
