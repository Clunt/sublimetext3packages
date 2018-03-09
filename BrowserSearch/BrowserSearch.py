#!/bin/python3
import sublime
import sublime_plugin
import webbrowser
import re
from urllib import parse


def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])

SEARCH = {}
SEARCH['npmjs'] = 'https://www.npmjs.com/search?q=${search}'
SEARCH['baidu'] = 'https://www.baidu.com/s?wd=${search}'
SEARCH['google'] = 'https://www.google.com/search?q=${search}'
SEARCH['caniuse'] = 'https://caniuse.com/#search=${search}'
URL['search'] = 'https://www.baidu.com/s?wd=${search}'
URL['express'] = 'http://expressjs.com/'
URL['vuejs'] = 'https://cn.vuejs.org/v2/guide/'


class BrowserSearchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        sublime.active_window().show_input_panel('快速搜索', '', self.on_done, None, self.on_cancel)

    def on_done(self, words):
        search = trim(str(words));
        if search != '':
            try:
              searchIndex = search.index('.');
              searchType = search[:searchIndex];
              searchValue = search[searchIndex + 1:]
              for key in sorted(SEARCH.keys()):
                if searchType in key:
                  url = re.sub(r'\${search}', parse.quote(searchValue), SEARCH[key])
                  webbrowser.open_new_tab(url)
                  return
              sublime.status_message('没有找到可打开链接')
            except BaseException:
              try:
                for key in sorted(URL.keys()):
                  if search in key:
                    webbrowser.open_new_tab(URL[key])
                    return
              except BaseException:
                url = re.sub(r'\${search}', parse.quote(search), URL['search'])
                webbrowser.open_new_tab(url)

    def on_cancel():
        pass

