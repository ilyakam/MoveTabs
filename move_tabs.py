import sublime_plugin

class MoveTabsToIndexCommand(sublime_plugin.WindowCommand):
  def run(self, index):
    # Get active view, group, and index:
    active_view = self.window.active_view()
    (active_group, active_index) = self.window.get_view_index(active_view)

    # Prevent user from going out-of-bounds:
    if index >= len(self.window.views_in_group(active_group)):
      return

    # Move active view to index:
    self.window.set_view_index(active_view, active_group, index)

class MoveTabsToDirectionCommand(sublime_plugin.WindowCommand):
  def run(self, direction):
    # Get active view, group, and index:
    active_view = self.window.active_view()
    (active_group, active_index) = self.window.get_view_index(active_view)

    # Initialize:
    new_group = active_group
    new_index = None

    # Left:
    if direction < 0:
      # Move to group on the left, if possible:
      if active_index+direction < 0:
        if active_group-1 >= 0:
          new_group = active_group-1
          new_index = len(self.window.views_in_group(new_group))
        else:
          new_index = 0

    # Right:
    else:
      # Move to group on right, if possible:
      if active_index+direction >= len(self.window.views_in_group(active_group)):
        if active_group+1 <= self.window.num_groups()-1:
          new_group = active_group+1
          new_index = 0
        else:
          new_index = len(self.window.views_in_group(new_group))-1

    # Perform regular move if all exceptions have been caught:
    if new_index is None:
      new_index = active_index+direction

    # Move active view to new group and new index:
    self.window.set_view_index(active_view, new_group, new_index)
