#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ruslan N Bogatirenko"
__copyright__ = "Copyright 2017, The uInformed Project"
__credits__ = ["Ruslan N Bogatirenko", "Igor V Fomichov"]
__license__ = "GPL"
__version__ = "3.0.0"
__maintainer__ = "Ruslan N Bogatirenko"
__email__ = "neuro@abz.kiev.ua"
__status__ = "preProduction"

from flask import Blueprint, render_template, session, redirect, request
from datetime import datetime, timedelta
import time
from time import mktime
from common.xparcer import BankParcer
from common.html import html
h = html()
p = BankParcer()


banks = Blueprint('banks', __name__)

@banks.route("/bank", methods=['GET','POST'])
def banks_page():
    if request.method == 'POST':
        if request.form['date']:
            date = request.form['date']
            print(date)
        if 'prev' in request.form:
            if 'date' not in session:
                date = str(datetime.now().date() - timedelta(days = 1))
                session['date'] = date
                #print(date)
            else:
                d=datetime.fromtimestamp(mktime(time.strptime(session['date'],'%Y-%m-%d')))
                d = d - timedelta(days = 1)
                date = d.strftime('%Y-%m-%d')
                session['date'] = date
                #print(date)
        if 'next' in request.form:
            if 'date' not in session:
                date = str(datetime.now().date() + timedelta(days = 1))
                session['date'] = date
                #print(date)
            else:
                d=datetime.fromtimestamp(mktime(time.strptime(session['date'],'%Y-%m-%d')))
                d = d + timedelta(days = 1)
                date = d.strftime('%Y-%m-%d')
                session['date'] = date
                #print(date)
        print(session)
    else:
        session['date']=str(datetime.now().date())
        date = str(datetime.now().date())
        print(session)
    try:
        cassa = h.gen_summary_html(p.xml2dict_summary_bank("0", date),"0", date)
        ext_id_0 = h.gen_ext_bank(p.xml2dict_ext_bank("0", date), date)
    except:
        cassa = u"Нет данных"
        ext_id_0 = u'Нет контировок'
    try:
        bank_2 = h.gen_summary_html(p.xml2dict_summary_bank("2", date),"2", date)
        ext_id_2 = h.gen_ext_bank(p.xml2dict_ext_bank("2", date), date)
    except:
        bank_2 = u"Нет данных"
        ext_id_2 = u"Нет контировок"        
    try:
        bank_3 = h.gen_summary_html(p.xml2dict_summary_bank("3", date),"3", date)
        ext_id_3 = h.gen_ext_bank(p.xml2dict_ext_bank("3", date), date)
    except:
        bank_3 = u"Нет данных"
        ext_id_3 = u"Нет контировок"
    try:
        bank_4 = h.gen_summary_html(p.xml2dict_summary_bank("4", date),"4", date) 
        ext_id_4 = h.gen_ext_bank(p.xml2dict_ext_bank("4", date), date)
    except:
        bank_4 = u"Нет данных"
        ext_id_4 = u"Нет контировок"



    return render_template('banks.html', 
                            bank_id_0=cassa, bank_id_2=bank_2, 
                            bank_id_3=bank_3, bank_id_4=bank_4,t='a',
                            ext_id_3=ext_id_3, ext_id_2=ext_id_2, ext_id_4=ext_id_4, ext_id_0=ext_id_0,
                            title=u" Банковские счета "+str(date), footer=__copyright__+' '+str(__credits__)+' status: '+__status__+' '+__version__)

