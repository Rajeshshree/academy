from odoo import fields, models, api


class namelistwizardacademy(models.TransientModel):
    _name = "name.list.academy"

    name = fields.Char("Name")
    value = fields.Integer("value")
    value2 = fields.Float("value2")
    value3 = fields.Char("value3")

    @api.model
    def create(self, vals):
#        import pdb
#        pdb.set_trace()
        # self.env['academy.academy'].browse(self._context.get('active_id')).name = vals.get('name')
        shop = self.env['academy.academy'].browse(self._context.get('active_id'))
        #import pdb
        # pdb.set_trace()
        shop.write({
            'name': vals.get('name'),
            'value': vals.get('value'),
            'value2': vals.get('value2'),
            'value3': vals.get('value3')
            })
        return super(namelistwizardacademy, self).create(vals)

    @api.multi
    def write(self, vals):
        self.env['academy.academy'].browse(self._context.get('active_id')).name = vals.get('name')
        return super(namelistwizardacademy, self).write(vals)
