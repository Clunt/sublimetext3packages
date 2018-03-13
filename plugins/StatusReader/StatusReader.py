import sublime
import sublime_plugin

def parseInt(s):
    res = 0
    base = ord('0')
    for c in s:
        if not ('0' <= c <= '9'):
            continue
        res *= 10
        res += ord(c) - base
    return res


class StatusReaderCommand(sublime_plugin.TextCommand):
  line = 0
  delay = 1200

  def getLine(self):
    region = self.view.sel()[0]
    line = self.view.line(region)
    return line;

  def run(self, edit):
    self.delay = parseInt(self.view.substr(self.view.line(sublime.Region(0)))) or self.delay
    self.line = self.getLine()
    self.show();


  def show(self):
    line = self.getLine()
    if self.line.a != line.a:
      return

    self.view.show_at_center(line)
    line_contents = self.view.substr(line)
    sublime.status_message(line_contents)

    next_line_begin = line.b + 1
    if self.view.size() < next_line_begin:
      return

    self.view.sel().clear()
    self.view.sel().add(sublime.Region(next_line_begin))
    self.line = self.getLine()
    sublime.set_timeout(self.show, self.delay)