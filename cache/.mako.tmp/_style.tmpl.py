# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541474444.0568461
_enable_loop = True
_template_filename = 'themes/yesplease/templates/_style.tmpl'
_template_uri = '_style.tmpl'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        if use_bundles:
            __M_writer('  <link rel="stylesheet" href="/assets/css/bundle.css"/>\n')
        else:
            __M_writer('  <link rel="stylesheet" href="/assets/css/fluidbox.min.css"/>\n  <link rel="stylesheet" href="/assets/css/highlight/default.css"/>\n  <link rel="stylesheet" href="/assets/css/font-awesome.css"/>\n  <link rel="stylesheet" href="/assets/css/pure.css"/>\n  <link rel="stylesheet" href="/assets/css/grids-responsive.css"/>\n  <link rel="stylesheet" href="/assets/css/side-menu.css"/>\n  <link rel="stylesheet" href="/assets/css/site.css"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/_style.tmpl", "uri": "_style.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 2, "24": 3, "25": 4, "31": 25}}
__M_END_METADATA
"""
