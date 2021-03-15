#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	setvbuf(stdout, NULL, _IONBF, 0);
	int hack_me = 0x2;
	char buf[25];

	puts("Enter a secret number: ");
	gets(buf);

	if (hack_me > 0x2){
		system("cat flag.txt");
    }
    else {
        printf("Nope");
    }

	return 0;
}
