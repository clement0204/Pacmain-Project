# Pacmain-Project
Project developed by a group of second-year students at CentraleSupélec. The objective was to propose a serious game to help patients who have to do hand rehabilitation exercises.

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com) 


## To get started

As this project is a serious game with hand movement recognition and retrieval, you will probably need to install the following libraries to run the game without problems: 

### Pre-requisites

The main libraries you'll need are:

- *Pygame*
  ```pip install pygame```
  
- *Mediapipe*
  ```pip install mediapipe```

- *cv2* 
  ```pip install cv2``` 
  
You may also need some basic libraries from python such as:

- *Numpy*
  ```pip install install```
  
- *Pandas* 
  ```pip install pandas``` 
  
- *Moviepy* 
  ```pip install moviepy```
  
 - *Xlswriter* 
   ```sudo pip install xlswriter```
  

## Starting the game 

To start the game, you simply have to run the ```run.py``` file. Once it has been done, you will end up in the menu.


### Menu 


![Capture d’écran 2022-01-20 à 13 39 13](https://user-images.githubusercontent.com/93545145/150343010-289ecd8d-e99f-4859-bb6c-56b425b0b50e.png)


3 options are available: 

1. Play
2. Tutorial
3. Quit


Press ```Jouer``` to go to the level selector.

Press ```Tutorial``` to see the rules of the game.

Press ```Quitter``` to quit the game.


### Level Selector

![Capture d’écran 2022-01-20 à 13 39 25](https://user-images.githubusercontent.com/93545145/150343019-1ce004af-fb8e-41f4-becb-7bb9765b1a31.png "Salut")

In the level selector, you can choose three different levels. Each level corresponds to a different difficulty. Level 1 has been designed for patients
who are not able to close completely their hands while level 3 is for people who are at the end of their reeducation. On the following figure you can see what movement is expecting for each level (from level 1 to 3):

![Capture d’écran 2022-01-20 à 14 06 58](https://user-images.githubusercontent.com/93545145/150345057-3fbad285-9be3-48d6-8c07-e4e032edeaa4.png "Level 1")
![Capture d’écran 2022-01-20 à 14 07 09](https://user-images.githubusercontent.com/93545145/150345063-faa101ba-0d30-4637-a815-13dc2e08bd63.png)
![Capture d’écran 2022-01-20 à 14 07 20](https://user-images.githubusercontent.com/93545145/150345068-dc0d44dd-7ac0-4a70-ad87-ae1d64490bac.png)


Once your level is chosen, you can start playing ! 

![Capture d’écran 2022-01-20 à 13 39 47](https://user-images.githubusercontent.com/93545145/150343262-a964c5ec-809f-493d-80a9-928b1ac11bb3.png)


## End of the game

When the timer indicates 0s, the game is over. Then appears the score. You can have access to the number of obstacles you have touched, the number you have avoided and finally the maximum hand closure angle you've done. 

![Capture d’écran 2022-01-20 à 14 32 26](https://user-images.githubusercontent.com/93545145/150348749-5dbf1b1f-ef59-42d7-a201-f4683334ca01.png)

When the code has been fully runned, you can find in the ```data_aquisition``` folder an  excel file called ```scatter.xls``` where you can have access to the variation of the angle of the player's hand over the game time. 

![Capture d’écran 2022-01-20 à 14 41 24](https://user-images.githubusercontent.com/93545145/150350018-a1647830-ef8c-498c-81e5-a9ed702fec6a.png)





## Auteurs

* **Clément Asseraf** 
* **Khawla Benitto**
* **Victor Perset**
* **Julien Pham Van**
* **Bruna Vicente Ribeiro**

