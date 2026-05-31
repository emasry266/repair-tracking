from odoo import models, fields


class RepairOrder(models.Model):
    _name = 'repair.order'
    _description = 'أوامر الصيانة'

    name = fields.Char(string='رقم الطلب', required=True)
    customer_name = fields.Char(string='اسم العميل', required=True)
    phone = fields.Char(string='رقم الهاتف')
    device = fields.Char(string='الجهاز', required=True)
    cost = fields.Float(string='التكلفة')

    # تم تعديل الحالات هنا لتتطابق تماماً مع شريط الحالات في الـ XML
    state = fields.Selection([
        ('draft', 'جديد / مسودة'),
        ('under_repair', 'تحت الصيانة'),
        ('done', 'تم التسليم')
    ], string='الحالة', default='draft', required=True)