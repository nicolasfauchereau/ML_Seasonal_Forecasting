# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541474444.157668
_enable_loop = True
_template_filename = 'themes/yesplease/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['page_title', 'subtitle', 'header_image']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comp', context._clean_inheritance_tokens(), templateuri='/_components.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comp')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/_base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def subtitle():
            return render_subtitle(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'subtitle'):
            context['self'].subtitle(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n\n<div class="pure-g">\n  <div class="pure-u-1">\n    <article class="yp-post__body">\n      ')
        __M_writer(str(post.text()))
        __M_writer('\n    </article>\n  </div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str(post.title()))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def subtitle():
            return render_subtitle(context)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str(post.description()))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_image(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        default_header_image = context.get('default_header_image', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.meta[lang].get('header-image'):
            __M_writer('    ')
            __M_writer(str(post.meta[lang]['header-image']))
            __M_writer('\n')
        elif default_header_image:
            __M_writer('    ')
            __M_writer(str(default_header_image))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 5, "29": 0, "39": 3, "40": 5, "41": 6, "46": 8, "51": 9, "52": 20, "53": 25, "54": 25, "60": 8, "67": 8, "73": 9, "80": 9, "86": 10, "93": 10, "94": 13, "95": 14, "96": 14, "97": 14, "98": 15, "99": 18, "100": 18, "101": 18, "107": 101}}
__M_END_METADATA
"""
