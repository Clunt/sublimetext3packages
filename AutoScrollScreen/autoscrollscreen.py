import sublime, sublime_plugin


DELAY = 1500
LINE_COUNT = 1;

class AutoscrollscreenCommand(sublime_plugin.TextCommand):
  CURRENT_LINE = 0

  def run(self, edit):
    self.CURRENT_LINE = self.getLine()
    self.auto()

  def auto(self):
    if self.view.viewport_position()[1] < self.CURRENT_LINE * self.view.line_height():
      return

    current_line = self.getLine() + 1

    self.CURRENT_LINE = current_line;

    if self.scroll(current_line):
      sublime.set_timeout(self.auto, DELAY)


  def getLine(self):
    line_height = self.view.line_height()
    position = self.view.viewport_position()
    position_y = position[1];

    line = int( ( position_y - position_y % line_height ) / line_height )

    return line


  def scroll(self, line):
    position_y = line * self.view.line_height()
    linePoint = self.view.text_point(line, 0)

    # Scroll Screen
    self.view.set_viewport_position((0, position_y), True)

    # Change Cursor
    self.view.sel().clear()
    self.view.sel().add(sublime.Region(linePoint))

    # Show Content
    self.show(line)

    return self.view.size() != linePoint;


  def show(self, line):
    content = ""

    if line > 0 and False:
      content = self.view.substr(self.view.line(self.view.text_point(line - 1, 0)))

    content = content + self.view.substr(self.view.line(self.view.text_point(line, 0)))

    # Show Content
    sublime.status_message(content)
