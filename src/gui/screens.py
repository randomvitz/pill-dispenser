"""
GUI Screens for the Pill Dispenser.
Main screen and configuration screens.
"""

import pygame
import pygame_gui
from hardware.screen import TouchScreen

class MainScreen:
    def __init__(self, config, timer_service):
        self.config = config
        self.timer_service = timer_service
        self.screen = TouchScreen()
        self.screen.setup()
        self.manager = self.screen.get_manager()

        # UI Elements
        self.status_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 10), (200, 50)),
            text="Pill Dispenser Ready",
            manager=self.manager
        )

        self.schedule_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, 70), (150, 50)),
            text="Edit Schedule",
            manager=self.manager
        )

        self.manual_dispense_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, 130), (150, 50)),
            text="Manual Dispense",
            manager=self.manager
        )

    def run(self):
        """Main event loop."""
        clock = pygame.time.Clock()
        running = True

        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.schedule_button:
                        self.show_schedule_screen()
                    elif event.ui_element == self.manual_dispense_button:
                        self.manual_dispense()

                self.screen.process_events(event)

            self.screen.update(time_delta)
            self.screen.get_surface().fill((0, 0, 0))  # Clear screen
            self.screen.draw()
            pygame.display.update()

        self.screen.cleanup()

    def show_schedule_screen(self):
        """Show schedule configuration screen."""
        # TODO: Implement schedule editing screen
        pass

    def manual_dispense(self):
        """Perform manual dispensing."""
        # TODO: Implement manual dispense dialog
        pass