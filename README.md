<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://jesvijonathan.github.io/jesvijonathan/">
    <img src="tg_bot/common/res/icon.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Jesvi Bot v2</h3>

  <p align="center">
    A Telegram Handler Bot With Multiple Features & Support
    <br />
    <a href="https://jesvijonathan.github.io/jesvijonathan/"><strong>Official Webpage</strong></a>
    <br />
    <br />
    <a href="https://github.com/jesvijonathan/Jesvi-Bot">View Demo</a>
    ·
    <a href="https://github.com/jesvijonathan/Jesvi-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/jesvijonathan/Jesvi-Bot/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS
## Table of Contents

- [About This Project](#about-this-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Normal Installation](#normal-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)



<!-- ABOUT THE PROJECT -->

## About This Project

[![Jesvi Bot Utility][menu-screenshot]](https://example.com)

This project was started as a program to handle several telegram groups that have a large number of members & also to serve several other unique features that were made simple & easy to users & admins.

Here's some shallow information :

- Open Framework for starting your own bot service or use the fully built branches with prebuilt modules
- Comes with tones of usefull bot modules that can be fully customized & used for efficient management
- Has cross-platform support across major platforms
- Comes with a utility application for setting up the requirements, tweaking the configurations & to access other functionalities across platforms
- Simple & easy Database setup for both servers & regular personal computers
- Debugging & live status info are upated live
- And lots more stuff... explore it yourself.

This project still being developing by the me & the dev community, So you can expect more features and updates quite often..

All the tools are packed in & the Bot is all set to go in a server via script mode & also in a PC via utility mode which proves to be a good feature for debugging & for running mainstream

Feel free to mention a issue or a feature request in this repository :)
& for more information, Check out [Jesvi Bot's Official Webpage](https://jesvijonathan.github.io/jesvijonathan/) (<--under construction)

### Built With

Jesvi Bot is built mainly with Python3 (3.8.6).. However, the OS specific Utility, tools & features are built using Batch & C++ (Mingw) for Windows.

- [Python](https://www.python.org/)
- [C++](http://www.mingw.org/)
- [Batch](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
- [Shell](https://www.shellscript.sh/)
- [MySQL](https://www.mysql.com/)

<!-- GETTING STARTED -->

## Getting Started

Getting this program up and running is just a piece of cake ! Follow the steps and its just a few clicks away from getting it running...

### Prerequisites

- Windows or Linux Operating System
- [Latest Jesvi Bot Release](https://github.com/jesvijonathan/Jesvi-Bot/releases)
- [Python 3](https://www.python.org/)
- [MySQL 80](https://www.mysql.com/)
- [MySQL Connection](https://dev.mysql.com/doc/workbench/en/wb-getting-started-tutorial-create-connection.html)
- _50MB Disk Space_
- _Network Connection_

### Installation

#### Normal Installation

1. Unpack the [latest release](https://github.com/jesvijonathan/Jesvi-Bot/releases) of Jesvi Bot using [7zip](www.7zip.com)

2. Run [`Jesvi Bot.exe`](https://github.com/jesvijonathan/Jesvi-Bot-Telegram/blob/Jesvi-Bot-v2/tg_bot/windows/bin/Jesvi%20Bot.exe) application present inside the unpacked `Jesvi-Bot/tg_bot/Windows/bin/` Folder

   - _Move the bot folder to `'C:/'` directory, only if your user-account-name has a space in it, else bot utility in windows will have trouble launching._

3. Select `3. Install Requirements` in the Jesvi Bot utility application to let the application automatically install all the required dependencies & modules the script requires to run

   - Make sure python3 path is set under system environment as '**`py`**' (**not as 'python' or 'py3' or 'python3**', else you will encounter errors & will have to manually change it across all scripts that use 'py' to call python) & test it from command line using '`python --version`'
   - [`Microsoft visual C++ distribution 2014`](https://www.google.com/search?q=microsoft+visual+c%2B%2B+2014&rlz=1C1GCEA_enIN966IN966&oq=microsoft+visual+c%2B%2B+2014&aqs=chrome..69i57j0i512l5.6438j0j7&sourceid=chrome&ie=UTF-8) is required by some libraries installed via pip/wheel, so make sure to install it if you encounter errors.
   - Check if different version of python libraries are clashing.

4. Setup MYSQL workbench & create/setup a new conection with a database

   - Make sure mysql paths are available in system Environment and are running as `mysql` or `mysqlsh`, check from command line to ensure they are working & start mysql server.
   - Linux users can install `mariadb-server` if mysql-server is not available in apt (both work the same).
   - You have to `create a user` in mysql **that has been given all privileges** to edit the database, once created try logging into mysql as the new user to make sure it is working

5. Add the database details to `Config.py` to respective variables. Example :

```bot_username = "your_bot_username"
database_name = "your_database"
database_user  = "root"
database_password = "your_database_password"

#do the same for other variables..
```

6. Get your `Bot API Token` from [@botfather](https://telegram.me/botfather) via `/newbot` command & owner (\*your) details from [@jesvi_bot](https://telegram.me/jesvi_bot) via `/info` command in telegram
7. Now you can select `Start` in the Jesvi Bot Application & get Jesvi Bot fully running !
   - Check logs for any errors or further requirements

<!-- USAGE EXAMPLES -->

## Usage

Jesvi Bot can come very handy when you have to manage a telegram group, channel, etc.. because of all the included features & tools that the bot is equiped with, It is easy for users & admins to get the full potential out of Jesvi Bot.

```
THERE ARE ALOT MORE (50+ MODULES) BUT IMMA LAZY TO TYPE ALL OF THEM...
yeah.. I'm just too frikin lazy to type all of them ...
```

<!-- CONTRIBUTING -->

## Contributing

Contributions make this projetc better n better. Any contributions you make are **greatly appreciated**, So Imma gonna keep expecting pull req from you ;).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

**Jesvi Jonathan** -

- _Telegram :_ [@jesvi_jonathan](https://twitter.com/your_username)
- _GitHub :_ [jesvijonathan](https://github.com/jesvijonathan/Jesvi-Bot)
- _Email :_ jesvi22j@gmail.com

**Project Link :** [https://github.com/jesvijonathan/Jesvi-Bot](https://github.com/jesvijonathan/Jesvi-Bot)
