# 얼굴 인식 프로그램
### 이 코드는 이미지 학습을 위해 데이터 셋을 만드는 과정에서 학습의 정확도를 높이고자 만든 코드입니다.
***
> 코드 순서:
> 1. 학습시킬 이미지를 크롤링 한다.
> 2. 크롤링한 이미지를 읽어서 흑백으로 만든다.
> 3. Open cv나 haarcascade를 이용해서 얼굴 부분만 크롭한다.
> 4. 크롭한 이미지를 저장한다.
***
### 이미지 크롤링 코드는 selenium webdriver를 이용하기 때문에 chromedriver를 다운 받아야 한다.
```py
driver = webdriver.Chrome('자신의 chromedriver 경로')
```
***
### 파일들의 경로를 각자 자신의 경로로 바꾸어야 한다.
```py
count_num_path = '자신의 파일 경로'
```
***
## Example:
|원본|결과|
|--|--|
|![원본](https://i.imgur.com/DXSHFGr.jpg)|![결과](https://i.imgur.com/tiSOJg1.jpg)|
***
## 후기 ✌️
### teachable machine을 이용해서 학습을 시킨 작업이었는데 개인적으로 머신러닝에 입문을 하는 사람이라면 꼭 추천하고 싶은 사이트였다.
### 다음에는 직접 python 코드로 머신러닝 모델을 만들어 학습시킬 것이다.
