# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541474444.104934
_enable_loop = True
_template_filename = 'themes/yesplease/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['page_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/_base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        len = context.get('len', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n\n\n<article class="yp-post-group__body">\n\n')
        if cat_items:
            __M_writer('    <h2>Categories</h2>\n\n')
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                for i in range(indent_change_before):
                    __M_writer('            <ul class="yp-post-list">\n')
                __M_writer('\n        <li class="yp-post-list__item">\n          <h3 class="yp-post-list__title">\n            <a class="reference yp-post-list__link" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n          </h3>\n\n')
                if indent_change_after <= 0:
                    __M_writer('            </li>\n')
                __M_writer('\n')
                for i in range(-indent_change_after):
                    __M_writer('            </ul>\n')
                    if i + 1 < len(indent_levels):
                        __M_writer('                </li>\n')
                __M_writer('\n')
        __M_writer('\n')
        if items:
            __M_writer('\n    <h2>Tags</h2>\n\n    <ul class="yp-post-list">\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer('          <li class="yp-post-list__item">\n            <h3 class="yp-post-list__title">\n              <a class="reference yp-post-list__link" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(text)))
                    __M_writer('</a>\n            </h3>\n          </li>\n')
            __M_writer('    </ul>\n\n')
        __M_writer('</article>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(messages("Categories")))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/tags.tmpl", "uri": "tags.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "41": 3, "42": 5, "47": 9, "48": 14, "49": 15, "50": 17, "51": 18, "52": 19, "53": 21, "54": 24, "55": 24, "56": 24, "57": 24, "58": 27, "59": 28, "60": 30, "61": 31, "62": 32, "63": 33, "64": 34, "65": 37, "66": 40, "67": 41, "68": 42, "69": 46, "70": 47, "71": 48, "72": 50, "73": 50, "74": 50, "75": 50, "76": 55, "77": 58, "83": 7, "90": 7, "91": 8, "92": 8, "98": 92}}
__M_END_METADATA
"""
