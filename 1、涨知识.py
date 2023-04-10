'''
xpath很灵活

选取父节点   /parent::*
包含
    //*[contains(@class,"666")]         //*[@class='666']
        //*[contains(name(),"sp")]      //sp
不包含
    //*[not(contains(@id,"qqq"))]
    //*[not(contains(text(),"qqq"))]

如果之前没有用到过的话，可以尝试一下
'''
# 已实践

'''
mysql、redis环境搭一下  后续需要用
'''
#mysql   self.conn = pymysql.Connect(host='106.13.1.144',port=3306,user='database1',password='admin',database='database1',charset='utf8',ssl={'ssl':{}})
#redis   DB_CONN = 'redis://:@106.13.1.144:6379/0'      TABLE_NAME = 'db0'
# 搞定
'''

q:那你大概计算一下每个平台五万个SKU，商品详情页 评论 qa，大概你写爬虫的话 ，需要写多久，爬虫需要运行多久

  
# 了解各大‍电商链接构成，面试可能会问，对后续实际工作也会有帮助
    京东    淘宝     苏宁     亚马逊
搜索
列表
详情
评论
qa
    
苏宁易购 链接都了解一下 大致写一个爬取步骤，不需要提取数据
    商品链接
    评论
    qa
1.对需求进行分析，明确需求，需要采集的具体字段，及目标网站的链接
分析网页，了解数据是服务器渲染还是客户端渲染。从而清楚怎样获取数据。服务器渲染就直接拿html数据  。客户端渲染就打开检查，看网络里面找对应的数据请求接口
通过排查找到能够获取数据的接口 PC端不好找可以尝试移动端

2.使用scrapy采集数据并存储
先采集列表页数据 抓取到shopId跟productId，然后组成详情页请求，通过yield抓取详情页数据通过parse方法解析，再提取评论id，请求评论接口获取评论数据
将获取到的数据通过管道提交给服务器。
每次爬取详情页前，先从服务器获取详情页链接，判断是否存在，存在就过滤掉  我知道这种方法可能会很慢，但不知道怎么做更好，实现增量式爬虫

3.根据需求，在管道实现 将采集到的产品productid做为主键，产品名称、价格、图片、关键字、评论文本、qa文本存入数据库,再次之前可以做一下数据清洗



苏宁
列表页接口：
https://search.suning.com/emall/mobile/wap/clientSearch.jsonp?cityId=755&keyword=%E5%86%B0%E7%AE%B1&channel=&cp=1&ps=10&st=0&set=5&cf=&iv=-1&ci=&ct=-1&channelId=WAP&sp=&sg=&sc=&prune=&operate=0&isAnalysised=1&istongma=1&jlfstoreCode=&jlfOnly=0&jlftownCode=&saleMode=&v=99999999&yjhx=&sesab=ABC0AAE&jzq=412&callback=success_jsonpCallback
其中keyword 是要搜索的关键字   cityId是城市编号  cp是页码  st是排序方式  jzq是添加了筛选条件  419就是默认 其他都是固定不变的
响应数据：其中catentdesc是标题名字  appAttrTitle是标签  dynamicImg图片地址前面需要拼接https:  catentryId 是产品id  salesCode是店铺id

详情页页面：https://m.suning.com/product/+店铺id+/+产品id+.html
详情页数据请求：https://pas.suning.com/nsenitemsale_000000012111740137_0071353485_5_999_190_755_7550199___________________1______________.html?_=1680167855473&callback=wapData
请求参数：店铺id  产品id  5_999_190_755_7550199这个是定值
响应参数：data-data1-data-clusterId 这个就是评论id


评论接口：
https://review.suning.com/mobile/business/mobile/getClusterReviewListOrFoldReviewListVI/cluster-38231625-000000012324720695-0070143049--total-1-default-10-----normal--callback1.htm?_=1680165064935&callback=callback1
请求参数  店铺id  产品id  38231625 是评论id
响应参数  content

qa接口：https://show.m.suning.com/mzis-web/qas/question/jsonp/questionListForCust_000000012111740137_0071353485__1_10__list1680167244530.html?callback=list1680167244530
请求参数  店铺id  产品id 时间戳    
响应参数   questionlist 里的text   answerlist 里的text


亚马逊 如上
    需要了解 US、DE、CA、JP这几个站点的
    US https://www.amazon.com/  美国加拿大德国日本
    DE https://www.amazon.de/
    DE https://www.amazon.ca/
    JP https://www.amazon.co.jp/
    
例如搜索的链接：https://www.amazon.co.jp/s?k=book
域名 + 参数k(搜索关键词)
'''
'''
亚马逊
列表页：
https://www.amazon.com/s?k=paula&__mk_zh_CN=亚马逊网站&ref=nb_sb_noss
请求参数k=watch
返回参数  直接是一个html页面
# //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div[3]/div[1]/h2/a
# //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div[2]/div[1]/h2/a
# //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[8]/div/div/div/div/div[2]/div[1]/h2/a
//*[contains(@class,'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')]   一般些部分就行，有时候会换位置
href="/-/zh/dp/B00EYVSOKY/ref=sr_1_6?__mk_zh_CN=亚马逊网站&amp;keywords=paula&amp;qid=1680173376&amp;sr=8-6"

详情页
https://www.amazon.com/-/zh/dp/B000GAWSDG/ref=sr_1_1?__mk_zh_CN=亚马逊网站&keywords=watch&qid=1680173667&sr=8-1
https://www.amazon.com/-/zh/dp/B008EPPIQ4/ref=sr_1_2?__mk_zh_CN=亚马逊网站&keywords=paula&qid=1680173376&sr=8-2
请求参数：直接从列表页获取请求连接拼接https://www.amazon.com
响应参数：

评论
https://www.amazon.com/-/zh/product-reviews/B00949CTQQ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
请求参数   只需要产品id  B00949CTQQ


qa



'''







'''
https://ec.minmetals.com.cn/open/home/platform-info
试着解一下参数种的 param
例如：param: "lkrjHqdMy7SBE/ub7oc7YIp4iqPWeco4ZPMzJaDAr0SMAYs/9o3+mnhjXZpqeI42p3KwXMUH9hp8EKj34oLFUcqy7fQQ2FEv2O5u2ydHQb+86UuRy+u91EbKBYOTOukU/K4dp7sshXgRF5T5mOcfyUwaDl9fKvuaZmkz7IRBi+8="
'''

