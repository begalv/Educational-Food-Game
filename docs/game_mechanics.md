# Game's Mechanics

## Screens

- **First Screen:**
When opening the game, a screen opens, containing the name of the game in large letters, a field for entry the user's name and two buttons, one to view the ranking and another to start the game.

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/gameIntro.png) <br/>
<br/>
<br/>

- **Ranking Screen:**
Screen that sorts and displays in a table the points saved in a txt file, according to the highest score, player who scored and the theme played. Also contains a "back" button that leads to the first screen of the game. 
The maximum amount of scores in the txt file is 15. After that the code will delete the lowest score and it's respective data (player's name and theme played). 

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/gameRanking.png) <br/>
<br/>
<br/>

- **Pre-Game Screen:**
When the start button is clicked, another screen appears. In it there is a button and a "display", the first to draw the theme of the match and the latter to show the theme drawn. There are three themes in the game: carbs, vitamins and proteins. According to the theme drawn, questions are chosen randomly from a txt file, having their answers stored in another file, also txt. There is an answer file and a question file for each theme of the game. After viewing the drawn theme, a countdown is started, and at the end, the game screen itself opens

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/preGame.png)
![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/preGame1.png) <br/>
<br/>
<br/>

- **Gameplay Screen**
In this screen the player can see the question chosen randomly at the top of the window. Underneath this, there is the area intended for gameplay itself. Four different food sprites spawn in random horizontal positions at the top of the intended gameplay area, moving with certain speed to the bottom. The goal of the player is to click on the foods to which the question refers to, before they pass the bottom of the screen. At each successful click the player receives a certain score and continues the rounds of the match until he misses a certain amount of times, at which point the match ends. Regardless of the correct answers, any clicked sprite is deleted from the screen.

![Alt](https://github.com/begalv/Educational-Food-Game/blob/master/docs/images/gameDisplay.png) <br/>
<br/>
<br/>

**obs: Although the number of questions on each theme is limited, the large number of possible foods to be instantiated in a given round allows questions to be repeated without diminishing or ending the fun of the match.**
