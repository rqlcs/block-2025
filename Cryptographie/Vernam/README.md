# Projet DEV Vernam - Groupe 4 BUT1INFO

<br>
<p align="center">
    <img src="https://cdn-icons-png.flaticon.com/512/1163/1163519.png" width="150" height="120">
</p>
<br>

# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Meuble_h%C3%A9raldique_Engrenage.svg/800px-Meuble_h%C3%A9raldique_Engrenage.svg.png" width="30" height="40"> Compilation , Makefile 

**La compilation du script principale** _vernam.c_ **se fait à l'aide de la commande :**
<br><br>
```:~$ make```
<br><br>
**Une fois la compilation du script** _vernam.c_ **terminé nous pouvons supprimer les fichiers d'extensions** ```.o``` **avec la commande :**
<br><br>
```:~$ make clean```
<br><br>

# <img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Octicons-terminal.svg" width="40" height="40"> Utilisation 

**Pour utiliser l'exécutable** _vernam_ **vous devez dans un premier temps, passer en premier argument l'option que vous souhaiter utiliser.**<br><br>
`Usage: ./vernam [-c|-d|-k] <fichier_message|message_c> <fichier_key> <fichier_message_c|message_dc>`<br><br>
**-> FLAG** ```-d``` **pour déchiffrer un message à l'aide de votre clé**<br>
**-> FLAG** ```-c``` **pour chiffrer un message à l'aide de votre clé**<br>
**-> FLAG** ```-k``` **pour créer une clé en fonction de votre message**<br><br>

**Dans un second temps, vous devez passer en second argument le** _fichier_ **contenant votre message (chiffrer ou en clair en fonction de votre option).**<br>
**Ensuite, vous devez passer en troisième argument le** _fichier_ **contenant votre clé.**<br>
**Enfin, le troisième argument (étant réservé pour les FLAGs** `-d` **&** `-c` **) devra contenir le fichier de votre message en sortie. (chiffrer ou vers déchiffrer)**  <br><br>

# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/High-contrast-utilities-terminal.svg/1024px-High-contrast-utilities-terminal.svg.png" width="40" height="40"> Exemples 

**Exemple de chiffrement d'un message stocker dans un fichier :**
<br>
`:~$ make && ./vernam -c message.txt cle.txt message_c.txt`
<br><br>
**Exemple de dechiffrement d'un message stocker dans un fichier :**
<br>
`:~$ make && ./vernam -c message_c.txt cle.txt message_dc.txt`
<br><br>
**Exemple de création d'une clé de chiffrement depuis un message stocker dans un fichier :**
<br>
`:~$ make && ./vernam -c message.txt key2.txt`
<br><br>

# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Green_Danger.svg/1170px-Green_Danger.svg.png" width="40" height="40"> Traitements d'erreurs 

**En cas de problème d'ouverture de fichier , le programme pourra renvoyer le problème d'ouverture sur le fichier en question** <br> **et quitter le programme grâce à la gestion d'erreur suivante :**
<br><br>
```
/** Exemple de gestion d'erreur avec fichier cle **/

FILE * fichier_cle;
fichier_cle = fopen(fichier_contenant_la_cle,"r");
if(fichier_cle == NULL){
    fprintf(stderr,"Probleme ouverture %s\n",fichier_contenant_la_cle);
    exit(1);
}
```
**La fonction** `fprintf(stderr,...)` **permet d'enregistrer les messages d’erreur ou de débogage pendant l’exécution du programme.**<br>
**La fonction** `exit()` **permet de marquer l'arrêt du programme.**
