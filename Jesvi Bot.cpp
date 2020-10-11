#include <iostream>
#include <conio.h>
#include <Windows.h>
#include <fstream>
#include <string>


using namespace std;    

string ans[8];


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

    jb[0] = "\n          _______   _______ \n";
    jb[1] = "     __  ___  __ \\ / __  __ _____  \n";
    jb[2] = "    |_ \\| __/' _| | |  \\/__|_   _| \n";
    jb[3] = "     _\\ | _|`._`` | | ~| \\/ || |   \n";
    jb[4] = "    /___|___|___/ | |__/\\__/ |_|   \n";
    jb[5] = "          _______/ \\_______\n";

    for(int i=0; i<=5;i++){
        cout<<jb[i];
    }
    
    cout<<"\n\n\n";//   --------------------------------

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
    if (ans[2] == "true"){
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
        case 3:
            system("start /MIN /b bin\\restart_database.bat");
            return 0;
            break;
        case 4:
            system("start /MIN /b bin\\requirements_installer.bat");
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
        case 3:
            system("start /MIN /b bin\\restart_database.bat");
            return 0;
            break;
        case 4:
            system("start bin\\requirements_installer.bat");
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


int assign_data(){
    string w;

    fstream myfile ("data.txt");

    while(myfile >> w) { //take word and print
        
        if (w=="bot_logging"){
            myfile >> w;
            myfile >> ans[0];
        }
        else if(w=="sql_logging"){
            myfile >> w;
            myfile >> ans[1];
        }
        else if(w=="minimise_log"){
            myfile >> w;
            myfile >> ans[2];
        }
        else if(w=="fresh_log"){
            myfile >> w;
            myfile >> ans[3];
        }
        else if(w=="general_log"){
            myfile >> w;
            myfile >> ans[4];
        }
        else if(w=="coloured_text"){
            myfile >> w;
            myfile >> ans[5];
        }
        else if(w=="auto_start"){
            myfile >> w;
            myfile >> ans[6];
        }
        else if(w=="req_installed_flag"){
            myfile >> w;
            myfile >> ans[7];
        }
    }

    myfile.close();

return 0;
}


int set_data(string var,string val){
    string word, line[14],w;
    int c=0;


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

    if (ans[0] == "true"){
        call(1,0);
    }
    if (ans[1] == "true"){
        call(2,0);
    }
    return 0;
}


int start(){
restart:

    char con;
    
    system("Color 0A");

    splash();
    
    if (ans[3]=="true"){
        ofstream ofs;
        ofs.open("logs\\log_sql_runtime.log", ios::out | ios::trunc);
        ofs.close();
    }
    
    call(5);
    
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
                call(1);
                Sleep(200);
                //stop(2);
                printf("\33[2K\r");
                break;
            case 3:
                printf("Opening SQL Live Logger...");
                call(2);
                Sleep(200);
                //stop(3);
                printf("\33[2K\r");
                break;
            case 4:
                printf("Test Text Sent !");
                Sleep(200);
                
                printf("\33[2K\r");
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


int credits(){
    printf("By Jesvi Jonthan");
    _getch();
    return 0;
}


int settings(){

    string options[8];
    int op;

    options[0] = "1. Live Log Bot on start : " + ans[0];
    options[1] = "\n2. Live Log SQL on start : " + ans[1];
    options[2] = "\n3. Minimise log window on start : " + ans[2];
    options[3] = "\n4. Clean log on start : " + ans[3];
    options[4] = "\n5. Database general log : " + ans[4];
    options[5] = "\n6. Cool Text : " + ans[5];
    options[6] = "\n7. Auto start on login : " + ans[6];
    
    
    splash();
    
   for (int i=0;i<8;i++)
    {
        cout<<options[i];

    }

    op=_getch(); 
    op = (int)((char)op - '0');

    switch(op){
        case 1:
            if (ans[0]=="true"){
                ans[0]= "false";
                set_data("bot_logging","false");
            }
            else{
                ans[0]= "true";
                set_data("bot_logging","true");
            }
            break;
        case 2:
            if (ans[1]=="true"){
                ans[1]= "false";
                set_data("sql_logging","false");
            }
            else{
                ans[1]= "true";
                set_data("sql_logging","true");
            }
            break;
        case 3:
            if (ans[2]=="true"){
                ans[2]= "false";
                set_data("minimise_log","false");
            }
            else{
                ans[2]= "true";
                set_data("minimise_log","true");
            }
            break;
        case 4:
            if (ans[3]=="true"){
                ans[3]= "false";
                set_data("fresh_log","false");
            }
            else{
                ans[3]= "true";
                set_data("fresh_log","true");
            }
            break;
        case 5:
            if (ans[4]=="true"){
                set_data("general_log","false");
                ans[4]= "false";
                system("py bin\\general_log_switch.py OFF");
            }
            else{
                set_data("general_log","true");
                ans[4]= "true";
                system("py bin\\general_log_switch.py ON");  
            }
            break;
        case 6:
            if (ans[5]=="true"){
                set_data("coloured_text","false");
                ans[5]= "false";
            }
            else{
                set_data("coloured_text","true");
                ans[5]= "true";  
            }
            break;
        case 7:
            if (ans[6]=="true"){
                set_data("auto_start","false");
                ans[6]= "false";
            }
            else{
                set_data("auto_start","true");
                ans[6]= "true";  
            }
            break;
        default:
            return 0;
    }

    return 0;
}


int menu(){
    string options[16];
    int op;

    options[0] = "1. Start\n";
    options[1] = "2. Open Resource Folder\n";
    options[2] = "3. Install Requirements\n";
    options[3] = "4. Restart Database\n";
    options[4] = "5. Settings\n";
    options[5] = "6. Refresh\n";
    options[6] = "7. Credits\n";
    options[7] = "8. Exit\n";
    

    splash();

    for (int i=0;i<8;i++)
    {
        cout<<options[i];
    }
    cout<<"\n";

    op=_getch(); 
    op = (int)((char)op - '0');

    switch (op)
    {
    case 1:
        printf("Starting Jesvi Bot..");
        start();
        break;

    case 2:
        printf("Opening Resource folder...");
        system("start explorer.exe %cd%\\logs");
        Sleep(850);
        printf("\33[2K\r");
        break;

    case 3:
        printf("Running Requirements Installer...");
        call(4);
        Sleep(350);
        break;

    case 4:
        printf("Restarting Database..\n\n");
        call(3);
        Sleep(800);
        break;

    case 5:
    settings();
    Sleep(200);
    break;

    case 6:
    printf("Refreshing..");
    Sleep(200);
    printf("\33[2K\r");
    break;

    case 7:
    printf("Viewing Credits..");
    Sleep(200);
    printf("\33[2K\r");
    credits();
    break;

    case 8:
        printf("Exiting..");
        Sleep(250);
        exit(10);
        break;

    default:
        cout<<"Out of field !";
        break;
    }

    return 0;
}


int main(){
    
    //set_data("bot_logging","false");
    assign_data();

    window();

    while(1){
        system("Color 07");
        menu();
    }

    _getch();
}