# Tennis emulator

The program is an automatic tennis emulator.

# Scoring Rules
#### Game, set, match

The scoreboard of a tennis match.
#### **Game**
A game consists of a sequence of points played with the same player serving. A game is won by the first player to have won at least four points in total and at least two points more than the opponent. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as "love", "15", "30", and "40", respectively. If at least three points have been scored by each player, making the player's scores equal at 40 apiece, the score is not called out as "40–40", but rather as "deuce". If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is "advantage" for the player in the lead. During informal games, advantage can also be called "ad in" or "van in" when the serving player is ahead, and "ad out" or "van out" when the receiving player is ahead; alternatively, either player may simply call out "my ad" or "your ad" during informal play.

The score of a tennis game during play is always read with the serving player's score first. In tournament play, the chair umpire calls the point count (e.g., "15–love") after each point. At the end of a game, the chair umpire also announces the winner of the game and the overall score.

#### Set
A set consists of a sequence of games played with service alternating between games, ending when the count of games won meets certain criteria. Typically, a player wins a set by winning at least six games and at least two games more than the opponent. If one player has won six games and the opponent five, an additional game is played. If the leading player wins that game, the player wins the set 7–5. If the trailing player wins the game (tying the set 6–6) a tiebreak is played. A tiebreak, played under a separate set of rules, allows one player to win one more game and thus the set, to give a final set score of 7–6. A tiebreak game can be won by scoring at least seven points and at least two points more than the opponent. In a tiebreak, two players serve by 'ABBA' system which has been proven to be fair. If a tiebreak is not played, the set is referred to as an advantage set, where the set continues without limit until one player leadsby a two-game margin. A "love set" means that the loser of the set won zero games, colloquially termed a "jam donut" in the US. In tournament play, the chair umpire announces the winner of the set and the overall score. The final score in sets is always read with the winning player's score first, e.g. "6–2, 4–6, 6–0, 7–5".

#### Match
A match consists of a sequence of sets. The outcome is determined through a best of three or five sets system. On the professional circuit, men play best-of-five-set matches at all four Grand Slam tournaments, Davis Cup, and the final of the Olympic Games and best-of-three-set matches at all other tournaments, while women play best-of-three-set matches at all tournaments. The first player to win two sets in a best-of-three, or three sets in a best-of-five, wins the match. Only in the final sets of matches at the French Open, the Olympic Games, and Fed Cup are tiebreaks not played. In these cases, sets are played indefinitely until one player has a two-game lead, occasionally leading to some remarkably long matches.

In tournament play, the chair umpire announces the end of the match with the well-known phrase "Game, set, match" followed by the winning person's or team's name.


# Functional

The program supports all the rules of tennis with the exception of the duel when the points in the game reach 40-40. Also, the set is played to 6 points (tie-break is not included)
- Display players / sorted list
- Adding / Removing players
- Tournament's emulator
	- Between two players on your chooce
	- Random tournament between ``` 2 ** random.randrange(1,4) ``` players
- Navigation in menu

# Settings

```python
SLEEP_TIME=0.05                             # delay for print results
SETS=3                                      # count of set by the rules
pamount = 2 ** random.randrange(1,4)        # count of participants  
```

# Display

![](https://i.ibb.co/CMXBRp1/tennis.gif)
