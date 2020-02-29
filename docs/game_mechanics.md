# Game's Mechanics

## Screens

- **First Screen:**
It Contains the game's name in large letters, a field for the user's name input and two buttons, one that leads to the ranking screen and another that starts the game.

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/gameIntro.png) <br/>
<br/>
<br/>

- **Ranking Screen:**
Screen that displays in a table the points saved to a txt file, according to the highest score, player who scored and the theme played. Also contains a "back" button that leads to the first screen. 
The maximum amount of scores in the txt file is 15. Passed that, the code will delete the lowest score. 

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/gameRanking.png) <br/>
<br/>
<br/>

- **Pre-Game Screen:**
Screen initiated by the start button. It contains a button and a "display", the first one to draw the match's theme and the latter to show the theme drawn. There are three themes in the game: carbs, vitamins and proteins. According to the theme drawn, questions are chosen randomly from a txt file, having their answers stored in another file. After the theme shows up, a countdown is started, and at the end, the game screen opens.

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/preGame.png)
![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/preGame1.png) <br/>
<br/>
<br/>

- **Gameplay Screen**
In this screen the player can see the question chosen randomly at the top of the window. Underneath it is an area intended for gameplay itself. Four different foods spawn in random horizontal positions at the top, all moving with a certain speed to the bottom. The goal of the player is to click on the foods to which the question refers to, before they pass the bottom of the screen. At each successful click the player receives a certain score and continues the rounds until he misses a certain amount of times, at which point the match ends. Regardless of the correct answers, any clicked food is deleted from the screen.

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/gameDisplay.png) <br/>
<br/>
<br/>

- **GameOver Screen**
When all chances are over, the match ends and the game over screen pops up. In it the player can see their final score and chooses to play again or leave the game: For the first choice, the player goes to Pre-game screen, and, for the latter, the player goes to the first screen, where the ranking button is available. 

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/gameOver.png) <br/>
<br/>
<br/>

**obs: Although the number of questions on each theme is limited, the large number of possible foods to be instantiated in a given round allows questions to be repeated without diminishing or ending the fun of the match.**
