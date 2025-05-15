# include <stdio.h>

void main()
{

    // Assignments
    int a, b, c;
    float f = 2.45;

    a = f;  // a == INT, the decimals are not stored
    a = b = 30; // multiple assignment
    printf("%i\n", a);

    // INPUT
        // scanf("", &d) - data type(lecture format), address of data

    // scanf("%i", &c);
    // printf("%i\n", c);

    // Arithmetic operators
    // (+, -, /, *)

    int num1 = 2, num2 = 3;
    int result = num1 / num2; // = 0, int return int

    // Relational operators
    // (<, <=, >, >=, ==, !=)

    // Logic operators
    // (&&, ||, !)

    //Increment operators
    // (+=, -=, *=, /=, ++, --)

    int num3 = 0;
    printf("%i", num3++);
    printf("\n%i", num3++); // ++ or -- after the variable increment after exec. and before the variable...
    result = (++num3) + (num3--); // num3-- is 0 and ++num3 is 1, the pos fixed has priority

    // Math.h
    // pow(float x, float y) base, exponent
    // sqrt(float x) raiz
    // log10(float x)
}