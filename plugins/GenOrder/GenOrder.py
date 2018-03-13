import sublime, sublime_plugin
import re


class GenorderCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    begin = 0
    times = 26
    number = True
    addContent = 1
    strs = 'abcdefghijklmnopqrstuvwxyz'
    content = self.view.substr(self.view.line(self.view.text_point(0, 0))).split(',')
    beginContent = ''
    timesContent = ''
    if content[0]:
      beginContent = content[0]
    if len(content) == 2:
      timesContent = content[1]
    if len(content) == 3:
      timesContent = content[1]
      addContent = int(content[2])

    beginMatch = re.compile(r'^[^\w\d]*(\w|\d*)[^\w\d]*$').match(beginContent)
    timesMatch = re.compile(r'^[^\d]*(\d*)[^\d]*$').match(timesContent)
    if beginMatch and beginMatch.group(1):
      begin = beginMatch.group(1)
      number = False
      numberMatch = re.compile(r'^\d*$').match(begin)
      if numberMatch:
        begin = int(begin)
        number = True
    if timesMatch and timesMatch.group(1):
      times = timesMatch.group(1)

    times = int(times)

    index = 0;
    if not number:
      index = strs.index(begin)

    resultArr = [];
    while times > 0:
      resultArr.append(str(begin))
      times = times - 1
      if number:
        begin += addContent;
      else:
        begin = strs[index:index + 1]
        index += 1;
        if index > 25:
          index = 0;

    result = '\n'.join(resultArr)

    self.view.replace(edit, sublime.Region(0, self.view.size() + 1), result)