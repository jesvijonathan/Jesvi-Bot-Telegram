#include <iostream>
#include <conio.h>
#include <Windows.h>

using namespace std;

int splash(){
    string jb[30];

    jb[0] = "\n __  ___  __ _   _ _   __  __ _____  \n";
    jb[1] = "|_ \\| __/' _| \\ / | | |  \\/__|_   _| \n";
    jb[2] = " _\\ | _|`._``\\ V /| | | -| \\/ || |   \n";
    jb[3] = "/___|___|___/ \\_/ |_| |__/\\__/ |_|   \n\n";

    for(int i=0; i<=3;i++){
        cout<<jb[i];
    }
    
    cout<<"----------------------------------\n\n";

    return 0;
}


int menu(){
    string options[2];
    int op;

    splash();

    options[0] = "1. Start Jesvi Bot\n";
    options[1] = "2. Install Requirements";
    

    for (int i=0;i<=1;i++)
    {
        cout<<options[i];

    }

    cin>>op; 
 
    switch (op)
    {
    case 1:
        system("\"bin\\run.bat\"");
        break;

    case 2:
        system("\"bin\\requirements_installer.bat\"");
        break;
    
    default:
        cout<<"Out of field !";
        break;
    }

    return 0;
}


int main(){
    menu();
    _getch();
}