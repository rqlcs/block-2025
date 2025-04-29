#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int codage(char *message,char *key,char *message_c) {
	FILE *f_m; /** ouverture fichier message **/
	FILE *f_k; /** ouverture fichier key **/
	FILE *f_mc; /** ouverture fichier message_chiffre **/
	
	/* strcutures permettant, une fois FOPEN 
	exécuté de recupérer des informations pour manipuler les fichiers
	en C */
	
	int c;
	int k1;
	int calcul;
	
	char * cheminFic_m = message;
	f_m = fopen(cheminFic_m, "r");
	/* Traitement erreur */
	if(f_m == NULL){
		fprintf(stderr,"Probleme ouverture %s\n",message);
		exit(1);
	}
	char * cheminFic_k = key;
	f_k = fopen(cheminFic_k, "r");
	if(f_k == NULL){
		fprintf(stderr,"Probleme ouverture %s\n",key);
		exit(2);
	}
	/* Traitement erreur */
	char * cheminFic_mc = message_c;	
	f_mc = fopen(cheminFic_mc, "w");
	if(f_mc == NULL){
		fprintf(stderr,"Probleme ouverture %s\n",message_c);
		exit(3);
	}
	while ((c = fgetc(f_m)) != EOF)
		
	{
		k1 = fgetc(f_k);
		calcul = (c+k1) % 256;
		fputc(calcul, f_mc);
	}
	
	
	fclose(f_m);
	fclose(f_k);
	fclose(f_mc);
	
	return EXIT_SUCCESS;
	
}
