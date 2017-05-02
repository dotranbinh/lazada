# -*-  coding: utf-8 -*-
from odoo import fields,models,api

class Seller(models.Model):
    _name = 'seller.seller'

    name = fields.Char(string='Name',required=True)
    code = fields.Char(string='Code',required=True)
    url_api = fields.Char(string='Url API',required=True)
    user_id = fields.Char(string='User ID',required=True)
    api_key = fields.Char(string='Api Key',required=True)