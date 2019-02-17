# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dueno(models.Model):
     _name = 'concesionario.dueno'
     name = fields.Char(string="Nombre", required=True)
     apellido = fields.Char(string="Apellido")
     coche_id = fields.One2many('concesionario.coche','dueno_id', string="Coche")

class Coche(models.Model):
     _name = 'concesionario.coche'
     marca = fields.Char(string="Marca")
     modelo = fields.Char(string="Modelo")
     dueno_id = fields.Many2one('concesionario.dueno', string="Dueno")

class Productos(models.Model):
    _inherit = 'res.partner'
    nombre = fields.Char(string="Nombre")