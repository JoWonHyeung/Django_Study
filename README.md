# Django

## 2022/02/16

- ### **View**
 
웹 클라이언트(브라우저)에서 요청이 전달되면 알맞는 서비스 로직을 수행하고, 그 결과를 직접 응답하거나 템플릿을 통해서 응답한다. 파이썬 함수 또는 클래스로 구현하는데 함수로 구현한다.

선택적으로 다음 기능들을 구현하게 된다.

1. Query 문자열 추출

요청 방식에 따라서 2가지 방법이 있다.

Get 방식 요청: request.GET

Post 방식 요청: request.Post

2. 요청 방식을 방식을 체크: request.method 
3. 서비스 로직, 처리 로직을 구현한다.
4. 템플릿을 통해서 응답 페이지 구성되도록 처리한다.
5. 응답 페이지를 구성하게 될 템플릿(HTML)에게 전달할 데이터가 존재하면 dict 객체에 담아서 반환한다.

cf) request.GET['name'] => key값 없으면 오류난다. / request.GET.get(key, default value) => 없으면 none을 return 한다.


- ### **Template**

HTML, CSS, Javascript로 작성한다. 장고에서 제공하는 구문을 이용해서 동적인 처리를 구현할 수 있다.

동적 처리가 수행되는 위치에 따라서

Server : 장고의 템플릿 변수, 장고의 템플릿 태크

Client : javascript 사용


- ### **Http 요청 방식(method)**
  - 기본 요청 방식: GET
  - 브라우저에서 URL 문자열을 입력해서 요청: GET
  - GET 방식으로 요청할 때는 Query 문자열 없이 요청할 수도 있고, Query 문자열을 전달하면서 요청할 수도 있다. <form> 태그를 사용해서 요청하는 것도 가능하다. <a> 태그로도 요청할 수 있다.
  - Query 문자열을 전달하면서 GET 방식으로 요청할 때의 제한사항을 보안하기 위해서 POST 요청 방식이 추가되었다.
  - Post요청 방식 Query 문자열을 전달하면서 요청하는 것만 지원한다.
  - <form> 태그를 사용해서 요청하는 것만 가능하다.
 
 ## 2022/02/18

 - ### **CSRF** : Cross-site request forgery(사이트간의 요청 위조)
Get 방식은 보안이 필요하지 않은 경우에 사용하지만 Post 는 보안이 필요한 요청에 사용하기 때문에 외부로 부터의 공격을 차단하기 위해 서버에 요청을 하는 클라이언트가
서버에서 보낸 웹페이지로 부터의 요청인지 확인하기 위해서 Csrf token 이라는 것을 사용한다. 즉 장고에서는 csrf를 방지하기 위해서 post 요청시에는 csrf token을 사용해야만
요청할 수 있게 하고 있다. 이때 사용하는 태그가 {% csrf_token %}이다.
ex) 캡차
 
 - ### Query 문자열 
 
웹 클라이언트에서 웹 서버에게 정보 요청할 때 함께 전달하는 key = value 형식의 문자열
서버에게 무엇을 요청하는 것인지 좀 더 구체적으로 정보를 전달할 수 있게 된다.
문자열에서 어떤 이름의 값을 추출하려고 하는데 이름 자체가 없을 때는 None이 return되거나 기본값이 return된다. 이름은 있는데 비어있는 경우에는 ""(널문자열)이 return된다.
빈 값을 전달하는 것을 방지하기 위해서 required로 속성을 추가하면 좋을 것 같다.
 
 - ### Query 문자열 인코딩 규칙(Get과 Post방식이 똑같다)
    1. name = value 형식
    2. 여러개의 name = value는 &기호로 분리되어야 한다.
    3. 공백은 + 문자 또는 %20으로 전달된다.
    4. 영문과 숫자를 제외하고 %기호와 함께 16진수 코드값으로 구성
    5. ""(이름은 있는데 비어있으면 NULL), NONE(이름 요청이 없음)
  
 - ### Ajax
 Javascript로 구현해야 한다.(jQuery 라이브러리를 사용하면 구현 방법이 더 간단해 진다.)
 
 페이지 이동이 일어나지 않는다.
 
 데이터 전송량이 많이 축소되므로 모바일 환경에서는 더욱 적합하다.
 
 HTML, XML, JSON, ...응답형식에 제한이 없다.
 
 
 - ### Ajax 기술의 구현 방법
    1. XMLHttpRequest 객체를 생성한다.
  
    2. Ajax 기술로 서버에 요청하고 응답이 왔을 때 수행할 코드를 함수로 만들어서 load이벤트에 대한 핸들러를 등록한다.
 
    3. Ajax 통신으로 요청하려는 서버 프로그램의 URL 문자열을 가지고 정보를 작성한다. ref) Ajax는 Get방식을 많이 사용한다.
 
    4. Ajax 통신 요청을 서버에 보낸다
 
```javascript
  let req = new XMLHttpRequest();
  req.onload = 함수;
  req.open('요청방식','URL',true)
  req.send()
```

- ### Ajax 함수 구현
Ajax 통신에 대한 응답이 왔을 때 수행하게 되는 기능을 구현한다. 서버로 부터 응답되는 형식(일반 텍스트, HTML, XML, JSON, 이미지...)에 따라 구현 방법이 좀 달라진다.
req.responseText를 사용해서 응답된 내용을 읽는다. Json 응답일 때는 JSON.parse()를 사용해서 JS객체로 생성하여 사용한다.
 
 ## 2022/02/20
 
 - ### 사용자 정의 template tag 만들기
 1. templatetags라는 파일을 만든다.(__init__파일 자동생성)
 2. tag를 정의할 index.py를 만든다.(이름은 임의로 정한다.)
 3. 아래와 같은 함수를 정의한다.(list가 넘어오면 index접근을 가능하게 하기위한 함수이다.)
 
```python
 from django import template

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]
 ```
 4. template에 아래와 같이 작성한다.
 ```html
 {% load index %}
 <a href="{{ urls|index:forloop.counter0 }}">
     <li style="list-style-type:none;"><img src="{{ images|index:forloop.counter0 }}" class="slide_content slide0{{forloop.counter}}" alt=""></li>
 </a>
 ```
 
 
 ## 2022/03/04
 
 - ### 한글명 첨부파일을 강제 다운로드 시키기
 유니코드 파일명인 경우(예를 들어, 한글명 파일)는 따로 처리를 해줘야 한다. 강제 다운로드의 핵심은 Content-Disposition 헤더에 'attachment;'를 추가 해주는 것이다.
 ```python
filename_header = ‘filename*=UTF-8\’\’%s’ % urllib.quote(filename.encode(‘utf-8’))
response[‘Content-Disposition’] = ‘attachment; ‘ + filename_header
 ```

 ## 2022/03/11
 
 - ### DB 모델 생성 안 될때 
 
 https://velog.io/@haileeyu21/Error-dJango-migrate-%ED%96%88%EB%8A%94%EB%8D%B0-No-migrations-to-apply-%EC%9D%BC-%EA%B2%BD%EC%9A%B0
