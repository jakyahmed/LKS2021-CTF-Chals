#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char* xor(FILE *file, int key) {    
    int c;
    size_t n = 0;
    char *result;

    result = malloc(1000);

    while ((c = fgetc(file)) != EOF)
    {
        result[n] = c ^ key;
        n += 1;
    }

    return result;
}


int main(int argc, char *argv[]){
    srand(time(0));
 
    FILE *fp;
    int num = (rand() % (255 - 1 + 1)) + 1;

    if( argc != 2 ) {
        printf("Usage: ./chall [FILENAME]");
    }
    else {
        fp = fopen(argv[1], "r");
        printf("%s", xor(fp, num));            
    }

}