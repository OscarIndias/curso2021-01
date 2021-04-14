from odoo import models,fields

class Helpdeskticket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Ticket"

    name = fields.Char(string = "name", required = True)
    description = fields.Text(string = "description")
    date = fields.Date(string = "fecha")
    estado = fields.Selection(
        [('nuevo', 'Nuevo'), 
        ('asignado', 'Asignado'),
        ('proceso', 'En proceso'),
        ('pendiente','Pendiente'),
        ('resuelto', 'Resuelto'),
        ('cancelado', 'Cancelado')],
        string= 'State',
        default= 'nuevo'
    )
    time = fields.Float(sting = 'Time')
    assigned = fields.Boolean(string = 'Assigned',
     readonly=True)
    date_limit = fields.Date(string = 'Date Limit')
    action_corrective = fields.Html(string='Corrective Action',
     help = 'Descrive corrective actions to do')
    action_preventive = fields.Html(string = 'Preventive Action',
     help = 'Descrive preventive actions to do')
