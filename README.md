# SlotMachine
基于Python Flask开发的老虎机Dome 禁止商业使用或个人运营

#### 使用方法
下载dome到本地 安装依赖库 启动地址为127.0.0.1 需要mysql支持

在 __config.py__ 内修改数据库地址

## 项目结构
    *app
    **account(账户api)
    ***登录
    ***注册
    ***登出
    **game(游戏逻辑部分)
    ***生成游戏结果
    ***判断奖励机制
    ***数据库消费记录生成
    **index*(主界面视图)
    ***根据用户是否登录渲染指定文件 未登录渲染index 登录后渲染game
    **temolates
    ***index.html 登录注册界面
    ***game.html 游戏界面
    ***roc.html 消费记录页面
    **DB_account.py 账户数据库
    **DB_module.py 扩展数据库（消费记录）
    **blueprint.py 蓝图模块
    **payment.py 支付
    ***purchase() 每参与一次 扣除5元
    ***gamereward() 奖励 更新用户金额添加数额
    **redis.py

老虎机主界面
![Image text](https://github.com/ShenVi/SlotMachine/blob/master/img/1.jpg)
消费记录
![Image text](https://github.com/ShenVi/SlotMachine/blob/master/img/2.jpg)
登录注册界面
![Image text](https://github.com/ShenVi/SlotMachine/blob/master/img/3.jpg)
![Image text](https://github.com/ShenVi/SlotMachine/blob/master/img/4.jpg)