# flaskwork

项目名称：Takeaway Platform （外卖平台）
语言：python
框架：flask

因为赶着交所以做的有些简陋 大概实现了功能

最开始是一个主页  包含注册和登录功能，通过数据库中存储的账号类型来导向三个不同的个人中心（通过session来实现登录保持）
（注销功能忘记加到html里了）
个人中心有统一的修改密码功能

模块1：用户
包含点餐和查看订单和上传头像功能   （点餐功能实现了查看商店列表、进入商店主页  但是点餐页面的javascrip等还不会写所以还没有实现  先在数据库里存了假订单）
（商家的分类有存入了数据库里面，但是前端忘记搞了  只要做几个按钮然后分别slect数据库中不同类型的商家就行）

模块二：商家
包括编辑商店信息、上传菜品和查看商店主页功能

模块三：骑手
查看现有订单、接单和查看我接的单功能
