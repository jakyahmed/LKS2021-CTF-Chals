#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]){
    srand(time(0));
    
    int number = rand();
    int guess; 

    setbuf(stdout, 0);
    printf("Welcome to Guessing Game\n");
    printf("The rule is simple, just guess what number I'm thinking right now\n");
    printf("I'll give you the flag if you can answer correctly\n");

    printf("Guessed Number: ");
    scanf("%d", &guess);
    printf("Correct number: %d", number);

    if (guess != number){
        printf("\n\nWrong, no flag for you");
    }
    else{
        FILE *fp = fopen("flag.txt", "r");
        char flag = fgetc(fp);
        
        printf("\n\nCorrect, here is the flag\n");
        while((flag=fgetc(fp))!=EOF) {
            printf("%c", flag);
        }
    }

}