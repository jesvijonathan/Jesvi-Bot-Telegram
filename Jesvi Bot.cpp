#include <iostream>
#include <conio.h>
#include <Windows.h>
#include <fstream>
#include <string>


using namespace std;    


int window(){
    SetConsoleTitle(("Jesvi Bot"));

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


int stop(int a){
    switch(a){
        case 1:
            system("taskkill /f /im cmd.exe /fi \"windowtitle eq Jesvi Bot Status\"");
            return 0;
        case 2:
            system("taskkill /f /im cmd.exe /fi \"windowtitle eq Bot Debugger\"");
            return 0;
        case 3:
            system("taskkill /f /im cmd.exe /fi \"windowtitle eq SQL Debugger\"");
            return 0;
        default:
            return 0;
    }
}

int call(int a=10,int an=0){
    
    if (an==1){
        switch(a){
        case 0:
            system("start /MIN /b bin\\start.bat");
            return 0;
            break;
        case 1:
            system("start /MIN bin\\logger_bot.bat");
            return 0;
            break;
        case 2:
            system("start /MIN bin\\logger_sql.bat");
            return 0;
            break;
        default:
            return 0;
        }
    }
    else{
        switch(a){
        case 0:
            system("start /b bin\\start.bat");
            return 0;
            break;
        case 1:
            system("start bin\\logger_bot.bat");
            return 0;
            break;
        case 2:
            system("start bin\\logger_sql.bat");
            return 0;
            break;
        default:
            return 0;
            }
        }

}


string data(string search){
  string word;

  ifstream myfile ("data.txt");

  while (myfile >> word) 
    {  
        if (word == search){
            myfile >> word >>word;
            myfile.close();
            return  word;
        } 
    } 

    myfile.close();

return "NULL";
}


string split(string str){
    char word[50],s[50];

    int c = 0;

    for(int i=0;i<str.length();i++){
        
        if (str[i] == ' ' || str[i] == '\0'){
            return word;
        }

        else{
            word[c] = str[i];
            c++;
        }
    }
    return "NULL";
}


int set_data(string var,string val){
    string word, line[14],w;
    int c=0;
    
    var= "bot_logging";
    val = "false";

    fstream myfile ("data.txt");

    while (getline(myfile,word))
    {
        w = split(word);

        if (w == var){
            line[c] = (w + " : " + val).c_str();
        }
        else{
            line[c] = word;
        }
        c++;
    }

    myfile.close();
    
    ofstream mfile;
    mfile.open ("data.txt", ios::trunc);


    for(int i=0;i<14;i++){
        mfile<<line[i]<<'\n';
    }

    mfile.close();

    return 0;
}


int launch_set(){

    if (data("bot_logging") == "true"){
        call(1,1);
    }
    if (data("sql_logging") == "true"){
        call(2,1);
    }
    return 0;
}


int start(){
restart:

    char con;
    
    system("Color 0A");

    splash();

    launch_set();

    cout<<"1-Stop | 2-Log Bot | 3-Log SQL\n4-Test | 5-Restart | 6-Folder\n\n";

    call(0);

    Sleep(7770);
    
    while(1){
        //system("Color 07");
        
        con=_getch();
        con = (int)((char)con - '0');

        switch(con){
            case 1:
                printf("Halting...\n");
                Sleep(500);
                stop(1);
                return 0;
                break;
            case 2:
                printf("Opening Bot Live Logger...");
                Sleep(200);
                call(2);
                //stop(2);
                printf("\33[2K\r");
                break;
            case 3:
                printf("Opening SQL Live Logger...");
                Sleep(200);
                call(3);
                //stop(3);
                printf("\33[2K\r");
                break;
            case 4:
            stop(2);
                break;
            case 5:
                printf("Restarting...\n");
                Sleep(1000);
                stop(1);
                goto restart;
                break;
            case 6:
                printf("Opening Resource...");
                Sleep(200);
                system("start explorer.exe %cd%\\logs");
                printf("\33[2K\r");
                break;
            default:
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
    
    //set_data("bot_logging","false");
    
    window();

    while(1){
        system("Color 07");
        menu();
    }

    _getch();
}