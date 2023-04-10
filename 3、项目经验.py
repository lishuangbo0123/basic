'''
2021年文档苏宁：
自营店铺shop_id目前发现的是1和3开头，非自营店铺是7开头

需求用时
试着理解一下。不理解的晚上给你讲。你记好问题

##### Core:

由于苏宁的商品链接都是细化到对应变体的，故core不需要抓变体

目前日度的Core主数据大概1万条左右，可以正常抓完
--------------------------------------日度的主数据是什么决定的，是不是反爬机制决定的   还是需求决定的  coach
目前并发开的比较低，暂时没遇到其他反爬之类的问题，预计core有30万左右的盈余空间
ls = [1232332,232342,2342,243234]
ls1 = [1232332,232342,2342,]

ls2 = [1232332,232342,2342,]
ls3 = [1232332,232342,2342,]

set
目前抓取速率：

网络环境良好的状况下，目前1000条主数据链接 / 10
min，跑完日度的core需要100min，app
同
web

可能出现的需求，给n个关键词，需要知道每个关键词前100的排名及广告，还有自己家产品sku的排名是多少
##### Search:
-----------------------------每日一万条链接，一条链接大概30条数据   关键词去重大概是3000条？
目前所有search关键词总共3000左右，每日落盘数据30万左右，可以正常抓完
---------------日度  是每日采集量么
预计日度关键词总量6000以内没什么问题

目前抓取速率：

网络环境良好的状况下，目前1000条主数据关键词 / 10
min，跑完日度的search需要30min，app
同
web

##### IM：

目前周度im
关键词总共1500左右（月度geo
im关键词也有1500左右），周度落盘40万

im目前并发开的比较低，预计关键词总量5千以内，周度可以抓完


目前抓取速率：

网络环境良好的状况下，目前1000条主数据关键词 / 1500
min，跑完周度需要40个小时左右

##### review:

目前日度主数据8000多，每日落盘数据9000左右

预计review有10万左右的盈余空间

目前抓取速率：
redis的数据类型   set (只有value) z-set（有序的set,有key-value）hash (无序 有key-value) list str txt
review是先进详情页再进评论页，假设商品一天内评价少于十条（不需要翻评论页），则速率为1000条主数据链接 / 20
min，
跑完日度的review需要180min
'''
部署服务器端怎么操作？
'''
def a():
        '''
    服务管理命令：
    systemctl      例子：systemctl status redisd
    service    例子：service redisd status
    启动、停止、重启、尝试重启、重载、强制重载、状态
    start, stop, restart, try-restart, reload, force-reload, status

    设置chromedriver位可执行文件
    chmod a+x chromedriver

    JumpServer 部署安装脚本

    Usage:
      jmsctl [COMMAND] ...
      jmsctl --help

    Commands:
      install      安装 JumpServer
      start        启动 JumpServer
      stop         停止 JumpServer
      restart      重启 JumpServer
      status       检查 JumpServer
      uninstall    卸载 JumpServer
      upgrade      升级 JumpServer
      reset        重置组件

esc 退出文本编辑
vim dadas.txt
i 开始编辑


:quit()
:w
:wq
:q!
:w!



    如： ./jmsctl.sh install

    Upgrade
    cd /opt/setuptools
    git pull
    ./jmsctl.sh upgrade

    JumpServer 启动成功!
    Web 登陆信息: http://172.18.187.29:8000
    SSH 登录信息: ssh admin@172.18.187.29 -p2222
    初始用户名密码: admin admin

    [如果你是云服务器请在安全组放行 8000 和 2222 端口]




    k8s项目管理工具    docker项目打包工具   文件服务器
    https://www.jianshu.com/p/dbcba32c2de4
        '''




