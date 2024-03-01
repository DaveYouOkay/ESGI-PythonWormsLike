# Illustration du jeu

**Ceci est un Worms-like fait en Python en utilisant Pygame**

![title_screen](https://github.com/DaveYouOkay/ESGI-PythonWormsLike/assets/97070339/526a3531-696b-44b4-8674-9744781a1830)

## Generation Procedural 
### À partir de noise

![allGeneration](https://github.com/DaveYouOkay/ESGI-PythonWormsLike/assets/97070339/90a77af1-6526-42a9-8bdf-7ec38926d477)

## Choix du nombre de joueurs par équipes

![ChangeEquipe](https://github.com/DaveYouOkay/ESGI-PythonWormsLike/assets/97070339/f483097d-7c71-4e9f-8674-971ec1c35225)

### Le choix minimum est un duel quant au maximum est de 8 équipes de 4 joueurs 
### Vert = FPS | Blanc = Temps du tour | Rouge = Vie du personnage sélectionné

![allEquipeMinMax](https://github.com/DaveYouOkay/ESGI-PythonWormsLike/assets/97070339/73a7f1b1-c077-41a7-bc58-b5311a8e1736)

## Commande

![Commande](https://github.com/DaveYouOkay/ESGI-PythonWormsLike/assets/97070339/b85c7a29-3949-452f-8661-8b7beed1ff8f)

### Par défaut la grenade est équipé ! 
### Clic Gauche pour tirer | Clic Droit pour visualiser le tir

## Grenade

![Throw Grenade](https://github.com/DaveYouOkay/ESGI-PythonWormsLike/assets/97070339/59a136fa-35b5-4230-8cae-fbefa7c39f59)

## Lance-Roquette

![Throw Rocket](https://github.com/DaveYouOkay/ESGI-PythonWormsLike/assets/97070339/3c81c312-bd58-45e8-867b-9f244141cf6b)

# ---------

# Enoncé du projet

# _Semestre 1_ | Matière liée au projet : _Langages de Scripting Shell et Python_

**Le but de ce projet est de réaliser un jeu en python (la librairie PyGame est fortement recommandée), dans 
le style du jeu classique : _Worms_.**

## **Description du jeu :**
<div>
	Une partie se déroule sur un plateau de jeu en mode plateforme, en visualisant les personnages de profil. 
	Chaque joueur possède un ou plusieurs personnages disposés aléatoirement sur le plateau.
	Le déroulement d'une partie se fait à tour de rôle et à chaque tour, un joueur manipule un seul de ses personnages. 
	il pourra alors le déplacer (avec une limite de temps et/ou de points d’action) et le faire utiliser une de ses armes, afin d'éliminer un personnage adverse.
	La partie est terminée quand tous les personnages restants appartiennent au même joueur : Celui-ci est alors le gagnant.
</div>

### Le terrain
<div>
	Dans le jeu original, le terrain est irrégulier et destructible. 
	C'est-à-dire que les impacts des armes peuvent enlever des bout du terrain qui sont trouve alors modifié.
  Le terrain est soumis à la gravité terrestre ainsi qu'à un vent ayant une intensité et un angle différents à chaque tour.
</div>

### Les armes
<div>
	Dans le jeu original il y a tout un arsenal d'armes différentes : 
	Des armes de corps-à-corps, des explosifs, des armes à distance de tous types. 
	Les impacts de ses armes ont plusieurs effets :
	Diminution des points de vie des personnages touchés
</div>

 ### modification le terrain
 <div>
	 Déplacement des personnages touchés, en fonction de la violence de l'impact. 
	 Au niveau des armes, il vous est demandé de gérer les 2 plus grands classiques, à savoir, la grenade et la roquette. 
	 Pour lancer un de ces projectiles l'utilisateur indique un angle et une force. 
	 La grenade est normalement soumise à la gravité et explose au bout de N secondes ce nombre pouvant être paramétré. en cas d'impact, la grenade rebondit.
	 La roquette est soumise à la gravité et au vent et explose à l'impact.
 </div>
 
### Les déplacements
<div>
	Les personnages peuvent se déplacer en marchant ou en sautant.
	Ce qui vous est demandé :
	Vous devez implémenter les mécaniques du jeu énoncé précédemment, avec une interface graphique et l'utilisation du clavier et/ou de la souris.
</div>

### Minimum pour espérer avoir la moyenne : 
- 2 joueurs
- Chaque joueur à un personnage
- On a deux armes : 
  - la grenade, soumise à la gravité, explose à l’impact
  - la roquette, soumise à la gravité et au vent, explose à l’impact
- Les projectiles tuent instantanément tout personnage dans leur rayon d’explosion
- Le terrain est une ligne horizontale indestructible

**Vous pouvez ensuite :**
- gérer plus de 2 joueurs.
- gérer plus de 1 personnage par joueur.
- gérer correctement la grenade pour qu'elle explose au bout de N secondes.
- gérer l'aire d’effet des projectiles à l'explosion c'est-à-dire qu'ils feront plus de dégâts à un personnage 
- proche qu'a un personnage un peu plus éloigné.
- gérer le déplacement des personnages causé par le souffle des explosions
- gérer un terrain constitué de plusieurs lignes
- gérer un terrain destructible
		
**Si vous avez fait tout cela vous pouvez encore rajouter d'autres choses comme :**
- des variations de gravité
- d'autres armes
- des déplacements plus élaborées
- des effets sonores
- la possibilité de générer ses propres niveaux

**En plus des sources de votre projet, vous fournirez :**
<div>
un rapport, contenant un résumé des fonctionnalités de votre programme
les détails techniques de votre programme qui vous semblent intéressants
la répartition des tâches au sein du groupe
le lien vers le dépot git (github, bitbucket) de votre projet
</div>
