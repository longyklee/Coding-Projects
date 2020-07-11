#include <iomanip>
#include <iostream>
#include <conio.h>
#include <unistd.h>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <time.h>
using namespace std;
int intinput(string out);
void output(string out);
string input(string out);
string fnames[1000],lnames[1000];
void save();
void openrooms();
void openfname();
void openlname();
int rooms[1000];

/*MAIN CODE*/
int main()
{
 srand(time(NULL));
 openrooms();
 int roomnum;
 output("##CFresort MANAGEMENT SYSTEM##");getch();
 for (;;){
 	 openrooms();
	 output("\n\nPlease Select Job\n");
	 output("1.Avaliable Room Query\t2.Call Room Service\t\n");
	 output("3.Check In\t\t4.Check Out\t5.Advanced Mode\n");
	 output("6.EXIT\n");
	 int job = intinput("JOB SELECT");
	 output("\n");
	 if (job==1){
	 	output("AVALIABLE ROOM QUERY\n");
	 	openrooms();
	 	roomnum=intinput("Room Number");
	 	if (rooms[roomnum]==1){
	 		char a[20];
	 		cout<<"ROOM *NOT* AVALIABLE"<<endl;
		}
		else{
			cout<<"ROOM *AVALIABLE*"<<endl;
		}
	 }
	 if (job==2){
	 	output("CALL ROOM SERVICE\n");
	 	roomnum=intinput("Room Number");
	 	if (rooms[roomnum]==1){
		 	string reason;
		 	cout<<"Reason: ";cin>>reason;
		 	output("CALLING ROOM SERVICE...\n");sleep(2);
		 	cout<<"SUCCESS IN CALLING ROOM SERVICE CODE "<<rand()%100<<" FOR ROOM "<<roomnum<<" FOR "<<reason<<endl;
		}
		else{
			output("ROOM DOES NOT EXIST\n");
		}
	 }
	 if (job==3){
	 	output("CHECK IN\n");
	 	roomnum=intinput("Room Number");
	 	output("CHECKING ROOM...\n");sleep(1.5);
	 	if (rooms[roomnum]==0){
	 		string fname,lname;
	 		output("First Name: ");
	 		cin>>fname;
		 	output("Last Name: ");
		 	cin>>lname;
		 	output("¡CCREDIT CARD¡C\n");getch();
			output("¡CID¡C\n");getch();
			output("¡CKEY CARD¡C\n");getch();
		 	output("LOADING...\n");sleep(1.5);
			cout<<fname<<" "<<lname<<" REGISTERED UNDER ROOM "<<setw(3)<<roomnum<<" SUCCESSFULLY"<<endl;
			rooms[roomnum]=1;
		}
		else{
			cout<<"ROOM "<<setw(3)<<roomnum<<" IS NOT AVALIABLE"<<endl;
		}
	}
	 if (job==4){
	 	output("CHECK OUT\n");
	 	roomnum=intinput("Room Number");
	 	output("CHECKING ROOM...\n");sleep(1.5);
	 	if (rooms[roomnum]==1){
	 		output("¡CCREDIT CARD¡C\n");getch();
			output("¡CID¡C\n");getch();
			output("¡CKEY CARD¡C\n");getch();
			cout<<"ROOM "<<roomnum<<" HAS SUCCESSFULLY CHECKED OUT"<<endl;
			rooms[roomnum]=0;
			lnames[roomnum]=' ';
			fnames[roomnum]=' ';
			save();
		}
		else{
			cout<<"ROOM "<<setw(3)<<roomnum<<" HAS ALREADY CHECKED OUT"<<endl;
	 	}
	 }
	 if (job==5){
	 	cout<<"ADVANCED MODE\n";
	 	cout<<"1.MODIFY ROOM AVALIABILITY\n2.RESET ALL ROOM AVALIABILITY DATA\n";
	 	job=intinput("SELECT JOB");
	 	if (job==1){
	 		roomnum=intinput("ROOM NUMBER");
	 		cout<<"ROOM NUMBER "<<roomnum<<" IS NOW CURRENTLY SET AS '"<<rooms[roomnum]<<"'"<<endl;
	 		int change;
	 		change=intinput("CHANGE TO");
	 		if (change==1 || change==0){
	 			rooms[roomnum]=change;
				save();
				output("SUCCESS!\n");
			}
			else{
				output("INVALID\n");
			}
		}
		if (job==2){
			char tf;
			cout<<"ARE YOU SURE?:";
			tf=getche();
			if (tf=='y'){
				int i;
				for (i=0;i<1000;i++){
					rooms[i]=rand()%2;
					fnames[i]=' ';
					lnames[i]=' ';
				}
				save();
				output("\nSUCCESS!\n");
			}
			else if (tf=='n'){
				output("\nJOB CANCELED\n");
			}else{
				output("\nFAILED.TRY AGAIN\n");
			}
		}
	 }
	 if (job==6){
	 	break;
	 }
 }
 save();
 output("PRESS ENTER TO EXIT...");getch();
 return 0;
}

/*EXTRA*/
int intinput(string out){
	int in;
	cout<<out<<":";
	cin>>in;
	return in;
}

string input(string out){
	string in;
	cout<<out<<": ";
	cin>>in;
	return in;
}

void output(string out){
	cout<<out;
}

void openrooms(){
	int i=0;
	ifstream infile("rooms.hotel");
	int a;
	while (infile >> a)
	{
		rooms[i]=a;
		i++;
	}
}

void save(){
	int i;
	ofstream myfile;
	myfile.open("rooms.hotel");
	for (i=0;i<1000;i++){
		myfile << rooms[i] << endl;
	}
	myfile.close();
	myfile.open("firstname.hotel");
	for (i=0;i<1000;i++){
		myfile << fnames[i] << endl;
	}
	myfile.close();
	myfile.open("lastname.hotel");
	for (i=0;i<1000;i++){
		myfile << lnames[i] << endl;
	}
	myfile.close();
}
