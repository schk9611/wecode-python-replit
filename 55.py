# Database 클래스 구현
# Database 클래스 내부에 다음의 속성(attrubute) 선언
# ･ name : database의 이름
# ･ size : 저장할 수 있는 데이터의 max 사이즈. Size를 넘어서는 데이터를 저장할 수 없다.

# Insert
# self 외에 2개의 parameter를 받는다.(field 와 value)
# field는 저장하고자 하는 데이터의 필드명이고 value는 값이다
# field와 value는 내부적으로 dictionary에 저장되어야 한다.
# insert 메소드 호출
# (객체이름이 db 라는 가정하에) db.insert("name", "정우성")
# insert 메소드는 특별한 return 값은 없다.
# 단, 만일 내부 dictionary의 총 사이즈가 Database 클래스의 size 속성보다 크면 더이상 새로운 값들을 저장하지 말아야 한다.

# Select
# self 외에 1개의 parameter를 받는다.(field)
# field는 읽고자 하는 데이터의 필드명이다.
# 내부적으로 데이터를 저장하고 있는 dictionary에서 해당 field에 해당하는 키와 연결되어 있는 값을 return 해주어야 한다.
# 예를 들어, 이미 name이라는 필드명으로 "정우성"이라는 값을 저장했다고 한다면:
# db.select("name")
# "정우성"
# 이 되어야 한다.
# 해당 필드값으로 지정되어 있는 값이 없다면 None을 return 한다.

# Update
# self 외에 2개의 parameter를 받는다.(field와 value)
# 이름 그대로 이미 저장되어 있는 값을 수정하는 메소드이다.
# db.update("name", "아이유")
# 만일 field값에 해당하는 데이터가 저장되어 있지 않으면 아무것도 하지 않는다.
# 특별한 return 값이 없다.

# Delete
# self 외에 1개의 parameter를 받는다.(field)
# field는 지우고자 하는 데이터의 필드명이다.
# db.delete("name")
# 만일 field 값에 해당하는 데이터가 저장되어 있지 않으면 아무것도 하지 않는다.
# 특별한 return 값은 없다.

class Database:
    def __init__(self, name, size):
        self.name = name  # name 변수 초기화
        self.size = size  # size 변수 초기화
        self.dict = {}  # 데이터의 값을 저장할 dictionary 생성

    def insert(self, field, value):
        if len(self.dict) < self.size:  # dictionary의 크기가 size보다 작을 경우 데이터 생성
            self.dict[field] = value

    def select(self, field):
        if field not in self.dict:  # field 값이 dict에 없다면
            return None  # None을 리턴
        else:  # 있다면
            return self.dict[field]  # field 값을 키로 갖는 dict의 value 리턴

    def update(self, field, value):
        if field in self.dict:  # field 값이 dict에 있다면
            self.dict[field] = value  # field 값을 키로 갖는 value 값을 수정

    def delete(self, field):
        if field in self.dict:  # field 값이 dict에 있다면
            del self.dict[field]  # 일치하는 값 삭제
