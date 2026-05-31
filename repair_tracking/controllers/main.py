from odoo import http
from odoo.http import request

class RepairWebsite(http.Controller):

    # 1. شاشة البحث (إدخال رقم الهاتف)
    @http.route(['/repair/check'], type='http', auth='public', website=True, sitemap=False)
    def repair_check_page(self, **kwargs):
        # إجبار أودو على البحث عن الـ template ورندرتها داخل الموقع
        return request.render('repair_tracking.check_status_page', {})

    # 2. استقبال البيانات وعرض النتيجة
    @http.route(['/repair/status'], type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def repair_status_result(self, **kwargs):
        phone = kwargs.get('phone', '').strip()
        
        order = False
        if phone:
            # البحث في موديل الصيانة برقم الهاتف
            order = request.env['repair.order'].sudo().search([('phone', '=', phone)], limit=1)
        
        return request.render('repair_tracking.status_result_page', {
            'order': order,
            'phone': phone
        })