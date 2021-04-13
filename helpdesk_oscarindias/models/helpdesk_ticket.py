from odoo import models,fields

class Helpdeskticket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Ticket"

    name = fields.Char(string = "name")
    description = fields.Text(string = "description")
    date = fields.Date(string = "fecha")
