# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541474444.068686
_enable_loop = True
_template_filename = 'themes/yesplease/templates/_components.tmpl'
_template_uri = '/_components.tmpl'
_source_encoding = 'utf-8'
_exports = ['fancy_date']


from uuid import uuid4 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_fancy_date(context,date_value):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer('\n\n  ')
        id_ = uuid4() 
        
        __M_writer('\n  <span id="')
        __M_writer(str(id_))
        __M_writer('">\n\n  </span>\n  <script>\n    (function(){\n      var el = document.getElementById("')
        __M_writer(str(id_))
        __M_writer('");\n      var fromNow = moment("')
        __M_writer(str(date_value.isoformat()))
        __M_writer('").fromNow();\n      el.innerHTML = fromNow;\n    })();\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/_components.tmpl", "uri": "/_components.tmpl", "source_encoding": "utf-8", "line_map": {"16": 6, "18": 0, "23": 5, "24": 6, "30": 8, "34": 8, "35": 13, "36": 15, "38": 15, "39": 16, "40": 16, "41": 21, "42": 21, "43": 22, "44": 22, "50": 44}}
__M_END_METADATA
"""
