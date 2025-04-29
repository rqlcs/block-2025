#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define CODAGE 3
#define DECODAGE 2
#define KEY 1
#include "decodage.h"
#include "codage.h"
#include "key.h"
int main(int argc, char *argv[]) {
    
    char * filename_msg;
    char * filename_key;
    char * filename_mc;
    char * filename_mdc;
    if(argc < 3){  /** code -? f1 f2 f3 = argc[0] + argc[1] + ... = 4 **/
        fprintf(stderr,"Usage: %s [-c|-d|-k] <fichier_message|message_c> <fichier_key> <fichier_message_c|message_dc>\n",argv[0]);
        exit(1);
    }
    
    int option;
    
    if(strcmp(argv[1],"-d") == 0){
        option = 2;
        filename_msg = argv[2];
	    filename_key = argv[3];
	    filename_mdc = argv[4];
	    decodage(filename_msg,filename_key,filename_mdc);
    }
    if(strcmp(argv[1],"-c") == 0){
        option = 3;
	    filename_msg = argv[2];
	    filename_key = argv[3];
	    filename_mc = argv[4];
	    codage(filename_msg,filename_key,filename_mc);
    }
    if(strcmp(argv[1],"-k") == 0){
        option = 1;
	    filename_msg = argv[2];
	    filename_key = argv[3];
	    makekey(filename_msg, filename_key);
    }
    /* recupération sur la ligne de commande des noms de fichiers et option (-c pour codage
        -d pour décodage : message cle message_calculé    
    code -c f1 f2 f3
    code -d f1 f2 f3
    
    */
    if(option != CODAGE && option != DECODAGE && option != KEY){
        fprintf(stderr,"Error FLAG !\nUsage: %s [-c|-d|-k] <fichier_message|message_c> <fichier_key> <fichier_message_c|message_dc>\n",argv[0]);
        exit(2);
    }
    return EXIT_SUCCESS;
}
