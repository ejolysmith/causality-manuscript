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

double tau = 1;
double tau_z = 1;//0.
double tau_w;
double a = 1;
double lambda_z ;
double lambda;
double lambda_w;
int stepsize = 1;
double alpha = 1;



double x_production_rate(int x, int y, int z, int w){
    return lambda*w;
}

double x_degradation_rate(int x, int y, int z){
    return x*1./tau;
}

double y_production_rate(int x, int y, int z, int w){
    return alpha*lambda*w;
    
}

double y_degradation_rate(int x, int y, int z){
    return y*1./tau;
}

double z_production_rate(int x, int y, int z, int w){
    return lambda_z*w*w/(0.01 + 0.1*x);
}

double z_degradation_rate(int x, int y, int z){
    return z/tau_z;
}

double w_production_rate(int x, int y, int z){
    return lambda_w;
}

double w_degradation_rate(int x, int y, int z, int w){
    return w/tau_w;
}


double rate_total_function(int x, int y, int z, int w){
    return ( x_production_rate(x,y,z,w) + x_degradation_rate(x,y,z) + y_production_rate(x,y,z,w) + y_degradation_rate(x,y,z) + z_production_rate(x,y,z, w) + z_degradation_rate(x,y,z) + w_production_rate(x,y,z) + w_degradation_rate(x,y,z,w));
}

main()
{
	
	clock_t begin = clock();
    srand ( time(NULL) );

    FILE *ff = fopen("with-causality-data-system-2.txt", "w"); //

    int seed = -1322;//atoi(argv[2]);

    double rate_total;

	int x, y, z, w;
        
    int kk;
	long N_steps;
	N_steps = 1e7;
    
	int number_of_components = 4*2;

    int N_sims = 1000   ; //Number of times to run the gillespie simulation
	int sim = 0;

    int N_parameters = 1;
    
	double random_number;
	int random_integer;


    double t, t_tot, t_tot_0, T_time, T_factor;

    double Probs[number_of_components];
	
    double xzbar, yzbar, xbar, ybar, zbar, xxbar, yybar, zzbar, xybar;
	//double Means[number_of_components];

	int i,j,k;
	
	int f = 0;
    int ii;
    int jj;
    int ww;
    int run;
    int nd = 0;
    double TT = 1;
    double etaxz, etayz, rhoxz, rhoyz, etaxy;
    
    for(run = 0; run < N_parameters; run++)
    {
        
       
        
	for(sim = 0; sim<N_sims; sim++)
		{

            
            
            tau = 1;
            alpha = (ran1(&seed))*2 ;
            stepsize = 1;
            tau_z =(ran1(&seed))*2;
            tau_w =(ran1(&seed))*2;
            lambda =(ran1(&seed))*10;
            lambda_w =(ran1(&seed))*10;
            lambda_z =(ran1(&seed))*10;
            
            x = 0;
            y = x;
            z = 0;
            w = 0;
		

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
				
				rate_total = rate_total_function(x,y,z,w);
                
                

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
                
                t_tot = t_tot + t;
            
                

				//Figure out which reaction occurs:

                Probs[0] = x_production_rate(x, y, z, w)/rate_total;
                Probs[1] = x_degradation_rate(x, y, z)/rate_total;
                Probs[2] = y_production_rate(x, y, z, w)/rate_total;
                Probs[3] = y_degradation_rate(x, y, z)/rate_total;
                Probs[4] = z_production_rate(x, y, z, w)/rate_total;
                Probs[5] = z_degradation_rate(x, y, z)/rate_total;
                Probs[6] = w_production_rate(x,y,z)/rate_total;
                Probs[7] = w_degradation_rate(x, y, z, w)/rate_total;


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
                
                    else if (random_number <= Probs[0] + Probs[1] + Probs[2] + Probs[3] + Probs[4] + Probs[5] )
                    {
                        z = z - 1;
                    }
                
                    else if (random_number <= Probs[0] + Probs[1] + Probs[2] + Probs[3] + Probs[4] + Probs[5] + Probs[6] )
                    {
                        w = w + 1;
                    }
                
                    else
                    {
                        w = w - 1;
                    }
            
            
                
                
                
                
                
                
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
            
        
            printf("%lf %lf %lf %lf \n", etaxz, etayz, alpha*xbar/ybar, zbar);
            fprintf(ff, "%lf %lf  \n", etaxz, etayz);
        }
         
         
        
    }
    
    
    clock_t end = clock();
    printf("The time spent is: %lf \n\n\n", (double)(end - begin)/ CLOCKS_PER_SEC);

	fclose(ff);
 
        

}
