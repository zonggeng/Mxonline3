# 引入Django表单
from django import forms


# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空 密码不能少于5
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
