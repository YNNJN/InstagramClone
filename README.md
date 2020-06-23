# gramClone

> Django를 이용한 인스타그램 클론 프로젝트



<br>
<br>

## 1. 개발 환경

1. Python Web Framework

   - Django 2.1.15

   - Python 3.74

     

2. 개발 아키텍처

   - Django & Vanila JS





<br>
<br>

## 2. 기능

- **게시물의 생성/수정/조회/삭제 기능**
  - `django-imagekit`를 활용하여, 게시물로 이미지를 업로드 할 수 있습니다
  - 게시물을 보여주는 화면인 index, modal, detail에서 UX를 고려하여 구성을 달리하였습니다 

- **댓글 기능**
  - 댓글의 수정/삭제가 가능합니다
  - `Ajax/Vanila JS`를 활용한 비동기 요청으로 새로고침 없이 동작합니다

- **좋아요 기능**
  - 좋아요 수와 좋아요를 누른 사람의 목록을 제공합니다
  - `Ajax/Vanila JS`를 활용한 비동기 요청으로 새로고침 없이 동작합니다

- **팔로우 기능**

  - 팔로잉 여부에 따라 팔로우/언팔로우 버튼을 구분하여 제공합니다

  - 유저 별 팔로워/팔로잉 목록을 제공합니다

- **소셜 로그인 기능**
  - `django-allauth`를 활용하여, 구글 계정으로 로그인 할 수 있습니다

- **해쉬태그 기능**
  - `사용자 정의 필터`로 해시태그 링크를 구현하였습니다
  - 해쉬태그를 이용한 검색이 가능합니다

- **프로필 이미지 기능**
  - `gravatar`에 등록한 프로필 이미지가 적용됩니다





<br>
<br>

## 3. 화면 상세

> Index

<img width="1680" alt="스크린샷 2020-06-24 오전 2 01 46" src="https://user-images.githubusercontent.com/60057425/85442780-81ddb280-b5cb-11ea-9141-8f1ac22be002.png">

> Post modal

<img width="1680" alt="스크린샷 2020-06-24 오전 2 00 48" src="https://user-images.githubusercontent.com/60057425/85442777-80ac8580-b5cb-11ea-9431-77a09f95f0b8.png">

> Post detail

<img width="1680" alt="스크린샷 2020-06-24 오전 1 57 08" src="https://user-images.githubusercontent.com/60057425/85442764-7d18fe80-b5cb-11ea-8d3e-a06f4e50cbc5.png">

> Profile

<img width="1680" alt="스크린샷 2020-06-24 오전 1 55 34" src="https://user-images.githubusercontent.com/60057425/85442720-74282d00-b5cb-11ea-8810-14ad4a664e59.png">

> Following/Followers

<img width="1680" alt="스크린샷 2020-06-24 오전 1 56 51" src="https://user-images.githubusercontent.com/60057425/85442758-7b4f3b00-b5cb-11ea-80fe-3e016924bbc1.png">

> Likers

<img width="1680" alt="스크린샷 2020-06-24 오전 1 59 54" src="https://user-images.githubusercontent.com/60057425/85442773-7f7b5880-b5cb-11ea-8a7a-8273b95669ec.png">



> Search by hash tag

<img width="1680" alt="스크린샷 2020-06-24 오전 2 02 00" src="https://user-images.githubusercontent.com/60057425/85442782-830edf80-b5cb-11ea-85ff-0170dfb653fb.png">





<br>
<br>

## 4. 반응형 웹

> Index (iPhone X - iPad - iPad Pro 순서)

![반응형 001](https://user-images.githubusercontent.com/60057425/85442798-886c2a00-b5cb-11ea-8506-b0dbabc093a6.png)

> Post modal (iPhone X - iPad - iPad Pro 순서)

![반응형 002](https://user-images.githubusercontent.com/60057425/85442814-8c984780-b5cb-11ea-8517-ed260a0dc181.png)

> Profile (iPhone X - iPad - iPad Pro 순서)

![반응형 003](https://user-images.githubusercontent.com/60057425/85442819-8d30de00-b5cb-11ea-9f51-93fa42a9fe98.png)