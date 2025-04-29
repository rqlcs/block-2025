#include <stdio.h>
#include <stdlib.h>
int decodage(char * message_c,char * key,char *message_dc){
	FILE *f_m; /* ouverture fichier message */
        FILE *f_k; /* ouverture fichier cle */
        FILE *f_mdc; /* ouverture fichier message chiffre */ 
	
	
	/* strcutures permettant, une fois FOPEN 
	exécuté de recupérer des informations pour manipuler les fichier
	en C */
	
	int c;
	int k1;
	int calcul;
	
	char * cheminFic_m = message_c;
	f_m = fopen(cheminFic_m, "r");
	if(f_m == NULL){
		fprintf(stderr,"Probleme ouverture %s\n",cheminFic_m);
		exit(1);
	}
	char * cheminFic_k = key;
	f_k = fopen(cheminFic_k, "r");
	if(f_k == NULL){
		fprintf(stderr,"Probleme ouverture %s\n",cheminFic_k);
		exit(2);
	}
	/* Traitement erreur */
	char * cheminFic_mdc = message_dc;
	f_mdc = fopen(cheminFic_mdc, "w");
	if(f_mdc == NULL){
		fprintf(stderr,"Probleme ouverture %s\n",cheminFic_mdc);
		exit(3);
	}
		/* Traitement erreur */
	
	while ((c = fgetc(f_m)) != EOF)
		
	{
		k1 = fgetc(f_k);
		calcul = c-k1 >= 0?c-k1:256-(c-k1);
		fputc(calcul, f_mdc);
	}
	
	
	fclose(f_m);
	fclose(f_k);
	fclose(f_mdc);
	
	return EXIT_SUCCESS;
	
}
