# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session

class MyscrapPipeline(object):

    def __init__(self):
        basename = 'data_proxies.db'
        _engine = create_engine("sqlite:///%s" % basename, echo=False)
        _connection = _engine.connect()
        _metadata = MetaData()
        table_name='proxies'
        _stack_items = Table(table_name, _metadata,
                             Column("id", Integer, primary_key=True),
                             Column("proxy_address", String))
        _metadata.create_all(_engine)
        self.connection = _connection
        self.stack_items = _stack_items

    def process_item(self, item, spider):
            try:
                ins_data = self.stack_items.insert().values(
                proxy_address=item['proxy_address'],)
                self.connection.execute(ins_data)
            except IntegrityError:
                    print('WE ARE DUMPING')
            return item	

