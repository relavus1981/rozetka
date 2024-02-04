#!/usr/bin/env python3
# -*- coding: utf-8 -*-

end_file = """</offers>
</shop>
</yml_catalog>"""

my_file = open('/home/relavus/rozetka.xml', 'a')
my_file.write(end_file)
my_file.close()