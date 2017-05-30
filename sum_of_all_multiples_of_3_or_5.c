//Kunal Gautam
//Codewars : @Kunalpod
//Problem name: Sum of all the multiples of 3 or 5
//Problem level: 7 kyu

int findSum (int n){
  int count = 0;
  for(int i=1; i<=n; i++)
    if(i%3==0||i%5==0)
      count = count + i;
  return(count);
}
