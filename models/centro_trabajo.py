# modelos/centro_trabajo.py
from odoo import models, fields

class CentroTrabajo(models.Model):
    _inherit = 'mrp.workcenter'

    usuarios_acceso = fields.Many2many(
        'res.users',
        string="Usuarios con Acceso"
    )
