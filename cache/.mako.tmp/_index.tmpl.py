# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541474444.0481138
_enable_loop = True
_template_filename = 'themes/yesplease/templates/_index.tmpl'
_template_uri = '_index.tmpl'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comp', context._clean_inheritance_tokens(), templateuri='/_components.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comp')] = ns

def render_body(context,include_content=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(include_content=include_content,pageargs=pageargs)
        exclude_index_content = context.get('exclude_index_content', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        comp = _mako_get_namespace(context, 'comp')
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n<div class="pure-g">\n')
        for post in posts:
            __M_writer('\n    <div class="pure-u-1-5">\n      <div class="yp-index-meta">\n        <i class="fa fa-clock-o"></i>\n        <time datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('"\n              class="yp-index-meta__date">\n              ')
            __M_writer(str(comp.fancy_date(post.date)))
            __M_writer('\n        </time>\n')
            __M_writer('        <div class="yp-index-meta__tags">\n')
            for tag in post.tags:
                __M_writer('            <span class="yp-index-meta__tag">')
                __M_writer(str(tag))
                __M_writer('</span>\n')
            __M_writer('        </div>\n')
            __M_writer('      </div>\n    </div>\n\n    <div class="pure-u-4-5">\n      <article class="yp-index-post">\n        <h2 class="yp-index-post__title">\n          <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="yp-index-post__link">\n            ')
            __M_writer(str(post.title()))
            __M_writer('\n          </a>\n        </h2>\n        <h3 class="yp-index-post__subtitle">\n          ')
            __M_writer(str(post.description()))
            __M_writer('\n        </h3>\n')
            if include_content and not exclude_index_content:
                __M_writer('          <div class="yp-index-post__body">\n            ')
                __M_writer(str(post.text(teaser_only=index_teasers)))
                __M_writer('\n          </div>\n')
            __M_writer('      </article>\n    </div>\n')
        __M_writer('</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/yesplease/templates/_index.tmpl", "uri": "_index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 6, "26": 5, "35": 4, "36": 5, "37": 6, "38": 9, "39": 10, "40": 14, "41": 14, "42": 16, "43": 16, "44": 21, "45": 22, "46": 23, "47": 23, "48": 23, "49": 25, "50": 29, "51": 35, "52": 35, "53": 36, "54": 36, "55": 40, "56": 40, "57": 42, "58": 43, "59": 44, "60": 44, "61": 47, "62": 50, "68": 62}}
__M_END_METADATA
"""
