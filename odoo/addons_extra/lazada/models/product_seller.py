# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductSeller(models.Model):
    _name = 'product.seller'
    _description = 'Product Seller'

    product_id = fields.Many2one('product.product',string='Product')
    seller_id = fields.Many2one('seller.seller',string='Seller')
    price_bidding = fields.Float(string = 'Current Price')
    seller_name_bidding = fields.Float(string = 'Current Seller Name')
    seller_code_bidding = fields.Float(string='Current Seller Code')

class ProductSellerBidding(models.Model):
    _name = 'product.seller.bidding'
