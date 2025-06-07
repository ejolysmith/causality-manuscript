#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// defining some constants used for the random number generator
#define IA 16807
#define IM 2147483647
#define AM (1.0/IM)
#define IQ 127773
#define IR 2836
#define NTAB 32
#define NDIV (1+(IM-1)/NTAB)
#define EPS 1.2e-7
#define RNMX (1.0-EPS)

// defining the random number generator
float ran1(int *idum)
{
	int j;
	long k;
	static long iy=0;
	static long iv[NTAB];
	float temp;

	if (*idum<=0 || !iy)
	{
        if (-(*idum)<1) *idum=1;
        else *idum=-(*idum);
        for (j=NTAB+7;j>=0;j--)
		{
			k=(*idum)/IQ;
			*idum=IA*(*idum-k*IQ)-IR*k;
			if (*idum<0) *idum+=IM;
			if (j<NTAB) iv[j]=*idum;
		}
        iy=iv[0];
	}

	k=(*idum)/IQ;
	*idum=IA*(*idum-k*IQ)-IR*k;
	if (*idum<0) *idum+=IM;
	j=iy/NDIV;
	iy=iv[j];
	iv[j]=*idum;
	if ((temp=AM*iy)>RNMX) return RNMX;
	else return temp;
}

double beta = 0.01;//0.6931471805599453/30; //Individual prion degradation constant
double beta_z = 0.001;//0.6931471805599453/30; //aggregate degradation constant

double lambda = 0.001*10000;
double lambda_z = 0.02;

double a = 1;
double b = 0.01;
double k = 10;
int n = 20;
double B = 0;
long double x_production_rate(int x, int y, int z, int n){
    if ( n > 0){
        return B + lambda/(1 + pow(((float)x)/(float)(a*z + b), n));
    }
    else{
        return B + lambda/(1 + pow(((float)x)/(float)(a*z + b), 0.1));
    }
}

long double x_degradation_rate(int x, int y, int z){
    return beta*x;
}

long double y_production_rate(int x, int y, int z, int n){
    if ( n > 0){
        return B + lambda/(1 + pow(((float)x)/(float)(a*z + b), n));
    }
    else{
        return B + lambda/(1 + pow(((float)x)/(float)(a*z + b), 0.1));
    }
}


long double y_degradation_rate(int x, int y, int z){
    return beta*y;
}

long double z_production_rate(int x, int y, int z){
    return lambda_z/(1 + pow(((float)z)/k, 2));;
}

long double z_degradation_rate(int x, int y, int z){
    return beta_z*z;
}


double rate_total_function(int x, int y, int z, int n){
    return ( x_production_rate(x,y,z, n) + x_degradation_rate(x,y,z) + y_production_rate(x,y,z,n) + y_degradation_rate(x,y,z) + z_production_rate(x,y,z) + z_degradation_rate(x,y,z) );
}

main()
{
	
	clock_t begin = clock();
    srand ( time(NULL) );

	
	FILE *ff = fopen("simulated-etas.txt", "w");

    int seed = -500;//atoi(argv[2]);
    //int seed_int = -2;//atoi(argv[3]);
	double rate_total;

	int x, y, z;  //Individual prion
        
    int kk;
	long N_steps;  //Number of steps in the gillespie simulation
	N_steps = 1e7;
    
	int number_of_components = 3;

    int N_sims = 10   ; //Number of times to run the gillespie simulation
	int sim = 0;

    int N_parameters = 1;
    
	double random_number;
	int random_integer;


    double t, t_tot, t_tot_0;

    double Probs[number_of_components];
	
    double xzbar, yzbar, xbar, ybar, zbar, xxbar, yybar, zzbar, xybar;
	//double Means[number_of_components];

	int i,j,k;
	
	int f = 0;
    int ii;
    int jj;
    int ww;
    int run;
    int xx, yy, YY_tot;
    int nd = 0;

    double etaxz, etayz, rhoxz, rhoyz, etaxy;
        
        
        
        
	for(sim = 0; sim<N_sims; sim++)
		{
            n = sim;

            x = 0;
            y = x;
            z = 0;
		

		    t_tot = 0;
            
            xbar = 0;
            ybar = 0;
            zbar = 0;
            
            xxbar = 0;
            yybar = 0;
            zzbar = 0;
            
            xzbar = 0;
            yzbar = 0;
            xybar = 0;
            
		for (i = 0; i < N_steps - 1; i++)
			{	
				
				rate_total = rate_total_function(x,y,z, n);
                
                

                random_number = (ran1(&seed)) ;
				t = 0;
				t = - log(random_number)/rate_total; //Figure out when a reaction occurs
                
                xbar = xbar + x*t;
                ybar = ybar + y*t;
                zbar = zbar + z*t;
                
                xxbar = xxbar + x*x*t;
                yybar = yybar + y*y*t;
                zzbar = zzbar + z*z*t;
                
                xzbar = xzbar + x*z*t;
                yzbar = yzbar + y*z*t;
                
                xybar = xybar + x*y*t;
                
                //fprintf(ff, "%d %d %d \n", x, y, z);
                t_tot = t_tot + t;
                //fprintf(ff, "%lf %d %d %d \n",t_tot, x, y, z);
                

				//Figure out which reaction occurs:

                Probs[0] = x_production_rate(x, y, z, n)/rate_total;
                Probs[1] = x_degradation_rate(x, y, z)/rate_total;
                Probs[2] = y_production_rate(x, y, z, n)/rate_total;
                Probs[3] = y_degradation_rate(x, y, z)/rate_total;
                Probs[4] = z_production_rate(x, y, z)/rate_total;
                
                

                random_number = (ran1(&seed)) ;
                
                    if (random_number <= Probs[0])
                    {
                        x = x + 1;
                        //printf("%d", 1);
                         
                    }
                    
                    else if(random_number <= Probs[0] + Probs[1])
                    {
                        x = x - 1;
                        //printf("%d", 2);
                    }

                    else if (random_number <= Probs[0] + Probs[1] + Probs[2])
                    {
                        y = y + 1;
                    }
                    
                    
                    else if (random_number <= Probs[0] + Probs[1] + Probs[2] + Probs[3] )
                    {
                        y = y - 1;
                    }
                
                    else if (random_number <= Probs[0] + Probs[1] + Probs[2] + Probs[3] + Probs[4] )
                    {
                        z = z + 1;
                    }
                
                    else
                    {
                        z = z - 1;
                    }
            
                
                
                //fprintf(ff, "%lf %d %d %d \n",t_tot, x, y, z);
                
                
                
                
		 	}
		

            xbar = xbar/t_tot;
            ybar = ybar/t_tot;
            zbar = zbar/t_tot;
            
            xxbar = xxbar/t_tot;
            yybar = yybar/t_tot;
            zzbar = zzbar/t_tot;
            
            xzbar = xzbar/t_tot;
            yzbar = yzbar/t_tot;
            xybar = xybar/t_tot;
            
            etaxz = (xzbar - xbar*zbar)/xbar/zbar;
            etayz = (yzbar - ybar*zbar)/ybar/zbar;
            etaxy = (xybar - xbar*ybar)/xbar/ybar;
            
            rhoxz = (xzbar - xbar*zbar)/sqrt((xxbar - xbar*xbar))/sqrt((zzbar - zbar*zbar));
            rhoyz = (yzbar - ybar*zbar)/sqrt((yybar - ybar*ybar))/sqrt((zzbar - zbar*zbar));
        
            printf("%lf %lf %lf %d \n", rhoxz/rhoyz, etaxz/etayz, n*pow(xbar/zbar, n)/(1 + pow(xbar/zbar, n)), n);
            fprintf(ff, "%lf %lf %lf %d \n", rhoxz/rhoyz, etaxz/etayz, n*pow(xbar/zbar, n)/(1 + pow(xbar/zbar, n)), n);
            //t_loss = t_loss + t_tot;
        }
         
    
    
    clock_t end = clock();
    printf("The time spent is: %lf \n\n\n", (double)(end - begin)/ CLOCKS_PER_SEC);

	fclose(ff);
 
        

}
