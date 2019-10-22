from django.db import models


# ★★ models.Model을 상속받는 class에서 클래스 멤버 변수는 무.조.건 테이블의 컬럼이 됨 ★★  
class Article(models.Model):
    # id(pk)는 자동생성됨 id(pk) = INTEGER AUTO INCRFEMNT UNIQUE
    title = models.CharField(max_length=20)  # 이 줄을 쓰면 django ORM 에서 SQL문으로 바꿔서 DB에 저장하게 됨
    content = models.TextField()
    # 처음 저장(.save())될 때에만 시간 추가함
    created_at = models.DateTimeField(auto_now_add=True)
    # 저장(.save())될 때의 시간을 저장
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta를 쓰지않고 ordering 을 정의하면 ordering이라는 컬럼을 만듦(article정보에 대한 정보를 작성)
    class Meta:
        ordering = ['-created_at', ]

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


'''
0. DB를 다루고 싶지만, SQL 쓰기 싫다
1. DB 다룬다.
    1) 테이블 만들고 싶다
        - 테이블의 schema는 이렇게 되었으면 좋겠다.  => models.py에 class/멤버변수 정의
        - DB 전문가(ORM)에게 내 소원이 적절한지 물어보자  => $ makemigrations
        - (소원이 적절하면)ORM이 견적서를 만들어 줌 => APP/migrations/000N_... 파일(견적서 볼 필요 없음)
        - 소원이 바뀌면, 소원을 다시 적는다
        - 소원 바뀌면 =>다시 견적 받기
        ...
        - OK 견적서대로 갑시다 => $ migrate
        - 전문가(ORM)가 DB에 반영
    - ** 만약 db 망하면 => $ python manage.py migrate board zero 후, migrations의 0001, 0002, ... 지우면 됨 (db를 無로 만드는 과정)
'''





