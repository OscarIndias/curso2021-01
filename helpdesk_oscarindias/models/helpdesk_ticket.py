from odoo import models,fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
from datetime import timedelta

class helpdeskticketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Action'

    name = fields.Char()
    date = fields.Date()
    time = fields.Float(
        string='time')
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

    @api.model 
    def cron_delete_tag(self):
        tickets = self.search([('ticket_ids','=',False)])
        tickets.unlink()

class Helpdeskticket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Ticket"

    def _date_default_today(self):
        return fields.Date.today()

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
    
    color = fields.Integer("color index")
    name = fields.Char(string = "name", required = True)
    description = fields.Text(string = "description")
    date = fields.Date(string = "fecha", default = _date_default_today)
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
    time = fields.Float(string = 'Time', compute = '_get_time', inverse = '_set_time')
    assigned = fields.Boolean(string = 'Assigned',
     readonly=True)
    date_limit = fields.Date(string = 'Date Limit')
    action_corrective = fields.Html(string='Corrective Action',
     help = 'Descrive corrective actions to do')
    action_preventive = fields.Html(string = 'Preventive Action',
     help = 'Descrive preventive actions to do')

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

    @api.constrains("time")
    def time_constraint(self):
        for ticket in self:
            if ticket.time and ticket.time < 0:
                raise ValidationError(_("The time can not be nagative"))
 


    @api.onchange('date', 'time')
    def _onchange_date(self):
        self.date_limit = self.date and self.date + timedelta(hours=self.time)


    def _get_time(self):
        

    def _set_time(self):


    @api.depends('user_id')
    def _compute_ticket_qty(self):
        other_tickets = self.env['helpdesk.ticket'].search([('user_id','=', self.user_id.id)])
        self.ticket_qty = len(other_tickets)
    
    tag_name = fields.Char(
        string='Tag Name')

    def create_tag(self):
        self.ensure_one()
        #opcion 1
        # self.write({
        #     'tag_ids': [(0,0,{'name': self.tag_name})]
        # })
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
        # self.tag_name = False
        action = self.env.ref('helpdesk_oscarindias.create_tag_action').read()[0]
        action['context'] = {
            'default_name':self.tag_name,
            'default_ticket_ids':[(6,0,self.ids)]
        }
        return action  
    
    
    

    