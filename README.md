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
