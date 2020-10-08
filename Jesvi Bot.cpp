#include <iostream>
#include <conio.h>
#include <Windows.h>

using namespace std;


int window_size(){
    HWND console = GetConsoleWindow();
    RECT r;
    GetWindowRect(console, &r); //stores the console's current dimensions

    MoveWindow(console, r.left, r.top, 340, 480, TRUE); // 800 width, 100 height

    return 0;
}


void HideConsole()
{
    ::ShowWindow(::GetConsoleWindow(), SW_HIDE);
}


int splash(){
    system("Cls"); 
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


int stop(){
    system("taskkill /f /im cmd.exe /fi \"windowtitle eq Jesvi Bot Status\"");
    return 0;
}


int start(){
    char con;
    
    system("Color 0A");

    splash();

    cout<<"1-Stop | 2-Log Bot | 3-Log SQL\n4-Test | 5-Restart | 6-Folder\n\n";
    
    system("start /b bin\\start.bat");

    Sleep(7770);
    
    while(1){
        //system("Color 07");
        con=_getch();

        if (con == '1'){
            stop();
            return 0;
        }
        else{
            system("Color 0C");
            printf("Out of Field !");
            Sleep(200);
            printf("\33[2K\r");
            system("Color 0A");
        }
    }

    return 0;
}


int menu(){
    string options[4];
    int op;

    options[0] = "1. Start Jesvi Bot\n";
    options[1] = "2. Install Requirements\n";
    options[2] = "3. Log Bot\n";
    options[3] = "4. Log SQL\n";

    splash();

    for (int i=0;i<4;i++)
    {
        cout<<options[i];

    }

    op=_getch(); 
    op = (int)((char)op - '0');

    switch (op)
    {
    case 1:
        start();
        break;

    case 2:
        system("start bin\\requirements_installer.bat");
        break;

    case 3:
        //HideConsole();
        system("start bin\\logger_bot.bat");
        break;

    case 4:
        system("start bin\\logger_sql.bat");
        break;
    
    default:
        cout<<"Out of field !";
        break;
    }

    return 0;
}


int main(){
    
    window_size();

    while(1){
        system("Color 07");
        menu();
    }

    _getch();
}