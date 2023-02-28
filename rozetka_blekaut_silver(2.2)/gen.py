import dn_setting as dns
from itertools import cycle


class PromItem:
    def __init__(self, sku, title, title_ua, image, size, price, price_promo, color, color_cod, bcolor, bcolor_cod, color_ua, description, description_ua):
        self.sku = sku
        self.title = title
        self.title_ua = title_ua
        self.image = image
        self.size = size
        self.price = price
        self.price_promo = price_promo
        self.color = color
        self.color_cod = color_cod
        self.bcolor = bcolor
        self.bcolor_cod = bcolor_cod
        self.color_ua = color_ua
        self.description = description
        self.description_ua = description_ua
    def __repr__(self):
        return self.title



hub = []

for i in dns.products:
    for j in dns.price.keys():
        sku = f'silver{i["tkan"]}{j}'
        title = f'Рулонная штора термо {i["tkan"]} (ролета блэкаут) солнцезащитная светонепроницаемая DecoSharm {j}x170 см {i["color_ru"].capitalize()}'
        title_ua = f'Рулонна штора термо {i["tkan"]} (ролета блекаут) сонцезахисна світлонепроникна DecoSharm {j}x170 см {i["color_ua"].capitalize()}'
        image = i['img']
        size = j
        price = round(dns.price[j] * dns.kurs * dns.nacenka)
        price_promo = round(dns.price[j] * dns.kurs * dns.nacenka * dns.promo_skidka)
        color = i['ottenok']
        color_cod = i['ottenok_valuecode']
        bcolor = i['basic_color']
        bcolor_cod = i['basic_color_valuecode']
        color_ua = i['color_ua']
        description = dns.description
        description_ua = dns.description_ua
        hub.append(PromItem(sku, title, title_ua, image, size, price, price_promo, color, color_cod, bcolor, bcolor_cod, color_ua, description, description_ua))

"""
# Запись данных в файл
my_file = open('/home/relavus/rozetka.xml', 'a')
for item in hub:
    my_file.write(f'<offer id="{item.sku}" available="true" product_in_promotion="true">\n')
    my_file.write(f'<price>{item.price}</price>\n')
    my_file.write('<category code="3806">Рулонні штори</category>\n')
    my_file.write('<attribute_set code="3806">Рулонні штори</attribute_set>\n')
    my_file.write(f'<name lang="ru">{item.title}</name>\n')
    my_file.write(f'<name lang="ua">{item.title_ua}</name>\n')
    my_file.write(f'<picture>{item.image}</picture>\n')
    my_file.write('<picture>https://raw.githubusercontent.com/relavus1981/prom/master/red.jpeg</picture>\n')
    my_file.write('<picture>https://raw.githubusercontent.com/relavus1981/prom/master/blue.jpg</picture>\n')
    my_file.write('<picture>https://raw.githubusercontent.com/relavus1981/prom/master/bech.jpeg</picture>\n')
    my_file.write('<picture>https://raw.githubusercontent.com/relavus1981/prom/master/silver.jpg</picture>\n')
    my_file.write(f'<description lang="ru">{item.description}</description>\n'.format(item.size,item.color))
    my_file.write(f'<description lang="ua">{item.description_ua}</description>\n'.format(item.size,item.color_ua))
    my_file.write('<vendor code="49ae5405a4d211e580cf42f2e9bc64ff">DECO SHARM</vendor>\n')
    my_file.write('<country_of_origin code="ukr">Украина</country_of_origin>\n')
    my_file.write('<param name="Комплектация" paramcode="767">готовое к установке изделие, крепежи</param>\n')
    my_file.write('<param name="Тип ткани" paramcode="5336" valuecode="bb8c2cfc042748092c71095e262f6113">полиэстер</param>\n')
    my_file.write('<param name="Вид" paramcode="7276" valuecode="27b1db5570aba99ee5add7782acfa4a3">рулонная штора</param>\n')
    my_file.write('<param name="Длина" paramcode="2470">170</param>\n')
    my_file.write(f'<param name="Ширина ткани" paramcode="11924">{item.size}</param>\n')
    my_file.write(f'<param name="Базовый цвет" paramcode="12097" valuecode="{item.bcolor_cod}">{item.bcolor}</param>\n')
    my_file.write('<param name="Дизайн" paramcode="4844" valuecode="990223541e83ec0fbfa47b7cf1e8fa40">однотонный</param>\n')
    my_file.write('<param name="Тип крепления" paramcode="5312" valuecode="e8fe28bf92057e51cf7b96cef39e8fae">на створку окна</param>\n')
    my_file.write('<param name="Упаковка" paramcode="5344" valuecode="46535740eea34f31afd9b9894c1988c2">блистер</param>\n')
    my_file.write('<param name="Материал полотна" paramcode="5416" valuecode="ba4476f70260837d2bc5bf41f2add933">ткань</param>\n')
    my_file.write('<param name="Вид ролеты" paramcode="12506" valuecode="38f7fbb68daa533fd776bd61c562e0ee">термо (blackout)</param>\n')
    my_file.write(f'<param name="Оттенок" paramcode="2099" valuecode="{item.color_cod}">{item.color}</param>\n')
    my_file.write('<param name="Мера измерения" paramcode="measure" valuecode="measure_pcs">шт.</param>\n')
    my_file.write('<param name="Минимальная кратность товара" paramcode="ratio">1</param>\n')
    my_file.write('<param name="Стиль" paramcode="5135" valuecode="a7deaa6d3e56fa0fe6dbf845e23decd6">современный</param>\n')
    my_file.write('</offer>\n')
my_file.close()
"""


# Запись данных в файл
my_file = open('/home/relavus/rozetka.xml', 'a')
for item in hub:
    my_file.write(f'<offer id="{item.sku}" available="true">\n')
    my_file.write(f'<price>{item.price}</price>\n')
    my_file.write(f'<price_promo>{item.price_promo}</price_promo>\n')
    my_file.write('<stock_quantity>10</stock_quantity>\n')
    my_file.write('<currencyId>UAH</currencyId>\n')
    my_file.write('<categoryId>1</categoryId>\n')
    my_file.write(f'<picture>{item.image}</picture>\n')
    my_file.write('<picture>https://raw.githubusercontent.com/relavus1981/prom/master/red.jpeg</picture>\n')
    my_file.write('<picture>https://raw.githubusercontent.com/relavus1981/prom/master/blue.jpg</picture>\n')
    my_file.write('<picture>https://raw.githubusercontent.com/relavus1981/prom/master/bech.jpeg</picture>\n')
    my_file.write('<picture>https://raw.githubusercontent.com/relavus1981/prom/master/silver.jpg</picture>\n')
    my_file.write(f'<name>{item.title}</name>\n')
    my_file.write(f'<name_ua>{item.title_ua}</name_ua>\n')
    my_file.write(f'<article>{item.sku}</article>\n')
    my_file.write(f'<vendor>DecoSharm</vendor>\n')
    my_file.write(f'<description><![CDATA[ {item.description} ]]></description>\n'.format(item.size,item.color))
    my_file.write(f'<description_ua><![CDATA[ {item.description_ua} ]]></description_ua>\n'.format(item.size,item.color_ua))
    my_file.write(f'<param name="Материал" paramid="95285"><![CDATA[ Полиэстер, Текстиль ]]></param>\n')
    my_file.write(f'<param name="Размеры" paramid="99600">{item.size}x170 см</param>\n')
    my_file.write(f'<param name="Ширина" paramid="95292">{item.size} см</param>\n')
    my_file.write(f'<param name="Висота" paramid="95299"><![CDATA[ 100 см, 105 см, 110 см, 115 см, 120 см, 125 см, 130 см, 135 см, 140 см, 145 см, 150 см, 155 см, 160 см, 165 см, 170 см, 175 см, 180 см, 185 см, 190 см, 195 см, 200 см, 210 см, 220 см, 230 см ]]></param>\n')
    my_file.write(f'<param name="Цвет" paramid="95306">{item.color}</param>\n')
    my_file.write(f'<param name="Декорирование" paramid="113211">Однотонные модели</param>\n')
    my_file.write(f'<param name="Страна-производитель товара" paramid="98900">Украина</param>\n')
    my_file.write(f'<param name="100% светонепроницаемость" paramid="127260">Да</param>\n')
    my_file.write(f'<param name="Гарантия" paramid="20769">12 месяцев</param>\n')
    my_file.write(f'<param name="Тип" paramid="95278"><![CDATA[ Ролеты тканевые, Рулонные шторы ]]></param>\n')
    my_file.write(f'<param name="Механизм" paramid="95327"><![CDATA[ Цепочный, Навесной, На крючках ]]></param>\n')
    my_file.write('</offer>\n')
my_file.close()
