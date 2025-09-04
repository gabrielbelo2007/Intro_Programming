#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            int average = round(image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            int sepiaRed = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);

            sepiaRed = sepiaRed <= 255 ? sepiaRed : 255;
            sepiaGreen = sepiaGreen <= 255 ? sepiaGreen : 255;
            sepiaBlue = sepiaBlue <= 255 ? sepiaBlue : 255;

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int red;
    int blue;
    int green;

    for(int i = 0; i < height; i++){
        for(int j = 0; j < (width / 2); j++){
            red = image[i][j].rgbtRed;
            blue = image[i][j].rgbtBlue;
            green = image[i][j].rgbtGreen;

            image[i][j].rgbtRed = image[i][width - j].rgbtRed;
            image[i][j].rgbtBlue = image[i][width - j].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width - j].rgbtGreen;

            image[i][width - j].rgbtRed = red;
            image[i][width - j].rgbtBlue = blue;
            image[i][width - j].rgbtGreen = green;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            int average_red = 0;
            int average_green = 0;
            int average_blue = 0;

            // Bordas superiores
            if(i == 0 && j == 0){
                for(int l = 0; l < 2; l++){
                    for(int c = 0; c < 2; c++){
                        average_red += image[i + l][j + c].rgbtRed;
                        average_green += image[i + l][j + c].rgbtGreen;
                        average_blue += image[i + l][j + c].rgbtBlue;
                    }
                }
                image[i][j].rgbtRed = (average_red / 4);
                image[i][j].rgbtGreen = (average_green / 4);
                image[i][j].rgbtBlue = (average_blue / 4);

            }
            else if(i == 0 && j == (width - 1)){
                for(int l = 0; l < 2; l++){
                    for(int c = 0; c < 2; c++){
                        average_red += image[i + l][j - c].rgbtRed;
                        average_green += image[i + l][j - c].rgbtGreen;
                        average_blue += image[i + l][j - c].rgbtBlue;
                    }
                }
                image[i][j].rgbtRed = (average_red / 4);
                image[i][j].rgbtGreen = (average_green / 4);
                image[i][j].rgbtBlue = (average_blue / 4);
            }

            // Bordas inferiores
            else if(i == (height - 1) && j == 0){
                for(int l = 0; l < 2; l++){
                    for(int c = 0; c < 2; c++){
                        average_red += image[i - l][j + c].rgbtRed;
                        average_green += image[i - l][j + c].rgbtGreen;
                        average_blue += image[i - l][j + c].rgbtBlue;
                    }
                }
                image[i][j].rgbtRed = (average_red / 4);
                image[i][j].rgbtGreen = (average_green / 4);
                image[i][j].rgbtBlue = (average_blue / 4);

            }
            else if(i == (height - 1) && j == (width - 1)){
                for(int l = 0; l < 2; l++){
                    for(int c = 0; c < 2; c++){
                        average_red += image[i - l][j - c].rgbtRed;
                        average_green += image[i - l][j - c].rgbtGreen;
                        average_blue += image[i - l][j - c].rgbtBlue;
                    }
                }
                image[i][j].rgbtRed = (average_red / 4);
                image[i][j].rgbtGreen = (average_green / 4);
                image[i][j].rgbtBlue = (average_blue / 4);
            }

            // Primeira  e última coluna (além das bordas)
            else if(j == 0){
                for(int l = 0; l < 3; l++){
                    for(int c = 0; c < 2; c++){
                        average_red += image[(i - 1) + l][j + c].rgbtRed;
                        average_green += image[(i - 1) + l][j + c].rgbtGreen;
                        average_blue += image[(i - 1) + l][j + c].rgbtBlue;
                    }
                }

                image[i][j].rgbtRed = (average_red / 6);
                image[i][j].rgbtGreen = (average_green / 6);
                image[i][j].rgbtBlue = (average_blue / 6);
            }
            else if(j == (width - 1)){
                for(int l = 0; l < 3; l++){
                    for(int c = 0; c < 2; c++){
                        average_red += image[(i - 1) + l][j - c].rgbtRed;
                        average_green += image[(i - 1) + l][j - c].rgbtGreen;
                        average_blue += image[(i - 1) + l][j - c].rgbtBlue;
                    }
                }

                image[i][j].rgbtRed = (average_red / 6);
                image[i][j].rgbtGreen = (average_green / 6);
                image[i][j].rgbtBlue = (average_blue / 6);
            }

            // Primeira e última linha (além das bordas)
            else if(i == 0){
                for(int l = 0; l < 2; l++){
                    for(int c = 0; c < 3; c++){
                        average_red += image[i + l][(j - 1) + c].rgbtRed;
                        average_green += image[i + l][(j - 1) + c].rgbtGreen;
                        average_blue += image[i + l][(j - 1) + c].rgbtBlue;
                    }
                }

                image[i][j].rgbtRed = (average_red / 6);
                image[i][j].rgbtGreen = (average_green / 6);
                image[i][j].rgbtBlue = (average_blue / 6);
            }
            else if(i == (height - 1)){
                for(int l = 0; l < 2; l++){
                    for(int c = 0; c < 3; c++){
                        average_red += image[i - l][(j - 1) + c].rgbtRed;
                        average_green += image[i - l][(j - 1) + c].rgbtGreen;
                        average_blue += image[i - l][(j - 1) + c].rgbtBlue;
                    }
                }

                image[i][j].rgbtRed = (average_red / 6);
                image[i][j].rgbtGreen = (average_green / 6);
                image[i][j].rgbtBlue = (average_blue / 6);
            }

            // Centro
            else {
                for(int l = 0; l < 3; l++){
                    for(int c = 0; c < 3; c++){
                        average_red += image[(i - 1) + l][(j - 1) + c].rgbtRed;
                        average_green += image[(i - 1) + l][(j - 1) + c].rgbtGreen;
                        average_blue += image[(i - 1) + l][(j - 1) + c].rgbtBlue;
                    }
                }

                image[i][j].rgbtRed = (average_red / 9);
                image[i][j].rgbtGreen = (average_green / 9);
                image[i][j].rgbtBlue = (average_blue / 9);
            }
        }
    }
}
