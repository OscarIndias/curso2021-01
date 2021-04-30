from odoo import models , fields, api

class CreateTicket(models.TransientModel):
    _name = "create.ticket"
    _description = "create a new ticket"

    name = fields.Char()

    def create_ticket(self):
        self.ensure_one()
        active_id = self._context.get('active_id', False)
        if active_id and self._context.get('active_model') == 'helpdesk.ticket.tag':
            ticket = self.env['helpdesk.ticket'].create({
                'name' : self.name,
                'tag_ids':[(6,0,[active_id])]
            })
            action = self.env.ref('helpdesk_oscarindias.helpdesk_ticket').read()[0]
            action['res_id'] = ticket.id
            action['views'] = [(self.env.ref('helpdesk_oscarindias.view_helpdesk_ticket_form').id, 'form')]
            return action
        return {'type':'ir.actions.act_window_close'} 