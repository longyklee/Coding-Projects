#include <iomanip>
#include <iostream>
#include <ctype.h>
#include <conio.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int main()
{
 cout<<"***APPSUNGLE QUERY SYSTEM***";getch();
 for (;;){
	 char modelnum[10];
	 cout<<endl<<endl<<"MODEL NUMBER or BRAND:";cin>>modelnum;
	 cout<<endl<<"RESULTS:"<<endl;
	 if (strcmp(modelnum,"a20")==0){
	 		cout<<endl<<"SAMSUNG GALAXY A20 3G/32G"<<endl;
	 }
	 if (strcmp(modelnum,"a30s")==0){
	 		cout<<"SAMSUNG GALAXY A30s 4G/128G"<<endl;
	 }
	 if (strcmp(modelnum,"a40s")==0){
	 		cout<<"SAMSUNG GALAXY A40s 6G/64G"<<endl;
	 }
	 if (strcmp(modelnum,"a50")==0){
	 		cout<<"SAMSUNG GALAXY A50 6G/128G [OUT OF STOCK]"<<endl;
	 }
	 if (strcmp(modelnum,"a51")==0){
	 		cout<<"SAMSUNG GALAXY A51 6G/128G"<<endl;
	 }
	 if (strcmp(modelnum,"a60")==0){
	 		cout<<"SAMSUNG GALAXY A60 6G/128G"<<endl;
	 }
	 if (strcmp(modelnum,"a70")==0){
	 		cout<<"SAMSUNG GALAXY A70 6G/128G"<<endl;
	 }
	 if (strcmp(modelnum,"a71")==0){
	 		cout<<"SAMSUNG GALAXY A71 8G/128G"<<endl;
	 }
	 if (strcmp(modelnum,"a80")==0){
	 		cout<<"SAMSUNG GALAXY A80 8G/128G"<<endl;
	 }
	 if (strcmp(modelnum,"a8s")==0){
	 		cout<<"SAMSUNG GALAXY A8s 6G/128G"<<endl;
	 }
	 if (strcmp(modelnum,"s10")==0){
	 		cout<<"SAMSUNG GALAXY S10e 6G/128G ##OUT OF STOCK## ##END PRODUCTION##"<<endl;
	 		cout<<"SAMSUNG GALAXY S10  8G/128G ##OUT OF STOCK## ##END PRODUCTION##"<<endl;
	 		cout<<"SAMSUNG GALAXY S10  8G/512G ##OUT OF STOCK## ##END PRODUCTION##"<<endl;
	 		cout<<"SAMSUNG GALAXY S10+ 8G/512G"<<endl;
	 		cout<<"SAMSUNG GALAXY S10+ 12G/1TB"<<endl;
	 }
	 if (strcmp(modelnum,"note9")==0){
	 		cout<<"SAMSUNG GALAXY Note 9 6G/128G ##1 LEFT (BLUE)## ##END PRODUCTION##"<<endl;
	 		cout<<"SAMSUNG GALAXY Note 9 8G/512G ##END PRODUCTION##"<<endl;
	 }
	 if (strcmp(modelnum,"note10")==0){
	 		cout<<"SAMSUNG GALAXY Note 10      8G/256G"<<endl;
	 		cout<<"*SAMSUNG GALAXY Note 10 Lite 8G/128G ##NEW##"<<endl;
	 		cout<<"SAMSUNG GALAXY Note 10+     12G/256G"<<endl;
	 		cout<<"SAMSUNG GALAXY Note 10+     12G/512G"<<endl;
	 }
	 
	 if (strcmp(modelnum,"pixel3")==0 || strcmp(modelnum,"pixel3xl")==0){
	 		cout<<"GOOGLE PIXEL 3   4G/64G  ##OUT OF STOCK##"<<endl;
	 		cout<<"GOOGLE PIXEL 3   4G/128G ##OUT OF STOCK##"<<endl;
	 		cout<<"GOOGLE PIXEL 3XL 4G/64G  ##OUT OF STOCK##"<<endl;
	 		cout<<"GOOGLE PIXEL 3XL 4G/128G ##OUT OF STOCK##"<<endl;
	 }
	 if (strcmp(modelnum,"pixel3a")==0 || strcmp(modelnum,"pixel3axl")==0){
	 		cout<<"GOOGLE PIXEL 3a   4G/64G ##OUT OF STOCK##"<<endl;
	 		cout<<"GOOGLE PIXEL 3aXL 4G/64G ##FINAL SALE##"<<endl;
	 }
	 if (strcmp(modelnum,"pixel4")==0 || strcmp(modelnum,"pixel4xl")==0){
	 		cout<<"*GOOGLE PIXEL 4   6G/64G  ##NEW##"<<endl;
	 		cout<<"*GOOGLE PIXEL 4   6G/128G ##NEW##"<<endl;
	 		cout<<"*GOOGLE PIXEL 4XL 6G/64G  ##NEW##"<<endl;
	 		cout<<"*GOOGLE PIXEL 4XL 6G/128G ##NEW##"<<endl;
	 }
	 
	 if (strcmp(modelnum,"i11")==0){
	 		cout<<"APPLE iPHONE 11  4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 11  4G/128G"<<endl;
	 		cout<<"APPLE iPHONE 11  4G/256G"<<endl;
	 		cout<<"Black / Green / Yellow / Purple / Red/ White"<<endl;
	 		cout<<"  O       X        O       O       X     O"<<endl;
	 }
	 if (strcmp(modelnum,"i11pro")==0 || strcmp(modelnum,"i11p")==0){
	 		cout<<"APPLE iPHONE 11 Pro 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro 4G/256G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro 4G/512G"<<endl;
	 }
	 if (strcmp(modelnum,"i11promax")==0 || strcmp(modelnum,"i11pm")==0){
	 		cout<<"APPLE iPHONE 11 Pro Max 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro Max 4G/256G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro Max 4G/512G"<<endl;
	 }
	 if (strcmp(modelnum,"ixr")==0 || strcmp(modelnum,"xr")==0){
	 		cout<<"APPLE iPHONE Xr  4G/64G"<<endl;
	 		cout<<"APPLE iPHONE Xr  4G/128G"<<endl;
	 		cout<<"APPLE iPHONE Xr  4G/256G"<<endl;
	 }
	 if (strcmp(modelnum,"ixs")==0 || strcmp(modelnum,"xs")==0){
	 		cout<<"APPLE iPHONE Xs 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE Xs 4G/256G"<<endl;
	 		cout<<"APPLE iPHONE Xs 4G/512G"<<endl;
	 }
	 if (strcmp(modelnum,"ixsmax")==0 || strcmp(modelnum,"xsm")==0){
	 		cout<<"APPLE iPHONE Xs Max 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE Xs Max 4G/256G"<<endl;
	 		cout<<"APPLE iPHONE Xs Max 4G/512G ##OUT OF STOCK##"<<endl;
	 }
	 if (strcmp(modelnum,"i8")==0 || strcmp(modelnum,"i8p")==0){
	 		cout<<"APPLE iPHONE 8      4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 8      4G/128G"<<endl;
	 		cout<<"APPLE iPHONE 8      4G/256G"<<endl;
	 		cout<<"APPLE iPHONE 8 Plus 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 8 Plus 4G/128G"<<endl;
	 		cout<<"APPLE iPHONE 8 Plus 4G/256G"<<endl;
	 }
	 if (strcmp(modelnum,"i7")==0 || strcmp(modelnum,"i7p")==0){
	 		cout<<"APPLE iPHONE 7      4G/32G"<<endl;
	 		cout<<"APPLE iPHONE 7      4G/128G"<<endl;
	 		cout<<"APPLE iPHONE 7 Plus 4G/32G"<<endl;
	 		cout<<"APPLE iPHONE 7 Plus 4G/128G"<<endl;
	 }
	 if (strcmp(modelnum,"ix")==0 || strcmp(modelnum,"x")==0){
	 		cout<<"APPLE iPHONE X 4G/64G  ##OUT OF STOCK##"<<endl;
	 		cout<<"APPLE iPHONE X 4G/256G ##OUT OF STOCK##"<<endl;
	 		cout<<"APPLE iPHONE X 4G/512G ##OUT OF STOCK##"<<endl;
	 }
	 

	 if (strcmp(modelnum,"samsung")==0 || (strcmp(modelnum,"sam")==0)){	
		cout<<"SAMSUNG GALAXY A20  3G/32G"<<endl;
		cout<<"SAMSUNG GALAXY A30s 4G/128G"<<endl;
		cout<<"SAMSUNG GALAXY A40s 6G/64G"<<endl;
		cout<<"SAMSUNG GALAXY A50  6G/128G [OUT OF STOCK]"<<endl;
		cout<<"SAMSUNG GALAXY A51  6G/128G"<<endl;
		cout<<"SAMSUNG GALAXY A60  6G/128G"<<endl;
		cout<<"SAMSUNG GALAXY A70  6G/128G"<<endl;
		cout<<"SAMSUNG GALAXY A71  8G/128G"<<endl;
		cout<<"SAMSUNG GALAXY A80  8G/128G"<<endl;
		cout<<"SAMSUNG GALAXY A8s  6G/128G"<<endl<<endl;
		cout<<"SAMSUNG GALAXY S10e 6G/128G ##OUT OF STOCK## ##END PRODUCTION##"<<endl;
		cout<<"SAMSUNG GALAXY S10  8G/128G ##OUT OF STOCK## ##END PRODUCTION##"<<endl;
		cout<<"SAMSUNG GALAXY S10  8G/512G ##OUT OF STOCK## ##END PRODUCTION##"<<endl;
		cout<<"SAMSUNG GALAXY S10+ 8G/512G"<<endl;
		cout<<"SAMSUNG GALAXY S10+ 12G/1TB"<<endl<<endl;
		cout<<"SAMSUNG GALAXY Note 9       6G/128G ##1 LEFT## ##END PRODUCTION##"<<endl;
		cout<<"SAMSUNG GALAXY Note 9       8G/512G ##END PRODUCTION##"<<endl;
		cout<<"SAMSUNG GALAXY Note 10      8G/256G"<<endl;
		cout<<"*SAMSUNG GALAXY Note 10 Lite 8G/128G ##NEW##"<<endl;
		cout<<"SAMSUNG GALAXY Note 10+     12G/256G"<<endl;
		cout<<"SAMSUNG GALAXY Note 10+     12G/512G"<<endl;
	 }
	 if (strcmp(modelnum,"google")==0 || strcmp(modelnum,"gle")==0){
		cout<<"GOOGLE PIXEL 3   4G/64G  ##OUT OF STOCK##"<<endl;
		cout<<"GOOGLE PIXEL 3   4G/128G ##OUT OF STOCK##"<<endl;
		cout<<"GOOGLE PIXEL 3XL 4G/64G  ##OUT OF STOCK##"<<endl;
		cout<<"GOOGLE PIXEL 3XL 4G/128G ##OUT OF STOCK##"<<endl<<endl;
		cout<<"GOOGLE PIXEL 3a   4G/64G ##OUT OF STOCK##"<<endl;
		cout<<"GOOGLE PIXEL 3aXL 4G/64G ##FINAL SALE##"<<endl<<endl;
		cout<<"*GOOGLE PIXEL 4   6G/64G  ##NEW##"<<endl;
		cout<<"*GOOGLE PIXEL 4   6G/128G ##NEW##"<<endl;
		cout<<"*GOOGLE PIXEL 4XL 6G/64G  ##NEW##"<<endl;
		cout<<"*GOOGLE PIXEL 4XL 6G/128G ##NEW##"<<endl;
	 }
	 if (strcmp(modelnum,"apple")==0 || strcmp(modelnum,"appl")==0){
		cout<<"APPLE iPHONE 11  4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 11  4G/128G"<<endl;
	 		cout<<"APPLE iPHONE 11  4G/256G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro 4G/256G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro 4G/512G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro Max 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro Max 4G/256G"<<endl;
	 		cout<<"APPLE iPHONE 11 Pro Max 4G/512G"<<endl<<endl;
	 		cout<<"APPLE iPHONE Xr  4G/64G"<<endl;
	 		cout<<"APPLE iPHONE Xr  4G/128G"<<endl;
	 		cout<<"APPLE iPHONE Xr  4G/256G"<<endl;
	 		cout<<"APPLE iPHONE Xs 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE Xs 4G/256G"<<endl;
	 		cout<<"APPLE iPHONE Xs 4G/512G"<<endl;
	 		cout<<"APPLE iPHONE Xs Max 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE Xs Max 4G/256G"<<endl;
	 		cout<<"APPLE iPHONE Xs Max 4G/512G ##OUT OF STOCK##"<<endl<<endl;
	 		cout<<"APPLE iPHONE 8      4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 8      4G/128G"<<endl;
	 		cout<<"APPLE iPHONE 8      4G/256G"<<endl;
	 		cout<<"APPLE iPHONE 8 Plus 4G/64G"<<endl;
	 		cout<<"APPLE iPHONE 8 Plus 4G/128G"<<endl;
	 		cout<<"APPLE iPHONE 8 Plus 4G/256G"<<endl<<endl;
	 		cout<<"APPLE iPHONE 7      4G/32G"<<endl;
	 		cout<<"APPLE iPHONE 7      4G/128G"<<endl;
	 		cout<<"APPLE iPHONE 7 Plus 4G/32G"<<endl;
	 		cout<<"APPLE iPHONE 7 Plus 4G/128G"<<endl<<endl;
	 		cout<<"APPLE iPHONE X 4G/64G  ##OUT OF STOCK##"<<endl;
	 		cout<<"APPLE iPHONE X 4G/256G ##OUT OF STOCK##"<<endl;
	 		cout<<"APPLE iPHONE X 4G/512G ##OUT OF STOCK##"<<endl;
	 }
	 if (strcmp(modelnum,"exit")==0){
	 	break;
	 }
	 getch();
}
 return 0;
}
