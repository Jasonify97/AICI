# <img src="https://t4.ftcdn.net/jpg/05/34/18/69/240_F_534186910_T3ieVilB86S6uNqbXnT6LEvepbpBvF7z.jpg"  width="30" height="30"/> AICI
<p align="center"><img src="https://github.com/Jasonify97/AICI/assets/98500133/533b82c6-a3b8-4ef3-9e5c-85f57c32b4df"  width="600" height="400"/></p>

# <img src="https://github.com/Jasonify97/AICI/assets/98500133/604d456c-cd5d-46df-850b-884e713fe51c"  width="30" height="30"/>프로젝트 소개
**본 프로젝트는 KT의 사업부서의 과제인 효율적인 업무를 위한 자동화 시스템 AICI로 사업 부서에서 제시한 2가지의 요구사항을 목적으로 함** </br>
* 고객TM 확인 서비스</br>
AICI 시스템으로 장애 영향 고객에게 동시다발 고객 TM을 시행 후 결과를 수합하여, 일괄적으로 확인, 관리할 수 있는 서비스 개발</br></br>
* 사외공사 신고 서비스</br>
공사 담당자가 AICI시스템으로 사외 공사를 신고하고, 관리 및 자동 응대를 시행할 수 있는 사외 공사 신고 서비스를 개발</br></br></br>

# <img src="https://github.com/Jasonify97/AICI/assets/98500133/324a82c7-c47a-40fa-b5fc-2b556b5f4da5"  width="30" height="30"/>프로젝트 목표
**1. 고객TM 확인 서비스**
* 장애 영향 고객에게 동시다발 고객 TM을 시행 후 결과를 수합
* 수합된 결과를 STT AI를 이용하여 양호/불량 판별
* AI를 이용해 텍스트 요약 후 긍부정 판별</br>

**2. 사외공사 신고 서비스**
* 사외공사 담당자의 전화를 받아 텍스트로 변환
* 텍스트에서 필요 단어를 추출 후 엔지니어에게 제공
* 공사 정보 캘린더 제작 및 공사 위치 제공</br>

**3. 기타**
* 공지사항 게시판
* 로그인 및 회원가입 페이지
* 개인정보처리방침/이용약관 페이지</br></br></br>

# <img src="https://github.com/Jasonify97/AICI/assets/98500133/d385f4a0-736b-4a27-98fd-737adf470707"  width="30" height="30"/>배포주소
[AICI Service](http://52.63.184.150)</br>
ID : hello1234</br>
PW : a123456~
</br></br></br>
# <img src="https://github.com/Jasonify97/AICI/assets/98500133/ea0eceae-c6e7-45ee-960e-b6b43b8e83c8"  width="30" height="30"/>Architecture
### Presentation  
<div class="badge-container">
<img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></div>
   
### Application    
<div class="badge-container">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white"/></div>  

### Database   
<div class="badge-container">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/></div></br></br></br>

# <a src="https://avatars.githubusercontent.com/u/98500133?v=4"><img src="https://github.com/Jasonify97/AICI/assets/98500133/88037072-2eee-4fcc-8824-ca2c299d7baf"  width="30" height="30"/></a>팀원소개
### Front-End
|이준용|한세린|
|:---:|:---:|
|<img src="https://avatars.githubusercontent.com/u/98500133?v=4"  width="170" height="220"/>|<img src="https://avatars.githubusercontent.com/u/62207913?v=4"  width="170" height="220"/>|
|[@Jasonify97](https://github.com/Jasonify97)|[@jhsy0429](https://github.com/jhsy0429)|

### Back-End


### AI




# <img src="https://github.com/Jasonify97/AICI/assets/98500133/bcd48281-26a3-448b-b6d7-01867f36b64a"  width="30" height="30"/>프로젝트 상세내용






## Version
- python==3.10.11
- Django==4.2.2
- gunicorn==20.1.0
- ``pip install -r requirements.txt``

## Directory
```
├── AICI_WEB                    # configuration
├── board                       # main page
├── construction                # construction page
├── users                       # sign in / sign up page
├── voc                         # voc page
│
├── media                       # file storage
│   ├── board                   # attatched file in board
│   └── voc                     # attatched excel file in voc
├── static
│   ├── admin
│   │   ├── css
│   │   │   └── vendor
│   │   │       └── select2
│   │   ├── img
│   │   │   └── gis
│   │   └── js
│   │       ├── admin
│   │       └── vendor
│   │           ├── jquery
│   │           ├── select2
│   │           │   └── i18n
│   │           └── xregexp
│   ├── construction
│   ├── home
│   ├── privacy
│   └── service
└── templates
    ├── board
    ├── construction
    ├── users
    └── voc
```

## Apps
### users
- Sign Up / Sign In
- Custom User model
- board
- construction
- voc
