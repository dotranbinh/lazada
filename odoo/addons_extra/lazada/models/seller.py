# -*-  coding: utf-8 -*-
from odoo import fields,models,api

import urllib
from hashlib import sha256
from hmac import HMAC
from datetime import datetime
import json

class Seller(models.Model):
    _name = 'seller.seller'

    name = fields.Char(string='Name',required=True)
    code = fields.Char(string='Code',required=True)
    url_api = fields.Char(string='Url API',required=True)
    user_id = fields.Char(string='User ID',required=True)
    api_key = fields.Char(string='Api Key',required=True)

    @api.multi
    def get_products_seller(self):
        for seller in self:
            parameters = {
                'UserID': seller.user_id,
                'Version': '1.0',
                'Action': 'GetProducts',
                'Format': 'json',
                'Timestamp': datetime.utcnow().replace(microsecond=0).isoformat()
            }
            api_key = str(seller.api_key)
            concatenated = urllib.urlencode(sorted(parameters.items()))
            parameters['Signature'] = HMAC(api_key, concatenated, sha256).hexdigest()
            concatenated = urllib.urlencode(sorted(parameters.items()))
            url = '{0}?{1}'.format(seller.url_api, concatenated)
            res = urllib.urlopen(url)
            print res.read()['SuccessResponse']
            data = json.loads(res.read().decode('utf-8'))
            print data
        return True