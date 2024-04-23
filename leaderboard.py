from datetime import datetime


class Leaderboard:
  def __init__(self):
    self.user_to_data: dict[str, WordleStats] = {}

class WordleStats:
  def __init__(self):
    self.average: float = 0
    self.colors: dict[str, int] = {}
    self.num_solved: int = 0
    self.last_game: datetime
