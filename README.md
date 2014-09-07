지금부터 웹 프로그램을 맨땅에서 부터 시작하기로 한다.
1. 먼저 웹을 구동시킬 전산 장비를 장만한다.
    참고로 내 전산 환경은 다음과 같다
    직원들이 쓰다가 느리다고 한쪽 구석에 쳐박아 놓은 펜티엄 1대(그래도 2코아)에 ubuntu14.04를 설치
    실서버로는 아마존 EC2 micro instance(한국에는 아직 없고 일본 동경 사이트) 1년 무료 ubuntu14.04
    이상 들어간 비용 $1 아마존에서 카드 인증시에 결제됨(이게 실제 지불해야하는 건지 환불되는 건지는 잘 모름)
2. 로칼 서버에다가 개발 환경을 구축한다.
    우분투14.04에는 Python 2.7과 3.4가 기본 깔려있는데 2.7을 사용하기로 한다.
    편집기는 PyCharm3.4 Community Version(이것도 공짜... 대머리 까지것네 ㅋㅋ)
    작업 디렉토리를 만들고 그리로 출근하자.

    $ mkdir -p work/InnoMVA
    $ cd work/InnoMVA
3. 첫번째 test를 작성한다.
4. 
    $ touch app-test.py
    [...]
    $ python app-test.py
Traceback (most recent call last):
  File "app-test.py", line 2, in <module>
    from app import app
ImportError: No module named app

    $ touch app.py
    [...]
    $ python app-test.py
Traceback (most recent call last):
  File "app-test.py", line 2, in <module>
    from app import app
  File "/home/cheon/work/InnoMVA/app.py", line 1, in <module>
    from flask import Flask
ImportError: No module named flask

$ virtualenv env
New python executable in env/bin/python
Installing setuptools, pip...done.

$ source env/bin/activate
(env)[base]16:38:21-cheon~/work/InnoMVA$

이제 python virtualenv 환경에 있다는 걸 알 수 있다.
빠져나오는 방법은
(env)[base]16:40:59-cheon~/work/InnoMVA$ deactivate
[base]16:41:03-cheon~/work/InnoMVA$

virtualenv에서 pip가 실행되는 지 확인하고
(env)[base]16:41:48-cheon~/work/InnoMVA$ which pip
/home/cheon/work/InnoMVA/env/bin/pip

flask를 설치한다.
(env)[base]16:41:54-cheon~/work/InnoMVA$ pip install flask

그리고 다시 app-test를 실행시키면,
(env)[base]16:44:32-cheon~/work/InnoMVA$ python app-test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.011s

OK

아싸! 성공이다.
이 테스트로 이용자가 웹브라우져로 http://localhost:5000 에 접속하면
우리가 작성한 코드가 정상적으로 작동해서,
요구한 페이지를 가져왔다는 것(response.status_code==200)을 알 수 있다.

그러나 아직 이 첫 페이지에는 아무런 내용도 없으므로 무언가 내용을 뿌려주는 테스트를
만들어 일부러 Failure를 만든다.
이것이 바로 Test Driven Development 의 핵심이니까...

app-test.py

          self.assertEqual(response.status_code, 200)
+         self.assertEqual(response.data, u"InnoMVA: 주식회사 이노지투비")

(env)[base]16:45:43-cheon~/work/InnoMVA$ python app-test.py
F
======================================================================
FAIL: test_landing_page (__main__.BasicTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "app-test.py", line 12, in test_landing_page
    self.assertEqual(response.data, u"InnoMVA: 주식회사 이노지투비")
AssertionError: 'Hello world!' != u'InnoMVA: \uc8fc\uc2dd\ud68c\uc0ac \uc774\ub178\uc9c0\ud22c\ube44'

----------------------------------------------------------------------
Ran 1 test in 0.012s

FAILED (failures=1)

헐? 아니 아싸! 이건 예상했던 오류기 때문에 아싸!
참 잘했기 때문에 여기서 한바탕 쉬기 위해 버전관리를 하자.

$ git init
Initialized empty Git repository in /home/cheon/work/InnoMVA/.git/
(env)[base]17:03:40-cheon~/work/InnoMVA (master)$

env 디렉토리에는 python 프로그램이 들어있으므로 버전관리에서 제외한다.
그리고 python compiled files *.pyc도 제외한다.
(env)[base]17:06:04-cheon~/work/InnoMVA (master)$ vi .gitignore

+ env/*
+ *.pyc
+ .idea

(env)[base]17:11:29-cheon~/work/InnoMVA (master)$ git add .
(env)[base]17:11:31-cheon~/work/InnoMVA (master)$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   .gitignore
	new file:   README
	new file:   app-test.py
	new file:   app.py

우리가 작성한 파일이 커밋을 기다리고 있다.
커밋한 다음 로그를 확인하고 육신의 건강을 위해 잠시 서성이기로 한다.

(env)[base]17:11:32-cheon~/work/InnoMVA (master)$ git commit -m "테스트 추진 홈페이지 개통되었슈~"
[master (root-commit) 00404ea] 테스트 추진 홈페이지 개통되었슈~
 4 files changed, 154 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README
 create mode 100644 app-test.py
 create mode 100644 app.py
(env)[base]17:14:19-cheon~/work/InnoMVA (master)$ git log
commit 00404eaf1497ed646d3dc7e73a31460091f4510b
Author: kecheon <kecheon@gmail.com>
Date:   Sat Sep 6 17:14:19 2014 +0900

    테스트 추진 홈페이지 개통되었슈~




자 이제 앞의 오류를 고쳐보자.

[...]
@app.route('/')
def index():
    return u"InnoMVA: 주식회사 이노지투비"
[...]

(env)[base]18:36:53-cheon~/work/InnoMVA (master)$ python app-test.py
Traceback (most recent call last):
  File "app-test.py", line 2, in <module>
    from app import app
  File "/home/cheon/work/InnoMVA/app.py", line 6
SyntaxError: Non-ASCII character '\xec' in file /home/cheon/work/InnoMVA/app.py on line 6, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details

엥? 이 머꼬?
아항~ 한글이 제대로 처리되지 못했네...

app.py 맨 앞에다가
+ #-*-coding:utf8-*-

(env)[base]18:41:06-cheon~/work/InnoMVA (master)$ python app-test.py
/usr/lib/python2.7/unittest/case.py:505: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if not first == second:
F
======================================================================
FAIL: test_landing_page (__main__.BasicTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "app-test.py", line 12, in test_landing_page
    self.assertEqual(response.data, u"InnoMVA: 주식회사 이노지투비")
AssertionError: 'InnoMVA: \xec\xa3\xbc\xec\x8b\x9d\xed\x9a\x8c\xec\x82\xac \xec\x9d\xb4\xeb\x85\xb8\xec\xa7\x80\xed\x88\xac\xeb\xb9\x84' != u'InnoMVA: \uc8fc\uc2dd\ud68c\uc0ac \uc774\ub178\uc9c0\ud22c\ube44'

----------------------------------------------------------------------
Ran 1 test in 0.013s

FAILED (failures=1)

헉! 니 왜그냐?

$ vi env/lib/python2.7/site.py

525 def setencoding():
526     """Set the string encoding used by the Unicode implementation.  The
527     default is 'ascii', but if you're willing to experiment, you can
528     change this."""
529    - encoding = "ascii" # Default value set by _PyUnicode_Init()
529    + encoding = "utf8" # Default value set by _PyUnicode_Init()
530     if 0:
531         # Enable to support locale aware default string encodings.
532         import locale

이렇게 파이ㅌ선 환경을 바꿔주고 다시 테스트

(env)[base]18:44:27-cheon~/work/InnoMVA (master)$ python app-test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.011s

OK

아싸!
이제 홈페이지가 뭔가가 나온다 얘기니 확인!
웹브라우저 불여시를 열고 주소창에 http://localhost:5000

Unable to connect

Firefox can't establish a connection to the server at localhost:5000.

음마? 요 여시 잠 보소잉,  나 이런거 써넣은적 없는디~
아!

(env)[base]18:45:24-cheon~/work/InnoMVA (master)$ python app.py
 * Running on http://127.0.0.1:5000/

요로코롬 웹서버를 구동혀야 제대로 나오제...
흠흠! 조아부렀어.

근데 모양이 쪼까 허섭스럽구마이~
요즘은 속보다 겉이 우선인게
위치도 잡고 색칠도 해야겠는데,
웹디자이너를 데려오면 좋기는 하겠지만 돈이 들고,
돈들여 데려와도

@app.route('/')
def index():
    return u"InnoMVA: 주식회사 이노지투비"

여기다 어떻게 디자인을 입힌다냐?
파이ㅌ선 코드에다 html을 입혀줄 디자이너는 몸값 겁~나 높...

그래서 template을 활용해서 디자인과 코드를 분리해야 한다.
우리가 사용하는 프레임웤은 flask이고
flask는 jinja2 template을 사용하고 있다.
그래서 테스트도 flask에 좀더 적합한 flask-test를 사용하도록
refactoring 하기로 한다.
refactoring은 test가 성공한 상태에서 해야 하므로
test Failure가 없는 지 확인하고 commit을 한 다음 refactoring을 하기로 한다.

(env)[base]19:19:19-cheon~/work/InnoMVA (master)$ python app-test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.011s

OK

(env)[base]19:19:27-cheon~/work/InnoMVA (master)$ git commit -am "홈페이지 헤더 추가"
[master 3de19f9] 홈페이지 헤더 추가
 1 file changed, 7 insertions(+)

먼저 app-test.py에서 flask test를 사용하도록 한다.

[...]
+ from flask.ext.testing import TestCase

- class BasicTestCase(unittest.TestCase):
+ class BasicTestCase(TestCase):
[...]

(env)[base]19:19:35-cheon~/work/InnoMVA (master)$ python app-test.py
Traceback (most recent call last):
  File "app-test.py", line 4, in <module>
    from flask.ext.testing import TestCase
  File "/home/cheon/work/InnoMVA/env/local/lib/python2.7/site-packages/flask/exthook.py", line 87, in load_module
    raise ImportError('No module named %s' % fullname)
ImportError: No module named flask.ext.testing


플라스크 테스트를 깔아야 되네...
(env)[base]19:25:45-cheon~/work/InnoMVA (master)$ pip install flask-testing
Downloading/unpacking flask-testing
  Downloading Flask-Testing-0.4.2.tar.gz (40kB): 40kB downloaded
[...]

(env)[base]19:27:13-cheon~/work/InnoMVA (master)$ python app-test.py
Traceback (most recent call last):
  File "app-test.py", line 15, in <module>
    unittest.main()
 [...]
  File "/home/cheon/work/InnoMVA/env/local/lib/python2.7/site-packages/flask_testing/utils.py", line 82, in create_app
    raise NotImplementedError
NotImplementedError

헐~
할 수 없이 메뉴얼을 봤더니...(https://pythonhosted.org/Flask-Testing/)
create_app() 이란 놈을 해 줘야 flask testing을 할 수가 있군.

You must specify the create_app method, which should return a Flask instance:

from flask import Flask
from flask.ext.testing import TestCase

class MyTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

If you don’t define create_app a NotImplementedError will be raised.

메뉴얼이 시키는 대로 app-test.py에 create_app()을 정의해 주고
(env)[base]19:34:48-cheon~/work/InnoMVA (master)$ python app-test.py
Traceback (most recent call last):
 [...]
  File "/home/cheon/work/InnoMVA/env/local/lib/python2.7/site-packages/flask_testing/utils.py", line 97, in _pre_setup
    self.app = self.create_app()
  File "app-test.py", line 8, in create_app
    app = Flask(__name__)
NameError: global name 'Flask' is not defined

헐~헐~ Flask도 import 해야하고...
해 줄거 다 한 다음
(env)[base]20:12:56-cheon~/work/InnoMVA (master)$ python app-test.py
.E
======================================================================
ERROR: test_use_template (__main__.BasicTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "app-test.py", line 23, in test_use_template
    self.assert_template_used('home.html')
  File "/home/cheon/work/InnoMVA/env/local/lib/python2.7/site-packages/flask_testing/utils.py", line 159, in assertTemplateUsed
    raise RuntimeError("Signals not supported")
RuntimeError: Signals not supported

----------------------------------------------------------------------
Ran 2 tests in 0.014s

FAILED (errors=1)

엥? 이건 또 멍미?
겁나 구글링 한 다음
(env)[base]20:14:37-cheon~/work/InnoMVA (master)$ pip install blinker
Downloading/unpacking blinker
  Downloading blinker-1.3.tar.gz (91kB): 91kB downloaded
  Running setup.py (path:/home/cheon/work/InnoMVA/env/build/blinker/setup.py) egg_info for package blinker

Installing collected packages: blinker
  Running setup.py install for blinker

Successfully installed blinker
Cleaning up...
(env)[base]20:17:16-cheon~/work/InnoMVA (master)$ python app-test.py
.F
======================================================================
FAIL: test_use_template (__main__.BasicTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "app-test.py", line 23, in test_use_template
    self.assert_template_used('home.html')
  File "/home/cheon/work/InnoMVA/env/local/lib/python2.7/site-packages/flask_testing/utils.py", line 164, in assertTemplateUsed
    raise AssertionError("template %s not used" % name)
AssertionError: template home.html not used

----------------------------------------------------------------------
Ran 2 tests in 0.013s

FAILED (failures=1)

아싸! 원하는 failure 도출 성공.
수많은 삽질로 뭐가 어찌 됐는지 어리둥절한데 요점은 blink를 설치해야 template rendering을 테스트할 수 잇다는 사실
복잡한 과정이 있었고 결과가 나왔으므로 커밋 한번 해주기로 한다.

이제 home.html 이란 템플릿을 사용하도록 코딩하면 된다.
template은 여러개 생길 것이고 디자이너가 이용할 파일들이므로 별도의 디렉토리에 두기로 한다.
$ mkdir templates
$ cd templates
$ touch home.html

home.html 의 내용을 집어옇고 테스트 시행하니

(env)[base]21:27:21-cheon~/work/InnoMVA (master)$ python app-test.py
F.
======================================================================
FAIL: test_landing_page (__main__.BasicTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "app-test.py", line 17, in test_landing_page
    self.assertEqual(response.data, u"InnoMVA: 주식회사 이노지투비")
AssertionError: '<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title>InnoMVA: \xec\xa3\xbc\xec\x8b\x9d\xed\x9a\x8c\xec\x82\xac \xec\x9d\xb4\xeb\x85\xb8\xec\xa7\x80\xed\x88\xac\xeb\xb9\x84</title>\n</head>\n<body>\n    <h2>InnoMVA: \xec\xa3\xbc\xec\x8b\x9d\xed\x9a\x8c\xec\x82\xac \xec\x9d\xb4\xeb\x85\xb8\xec\xa7\x80\xed\x88\xac\xeb\xb9\x84</h2>\n</body>\n</html>' != u'InnoMVA: \uc8fc\uc2dd\ud68c\uc0ac \uc774\ub178\uc9c0\ud22c\ube44'

----------------------------------------------------------------------
Ran 2 tests in 0.016s

FAILED (failures=1)


어어 예측 못한 에라가 발생했네...
home.html에는 여러가지 tag가 붙어있어서 assertEqual은 적합하지 않다.

$ vi app-test.py
        - self.assertEqual(response.data, u"InnoMVA: 주식회사 이노지투비")
        + self.assertIn(u"InnoMVA: 주식회사 이노지투비", response.data)

(env)[base]21:30:27-cheon~/work/InnoMVA (master)$ python app-test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.016s

OK

흠흠! 아주 좋군.
그런데 한가지 이상한 점은 home.html이 templates 디렉토리 안에 있는데,
flask는 신통하게 그걸 알아서 찾아오네, 난 아직 아무런 path정보를 만들어주지 않았는데 말이다.
왜 그렇게 되는지는 차차 확인하기로 하자 아님 말고.

아하! 이건 flask가 디폴트 templates 디렉토리를 사용한다고 문서에 나와 있다.

이제 템플릿을 사용해서 홈피가 렌더링되니까 home.html을 원하는 만큼 예쁘게 만들면 되고!
내가 애용하는 방법은 twitter bootstrap인데 디자이너 없이도 그럴듯한 홈피를 만들 수 있게 해준
트위터 디자인팀에게 무한 감사하면서...
다음 오류 테스트를 작성하자.
다음 할 일은 home.html에 bootstrap을 입히는 것으로 한다.

$ vi app-test.py
from flask import url_for

    def test_apply_css(self):
        response = self.client.get(url_for('static', filename='custom.css'))
        self.assertEqual(response.status_code, 200)

(env)[base]22:17:52-cheon~/work/InnoMVA (master)$ python app-test.py
F..
======================================================================
FAIL: test_apply_css (__main__.BasicTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "app-test.py", line 27, in test_apply_css
    self.assertEqual(response.status_code, 200)
AssertionError: 404 != 200

----------------------------------------------------------------------
Ran 3 tests in 0.018s

FAILED (failures=1)


흠! 아직 static 디렉토리 설치하지 않았으므로 당연한 결과를
flask는 디폴트로 static 디렉토리를 참조한다.

$ mkdir static
$ touch static/custom.css

(env)[base]22:26:09-cheon~/work/InnoMVA (master)$ python app-test.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.020s

OK


이제 custom.css에 스타일시트를 정의하고 템플릿에서 사용하면 된다.
그런데 bootstrap 하나만으로도 충분히 원하는 디자인이 가능하다.

그러면 flask에서 bootstrap을 활용하기는 방법을 살펴보자.

$ pip install flask-boostrap
$ vi app.py
+ from flask.ext.bootstrap import Bootstrap
[...]
+ bootstrap = Bootstrap(app)

flask-bootstrap이 설치된 뒤에는 템플릿 파일에서 bootstrap css class를 사용하면 된다.
home.html에 bootstrap class를 적용해 보기로 하자.

(env)[base]22:37:32-cheon~/work/InnoMVA (master)$ cat templates/home.html
{% extends "bootstrap/base.html" %}
{% block title %}InnoMVA: 주식회사 이노지투비{% endblock %}
{% block content %}
    <div class="jumbotron">
        <h2>InnoMVA: 주식회사 이노지투비</h2>
    </div>
{% endblock %}

home.html의 내용을 위와 같이 바꾸고 테스트하면
(env)[base]22:44:03-cheon~/work/InnoMVA (master)$ python app-test.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.027s

OK

오끼도끼 It's time to git!
$ git diff *.py
$ git commit -am "bootstrap 적용"

잠깐 정리하면 이 웹앱을 구동하기 위해 설치된 패키지들이 뭐였지?

(env)[base]22:47:28-cheon~/work/InnoMVA (master)$ pip freeze >requirements.txt
(env)[base]22:50:50-cheon~/work/InnoMVA (master)$ cat requirements.txt
Flask==0.10.1
Flask-Bootstrap==3.2.0.2
Flask-Testing==0.4.2
Jinja2==2.7.3
MarkupSafe==0.23
Werkzeug==0.9.6
argparse==1.2.1
blinker==1.3
itsdangerous==0.24
wsgiref==0.1.2

흠흠~ 뭐시지~ 뭔지도 모르겠다만 여하튼 현재까지 이런 패키지들이 설치되었다.

reqirements.txt를 커밋하고 여기서 일단락 짓기로 한다.



