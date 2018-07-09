# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class QuanshuwangPipeline(object):
    if not os.path.exists('F:\py_projects\zhizhupaojiao\全书网\quanshuwang\\Novels'):
        os.mkdir('F:\py_projects\zhizhupaojiao\全书网\quanshuwang\\Novels')
    def process_item(self, item, spider):
        # 切换到全部小说文件夹
        os.chdir('F:\py_projects\zhizhupaojiao\全书网\quanshuwang\\Novels')
        # 创建新的单个小说文件夹
        if not os.path.exists(str(item['title'])):
            os.mkdir(str(item['title']))
        # 进入新的单个小说文件夹
        os.chdir('F:\py_projects\zhizhupaojiao\全书网\quanshuwang\\Novels' + os.path.sep + str(item['title']))
        # if not os.path.exists('info.txt'):
        #     with open('info.txt', 'w+') as f:
        #         info_content = item['title'] + '\n' + item['author'] + '\n' + item['category']
        #         f.write(info_content)
        # os.chdir('/home/pyvip/python/project/quanshuwang/Novels/' + item['title'])
        # if not os.path.exists(item['title'] + '.txt'):
        with open(item['chapter'] + '.txt', 'w+') as f:
            novel_chapter = item['chapter'] + '\n'
            f.write(novel_chapter)
            for each in item['content']:
                rs1 = "".join(each.split())
                # print(rs1)
                rs2 = rs1 + '\n'
                f.write(rs2)
        return item


