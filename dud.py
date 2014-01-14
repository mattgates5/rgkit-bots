# dud.py
# mg 2013
# Do nothing you cheap bastard
# DUD ALGORITHM

import rg
import random

class Robot:
  def act(self, game):
    direction = rg.toward(self.location, rg.CENTER_POINT)
    around = rg.locs_around(self.location, filter_out=('invalid','obstacle'))
    good_locs = []

    for l in around:
      if direction == l:
        good_locs.append(l)

    if good_locs:
      r = range(0, len(good_locs))
      x = random.choice(r)
      direction = rg.toward(self.location, good_locs[x])

    if self.location == rg.CENTER_POINT:
      return ['guard']
    else:
      return ['move', direction]
