/*
	MPI version for PI for acceleration of execution time with the help of parallelism.

	compiler: mpicc -o mpi monte-carlo-pi-mpi.c
        execution: mpirun -np ${PROCS_NUM} ./mpi
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "mpi.h"

int main(int argc, char* argv[])
{
  int niter = 100000000;
  int myid;//hold's process's rank id
  double x,y;//x,y value for the random coordinate
  int i;
  int count=0;//Count holds all the number of how many good coordinates
  double z;//Used to check if x^2+y^2<=1
  double pi;//holds approx value of pi
  int reducedcount;//total number of "good" points from all nodes
  int reducedniter;//total number of ALL points from all nodes
  int size;
  MPI_Init(&argc, &argv);//Start MPI
  MPI_Comm_rank(MPI_COMM_WORLD, &myid);//get rank of node's process
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  int nb = niter/(size-1);
  int nb2 = niter % (size - 1) + nb;
  double start, end, difftime;
  start = MPI_Wtime();
  if(myid != 0 && myid !=size-1)
    {
      srand48(time(NULL));//Give rand() a seed value
      for (i=0; i<nb; ++i)//main loop
	{
	  x = (double)drand48();//gets a random x coordinate
	  y = (double)drand48();//gets a random y coordinate
	  z = ((x*x)+(y*y));//Checks to see if number in inside unit circle
	  if (z<=1)
	    {
	      ++count;//if it is, consider it a valid random point
	    }
	}
    }

  else if( myid ==size-1)
    {
      srand48(time(NULL));//Give rand() a seed value
      for (i=0; i<nb2; ++i)//main loop
        {
          x = (double)drand48();//gets a random x coordinate
          y = (double)drand48();//gets a random y coordinate
          z = ((x*x)+(y*y));//Checks to see if number in inside unit circle
          if (z<=1)
            {
              ++count;//if it is, consider it a valid random point
            }
        }
    }

  MPI_Reduce(&count, &reducedcount, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
  MPI_Reduce(&niter, &reducedniter, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
  reducedniter -= niter;//to compensate for no loop on master node

  end = MPI_Wtime();
  difftime = end - start;
  if (myid == 0)//if root process
    {      
      //p = 4(m/n)
      pi = ((double)reducedcount/(double)reducedniter)*4.0;
      pi = ((double)reducedcount/(double)niter)*4.0;
      printf("Pi: %.13f in %f s\n", pi, difftime);
    }
  MPI_Finalize();//Close the MPI instance
  return 0;
}
