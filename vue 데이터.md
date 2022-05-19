
---
홈페이지 ( 추천페이지 )
/

```json
{
  "popularMovies": [
    {
      "id": 1,
      "poster_path": "https://poster.com/poster/1",
      "title": "아이언맨",
      "running_time": 100,
      "gerne_ids": [3, 4],
      "tag_ids": [1, 2],
    }
  ],
  "actionMovies": [],
  "성민님추천영화": [],
  "정원님추천영화": [],
  "시험 끝나면 이것부터 조진다": [],
}
```
---

검색페이지
/search
```json
{
  "movies": [
    {
      "id": 1,
      "poster_path": "https://poster.com/poster/1",
      "title": "아이언맨",
      "running_time": 100,
      "gerne_ids": [3, 4],
      "tag_ids": [1, 2],
    }
  ]
}
```
---

평가페이지 
/evaluate
```json
{
  "movies": [
    {
      "id": 1,
      "poster_path": "https://poster.com/poster/1",
      "title": "아이언맨",
      "release_date": "2017-01-01",
    }
  ]
}
```
---

디테일 
/movies/:pk
```json
{
  "id": 1,
  "poster_path": "https://poster.com/poster/1",
  "title": "아이언맨",
  "running_time": 100,
  "gerne_ids": [1, 2, 3],
  "tag_ids": [1, 2, 4],
  "release_date": "2020-02-02",
  "overview": "줄거리줄거리줄거리",
  "trailer_path": "https://poster.com/trailer/1",
  "comments": [],
}
```
---

보고싶은 영화목록 페이지
/wishes
```json
{
  "movies": [
    {
      "id": 1,
      "poster_path": "https://poster.com/poster/1",
      "title": "아이언맨",
      "running_time": 100,
      "gerne_ids": [3, 4],
      "tag_ids": [1, 2],
    }
  ]
}
```
---

평가했던 목록 페이지
/evaulated
```json
{
  "movies": [
    {
      "id": 1,
      "poster_path": "https://poster.com/poster/1",
      "title": "아이언맨",
      "running_time": 100,
      "gerne_ids": [3, 4],
      "tag_ids": [1, 2],
    }
  ]
}
```
---

개인취향분석 ( 미정 )
/analysis/:pk
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
---