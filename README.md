### `가상환경 설치 (python version:3.6+)`
```console
$ python -m venv fastapi 
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
