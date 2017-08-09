/*
	OpenMP version for PI, using the thread level parallelism

	Compiler: gcc -o omp monte-carlo-pi-omp.c
	Execution: ./omp
*/
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define NUM_SAMPLING 1000000

int main(int argc, char* argv[])
{	
	double x,y;							//x,y value for the random coordinate
	int i;
        int counting=0;							//Count holds all the number of how many good coordinates
	double d;							
	double pi;							
	int numthreads = 2;
	double start = omp_get_wtime();
	double end, timediff;

	#pragma omp parallel private(x, y, d, i) reduction(+:counting) num_threads(numthreads)
	{
		srand48((int)time(NULL) ^ omp_get_thread_num());
		for (i=0; i<NUM_SAMPLING; i++)					//main loop
		{
			x = (double)drand48();				//gets a random x coordinate
			y = (double)drand48();				//gets a random y coordinate
			d = ((x*x)+(y*y));				//Checks to see if number is inside unit circle
			if (d<=1)
			{
				counting++;				//if it is, consider it a valid random point	
			}		
		}
	} 
	pi = ((double)counting/(double)(NUM_SAMPLING*numthreads))*4.0;

	end = omp_get_wtime();
	timediff = end - start;

	printf("Pi: %.13f, with %d threads, execution time %f s\n", pi, numthreads, timediff);

	return 0;
}
