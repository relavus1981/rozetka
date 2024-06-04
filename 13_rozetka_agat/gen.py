import dn_setting as dns
from itertools import cycle


class PromItem:
    def __init__(self, sku, title, title_ua, image, size, price, price_promo, color, color_ua, description, description_ua):
        self.sku = sku
        self.title = title
        self.title_ua = title_ua
        self.image = image
        self.size = size
        self.price = price
        self.price_promo = price_promo
        self.color = color
        self.color_ua = color_ua
        self.description = description
        self.description_ua = description_ua
    def __repr__(self):
        return self.title



hub = []

for i in dns.rolet:
    for j in dns.price.keys():
        sku = f'agat{i[0]}{j}'
        title = f'Рулонная штора агат {i[0]} Decoharm {j}x170 см {i[1]}'
        title_ua = f'Рулонна штора агат {i[0]} DecoSharm {j}x170 см {i[2]}'
        image = i[3]
        size = j
        price = round(dns.price[j] * dns.kurs * dns.nacenka + 70)
        price_promo = round(dns.price[j] * dns.kurs * dns.nacenka * dns.promo_skidka)
        color = i[1]
        color_ua = i[2]
        description = dns.description
        description_ua = dns.description_ua
        hub.append(PromItem(sku, title, title_ua, image, size, price, price_promo, color, color_ua, description, description_ua))


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
    my_file.write(f'<param name="100% светонепроницаемость" paramid="127260">Нет</param>\n')
    my_file.write(f'<param name="Гарантия" paramid="20769">12 месяцев</param>\n')
    my_file.write(f'<param name="Тип" paramid="95278"><![CDATA[ Рулонные шторы, Ролеты тканевые ]]></param>\n')
    my_file.write(f'<param name="Механизм" paramid="95327"><![CDATA[ Цепочный, Навесной, На крючках ]]></param>\n')
    my_file.write('</offer>\n')
my_file.close()
