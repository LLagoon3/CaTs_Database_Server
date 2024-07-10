# CaTs_Database

## Token

JWT기반 인증 방식

### 토큰 발급

> `POST` /api/token/login/
> 

```python
body = {
	'username': 'username',
	'password': 'password'
	}
```

### 토큰 재발급

> `POST` /api/token/refresh/
> 

```python
body = {
	'refresh': '이전에 발급받은 refresh 토큰 값'
	}
```

### 토큰 검증(401)

> `POST` /api/token/verify/
> 

```python
body = {
	'token': 'refresh 또는 access 토큰 값'
	}
```

## 인증 방식

- 헤더에 access 토큰 값을 포함 시킬 것

```python
header = {
	'Authorization': 'Bearer {access 토큰 값}'
	}
```

## API 설명

### Info(앱 - 테이블 명)

- api
    - user
    - userkakaoinfo
    - userfcmtoken
- catsapp
    - userprofile
    - posts
    - comments
    - likes
    - commentlikes
    - attendance
    - fcmlog
    - stocksteward

### Swagger - API 문서

> `GET`/swagger/
> 

주의사항 : nginx 사용 시, 사용자의 static 경로 추가할 것

<aside>
💡 # /etc/nginx/nginx.conf

server {
    listen 80;
    server_name cats.chungbuk.ac.kr;

    # Static files location
    location /static/ {
        alias {path_to_static}/static/;
    }
}

</aside>

## API Method

### List

> `GET` /{앱 이름}/{테이블 명}/
> 
- 테이블 전체를 반환

### Retrieve

> `GET` /{앱 이름}/{테이블 명}/{pk 값}/
> 
- pk 값에 해당되는 레코드를 반환

> `GET` /{앱 이름}/{테이블 명}/?{필드1=필드1 값}&{필드2 = 필드2 값}…/
> 
- 각각 필드 값에 모두 해당되는 레코드들을 반환

### Create

> `POST` /{앱 이름}/{테이블 명}/
> 

```python
body = {
	'필드1': '필드1 값',
	'필드2': '필드2 값',
	...
}
```

- 레코드 생성

### Update

> `PUT` /{앱 이름}/{테이블 명}/
> 

```python
body = {
	'필드1': '필드1 값',
	'필드2': '필드2 값',
	...
}
```

- 기존에 존재하는 레코드 수정
- 수정되지 않는 필드라도 모두 포함되어야 함

### Destroy

> `DELETE` /{앱 이름}/{테이블 명}/{pk 값}/
> 
- pk 값에 해당하는 레코드 삭제