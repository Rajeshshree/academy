from odoo import models, fields, api


class academy(models.Model):
    _name = 'academy.academy'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float()
    value3 = fields.Char()

class stock(models.Model):
    _name = 'stock.stock'

    brand = fields.Many2one('rajesh.rajesh', ondelete='set null')
    name = fields.Many2one('laptop.brand.model')
    # name = fields.Many2one('laptop.brand.model', domain=[('brandname', '=', 'Apple')])
    value = fields.Integer("Stock")

    # @api.onchange('name')
    # def _brandname_onchange(self,**kw):

        # import pdb
        # pdb.set_trace()
    #      res = {}
    #      res['domain']={'self.brand':[('self.name', '=', self.brand)]}
    #      return res

    # @api.model
    # def create(self, vals):
    #     import pdb
    #     pdb.set_trace()


class rajesh(models.Model):
    _name = 'rajesh.rajesh'
    _rec_name = "Brandname"

    Brandname = fields.Char(string="Brandname")
    # stock_id = fields.One2many('stock.stock','rajesh_id', string="Brandname", required=True)

class model(models.Model):
    _name = 'laptop.brand.model'
    _rec_name = "Model_Number"

    Model_Number = fields.Char(string="Model Number")
    brandname = fields.Many2one('rajesh.rajesh', ondelete='set null')



class family(models.Model):
    _name = 'family.family'

    familyname = fields.Char("Family FullName")

# class Courses(models.Model):
#     _name = 'academy.courses'
#     _inherit = 'product.template'
#     name = fields.Char()
#     teacher_id = fields.Many2one('academy.teachers', string="Teacher")

# class ProductTemplate(models.Model):
#     _inherit = 'product.template'

#     teacher_id = fields.Many2one('academy.teachers', string="Teacher")

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char("")

    biography = fields.Html()
    # course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
#    instructor_id = fields.Many2one('res.partner', string="Instructor")
    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=[('instructor', '=', True)])
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

class course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")
