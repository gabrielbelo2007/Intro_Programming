#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){

            int red_gx = 0, green_gx = 0, blue_gx = 0 ;
            int red_gy = 0, green_gy = 0, blue_gy = 0;

             for(int l = -1; l < 2; l++){
                 for(int c = -1; c < 2; c++){

                    int ni = i + l;
                    int nj = j + c;
                    
                    if(ni >= 0 && ni < height && nj >= 0 && nj < width){
                        red_gx += temp[ni][nj].rgbtRed * gx[l + 1][c + 1];
                        green_gx += temp[ni][nj].rgbtGreen * gx[l + 1][c + 1];
                        blue_gx += temp[ni][nj].rgbtBlue * gx[l + 1][c + 1];

                        red_gy += temp[ni][nj].rgbtRed * gy[l + 1][c + 1];
                        green_gy += temp[ni][nj].rgbtGreen * gy[l + 1][c + 1];
                        blue_gy += temp[ni][nj].rgbtBlue * gy[l + 1][c + 1];
                    }
                }

                image[i][j].rgbtRed = round(sqrt(red_gx * red_gx + red_gy * red_gy)) <= 255 ? round(sqrt(red_gx * red_gx + red_gy * red_gy)) : 255;
                image[i][j].rgbtGreen = round(sqrt(green_gx * green_gx + green_gy * green_gy)) <= 255 ? round(sqrt(green_gx * green_gx + green_gy * green_gy)) : 255;
                image[i][j].rgbtBlue = round(sqrt(blue_gx * blue_gx + blue_gy * blue_gy)) <= 255 ? round(sqrt(blue_gx * blue_gx + blue_gy * blue_gy)) : 255;
            }
        }
    }
}
