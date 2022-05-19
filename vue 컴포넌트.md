#### vue_08_workshop


---
/ URL을 통해 HomeView 컴포넌트 렌더링
HomeView에 MovieList 컴포넌트 렌더링
MovieList MovieCard 컴포넌트 렌더링

---
/search URL을 통해 SearchView 컴포넌트 렌더링
SearchView에 SearchBar 컴포넌트 렌더링
SearchView에 MovieCard 컴포넌트 렌더링

---
/evaluate URL을 통해 EvaluateView 컴포넌트 렌더링
EvaluateView에 MovieEvalute 컴포넌트 렌더링

---
/movies/:pk URL을 통해 MovieDetailView 컴포넌트 렌더링
MovieDetailView MovieEvalute 컴포넌트 렌더링 or MovieCard
MovieDetailView에 MovieDetail 컴포넌트 렌더링
(평가 취소 버튼)

MovieDetailView에 CommentList 컴포넌트 렌더링
MovieDetailView에 CommentListItem 컴포넌트 렌더링
MovieDetailView에 CommentForm 컴포넌트 렌더링

---
/wishes URL을 통해 WishesView 컴포넌트 렌더링
WishesView에 MovieCard 컴포넌트 렌더링

---
/evaulated URL을 통해 EvaluatedMovieView 컴포넌트 렌더링
EvaluatedMovieView에 MovieCard 컴포넌트 렌더링

---
/signup URL을 통해 SignupView 컴포넌트 렌더링

---
/login URL을 통해 LoginView 컴포넌트 렌더링

---
/logout URL을 통해 LogoutView 컴포넌트 렌더링

---
회원가입과 로그인은 완료 이후 Vuex state 및 localStorage에 토큰 저장

---
로그아웃은 Vuex state의 토근 삭제 및 서버의 token 테이블에서 token 삭제됨

---
에러 발생시 이를 알릴 수 있도록 AccountErrorList 컴포넌트 렌더링

---