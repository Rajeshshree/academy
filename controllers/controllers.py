# -*- coding: utf-8 -*-
import werkzeug

from odoo import http
from odoo.http import request


class Academy(http.Controller):

    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([]),
        })

    @http.route('/academy/delete/<model("academy.teachers"):obj>', auth='public', website=True, method='GET')
    def delete(self, obj, **kw):
        obj.unlink()
        return werkzeug.utils.redirect('/academy/academy/')

    @http.route('/academy/academy/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('academy.listing', {
            'root': '/academy/academy',
            'objects': http.request.env['academy.academy'].search([]),
        })

    @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('academy.object', {
            'object': obj
        })

    @http.route('/academy/create_form/', auth='public', website=True)
    def create_form(self):
        return http.request.render('academy.create_academy')

    @http.route('/academy/create/', auth='public', website=True, method='GET', csrf=False)
    def create(self, **kwargs):
        request.env['academy.teachers'].create(kwargs)
        return werkzeug.utils.redirect('/academy/academy/')

    @http.route('/academy/edit_form/<model("academy.teachers"):obj>', auth='public', website=True)
    def edit_form(self, obj=False, **kw):
        return http.request.render('academy.edit_academy', {
            'teachers': obj,
        })

    @http.route('/academy/edit/<model("academy.teachers"):obj>', auth='public', website=True, method='GET', csrf=False)
    def edit(self, obj=False, **kwargs):
        print(">>>>>>>", obj)
        obj.write(kwargs)
        return werkzeug.utils.redirect('/academy/academy/')
