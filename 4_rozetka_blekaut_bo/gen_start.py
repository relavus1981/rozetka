#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import strftime

data_now = strftime("%Y-%m-%d %H:%M")

# Запись данных в файл
start_file = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE yml_catalog SYSTEM "shops.dtd">
<yml_catalog date="{data_now}">
<shop>
<name>RolloLine</name>
<company>ФОП Мельник Р.А.</company>
<url>https://snug.biz.ua</url>
<currencies>
<currency id="UAH" rate="1"/>
</currencies>
<categories>
<category id="1" rz_id="4627673">Жалюзи и ролеты</category>
</categories>
<offers>
"""
my_file = open('/home/relavus/rozetka.xml', 'w')
my_file.write(start_file)
my_file.close()