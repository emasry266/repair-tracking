{
    'name': 'Repair Tracking',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Repair Tracking System',
    'author': 'Ehab',
    'depends': [
        'base',
        'website',  # تم إضافة موديول الموقع الإلكتروني هنا لتمكين الـ Controllers والصفحات العامة
    ],
'data': [
        'security/ir.model.access.csv',
        'views/repair_order_views.xml',
        'views/website_repair_templates.xml',
    ],
    'installable': True,
    'application': True,
}