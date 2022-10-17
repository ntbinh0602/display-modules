# from odoo import http



import logging
from odoo.addons.web.models.models import Base
import odoo
import odoo.modules.registry
from odoo import http
from odoo.http import request
from odoo import _, _lt, api
_logger = logging.getLogger(__name__)
from werkzeug.wrappers import Request, Response


# ----------------------------------------------------------
# Odoo Web web Controllers
# ----------------------------------------------------------



class MbfAPPI(odoo.http.Controller):

    @http.route('/modules', type='json', auth="none", sitemap=False, cors='*')
    def search_mbf_app(self, uid, model, fields=False, offset=0, limit=False, domain=None, sort=None):
        env = request.env(user=uid or request.uid or odoo.SUPERUSER_ID)
        Model = env[model]
        return Model.web_search_read_mbf(domain, fields=fields, offset=offset, limit=limit, order=sort)

class LoginHome(Base):
    _inherit = 'base'

    @api.model
    def web_search_read_mbf(self, domain=None, fields=None, offset=0, limit=None, order=None):
        records = self.search_read(domain, fields, offset=offset, limit=limit, order=order)
        # return records
        # return http.request.render('display_module.modules', {
        #     records
        # })

        # return http.request.render("display_module.modules", {
        #             'data': records
        # })
        # return http.request.env['ir.ui.view'].render_template("display_module.modules", {'datas': records})

        # class CodeTheme(http.Controller):
#     @http.route('/modules', auth='public')
#     # def display_homepage(self, uid, model, fields=False, offset=0, limit=False, domain=None, sort=None):
#     def display_homepage(self, **kw):

        response = http.request.render('display_module.modules', {
            records
        })

        return response


        # headers = {'Content-Type': 'application/json'}
        # body = records

        # return Response(json.dumps(body), headers=headers)

