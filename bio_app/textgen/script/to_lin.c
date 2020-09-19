#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h> 

int main(int argc, char *argv[])
{
    FILE* fichier1 = NULL;
    FILE* fichier2 = NULL;
    char d,e;
    fichier1 = fopen("eco_gen.txt", "r+");
    char c;
	while((c = fgetc(fichier1)) != EOF)
    { 
        if(c != '@' && c != '\n')
            putchar(c);
        else
        {
            if(c == '\n')
                continue;
            else
            {
            d = fgetc(fichier1);
            e = fgetc(fichier1);
            if (d == '@' && e == '@')
            {
                c = '\n';
                putchar(c);
            }
            else
            {
                putchar(d);
                putchar(e);
            }
        }
            

        }

    }
    c = 0;
    putchar(0);
    fclose(fichier1);
	fclose(fichier2);
    return 0;
}