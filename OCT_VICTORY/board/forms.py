from django import forms
from .models import Article, Comment

# Form/ ModelForm : 1. Data validation 2. HTML 생성
class AriclesForm(forms.ModelForm):
    # 1. HTML을 어떻게 만들 것인가?
    # 2. 검증 한다면, 어떤 조건으로 검증할 것인가?(title에 들어갈 자료를 form가 검증하는 것)
    # 3. 만약 아무것도 쓰지 않는다면,
        # 1. ModelForm은 Model을 알고 있기 때문에,
        # 2. 각 Model을 읽고, 알아서 HTML + 검증을 함
    title = forms.CharField(min_length=2, max_length=20)
    # content 에 대해 어떤 검증 /HTML 관련해 적지 않음 => models.Article 의 content 항목을 보고 할일을 한다.

    class Meta:
        model = Article
        # fields 에 적힌 컬럼은 검증 하겠다.
        fields = ('title', 'content', ) 


class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=20)

    class Meta:
        model = Comment
        fields = ('content', )  # 튜플이 리스트보다 훨씬 메모리를 절약할 수 있다