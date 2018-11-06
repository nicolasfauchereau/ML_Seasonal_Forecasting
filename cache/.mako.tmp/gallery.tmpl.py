# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541474444.1339352
_enable_loop = True
_template_filename = 'themes/yesplease/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
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
        folders = context.get('folders', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n\n')
        if post:
            __M_writer('  <article class="yp-post__body">\n    <div>\n      ')
            __M_writer(str(post.text()))
            __M_writer('\n    </div>\n  </article>\n')
        __M_writer('\n\n')
        if folders:
            __M_writer('  <article class="yp-post-group__body">\n\n')
            if photo_array:
                __M_writer('      <h3>Sub-Galleries:</h3>\n')
            __M_writer('\n    <ul class="yp-post-list">\n')
            for link, text in folders:
                __M_writer('        <li class="yp-post-list__item">\n          <h3 class="yp-post-list__title">\n            <a class="reference yp-post-list__link" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(text)))
                __M_writer('</a>\n          </h3>\n        </li>\n')
            __M_writer('    </ul>\n  </article>\n')
        __M_writer('\n\n<article class="yp-gallery__body">\n  <div class="yp-gallery__container">\n')
        if photo_array:
            for image in photo_array:
                __M_writer('        ')

                link = image['url']
                title = image['title']
                thumb_link = image['url_thumb']
                # Add the narrow class to figures in portrait
                extra_class = 'yp-gallery__figure--narrow' if image['size']['h'] > image['size']['w'] else ''
                        
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['thumb_link','title','link','extra_class'] if __M_key in __M_locals_builtin_stored]))
                __M_writer('\n\n        <figure class="yp-gallery__figure ')
                __M_writer(str(extra_class))
                __M_writer('">\n          <a href="')
                __M_writer(str(link))
                __M_writer('" class="yp-gallery__link image-reference" title="')
                __M_writer(str(title))
                __M_writer('">\n            <img class="yp-gallery__image" src="')
                __M_writer(str(thumb_link))
                __M_writer('" alt="')
                __M_writer(str(title))
                __M_writer('" title="')
                __M_writer(str(title))
                __M_writer('"/>\n          </a>\n        </figure>\n\n')
        __M_writer('  </div>\n\n</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        folders = context.get('folders', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if title != 'galleries':
            __M_writer('    ')
            __M_writer(str(title))
            __M_writer('\n')
        elif folders:
            __M_writer('    Photo Galleries\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "37": 21, "38": 23, "43": 31, "44": 33, "45": 34, "46": 36, "47": 36, "48": 40, "49": 42, "50": 43, "51": 45, "52": 47, "53": 49, "54": 51, "55": 52, "56": 54, "57": 54, "58": 54, "59": 54, "60": 58, "61": 61, "62": 65, "63": 66, "64": 67, "65": 67, "75": 73, "76": 75, "77": 75, "78": 76, "79": 76, "80": 76, "81": 76, "82": 77, "83": 77, "84": 77, "85": 77, "86": 77, "87": 77, "88": 83, "94": 24, "102": 24, "103": 26, "104": 27, "105": 27, "106": 27, "107": 28, "108": 29, "114": 108}}
__M_END_METADATA
"""
