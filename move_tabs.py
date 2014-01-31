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
    new_index = active_index
    
    # Set boundaries:
    min_group = 0
    max_group = self.window.num_groups()-1
    min_index = 0
    max_index = len(self.window.views_in_group(active_group))-1
    
    # logic:
    new_index += direction
    if new_index < min_index:
      # Move to previous group:
      new_group -= 1
      
      # Recalculate max index:
      if new_group < min_group:
        return
        
      max_index = len(self.window.views_in_group(new_group))
      new_index = max_index
      
    elif new_index > max_index:
      # Move to next group:
      new_group += 1
      new_index = min_index
      
    # Validation:
    if (min_group <= new_group <= max_group and
        min_index <= new_index <= max_index
    ):
      self.window.set_view_index(active_view, new_group, new_index)
