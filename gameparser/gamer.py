from gameparser.steam import Parser
try:
    import gameparser.__config__ as conf
except:
    import __config__ as conf


import mathematics.statistics

parser = Parser(conf.STEAMKEY)


class Gamer:
    def __init__(self, steam_id, game_names):
        '''
        Give steam id as an argument and get players game statisctics
        :param vk_id: vk id
        :param steam_id: suprisingly, steam id :)
        :param game_names: list of games (can find in __config__.py), example: ["csgo, "dota2"]
        '''

        self.steam_id = steam_id
        self.stats = list()
        for game in game_names:
            stats = parser.getUserStatsForGame(steam_id, conf.STEAMGAMES[game])

            self.stats.append({game : stats})
            
        """total_kills, total_deaths, total_time_played, total_wins, total_kills_headshot, total_shots_hit, total_shots_fired, total_mvps, total_matches_played"""
        self.csgo_stats=[self.stats[0]['csgo'][i] for i in self.stats[0]['csgo']]
        self.R=mathematics.statistics.set_R(*self.csgo_stats)
        self.bestMaps=parser.getUserBestMapsInCS(steam_id)
        
    def refresh_R(self, S, E):
        """
        S: match result: 1 if win, 0.5 if draw, 0 if lose
        E: predicted probability of win
    
        rewrites: new value of rating
        """
        self.R=mathematics.statistics.R_new(self.R, mathematics.statistics.K(self.R), S, E)

    def win_chance(self, R_friend):
        """
        R_friend: friends rating
        """
        return mathematics.statistics.E(self.R, R_friend)
