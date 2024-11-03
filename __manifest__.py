# __manifest__.py
{
    'name': 'Centro de Trabajo - Usuarios con Acceso',
    'version': '1.0',
    'author': 'Alphaqueb Consulting SAS',
    'category': 'Manufactura',
    'depends': ['mrp'],
    'data': [
        'vistas/centro_trabajo_vista.xml',
        'vistas/seguridad_reglas.xml', 
    ],
    'installable': True,
    'application': False,
    'summary': 'Permite seleccionar usuarios con acceso a cada centro de trabajo en Odoo',
}
