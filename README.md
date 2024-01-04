# Intro
## Requirement
1. 에디터 셋업 (pycharm)
	1. pycharm 설치방법
		1. https://www.jetbrains.com/pycharm/download/?section=mac
		2. 커뮤니티 .dmg 애플 실리콘
2. python 설치 (pyenv)
	1. 의존성 패키지 설치
	   `brew install openssl readline sqlite xz zlib`
	2. pyenv 설치
	   `brew install pyenv`
    3. pipenv 설치
       `brew install pipenv`
	4. pyenv-virtualenv 설치
	   `brew install pyenv-virtualenv`
## Hello World
1. Hello World 작성
```c
print("Hello World")
```
# Variable
## What is variable or constant?
python? 그냥 쓰면 돼
1. variable
```python
a = 10
b = '안녕하세요'
c = 0.1
d = True
```
2. ~~constant~~
상수가 따로 없음
## Type
1. int
2. float
3. bool
4. str
```python
a = 10
b = 0.1
c = '안녕하세요'
d = True
```
# Operation
## basic operation
1. `+`
2. `-`
3. `*`
4. `/`
5. `% (나머지)`
## compare operation
1. `>`, `<`
2. `>=`, `<=`
3. `==`, `is`, `!=`, `is not`
4. `and`
5. `or`
6. `not`
## complex assignment operation
1. `+=`
2. `-=`
3. `*=`
4. `/=`
5. `%=`
## 대입 연산자
1. `=`
# Print and Scan
## Print
1. print
2. f-string
```python
print("Hello World")
a = 10
print(f"a: {a}")
```
## Input
1. input
```python
a = input()
```
# Conditional
## if
1. if
2. else
3. elif
# Loop
## while
1. while
2. break
3. continue
## for
1. for
# Array
## one dimension array
1. `[]`
## two dimension array
1. `[][]`
# Function
## basic function
1. name, parameters, default value
```python
def myFunction(a, b=10):
	print("This is my function!")

```
2. variable lifecycle
# class
## basic class
1. class
```python
class Book:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def add(self):
		return self.a + self.b

book = Book(10, 20)
print(book.add())
```

