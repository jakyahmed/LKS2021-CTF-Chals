#include <stdio.h>
#include <stdbool.h>

bool validate_code (char *text){
    if (text[15] % text[5] != 5){
        return false;
    }

    if (text[0] + text[21] != 218){
        return false;
    }

    if (text[11] % text[14] - text[17] != -117){
        return false;
    }

    if (text[7] + text[10] != 227){
        return false;
    }

    if (text[24] * text[20] != 5610){
        return false;
    }

    if (text[19] + text[13] - text[1] != 41){
        return false;
    }

    if (text[6] - text[16] != 0){
        return false;
    }

    if (text[18] - text[22] * text[23] != -11475){
        return false;
    }

    if (text[9] - text[2] != 6){
        return false;
    }

    if (text[8] % text[4] + text[3] != 164){
        return false;
    }

    if (text[12] != 114){
        return false;
    }

    if (text[14] - text[19] + text[8] != 102){
        return false;
    }

    if (text[12] % text[20] + text[22] != 99){
        return false;
    }

    if (text[7] + text[15] % text[10] != 219){
        return false;
    }

    if (text[6] + text[17] != 212){
        return false;
    }

    if (text[5] * text[3] != 5712){
        return false;
    }

    if (text[9] * text[16] % text[0] != 0){
        return false;
    }

    if (text[4] - text[11] != 9){
        return false;
    }
    
    if (text[21] - text[18] != -12){
        return false;
    }
    
    if (text[24] + text[13] - text[2] != 39){
        return false;
    }
    
    if (text[23] % text[1] != 17){
        return false;
    }
    
    if (text[5] + text[4] != 159){
        return false;
    }
    
    if (text[9] * text[3] % text[21] != 5){
        return false;
    }
    
    if (text[6] + text[11] % text[2] != 194){
        return false;
    }
    
    if (text[20] + text[1] != 215){
        return false;
    }
    
    if (text[22] - text[19] != 46){
        return false;
    }
    
    if (text[23] - text[7] != 10){
        return false;
    }
    
    if (text[0] * text[18] != 13225){
        return false;
    }
    
    if (text[13] * text[10] != 11155){
        return false;
    }
    
    if (text[24] % text[17] != 51){
        return false;
    }
    
    if (text[12] + text[14] != 213){
        return false;
    }
    
    if (text[16] - text[8] != 43){
        return false;
    }
    
    if (text[15] != 107){
        return false;
    }
}

int main(){
    char passcode[25];

    printf("Enter code: ");
    scanf("%s", passcode);

    if (validate_code(passcode)) {
        printf("Correct");
        printf("\nThe flag is: LKS2021{%s}", passcode);
    }
    else {
        printf("Incorrect");
    }

    return 0;
}