double myPow(double x, int n){
    if(n == 0 || x == 1) return 1;
    if(x == 0) return 0;
              
    double half = myPow(x, n/2);
        
    if(n % 2 == 0) return half * half;
        
    if(n > 0) return half * half * x;
            
    return half * half / x;
}
