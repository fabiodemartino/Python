class GameStats():
    """ Track statistics for alien invasion """

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # start the game in inactive state
        self.game_active = False
        self.score = 0
        # High score should neve be reset
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
