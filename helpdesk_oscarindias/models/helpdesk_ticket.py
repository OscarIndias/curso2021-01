from odoo import models,fields, api
class helpdeskticketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Action'

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='ticket')
    
class helpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'tag'
    name =fields.Char()
    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='tickets')

class Helpdeskticket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Ticket"
    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='tags')
    
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='actions')
    
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='user_id')
    

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

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = self.user_id and True or False

    ticket_qty = fields.Integer(
        string='ticket Qty',
        compute='_compute_ticket_qty')

    @api.depends('user_id')
    def _compute_ticket_qty(self):
        for record in self:
            other_tickets = self.env['helpdesk.ticket'].search([('user_id','=', record.user_id.id)])
            record.ticket_qty = len(other_tickets)
    
    tag_name = fields.Char(
        string='Tag Name')

    def create_tag(self):
        self.ensure_one()
        #opcion 1
        self.write({
            'tag_ids': [(0,0,{'name': self.tag_name})]
        })
        # #opcion 2
        # tag = self.env['helpdesk.ticket.tag'].create({
        #     'name':sel.tag_name
        # })
        # self.write({
        #     'tag_ids': [(4,tag_id,0)]
        # })
        # #opcion3
        # tag = self.env['helpdesk.ticket.tag'].create({
        #     'name':sel.tag_name
        # })
        # self.write({
        #     'tag_ids': [(6,0,tag_id)]
        # })
        self.tag_name = False
    
    
