rgkit-bots
==========

Bots for [The Robot Game](http://robotgame.net) ([brandonhsiao/rgkit](https://github.com/brandonhsiao/rgkit)). 

To test it with the Robot Game Kit run:

    python rgkit/run.py defender.py dud.py

### DEFENDER Bot

The DEFENDER robot has three main actions in it's API:

* `look`
* `think`
* `behave`

These actions should be called in the order listed here. For example in the robot game:

	class Robot:
      def act(self, game):
        robot = self
        
		ai = Brain(robot, game)
		
		ai.look()
		ai.think()
		action = ai.behave()
		
		return action
		
When the bot is called to act, it will observe the game board, make an assessment and then act accordingly. The strategy of DEFENDER is to attack while its health is high and move towards the center of the board. Once it reaches the center it defends itself and the nearby friendlies until a 'castle' is formed. 

While in transit, if DEFENDER's health gets low and it comes under heavy attack, it will self-destruct in an attempt to harm the enemies around it. 

### DUD Bot

The DUD robot has one action: run like a mad fool. It will head straight for the middle of the board. 