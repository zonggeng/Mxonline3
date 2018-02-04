import xadmin

from .models import EmailVerifyRecord, Banner


# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']

    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']

    # 配置筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


# 创建banner的管理类
class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
