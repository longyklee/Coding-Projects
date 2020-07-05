#include <iomanip>
#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;
int randomppl(int target);
int randomhero(int tA, int tB);
void reassign();
int temp[]={9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9},temp1,counter,hero[8][6];
int stemp[][5]={{9,9,9,9,9},{9,9,9,9,9},{9,9,9,9,9},{9,9,9,9,9},{9,9,9,9,9},{9,9,9,9,9},{9,9,9,9,9},{9,9,9,9,9},{9,9,9,9,9}};
int main()
{
 srand(time(NULL));
 string ppl []={"Aaron","Alex","Austin","Cory","Hiro","Jeremy","Justin","Yili"};
 string hero[][5] = {{"Sigma","Bastion","Reaper","Genji","Moira"},{"Doom","Moira","Bastion","Reaper","Tracer"},{"Roadhog","Doom","Mei","Reaper","Junkrat"},{"S76","Genji","Hanzo","Junkrat","Bapsite"},{"Doom","Reaper","McCree","Tracer","Bapsite"},{"Reaper","Doom","Sigma","Genji","Moira"},{"S76","Orisa","D.VA","Sigma","Doom"},{"Doom","Tracer","Ashe","Zarya","McCree"}};
 int i,j;
 for (i=0;i<8;i++){
 	cout<<ppl[randomppl(i)]<<"\t\t";
 }temp1=9;
 cout<<endl<<endl<<endl<<endl<<endl;
 
 
 
 for (i=0;i<8;i++){
 	cout<<ppl[i]<<"\t\t";
 }
 cout<<endl;
 for (i=0;i<5;i++){
 	for (j=0;j<8;j++){
 		cout<<hero[j][randomhero(j,i)]<<"\t\t";
	 }
	 cout<<endl;
 }
 system("pause");
 return 0;
}

int randomppl(int target){
	do {
		temp1=rand()%8;
	} while(temp1==temp[0]||temp1==temp[1]||temp1==temp[2]||temp1==temp[3]||temp1==temp[4]||temp1==temp[5]||temp1==temp[6]||temp1==temp[7]);
	temp[target]=temp1;
	return temp1;
}

int randomhero(int tA, int tB){
	do {
		temp1=rand()%5;
	} while(temp1==stemp[tA][0]||temp1==stemp[tA][1]||temp1==stemp[tA][2]||temp1==stemp[tA][3]||temp1==stemp[tA][4]);
	stemp[tA][tB]=temp1;
	return temp1;
}

