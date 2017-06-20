{
    'name': "SMS Framework",
    'version': "1.0.9",
    'author': "Sythil Tech",
    'category': "Tools",
    'support': "steven@sythiltech.com.au",
    'summary':'Allows you to send and receive smses from multiple gateways',
    'description':'Allows you to send and receive smses from multiple gateways',    
    'license':'LGPL-3',
    'data': [
        'views/sms_views.xml',
        'views/res_partner_views.xml',
        'views/sms_message_views.xml',
        'views/sms_template_views.xml',
        'views/sms_account_views.xml',
        'views/sms_number_views.xml',
        'views/sms_compose_views.xml',
        'views/ir_actions_server_views.xml',
        'data/ir.cron.csv',
        'data/res.country.csv',
        'data/ir.model.access.csv',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'depends': [],
    'images':[
        'static/description/3.jpg',
    ],
    'installable': True,
}