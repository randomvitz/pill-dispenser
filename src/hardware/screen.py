"""
Touchscreen Display Interface.
Handles display output and touch input using pygame.
"""

import pygame
import pygame_gui
import os

class TouchScreen:
    def __init__(self, width=800, height=480):
        self.width = width
        self.height = height
        self.screen = None
        self.manager = None

    def setup(self):
        """Initialize pygame and touchscreen."""
        os.environ['SDL_FBDEV'] = '/dev/fb1'  # Framebuffer device
        os.environ['SDL_MOUSEDRV'] = 'TSLIB'  # Touchscreen driver
        os.environ['SDL_MOUSEDEV'] = '/dev/input/touchscreen'  # Touch device

        pygame.init()
        pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.screen = pygame.display.get_surface()
        self.manager = pygame_gui.UIManager((self.width, self.height))

    def get_surface(self):
        """Get pygame surface for drawing."""
        return self.screen

    def get_manager(self):
        """Get pygame_gui manager for UI elements."""
        return self.manager

    def update(self, time_delta):
        """Update the UI manager."""
        self.manager.update(time_delta)

    def draw(self):
        """Draw the UI."""
        self.manager.draw_ui(self.screen)

    def process_events(self, event):
        """Process pygame events."""
        return self.manager.process_events(event)

    def cleanup(self):
        """Clean up pygame."""
        pygame.quit()