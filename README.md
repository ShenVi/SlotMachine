# SlotMachine
基于Python Flask开发的老虎机Dome 禁止商业使用或个人运营

#### 更新历史
|版本|内容|
|--|--|
|v1.0 |主要基础代码工程。|

#### 使用方法
下载dome到本地 安装依赖库 运行python run.py执行flask应用
默认访问地址为127.0.0.1 改用域名需要设置blueprint.py(蓝图)内的 app.config['SERVER_NAME'] 以及 app.register_blueprint的 subdomain='www'参数
项目使用数据库为mysql 请先在在 __config.py__ 内修改数据库地址 写你的数据库 并且在DB_module.py下解除db.create_all()的封印 即刻创建数据库表格

每个账户的默认注册金额为0 需要设置默认注册金额在 DB_account.py内的 Account类下 修改 __init__(self, accounts=None, money=0(修改成你要的默认用户金额)):

该工程只是一个dome 注册界面仅需填写一个账户即刻注册 登录页面输入账户即刻登录账户 需要密码的请在DB_account.py内的 Account类下添加password字段并且在登录添加密码验证的功能

#### 返回数据结构
{'code': 1, 'a': 1, 'b': 8, 'c': 4, 'reward': 0, 'type': 0, 'money': 60, 'roc_date': '2019-04-10 05:55:18', 'roc_expendituremoney': 5, 'roc_income': 0, 'roc_money': 60, 'data': '1 - 8 - 4'}
本项目全部页面采用ajax交互开发 可嵌套H5移动端 （仅限参考）

## 项目结构
    *app
        *account(账户api)
            *登录
            *注册
            *登出


        *game(游戏逻辑部分)
            *生成游戏结果
            *判断奖励机制
            *数据库消费记录生成


        *index*(主界面视图)
            *根据用户是否登录渲染指定文件 未登录渲染index 登录后渲染game


        *temolates
            *index.html 登录注册界面
            *game.html 游戏界面
            *roc.html 消费记录页面


        *DB_account.py 账户数据库
        *DB_module.py 扩展数据库（消费记录）
        *blueprint.py 蓝图模块
        *payment.py 支付
            *purchase() 每参与一次 扣除5元
            *gamereward() 奖励 更新用户金额添加数额


        *redis.py 储存游戏许可token

老虎机主界面
![Image text](https://github.com/ShenVi/SlotMachine/blob/master/img/1.jpg)
消费记录
![Image text](https://github.com/ShenVi/SlotMachine/blob/master/img/2.jpg)
登录注册界面
![Image text](https://github.com/ShenVi/SlotMachine/blob/master/img/3.jpg)
![Image text](https://github.com/ShenVi/SlotMachine/blob/master/img/4.jpg)