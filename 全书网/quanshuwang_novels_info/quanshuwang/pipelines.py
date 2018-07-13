# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, pymongo
from scrapy.conf import settings


class QuanshuwangPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写

    # 保存到本地
    # def process_item(self, item, spider):
    #     with open('info.json', 'a+', encoding='utf-8') as f:
    #         info_content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
    #         f.write(info_content)
    #     return item

import pymongo
import charts

# 分析别前忘了先备份数据
client = pymongo.MongoClient('192.168.1.8',27017)
# 数据库
db = client['quanben']
# 使用备份后的表
table = db['novel_infoX']

for i in table.find().limit(300):
    print(i['author'])


# 先去重
author_list = []
for i in table.find():
    author_list.append(i['author'])
author_set = list(set(author_list))
print(author_set)
print(len(author_set))# 得知这个网站总作者数是1245



# 再把去重之后的index 拿去count 总的
appear_times = []
t, others_num = 0, 0

for index in author_set:
    appear_time = author_list.count(index)
    if appear_time <= 5:  # 所有4部及以下作者名都变为otehrs
        author_set[t] = 'others'
        others_num = others_num + appear_time
    else:  # 其他不变
        appear_times.append(appear_time)
    t += 1

author_others_set = list(set(author_set))  # 去掉所有4部及以下作者
author_others_set.remove('others')  # 先删除others 已对应顺序
# appear_times.append(others_num)# 在列表里添加others的总作品数
# author_others_set.append('others')# 在列表里添加others

# print(others_num)
print(author_others_set)
print(appear_times)


# 把数据变成charts.plot所使用的格式
def data_gen(types):
    length = 0
    if length <= len(author_others_set):
        for author, times in zip(author_others_set, appear_times):
            data = {
                'name': author,
                'data': [times],
                'type': types
            }
            yield data
            length += 1
for i in data_gen('column'):
    print(i)





# 传入type参数, 所在柱状图
series = [data for data in data_gen('column')]
# 展示图片
charts.plot(series, show='inline', options=dict(title=dict(text='全本网小说主要作者与作品总数')))





