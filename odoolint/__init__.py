# -*- coding: utf-8 -*-
# © 2016  Vauxoo (<http://www.vauxoo.com/>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import imp
import logging
import sys

from openerp.tools import convert
import openerp

from . import models

_logger = logging.getLogger(__name__)


def patch_openerp():
    orig_convert_file = convert.convert_file

    def convert_file(*args, **kwargs):
        import pdb;pdb.set_trace()
        return orig_convert_file(*args, **kwargs)
    convert.convert_file = convert_file
    openerp.tools.convert.convert_file = convert_file
    imp.reload(openerp.tools)
    import pdb;pdb.set_trace()
    sys.modules['openerp.tools.convert'].convert_file = convert_file


def post_load():
    _logger.warning(
        'Post load patching openerp.tools.convert.convert_file method')
    patch_openerp()
