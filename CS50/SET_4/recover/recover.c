#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define SIZE_BLOCK 512
typedef uint8_t BYTE;

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Uso: ./recover imagem_do_cartao\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL) {
        printf("Não foi possível abrir o arquivo.\n");
        return 2;
    }

    uint8_t buffer[SIZE_BLOCK];
    FILE *output = NULL;
    int jpeg_count = 0;

    while (fread(buffer, sizeof(BYTE), SIZE_BLOCK, input) == SIZE_BLOCK) {

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) {

            if (output != NULL) {
                fclose(output);
            }

            char filename[8];
            sprintf(filename, "%03i.jpg", jpeg_count);

            output = fopen(filename, "w");
            jpeg_count++;

            fwrite(buffer, sizeof(BYTE), SIZE_BLOCK, output);

        } else if (output != NULL) {
            fwrite(buffer, sizeof(BYTE), SIZE_BLOCK, output);
        }
    }

    if (output != NULL) {
        fclose(output);
    }

    fclose(input);

    return 0;
}
