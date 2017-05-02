# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Lazada Service Bidding',
    'version' : '1.0',
    'summary': 'Lazada Service Bidding',
    'sequence': 41,
    'description': """
    Allow pull product from lazada seller
    Allow CRUD product to lazada seller
    """,
    'website': 'https://biga.vn',
    'depends' : ['product'],
    'data': [
        'views/menu_view.xml',
        'views/product_seller_view.xml',
        'views/seller_views.xml'
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
