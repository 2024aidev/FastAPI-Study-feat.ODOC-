### `가상환경 설치 (python version:3.6+)`
```console
$ python -m venv <가상환경이름>  
```
### `가상환경 실행`
- mac
```console
$ . <가상환경이름>/bin/activate
```
- window 
```console
source <가상환경이름>/scripts/activate
```
### `설치`
```console
$ pip install -r requirements.txt
```
### `서버 실행`
```console
$ uvicorn main:app --reload
```
### `서버 종료`
- window
```console
$ ctrl + c
```
- mac
```console
$ command + c
```
### `가상환경 종료`
```console
$ deactivate
```

### `폴더 설명`
server2 : 간단하게 fastapi서버에서 데이터 불러오기 실습용



### for mac 
**\*기본적인 터미널 명령어**

설치 가능한 파이썬 버전확인 : pyenv install --list

파이썬 설치 : pyenv install 3.7.10 (3.7.10은 위에서 설치가능한 버전중 하나)

설치후 버전 확인 : pyenv versions

가상환경 이름짓기 : pyenv virtualenv py37 (py37은 가상환경 이름) 

가상환경 실행 : pyenv activate py37 (py37은 가상환경 이름) 

가상환경 종료 : pyenv deactivate

[https://jiyeonseo.github.io/2016/07/27/install-pyenv/](https://jiyeonseo.github.io/2016/07/27/install-pyenv/)

 [python 개발 환경을 위한 pyenv 설치하기 | Daily Log

python 개발 환경을 위한 pyenv 설치하기 pyenv? Simple Python version management 프로젝트 별로 각각 맞는 다양한 python 버전으로 실행해 볼 수 있도록 환경 제공. 이 프로젝트에서는 python 2, 저 프로젝트에서

jiyeonseo.github.io](https://jiyeonseo.github.io/2016/07/27/install-pyenv/)

[https://stackoverflow.com/questions/33321312/cannot-switch-python-with-pyenv](https://stackoverflow.com/questions/33321312/cannot-switch-python-with-pyenv)

 [Cannot switch Python with pyenv

I would like to use pyenv to switch python2 and python3. I successfully downloaded python2 and python3 and pyenv with following codes. brew install pyenv brew install pyenv-virtualenv pyenv ins...

stackoverflow.com](https://stackoverflow.com/questions/33321312/cannot-switch-python-with-pyenv)
