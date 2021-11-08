#include <iostream>
#include <conio.h>
#include <Windows.h>
#include <fstream>
#include <string>


using namespace std;

string ans[8];

int window(int s = 0)
{
    SetConsoleTitle("Jesvi Bot");
    
    if (s == 0)
    {
        system("MODE CON COLS=38 LINES=22");
    }
    else if (s == 1)
    {
        system("MODE CON COLS=38 LINES=28");
    }
    else if (s == 2)
    {
        system("MODE CON COLS=38 LINES=24");
    }

    return 0;
}

int splash(int full = 0)
{
    system("cls");

    string jb[30], g, g2;

    jb[0] = "\n          _______   _______  \n";
    jb[1] = "     __  ___  __ \\ / __  __ _____   \n";
    jb[2] = "    |_ \\| __/' _| | |  \\/__|_   _| \n";
    jb[3] = "     _\\ | _|`._`` | | ~| \\/ || |   \n";
    jb[4] = "    /___|___|___/ | |__/\\__/ |_|    \n";
    jb[5] = "          _______/ \\_______\n";

    auto l = "          _______/ \\_______  ",
         l2 = "          _______   _______  ";

    if (full == 1)
    {
        system("Color 0f");

        for (int i = 0; i < 30; i++)
        {
            g += l[i];
            g2 += l2[i];
            cout << "\n"
                 << g2 << "\n"
                 << jb[1] << jb[2] << jb[3] << jb[4] << g;
            Sleep(10);
            if (i == 29)
            {
                break;
            }
            cout << "\33[2K\r"
                 << "\x1b[A";
            cout << "\33[2K\r"
                 << "\x1b[A";
            cout << "\33[2K\r"
                 << "\x1b[A";
            cout << "\33[2K\r"
                 << "\x1b[A";
            cout << "\33[2K\r"
                 << "\x1b[A";
            cout << "\33[2K\r"
                 << "\x1b[A";
        }
        system("Color 07");
        return 0;
    }

    for (int i = 0; i <= 5; i++)
    {
        cout << jb[i];
    }

    cout << "\n\n\n"; //   --------------------------------

    return 0;
}

int stop(int a)
{
    switch (a)
    {
    case 1:
        system("taskkill /f /im cmd.exe /fi \"windowtitle eq Jesvi Bot Status\" /t");
        return 0;
    case 2:
        system("taskkill /f /im cmd.exe /fi \"windowtitle eq Bot Debugger\" /t");
        return 0;
    case 3:
        system("taskkill /f /im cmd.exe /fi \"windowtitle eq SQL Debugger\" /t");
        return 0;
    case 4:
        system("taskkill /f /im cmd.exe /fi \"windowtitle eq Jesvi Bot Auto Start\" /t");
        return 0;
    default:
        return 0;
    }

    return 0;
}

int call(int a = 10, int an = 0)
{
    if (ans[2] == "true")
    {
        switch (a)
        {
        case 0:
            return 0;
            break;
        case 1:
            system("start /MIN %cd%\\logger_bot.bat");
            return 0;
            break;
        case 2:
            system("start /MIN %cd%\\logger_sql.bat");
            return 0;
            break;
        case 3:
            system("start /MIN /b %cd%\\restart_database.bat");
            return 0;
            break;
        case 4:
            system("start /MIN /b %cd%\\requirements_installer.bat");
            
            return 0;
            break;
        case 5:
            system("start /MIN %cd%\\auto_start.bat");
            return 0;
            break;
        case 98:
            system("start /MIN /b %cd%\\shortcut_create.bat");
            break;
        default:
            return 0;
        }
    }
    else
    {
        switch (a)
        {
        case 0:
            system("start /b %cd%\\start.bat");
            return 0;
            break;
        case 1:
            system("start %cd%\\logger_bot.bat");
            return 0;
            break;
        case 2:
            system("start %cd%\\logger_sql.bat");
            return 0;
            break;
        case 3:
            system("start /MIN /b %cd%\\restart_database.bat");
            return 0;
            break;
        case 4:
            system("start %cd%\\requirements_installer.bat");
            return 0;
            break;
        case 5:
            system("start /MIN /b %cd%\\auto_start.bat");
            return 0;
            break;
        case 98:
            system("start /MIN /b %cd%\\shortcut_create.bat");
            break;
        default:
            return 0;
        }
    }

    return 0;
}

string data(string search)
{
    string word;

    ifstream myfile("data.txt");

    while (myfile >> word)
    {
        if (word == search)
        {
            myfile >> word >> word;
            myfile.close();
            return word;
        }
    }

    myfile.close();

    return "NULL";
}

string split(string str)
{

    char word[50], s[50];
    int c = 0;

    for (int i = 0; i < str.length(); i++)
    {

        if (str[i] == ' ' || str[i] == '\0')
        {
            return word;
        }
        else
        {
            word[c] = str[i];
            c++;
        }
    }

    return "NULL";
}

int assign_data()
{
    string w;

    fstream myfile("data.txt");

    while (myfile >> w)
    { //take word and print

        if (w == "bot_logging")
        {
            myfile >> w;
            myfile >> ans[0];
        }
        else if (w == "sql_logging")
        {
            myfile >> w;
            myfile >> ans[1];
        }
        else if (w == "minimise_log")
        {
            myfile >> w;
            myfile >> ans[2];
        }
        else if (w == "fresh_log")
        {
            myfile >> w;
            myfile >> ans[3];
        }
        else if (w == "general_log")
        {
            myfile >> w;
            myfile >> ans[4];
        }
        else if (w == "coloured_text")
        {
            myfile >> w;
            myfile >> ans[5];
        }
        else if (w == "auto_start")
        {
            myfile >> w;
            myfile >> ans[6];
        }
        else if (w == "req_installed_flag")
        {
            myfile >> w;
            myfile >> ans[7];
        }
    }

    myfile.close();

    return 0;
}

int set_data(string var, string val)
{
    string line[7], pre[7];
    int c = 0;

    pre[0] = "bot_logging";
    pre[1] = "sql_logging";
    pre[2] = "minimise_log";
    pre[3] = "fresh_log";
    pre[4] = "general_log";
    pre[5] = "coloured_text";
    pre[6] = "auto_start";

    for (int i = 0; i < 7; i++)
    {

        if (ans[i] == "")
        {
            ans[i] = "false";
        }

        line[i] = pre[i] + " : " + ans[i];
    }

    ofstream mfile;
    mfile.open("data.txt", ios::trunc);

    for (int i = 0; i < 7; i++)
    {
        mfile << line[i] << '\n';
    }

    mfile.close();

    return 0;
}

int launch_set()
{

    if (ans[0] == "true")
    {
        call(1, 0);
    }
    if (ans[1] == "true")
    {
        call(2, 0);
    }

    return 0;
}

int start()
{
restart:
    
    char con;

    if (ans[5] == "true")
    {
        system("Color 0A");
    }

    splash();

    cout << "\x1b[A"
         << "\33[2K\r"
         << "\x1b[A"
         << "\33[2K\r";

    cout << "--------------------------------------\n";

    if (ans[3] == "true")
    {
        ofstream ofs;
        ofs.open("logs\\log_sql_runtime.log", ios::out | ios::trunc);
        ofs.close();
    }

    launch_set();

    cout << "   1-Stop  |  2-Log Bot  |  3-LogSQL\n   4-Test  |  5-Restart  |  6-Folder\n";
    cout << "--------------------------------------\n\n";
    
    call(0);

    Sleep(2000);

    while (1)
    {
        con = _getch();
        con = (int)((char)con - '0');

        switch (con)
        {
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
            system("start explorer.exe %cd%");
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

int credits(int full = 1)
{
    int go;

    system("Color 0f");

    while (1)
    {
        splash(1);
        splash();

        cout << "\x1b[A"
             << "\33[2K\r";

        auto jb = "JESVI BOT", d = "Developed", j = "Jesvi Jonathan";

        if (full == 1)
        {
            for (int i = 0; i < 8; i++)
            {
                cout << "              ";
                for (int j = 0; j <= i; j++)
                {
                    cout << jb[j];
                }
                Sleep(30);
                printf("\33[2K\r");
            }
        }

        printf("              JESVI BOT\n\n");

        if (full == 1)
        {
            Sleep(500);

            for (int i = 0; i < 8; i++)
            {
                cout << "             ";
                for (int j = 0; j <= i; j++)
                {
                    cout << d[j];
                }
                Sleep(30);
                printf("\33[2K\r");
            }

            printf("             Developed ");
            Sleep(20);
            printf("\33[2K\r");
            printf("             Developed B");
            Sleep(30);
            printf("\33[2K\r");
            printf("             Developed By");
            Sleep(500);
            printf("\33[2K\r");
            printf("             Developed By   \b");
        }

        if (full == 1)
        {
            for (int i = 14; i >= 0; i--)
            {
                cout << j[i];
                Sleep(20);
                cout << "\b\b";
            }

            printf("\n");
            Sleep(400);
            printf("\33[2K\r\n");
        }
        else
        {
            printf("            Jesvi Jonathan\n\n");
        }
        //cout<<"\n\n";

        auto det1 = "          Version : 2.0               ",
             det2 = "          Release : 22.10.2021        ",
             det3 = "            State : Stable            ",
             det4 = "             Type : Full              ",
             line = "______________________________________";

        if (full == 1)
        {
            for (int i = 0; i < 40; i++)
            {
                for (int j = 0; j <= i; j++)
                {
                    cout << line[j];
                }

                cout << "\n";
                cout << "\n";

                for (int j = 0; j <= i; j++)
                {
                    cout << det1[j];
                }

                cout << "\n";
                for (int j = 0; j <= i; j++)
                {
                    cout << det2[j];
                }

                cout << "\n";

                for (int j = 0; j <= i; j++)
                {
                    cout << det3[j];
                }

                cout << "\n";

                for (int j = 0; j <= i; j++)
                {
                    cout << det4[j];
                }

                cout << "\n";

                for (int j = 0; j <= i; j++)
                {
                    cout << line[j];
                }

                Sleep(10);

                cout << "\33[2K\r"
                     << "\x1b[A";
                cout << "\33[2K\r"
                     << "\x1b[A";
                cout << "\33[2K\r"
                     << "\x1b[A";
                cout << "\33[2K\r"
                     << "\x1b[A";
                cout << "\33[2K\r"
                     << "\x1b[A";
                cout << "\33[2K\r"
                     << "\x1b[A";
            }

            cout << "\x1b[A"
                 << "\x1b[A"
                 << "\33[2K\r";
        }

        cout << "______________________________________";
        cout << "\n\n"
             << det1 << "\n"
             << det2 << "\n"
             << det3 << "\n"
             << det4 << "\n";
        cout << "______________________________________";

        cout << "\n\n";

        printf("\n  Main Webpage-1     2-Support Group");
        printf("\n   Source code-3     4-Jesvi Bot");
        printf("\n     Donations-5     6-Return\n");

        full = 0;
        go = _getch();

        printf("\33[2K\r\n");

        switch (go)
        {
        case '1':
            printf("Redirecting to Official Webpage..");
            system("start https://jesvijonathan.github.io/jesvijonathan/");
            break;
        case '2':
            printf("Redirecting to @Bot_Garage group..");
            system("start https://telegram.me/bot_garage");
            break;
        case '3':
            printf("Jesvi Bot Main GitHub repository..");
            system("start https://github.com/jesvijonathan/Jesvi-Bot");
            break;
        case '4':
            printf("Viewing Jesvi Bot in person");
            system("start https://telegram.me/jesvi_bot");
            break;
        case '5':
            printf("Developer Donation link :P");
            system("start www.google.com");
            break;
        case '6':
            printf("Moving back...");
            return 0;
            break;
        default:
            printf("Out of field !");
            break;
        }
    }

    return 0;
}

int settings()
{
    string options[8];
    int op;

    assign_data();

    while (1)
    {
        options[0] = "1. Live Log Bot on start : " + ans[0];
        options[1] = "\n2. Live Log SQL on start : " + ans[1];
        options[2] = "\n3. Minimise log window   : " + ans[2];
        options[3] = "\n4. Clean log on start    : " + ans[3];
        options[4] = "\n5. Database general log  : " + ans[4];
        options[5] = "\n6. Cool Text             : " + ans[5];
        options[6] = "\n7. Auto start on login   : " + ans[6];
        options[7] = "\n8. Return";

        splash();

        for (int i = 0; i < 8; i++)
        {
            cout << options[i];
        }

        cout << "\n\n";

        op = _getch();
        op = (int)((char)op - '0');

        printf("\33[2K\r");

        switch (op)
        {
        case 0:
            call(98);
            printf("Creating Bot Shortcut..");
            break;
        case 1:
            printf("Switching Bot log...");
            if (ans[0] == "true")
            {
                ans[0] = "false";
                set_data("bot_logging", "false");
            }
            else
            {
                ans[0] = "true";
                set_data("bot_logging", "true");
            }

            break;
        case 2:
            printf("Switching Sql log...");
            if (ans[1] == "true")
            {
                ans[1] = "false";
                set_data("sql_logging", "false");
            }
            else
            {
                ans[1] = "true";
                set_data("sql_logging", "true");
            }
            break;
        case 3:
            printf("Switching log window...");
            if (ans[2] == "true")
            {
                ans[2] = "false";
                set_data("minimise_log", "false");
            }
            else
            {
                ans[2] = "true";
                set_data("minimise_log", "true");
            }
            break;
        case 4:
            printf("Switching fresh log...");
            if (ans[3] == "true")
            {
                ans[3] = "false";
                set_data("fresh_log", "false");
            }
            else
            {
                ans[3] = "true";
                set_data("fresh_log", "true");
            }
            break;
        case 5:
            printf("Switching general log...");
            if (ans[4] == "true")
            {
                ans[4] = "false";
                set_data("general_log", "false");
                system("py %cd%\\gen_log.py OFF");
            }
            else
            {
                ans[4] = "true";
                set_data("general_log", "true");
                system("py %cd%\\gen_log.py ON");
            }
            Sleep(850);
            break;
        case 6:
            printf("Switching coloured...");
            if (ans[5] == "true")
            {
                ans[5] = "false";
                set_data("coloured_text", "false");
            }
            else
            {
                ans[5] = "true";
                set_data("coloured_text", "true");
            }
            break;
        case 7:
            printf("Switching auto start...");
            if (ans[6] == "true")
            {
                ans[6] = "false";
                set_data("auto_start", "false");
                string pp, dd = "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Jesvi Bot.lnk";
                pp = string(getenv("USERPROFILE"));
                auto y = pp + dd;
                remove((y).c_str());
            }
            else
            {
                ans[6] = "true";
                set_data("auto_start", "true");
                call(98);
            }
            break;
        case 8:
            printf("Returning..");
            return 0;
            break;
        default:
            printf("Out of field !");
            break;
        }
    }
    return 0;
}

int menu()
{
    string options[16];
    int op;

    options[0] = "1. Start\n";
    options[1] = "2. Open Resource Folder\n";
    options[2] = "3. Install Requirements\n";
    options[3] = "4. Restart Database\n";
    options[4] = "5. Settings\n";
    options[5] = "6. Refresh\n";
    options[6] = "7. About\n";
    options[7] = "8. Exit\n";

    splash();

    for (int i = 0; i < 8; i++)
    {
        cout << options[i];
    }

    cout << "\n";

    op = _getch();
    op = (int)((char)op - '0');

    switch (op)
    {
    case 0:
        printf("Openning Logs..");
        Sleep(200);
        window(1);
        printf("\33[2K\r");
        call(1);
        call(2);
        window(0);
        break;
    case 1:
        printf("Starting Jesvi Bot..");
        window(1);
        stop(1);
        stop(4);
        start();
        window(0);
        break;

    case 2:
        printf("Opening Resource folder...");
        system("start explorer.exe %cd%");
        Sleep(850);
        printf("\33[2K\r");
        break;

    case 3:
        printf("Running Requirements Installer...");
        call(4);
        call(98);
        Sleep(350);
        break;

    case 4:
        printf("Restarting Database..\n\n");
        call(3);
        Sleep(800);
        break;

    case 5:
        window(2);
        settings();
        Sleep(200);
        window(0);
        break;

    case 6:
        printf("Refreshing..");
        assign_data();
        Sleep(200);
        printf("\33[2K\r");
        break;

    case 7:
        printf("Viewing Credits & info..");
        Sleep(200);
        window(1);
        printf("\33[2K\r");
        credits();
        window(0);
        break;

    case 8:
        printf("              Jesvi Bot");
        Sleep(250);
        printf("\n          By Jesvi Jonathan");
        Sleep(500);
        exit(1);
        break;
    
    case 9:
        printf("Stopping All JBot Services..");
        Sleep(200);
        window(1);
        printf("\33[2K\r");
        stop(1);
        stop(2);
        stop(3);
        stop(4);
        window(0);
        break;

    default:
        cout << "Out of field !";
        break;
    }

    return 0;
}

int main()
{
    assign_data();

    window(0);

    splash(1);

    while (1)
    {
        system("Color 07");
        menu();
    }

    return 0;
}