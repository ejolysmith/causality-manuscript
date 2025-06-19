The causal-1, causal-2, causal-3, causal-4, and causal-5 directories are simulations of the systems with causal interaction. 
The non-causal-1 and non-causal-2 are directories are simulations of the systems without causal interaction (each directory is a separate system). 
In each directory there is C code that runs the Gillespie algorithm for the particular system multiple times with randomly varied parameters and outputs a txt file where each row is eta_xz and eta_yz for each parameter. 

All C code was compiled using the following command:
gcc code.c -o executable -lm
