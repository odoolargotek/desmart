# -*- coding: utf-8 -*-
{
    'name': 'AhoraSoft Factura de Compra',
    'version': '1.0.0',
    'category': 'Stock',
    'author': 'Ahorasoft',
    'summary': 'Customized Warehouse Management for Bolivia',
    'website': 'http://www.ahorasoft.com',
    'depends': [
        'base',
        'base_setup',
        'account',
        'product',
        'report_xlsx',
        'as_bo_configuration',
        'colesa_campos_base_1_0',

    ],
    'data': [
        'security/as_group_view.xml',
        'security/ir.model.access.csv',
        'data/as_tipo_factura_proveedor.xml',
        'views/as_tipo_factura_view.xml',
        'views/as_invoice_supplier.xml',
        'views/as_format_report.xml',
        'wizard/as_purchase_libro_compras.xml',
        'report/as_libro_compras_pdf.xml',
        'views/as_tipo_retencion.xml',
        # 'views/as_res_partner.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}