#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
int makekey(char* message, char* fichier_key) {
    FILE* fichier_message;
    FILE* fichier_cle;
    char* alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    size_t length = strlen(alphabet);
    int c;
    int n;
    srand(time(NULL));
    fichier_message = fopen(message, "r");
    if(fichier_message == NULL) {
        fprintf(stderr,"Probleme ouverture %s\n",message);
	exit(1);
    }
    fichier_cle = fopen(fichier_key, "w");
    if(fichier_cle == NULL) {
     fprintf(stderr,"Probleme ouverture %s\n",fichier_key);
     exit(2);
    }
    while ((c = fgetc(fichier_message)) != EOF) {
        n = rand() % length;
        fputc(alphabet[n], fichier_cle);
    }
    fclose(fichier_message);
    fclose(fichier_cle);
    return EXIT_SUCCESS;
}
