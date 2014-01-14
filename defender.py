# defender.py
# mg 2013
#
# look - think - behave

import rg

class Brain:
  # Empty actions dict
  actions = {}

  # Constructor
  #   initialize the actions dict
  # set the instance variables
  # copy down the game and the robot's parameters
  def __init__(self, r, g):
    self.actions = {'move': True,
      'guard': False,
      'attack': False,
      'suicide': False}

    self.center = False
    self.surrounded = False
    self.enemies = []

    self.robot = r
    self.game = g

  # Observe the board
  def look(self):
    # If I'm at the center, mark center as true
    if self.robot.location == rg.CENTER_POINT:
      self.center = True

    # If there are more than 2 enemies next to me
    # mark surrounded as true
    self.enemies = self.count_enemies()
    if len(self.enemies) > 2:
      self.surrounded = True

  # Make an assessment
  def think(self):
    # If I'm surrounded sacrifice myself for
    #  the greater good of the team
    if self.surrounded:
      self.actions['suicide'] = True

    # If I'm at the center, CASTLE UP!
    if self.center:
      self.stop()
      self.actions['guard']

    # If my health is low, head for the center
    if self.robot.hp <= 20:
      self.actions['move'] = True
    # If my health is ok, attack if I can,
    #  or head for the center
    elif self.robot.hp <= 50:
      self.actions['attack'] = True
      self.actions['move'] = True
    # If my health is high, attack with prejudice!
    else:
      self.actions['attack'] = True

  # Act accordingly
  def behave(self):
    # From hell's heart I stab at thee
    #  for hate's sake, my last breath I spit at thee
    if self.actions['suicide']:
      return ['suicide']

    # Attack if I can
    if self.actions['attack']:
      if len(self.enemies) > 0:
        for loc in self.enemies:
          if rg.dist(loc, self.robot.location) <= 1:
            return ['attack', loc]

    # Move towards the center
    if self.actions['move']:
      new_loc = rg.toward(self.robot.location, rg.CENTER_POINT)
      return ['move', new_loc]

    # Protect the herd
    if self.actions['guard']:
      return ['guard']

  # Read a list of enemy locations
  # Return a list of adjacent enemies
  def count_enemies(self):
    around = rg.locs_around(self.robot.location,
      filter_out=('invalid','obstacle'))

    enemies = self.check_for_enemies()

    enemy_locs = []
    for l in around:
      for e in enemies:
        if l == e:
          enemy_locs.append(e)

    return enemy_locs

  # Scan the board for a enemy bots
  # return a list of enemy locations (list of tuples)
  def check_for_enemies(self):
    bots = []
    for loc, bot in self.game.get('robots').items():
      if bot.player_id != self.robot.player_id:
        bots.append(loc)

    return bots

  # Clear all actions from the actions dict
  def stop(self):
    for a in self.actions:
      self.actions[a] = False

class Robot:

  def act(self, game):
    robot = self

    # Give the bot a brain
    ai = Brain(robot, game)

    # look - think - act
    ai.look()
    ai.think()
    action = ai.behave()

    # Do the needful
    return action
