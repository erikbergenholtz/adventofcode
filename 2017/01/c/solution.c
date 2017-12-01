#include <stdio.h>
#include <stdlib.h>

int readData(int **, char*);

int
main(int argc, char **argv)
{
    int sum1 = 0;
    int sum2 = 0;
    int *data = NULL;
    int length;
    length = readData(&data, argv[1]);
    if(data == NULL)
    {
        printf("Unable to read file\n");
        return 2;
    }
    for(int i=0 ; i<length ; i++)
    {
        if(data[i] == data[(i+1)%length])
            sum1 += data[i];
        if(data[i] == data[(i+(length/2))%length])
            sum2 += data[i];
    }
    printf("Task 1: %d\n",sum1);
    printf("Task 2: %d\n",sum2);

}

int
readData(int **data, char *fname)
{
    FILE *f = fopen(fname,"r");
    int i = 0;
    char c;
    int length = 0;
    if(f == NULL)
    {
        printf("Could not open file `%s` for reading\n", fname);
        return 0;
    }
    if( fseek(f,0,SEEK_END) == 0)
    {
        length = ftell(f);
        rewind(f);
    }
    *data = (int *)malloc(sizeof(int)*--length);
    do
    {
        c = (char)fgetc(f);
        if('0' <= c && c <= '9')
            (*data)[i++] = c-'0';
    }
    while(c != EOF);
    return length;
}
