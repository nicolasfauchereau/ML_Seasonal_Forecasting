# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541474444.038453
_enable_loop = True
_template_filename = 'themes/yesplease/templates/_base.tmpl'
_template_uri = '/_base.tmpl'
_source_encoding = 'utf-8'
_exports = ['page_title', 'extra_links', 'extra_scripts', 'subtitle']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        hasattr = context.get('hasattr', UNDEFINED)
        capture = context.get('capture', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def extra_scripts():
            return render_extra_scripts(context._locals(__M_locals))
        blog_title = context.get('blog_title', UNDEFINED)
        next = context.get('next', UNDEFINED)
        self = context.get('self', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        template_hooks = context.get('template_hooks', UNDEFINED)
        def subtitle():
            return render_subtitle(context._locals(__M_locals))
        blog_header_image = context.get('blog_header_image', UNDEFINED)
        body_end = context.get('body_end', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n    <meta http-equiv="x-ua-compatible" content="ie=edge">\n    <title>\n')
        __M_writer('      ')
        __M_writer(str('{} - '.format(blog_title) if capture(self.page_title) != blog_title else ''))
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n    </title>\n\n    ')
        runtime._include_file(context, '_style.tmpl', _template_uri)
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\n\n    ')
        runtime._include_file(context, '_scripts.tmpl', _template_uri)
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_scripts'):
            context['self'].extra_scripts(**pageargs)
        

        __M_writer('\n\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n  </head>\n  <body>\n    <div id="layout">\n      ')
        runtime._include_file(context, '_menu.tmpl', _template_uri)
        __M_writer('\n\n      <div id="main">\n\n')
        __M_writer('        ')
        header_image_url = None 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['header_image_url'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n')
        if hasattr(self, 'header_image'):
            __M_writer('          ')
            header_image_url = capture(self.header_image).strip() 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['header_image_url'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\n')
        __M_writer('\n')
        if not header_image_url and capture(self.page_title) == blog_title:
            __M_writer('          ')
            header_image_url = blog_header_image 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['header_image_url'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\n')
        __M_writer('\n        <div class="yp-header-container">\n')
        if header_image_url:
            __M_writer('\n            <div class="yp-header-background"\n                 style="background-image: url(')
            __M_writer(str(header_image_url))
            __M_writer(')">\n')
            __M_writer('              <div class="yp-header">\n                <h1 class="yp-header__title')
            __M_writer(str('--overlay' if header_image_url else ''))
            __M_writer('">')
            __M_writer(str(self.page_title()))
            __M_writer('</h1>\n                <h2 class="yp-header__subtitle')
            __M_writer(str('--overlay' if header_image_url else ''))
            __M_writer('">')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'subtitle'):
                context['self'].subtitle(**pageargs)
            

            __M_writer('</h2>\n                ')
            __M_writer(str(template_hooks['page_header']()))
            __M_writer('\n              </div>\n            </div>\n\n')
            __M_writer('            <div class="yp-header-background--blur"\n                 style="background-image: url(')
            __M_writer(str(header_image_url))
            __M_writer(')">\n              <div class="yp-header">\n                <h1 class="yp-header__title')
            __M_writer(str('--overlay' if header_image_url else ''))
            __M_writer('">')
            __M_writer(str(self.page_title()))
            __M_writer('</h1>\n                <h2 class="yp-header__subtitle')
            __M_writer(str('--overlay' if header_image_url else ''))
            __M_writer('">')
            __M_writer(str(self.subtitle()))
            __M_writer('</h2>\n                ')
            __M_writer(str(template_hooks['page_header']()))
            __M_writer('\n              </div>\n            </div>\n\n            <div class="yp-header">\n')
        else:
            __M_writer('            <div class="yp-header" style="border-bottom: 1px solid #eee;">\n')
        __M_writer('\n            <h1 class="yp-header__title')
        __M_writer(str('--overlay' if header_image_url else ''))
        __M_writer('">\n              ')
        __M_writer(str(self.page_title()))
        __M_writer('\n            </h1>\n            <h2 class="yp-header__subtitle')
        __M_writer(str('--overlay' if header_image_url else ''))
        __M_writer('">\n              ')
        __M_writer(str(self.subtitle()))
        __M_writer('\n            </h2>\n            ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n          </div>\n        </div>\n\n        <div class="yp-content">\n          ')
        __M_writer(str(next.body()))
        __M_writer('\n        </div>\n\n\n        ')
        runtime._include_file(context, '_footer.tmpl', _template_uri)
        __M_writer('\n      </div>\n    </div>\n\n    ')
        __M_writer(str(body_end))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_links():
            return render_extra_links(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_scripts():
            return render_extra_scripts(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_subtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def subtitle():
            return render_subtitle(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/_base.tmpl", "uri": "/_base.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "38": 1, "39": 9, "40": 9, "45": 9, "46": 12, "47": 12, "52": 13, "53": 15, "54": 15, "59": 16, "60": 18, "61": 18, "62": 19, "63": 19, "64": 23, "65": 23, "66": 29, "67": 29, "71": 29, "72": 30, "73": 32, "74": 32, "78": 32, "79": 34, "80": 38, "81": 39, "82": 39, "86": 39, "87": 41, "88": 43, "89": 44, "90": 46, "91": 46, "92": 49, "93": 50, "94": 50, "95": 50, "96": 50, "97": 51, "98": 51, "103": 51, "104": 52, "105": 52, "106": 59, "107": 60, "108": 60, "109": 62, "110": 62, "111": 62, "112": 62, "113": 63, "114": 63, "115": 63, "116": 63, "117": 64, "118": 64, "119": 69, "120": 71, "121": 73, "122": 74, "123": 74, "124": 75, "125": 75, "126": 77, "127": 77, "128": 78, "129": 78, "130": 80, "131": 80, "132": 85, "133": 85, "134": 89, "135": 89, "136": 93, "137": 93, "138": 94, "139": 94, "145": 9, "156": 13, "167": 16, "178": 51, "189": 178}}
__M_END_METADATA
"""
