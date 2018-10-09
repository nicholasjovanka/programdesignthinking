class Settings():
    def __init__(self):
        """Initializing game settings"""
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (255, 255, 255)
        self.ship_speed_factor=1.5
        self.bullet_width=3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1
        self.bullets_allowed = 3
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3



