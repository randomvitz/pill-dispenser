"""
Custom GUI Widgets for the Pill Dispenser.
"""

import pygame_gui

class TimePicker(pygame_gui.elements.UIButton):
    """Widget for selecting time."""
    def __init__(self, relative_rect, initial_time="08:00", manager=None):
        super().__init__(relative_rect=relative_rect,
                        text=f"Time: {initial_time}",
                        manager=manager)
        self.selected_time = initial_time

    def set_time(self, time_str):
        """Set the selected time."""
        self.selected_time = time_str
        self.set_text(f"Time: {time_str}")

class CompartmentSelector(pygame_gui.elements.UISelectionList):
    """Widget for selecting pill compartments."""
    def __init__(self, relative_rect, manager=None):
        options = [f"Compartment {i+1}" for i in range(6)]
        super().__init__(relative_rect=relative_rect,
                         item_list=options,
                         manager=manager)

    def get_selected_compartments(self):
        """Get list of selected compartment indices."""
        selected = self.get_multi_selection()
        return [int(item.split()[-1]) - 1 for item in selected]  # Convert to 0-based index