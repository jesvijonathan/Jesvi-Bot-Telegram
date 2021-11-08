import threading

from mysql import connector


try:
    from config1 import *
except:
    from config import *


import platform

import modules.core.database as database
import modules.core.extract as extract

import time

import speedtest #pip install speedtest-cli
import psutil #pip install psutil
import urllib.request
import subprocess
import socket
import os
import sys



class system_cls():
    def __init__(self,update,context) -> None:
        
        self.update = update
        self.context = context
        
        self.msg = None
        self.user = None
        self.tag_msg = None
        self.tag_user = None
        
        self.msg = update.message

        self.user = user = self.msg['from_user']
        self.chat = chat = self.msg['chat']

        self.db = database.bot_db()

        try:
            self.tag_msg = tag_msg = update.message.reply_to_message

            self.tag_user = tag_user = tag_msg['from_user']

            self.db.add_user(user=tag_user)
        except:
            pass

        self.db.parse(chat=chat, user=user)

        self.chat_id = self.chat["id"]
        self.msg_string = self.msg.text


    def change_config():
        pass

    def sql_cmd_line(self,sql):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=8,context=self.context,sudo=1)
        if m== 7:
            pass
        else: return

        try:
            x = self.db.cursor.execute(sql)
        except Exception as x:
            self.msg.reply_text("Error during Execution : \n\n" + str(x), parse_mode="HTML")
            return
        
        try:
            list = self.db.cursor.fetchall()
            
            text = ",\n ".join(map(str, list))
            self.msg.reply_text(text, parse_mode="HTML")
        except Exception as x:
            try:
                z = self.db.db.commit()
                self.msg.reply_text("Committed !", parse_mode="HTML")
            except Exception as y:
                self.msg.reply_text( "Fetch Error : \n" + str(x) + "\n\nCommit Error: \n" + str(y), parse_mode="HTML")
            
        
    def system_stat(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=8,context=self.context,sudo=1)
        if m== 7:
            pass
        else: return
        try:
            s1 = "<code>Python  v" + platform.python_version() + "</code>\n"
            s2 = "<code>" + platform.system() + " v" + platform.version() + "</code>\n"
        except:
            s1 = s2 = ""
        try:
            s3 = "Ram Usage : <code>" + str(psutil.virtual_memory().percent) + "%</code>\n"
            s4 = "Cpu Usage  : <code>" + str(psutil.cpu_percent()) + "%</code>\n"
        except:
            s3 = s4 = ""
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = str(s.getsockname()[0])
            s.close()
            s5 = "Local Ip        : <code>" + ip + "</code>\n"
        except:
            s5 = ""

        try:
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            s6 = "External Ip  : <code>" + external_ip + "</code>\n"
        except:
            s6 = ""
        
        try:
            current_network = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
            ssid_line = [x for x in current_network if 'SSID' in x and 'BSSID' not in x]
            if ssid_line:
                ssid_list = ssid_line[0].split(':')
                connected_ssid = ssid_list[1].strip()
            s7 = "Connected  : <code>" + connected_ssid + "</code>\n"
        except:
            s7 = ""

        text = s7 + s3 + s4 + s5 + s6 + s1 + s2 

        msg = self.msg.reply_text(text=text ,
                                        parse_mode="HTML")

    def bot_restart(self,quit=0):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=8,context=self.context,sudo=1)
        if m== 7:
            pass
        else: return
        
        if quit==1:
            ms = self.msg.reply_text(text="Terminating !" ,
                                        parse_mode="HTML")
            
            #self.updater.stop()
            exit(1)
            sys.exit(1)
            return
        try:
            ms = self.msg.reply_text(text="Stoping Current Instance..." ,
                                        parse_mode="HTML")
            #p = psutil.Process(os.getpid())
            #for handler in p.open_files() + p.connections():
            #    os.close(handler.fd)
        except Exception as e:
            self.msg.reply_text(text=str(e) ,
                                        parse_mode="HTML")
        ms.edit_text(text="Restarting in 5 Seconds.." ,
                                        parse_mode="HTML")
        time.sleep(5)
        ms.edit_text(text="Restarting" ,
                                        parse_mode="HTML")
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def pc_restart(self,shut=0):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=8,context=self.context,sudo=1)
        if m== 7:
            pass
        else: return
        
        if shut == 1:
            self.msg.reply_text(text="Shutting Down Server..." ,
                                        parse_mode="HTML")
            os.system("shutdown /s /t 1")
        else:
            self.msg.reply_text(text="Restarting Server..." ,
                                        parse_mode="HTML")
            os.system("shutdown /r /t 1")

    def system_cmd_line(self,line=""):
        output = subprocess.Popen([line],stdout=subprocess.PIPE)
        r = output.communicate()
        self.msg.reply_text(text=str(r) ,
                                        parse_mode="HTML")

    def activity_log_file(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=8,context=self.context,sudo=1)
        if m== 7 or m==8:
            pass
        else: return

        path = path = str(os.path.dirname(os.path.dirname(sys.argv[0])))
        
        wp1= path + '/logs/log_bot_runtime.log'
        try:
            self.context.bot.send_document(chat_id=self.chat_id, document=open(wp1, 'rb'), filename="bot_runtime.log")
        except Exception as x:
            self.msg.reply_text(text="<code>Bot : " + str(x) + "</code>",
                                        parse_mode="HTML")
        
        wp2= path + '/logs/log_sql_runtime.log'
        try:
            self.context.bot.send_document(chat_id=self.chat_id, document=open(wp2, 'rb'), filename="sql_server.log")
        except Exception as y:
            self.msg.reply_text(text="<code>Sql : " + str(y) + "</code>",
                                        parse_mode="HTML")
        """
        file = context.bot.getFile(update.message.audio.file_id)
        file.download('./voice.ogg')

        def downloader(update, context):
            context.bot.get_file(update.message.document).download()
    
            # writing to a custom file
            with open("custom/file.doc", 'wb') as f:
                context.bot.get_file(update.message.document).download(out=f)
        """

    def net(self):
        m = extract.sudo_check_2(msg=self.msg,del_lvl=8,context=self.context,sudo=1)
        if m== 7 or m==8:
            pass
        else: return
            

        msg = self.msg.reply_text(text="<code>" + "Connecting..." + "</code>",
                                        parse_mode="HTML")

        st = speedtest.Speedtest(secure=True)
        st.get_best_server()

        msg.edit_text(text="<code>" + "Checking download speed..." + "</code>",
                      parse_mode="HTML")
        st.download()

        megabyte = 1./1000000
        d = st.results.download
        d = megabyte * d
        d = round(d, 2)

        ds = "Download Speed : " + str(d) + " mb/s"

        msg.edit_text(text=("<code>" + ds + "\n\nChecking upload speed..." + "</code>"),
                      parse_mode="HTML")
        st.upload()

        u = st.results.upload
        u = megabyte * u
        u = round(u, 2)

        us = "\nUpload Speed : " + str(u) + " mb/s"

        servernames = []
        msg.edit_text(text=("<code>" + ds + us + "\n\nMeasuring ping..." + "</code>"),
                      parse_mode="HTML")
        st.get_servers(servernames)
        p = str(st.results.ping)
        ps = "\nPing : " + p + "ms"

        msg.edit_text(text=("<code>" + "Test Time : " + time.strftime("%Y-%m-%d (%H:%M:%S)") + "\n\n" + ds + us + ps + "</code>"),
                      parse_mode="HTML")
        #print("--net speed *(D:"+str(d)+"mb/s, U:" + +str(u) + "mb/s, P:"+str(p)+"ms)")
    
    def publish(self,pub=""):
        cha = self.db.get_chat()
        
        for x,y in enumerate(cha):
            try:
                self.context.bot.send_message(y[0], pub)
            except:
                pass
            if x == 0:
                break
    
    def rel(self,pub=""):
        cha = self.db.get_chat()
        
        for x,y in enumerate(cha):
            try:
                self.context.bot.send_message(y[0], pub)
            except:
                pass
            if x == 0:
                break

    def router(self):
        res = self.msg_string.split(None,1)
        
        if res[0] == "/net":
            self.net()
        elif res[0] == "/publish":
            self.publish(res[1])
        elif res[0] == "/sql":
            self.sql_cmd_line(res[1])
        elif res[0] == "/system":
            try:
                if res[1] == "stat":
                    self.system_stat()
                elif res[1] == "log":
                    self.activity_log_file()
                elif res[1] == "restart":
                    self.bot_restart()
                elif res[1] == "quit":
                    self.bot_restart(quit=1)
                else:
                    self.system_stat()
            except Exception as x:
                print(str(x))
                self.system_stat()
        elif res[0] == "/cmd":
            self.system_cmd_line(res[1])
        elif res[0] == "/server":
            if res[1] == "restart":
                self.pc_restart(shut=0)
            elif res[1] == "shutdown":
                self.pc_restart(shut=1)
            
def system_threading(update, context):
    threading.Thread(target=system_cls(update,context).router, args=(), daemon=True).start()