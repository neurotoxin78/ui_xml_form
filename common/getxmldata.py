#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ruslan N Bogatirenko"
__copyright__ = "Copyright 2017, The uInformed Project"
__credits__ = ["Ruslan N Bogatirenko", "Igor V Fimichev"]
__license__ = "GPL"
__version__ = "3.0.0"
__maintainer__ = "Ruslan N Bogatirenko"
__email__ = "neuro@abz.kiev.ua"
__status__ = "Production"

from datetime import datetime
import urllib.request, urllib.error

# import codecs, sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

# print sys.getdefaultencoding()


#[type_id]
# Типы данных
#0 = FinansKassa
#1 = FinansBank
#2 = Monitor

#[bank_id]
# Имена файлов банков 0 - это касса, то есть type_id 0 bank_id 0 - касса; type_id 1 bank_id 3 - Банк Пивденный
#0 = 
#1 = KBKPB
#2 = KBKiev
#3 = KBPivden
#4 = KBVBR

#[monitor_id]
# Имя файла монитора
#0 = Monitor

class config(object):

    """Docstring for config. """

    def __init__(self):
        """@todo: to be defined1. """
    def typeid(self):
        """@todo: Docstring for typeid.
        :returns: @todo

        """
        type_id = {'0':'FinansKassa', '1':'FinansBankOper', '2':'Monitor'}
        return type_id

    def bankid(self):
        """@todo: Docstring for bankid.
        :returns: @todo

        """
        bank_id = {'0':'', '1':'KPB', '2':'Alyans', '3':'Pivden', '4':'VBR'}
        return bank_id

    def monitorid(self):
        """@todo: Docstring for monitorid.
        :returns: @todo

        """
        monitor_id = {'0':'Monitor'}
        return monitor_id

c = config()



class get_xml_data(object):

    """Docstring for soap. """

    def __init__(self):
        """@todo: to be defined1. """

    def get_xml_file(self, type_id='0', bank_id='0',date=str(datetime.now().date())):
        """@todo: Docstring for function.
        :arg1: @todo
        :returns: @todo
        """
        tid = c.typeid()
        bid = c.bankid()
        filepart = tid[type_id]+bid[bank_id]
        filename = filepart+"_"+date+".xml"
        print (filename)
        try:
            with urllib.request.urlopen('http://127.0.0.1:8008/'+filename) as f:
                data = f.read()
            try:
                return data.decode('utf-8-sig')
            except:
                return data.decode('utf-8-BOM')
        except urllib.error.HTTPError as e:
            return e.code



    def get_data(self, type_id='0', bank_id='0', date=str(datetime.now().date()) ):
        """@todo: Docstring for get_data.

        :type_id: @todo
        :bank_id: @todo
        :monitor_id: @todo
        :returns: @todo

        """
        return self.get_xml_file(type_id, bank_id, date)

if __name__ == "__main__":
    raw=get_xml_data()
    print(raw.get_data("2","0"))
