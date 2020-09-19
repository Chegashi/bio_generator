#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h> 

int main(int argc, char *argv[])
{
    FILE* fichier1 = NULL;
    FILE* fichier2 = NULL;

    fichier1 = fopen("eco.txt", "r+");
    fichier2 = fopen("eco_n.txt", "a+");
    char c;
	while((c = fgetc(fichier1)) != EOF)
    {
		if((c > 31  && c < 58) || (c > 64 && c < 138) || (c > 96 && c < 123) || c == '\n' )
			if(isupper(c))
				fputc(tolower(c),fichier2);
			else
				fputc(c,fichier2);
        else
            fputc(' ',fichier2);
    }
    fclose(fichier1);
	fclose(fichier2);
    return 0;
}