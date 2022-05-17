#### vue_06_workshop


----
1. 목표
  * DRF(Django Rest Framework)를 활용한 API Server 제작
  * Vue를 활용한 SPA(Single Page Application) 제작
  * Oauth2 카카오톡 SNS 로그인 기능
  * 평가한 영화 정보를 통한 영화 추천 기능
----
2. 준비사항
    A. 개발도구 및 라이브러리
    * Visual Studio Code
    * Chrome browser
    * Django 3.2.12
    * Django Rest Framework
    * Postman
    * Vue 2.0
    * Vuex
----
3. Model
* User

|필드명|데이터 유형|역할|
|------|---|---|
|password|vahchar(100)|비밀번호|
|last_login|datetime|마지막 로그인 날짜|
|is_superuser|bool|관리자 여부|
|username|vahchar(100)|유저 이름|
|first_name|varchar(100)|이름|
|last_name|varchar(100)|성|
|email|vahchar(200)|이메일|
|is_staff|bool|직원 여부|
|is_active|bool|활성 여부|
|date_joined|datetime|가입 날짜|

* Movie

|필드명|데이터 유형|역할|
|------|---|---|
|title|vahchar(100)|영화 제목|
|running_time|integer|상영 시간|
|description|text|영화 줄거리|
|age_range|integer|영화 관람 가능 나이|
|like_users|integer|외래 키(User 참조)|
|genre|integer|외래 키(Genre 참조)|
|tag|integer|외래 키(Tag 참조)|
|release_year|integer|개봉 연도|
|trailer_url|text|예고편 URL|
|poster_url|text|포스터 URL|

* Comment

|필드명|데이터 유형|역할|
|------|---|---|
|content|text|리뷰 내용|
|score|float|평점|
|user|integer|외래 키(User 참조)|
|movie|integer|외래 키(Movie 참조)|

* Gerne

|필드명|데이터 유형|역할|
|------|---|---|
|name|varchar(50)|장르 이름|

* Tag

|필드명|데이터 유형|역할|
|------|---|---|
|name|varchar(50)|특성 이름|

----
