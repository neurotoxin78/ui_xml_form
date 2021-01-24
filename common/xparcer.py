#!/usr/bin/python3
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
from common.getxmldata import get_xml_data
from xml.etree.ElementTree import fromstring, ElementTree


class BankParcer(object):

    """Get xml file """

    def __init__(self):
        """@todo: to be defined1. """
        self.data = get_xml_data()

    def xml2dict_summary_bank(self, bank_id, date=datetime.now().date()):
        if bank_id == '0':
            xml = self.data.get_data('0',bank_id, date)
        else:
            xml = self.data.get_data('1',bank_id, date)            
        tree = ElementTree(fromstring(xml.encode('utf-8')))
        root = ElementTree.getroot(tree)
        children = root.getchildren()
        for item in children:
            summary = item.attrib
        return summary

    def xml2dict_ext_bank(self, bank_id, date=str(datetime.now().date())):
        """@todo:  Выборка расширеной информации"""
        if bank_id == '0':
            xml = self.data.get_data('0',bank_id, date)
        else:
            xml = self.data.get_data('1',bank_id, date)  
        tree = ElementTree(fromstring(xml.encode('utf-8')))
        root = ElementTree.getroot(tree)
        eb = root.getchildren()
        data_list=[]
        for items in eb[0].getchildren():
            data_list.append(items.attrib)
        return data_list


class MonitorParcer(object):

    """Docstring for MonitorParcer. """

    def __init__(self):
        """@todo: to be defined1. """
        self.data = get_xml_data()
          
    def monitor2dict(self, monitor_id, date=str(datetime.now().date())):
        """@todo: Docstring for monitor2dict.

        :arg1: @todo
        :returns: @todo

        """
        data_list=[]
        xml = self.data.get_data('2', '0', date)
        tree = ElementTree(fromstring(xml.encode('utf-8')))
        root = ElementTree.getroot(tree)
        child_dict={}
        for item in root:
            part_name = item.attrib['NSName']
            child = item.getchildren()
            child_dict[part_name]=child
        list_of_attribs=[]
        tuples=()
        for keys in child_dict:
            data = child_dict[keys]
            for items in data:
                attrib_tuple=()
                data = items.attrib
                attrib_tuple = data['str_name'], data['str_value']
                tuples = keys, attrib_tuple
                list_of_attribs.append(tuples)
        return list_of_attribs


