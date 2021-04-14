from odoo import models, fields

class taller(models.Model):
    _name = "taller.taller"
    _description = "taller"

    nombre = fields.Char(string = "nombre")
    fecha = fields.Date(string = "fecha")
    descripcion = fields.Text(string = "descripcion")