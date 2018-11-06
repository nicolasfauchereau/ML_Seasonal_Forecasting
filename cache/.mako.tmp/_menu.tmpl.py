# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541474444.062012
_enable_loop = True
_template_filename = 'themes/yesplease/templates/_menu.tmpl'
_template_uri = '_menu.tmpl'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        lang = context.get('lang', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        template_hooks = context.get('template_hooks', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<a href="#menu" id="menuLink" class="menu-link">\n')
        __M_writer('    <span></span>\n</a>\n\n<div id="menu">\n    <div class="pure-menu">\n        <a class="pure-menu-heading" href="/">')
        __M_writer(str(blog_title))
        __M_writer('</a>\n\n        <ul class="pure-menu-list">\n\n')
        for url, label in navigation_links[lang]:
            __M_writer('            <li class="pure-menu-item">\n              <a class="pure-menu-link" href="')
            __M_writer(str(url))
            __M_writer('">')
            __M_writer(str(label))
            __M_writer('</a>\n            </li>\n')
        __M_writer('\n')
        __M_writer('\n          ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n        </ul>\n    </div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/_menu.tmpl", "uri": "_menu.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "25": 2, "26": 4, "27": 9, "28": 9, "29": 14, "30": 15, "31": 16, "32": 16, "33": 16, "34": 16, "35": 19, "36": 21, "37": 22, "38": 22, "44": 38}}
__M_END_METADATA
"""
