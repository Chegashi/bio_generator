#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n = 0;
void file_cs(char *path, char *domaine, char *created_by)
{
    char *file_to_read = (char*)malloc(4*100); 
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    int read,m=0;
    int co=0;
    file_to_read = path;
    fp = fopen(file_to_read, "r");
    while ((read = getline(&line, &len, fp)) > 0)
    {
        n++;
        m=0;
        printf("\n\tdb.session.add(Content(\"");
        while (line[m] != '\n')
            putchar(line[m++]);
        printf("\", '%s', '%s'))",domaine, created_by);
    }
    //printf("\n");
    fclose(fp);
}

int main(int argc, char const *argv[])
{
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/datasets/data.txt","data","human");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/datasets/desing.txt", "desing", "human");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/datasets/dev.txt","devlepement","human");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/datasets/eco.txt", "economie", "human");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/datasets/security.txt", "security" , "human");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/output/data.txt","data","machine");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/output/desing.txt", "desing", "machine");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/output/dev.txt","devlepement","machine");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/output/eco.txt", "economie", "machine");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app//textgen/output/security.txt", "security" , "machine");
    file_cs("/home/abort/Desktop/pfe2/fssm_pfe/proget/bio_app/textgen/output/all.txt", "all" , "machine");
    printf("");
    return 0;
}