                                                                                             memory_layout.c                                                                                                        
#include<stdio.h>
#include<unistd.h>

int main(){
pid_t pid=getpid();
printf("=============================================================================================\n");
printf("Process running , PID: %d\n",pid);
printf("Run this command in another terminal to inspect its memory \n");
printf("  cat /proc/%d/maps \n",pid);
printf("=============================================================================================\n");

printf("Sleeping for 60 seconds\n");
sleep(60);

printf("Finished the execution of program \n");
return 0;
}

