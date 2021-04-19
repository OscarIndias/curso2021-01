from odoo import models,fields

class Helpdeskticket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Ticket"

    name = fields.Char(string = "name", required = True)
    description = fields.Text(string = "description")
    date = fields.Date(string = "fecha")
    state = fields.Selection(
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


    # @api.model
    # def close_leads(self):
    #     active_tickets = self.search([('active', '=', True)])
    #     for ticket in active_tickets:
    #         ticket.close()

    def do_assign(self):
        self.ensure_one()
        for ticket in self:
            ticket.state = 'asignado'
            ticket.assigned = True

    def proceso(self):
        self.ensure_one()
        self.state = 'proceso'
    
    def pendiente(self):
        self.ensure_one()
        self.state = 'pendiente'

    def resuelto(self):
        self.ensure_one()
        self.state = 'resuelto'

    def cancelado(self):
        self.ensure_one()
        self.state = 'cancelado'
