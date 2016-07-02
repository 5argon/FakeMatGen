#FakeMatGen - Generate C++ transformation matrix declaration for OpenGL debugging

This is a very small simple program that can generate a C++ program string of 4x4 transformation matrix declaration for you. Useful for debugging OpenGL program if certain rotation or translation is going in the way that you are expecting or not.

## Functions
- Rotation about only one axis of your choice : x y z.
- Translation.
- Transpose support. (Note that in OpenGL the translation corresponds to 13th, 14th and 15th element of 16-element matrix but this program outputs [4][4] matrix. Use transpose or not depends on your program.

## Need
Python

## How to use

**Syntax**

`python fakematgen.py [angle] [axis] [xTranslation] [yTranslation] [zTranslation] [transpose]`

`python fakematgen.py 30 x`

**Output**

    float fakeMat[4][4] = 
    {{1, 0, 0, 0}, 
    {0, 0.866, -0.5, 0}, 
    {0, 0.5, 0.866, 0}, 
    {0, 0, 0, 1}};


`python fakematgen.py 90 y`

**Output**

    float fakeMat[4][4] = 
    {{0.0, 0, 1.0, 0}, 
    {0, 1, 0, 0}, 
    {-1.0, 0, 0.0, 0}, 
    {0, 0, 0, 1}};

`python fakematgen.py 45 z 1 2 3`

**Output**

    float fakeMat[4][4] = 
    {{0.7071, -0.7071, 0, 1.0}, 
    {0.7071, 0.7071, 0, 2.0}, 
    {0, 0, 1, 3.0}, 
    {0, 0, 0, 1}};

`python fakematgen.py 45 z 1 2 3 transpose`

**Output**

    float fakeMat[4][4] = 
    {{0.7071, 0.7071, 0, 0}, 
    {-0.7071, 0.7071, 0, 0}, 
    {0, 0, 1, 0}, 
    {1.0, 2.0, 3.0, 1}};

## More information to read

https://en.wikipedia.org/wiki/Rotation_matrix
https://en.wikipedia.org/wiki/Transformation_matrix
