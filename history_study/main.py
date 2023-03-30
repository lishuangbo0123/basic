#
from lxml import etree
tree = etree.XML()
# tree = etree.XML(xml)
# tree = etree.parse(文件)
# tree = etree.HTML(html)
tree.xpath("/book/name/text()")
# //代表所有后代  *代表任意内容的一层节点  如果该节点是列表，则可用[1]来指定列表位置 xpath是从1开始的
# [@href='dapao'] 标签中href属性是href的节点   /@href   获取当前节点的属性为href的值
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    result = li.xpath("./a/text()")
    result1 = li.xpath("./a/@href")
