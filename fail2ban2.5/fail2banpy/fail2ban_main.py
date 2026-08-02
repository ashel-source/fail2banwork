#!/usr/bin/python
# coding: utf-8
# +-------------------------------------------------------------------
# | 宝塔Linux面板
# +-------------------------------------------------------------------
# | Copyright (c) 2015-2099 宝塔软件(http://bt.cn) All rights reserved.
# +-------------------------------------------------------------------
# | Author: zhwem <zhw@bt.cn>
# +-------------------------------------------------------------------

# +--------------------------------------------------------------------
# |   宝塔fail2ban管理器
# +--------------------------------------------------------------------
import public, re, os, json, system
import ipaddress


class fail2ban_main:
    _set_up_path = "/www/server/panel/plugin/fail2ban"
    _config = _set_up_path + "/config.json"
    _status = _set_up_path + "/status.json"
    _black_list = _set_up_path + "/black_list.json"
    _jail_local_file = "/etc/fail2ban/jail.local"
    _tmp_log_file = _set_up_path + "/tmp_log.json"

    def __init__(self):
        self._check_main_conf()
        self._fix_follow_start()
        self.sys_v = system.system().GetSystemVersion().replace(' ', '').lower()

    def _fix_follow_start(self):
        if not os.path.exists('/lib/systemd/system/fail2ban.service'):
            public.ExecShell(
                "wget -O /lib/systemd/system/fail2ban.service http://download.bt.cn/install/plugin/fail2ban/fail2ban.service -T 5")
            public.ExecShell('systemctl unmask fail2ban && systemctl daemon-reload')
        if not os.path.exists('/usr/bin/fail2ban-server'):
            public.ExecShell("ln -s /usr/local/bin/fail2ban-server /usr/bin/fail2ban-server")
            public.ExecShell("ln -s /usr/local/bin/fail2ban-client /usr/bin/fail2ban-client")
            public.ExecShell('/usr/bin/fail2ban-client stop')
            public.ExecShell('systemctl start fail2ban')

    # 备份配置文件
    def _back_file(self, file, act=None):
        file_type = "_bak"
        if act:
            file_type = "_def"
        os.system("/usr/bin/cp -p {0} {1}".format(file, file + file_type))

    # 还原配置文件
    def _restore_file(self, file, act=None):
        file_type = "_bak"
        if act:
            file_type = "_def"
        os.system("/usr/bin/cp -p {1} {0}".format(file, file + file_type))

    # 读取配置
    def _read_conf(self, path, l=None):
        conf = public.readFile(path)
        if not conf:
            if not l:
                conf = {}
            else:
                conf = []
            public.writeFile(path, json.dumps(conf))
            return conf
        return json.loads(conf)

    # 读fail2ban主配置
    def _read_conf_file(self, path):
        conf = public.readFile(path)
        if conf:
            return conf

    # 写配置
    def _write_jail_conf(self, path, values):
        c = self._read_conf(path)
        dir = ""
        if "dir" in values:
            dir = values["dir"]
        d = {
            "act": values["act"],
            "port": values["port"],
            "maxretry": values["maxretry"],
            "findtime": values["findtime"],
            "bantime": values["bantime"],
            "dir": dir
        }
        if values["mode"].startswith("custom-"):
            d["logpath"] = values["logpath"]
            d["keyword"] = values["keyword"]
            d["keyword_position"] = values.get("keyword_position", "both") 

        c[values["mode"]] = d
        public.writeFile(path, json.dumps(c))

    # 检查主配置是否存在
    def _check_main_conf(self):
        jail_local_file = "/etc/fail2ban/jail.local"
        conf = self._read_conf_file(jail_local_file)
        if not conf:
            content = """
#DEFAULT-START
[DEFAULT]
ignoreip = 127.0.0.1/8
bantime = 600
findtime = 300
maxretry = 5
banaction = firewallcmd-ipset  
action = %(action_)s
#DEFAULT-END
"""
            public.writeFile(jail_local_file, content)

    # 设置ip白名单
    def set_white_ip(self, get):
        '''
        get.while_ip    "192.168.1.1"
        :param get:
        :return:
        '''
        ip_list = self.get_white_ip(get)
        ip = [i.strip() for i in get.white_ip.split("\n") if i.strip()]
        if ip_list is False:
            return public.returnMsg(False, "没找到主配置文件")
        rep_ip = r"^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}($|[\/\d]+$)"
        rep_ipv6 = r"^\s*((([0-9A-Fa-f]{1,4}:){7}(([0-9A-Fa-f]{1,4})|:))|(([0-9A-Fa-f]{1,4}:){6}(:|((25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3})|(:[0-9A-Fa-f]{1,4})))|(([0-9A-Fa-f]{1,4}:){5}((:((25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3})?)|((:[0-9A-Fa-f]{1,4}){1,2})))|(([0-9A-Fa-f]{1,4}:){4}(:[0-9A-Fa-f]{1,4}){0,1}((:((25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3})?)|((:[0-9A-Fa-f]{1,4}){1,2})))|(([0-9A-Fa-f]{1,4}:){3}(:[0-9A-Fa-f]{1,4}){0,2}((:((25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3})?)|((:[0-9A-Fa-f]{1,4}){1,2})))|(([0-9A-Fa-f]{1,4}:){2}(:[0-9A-Fa-f]{1,4}){0,3}((:((25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3})?)|((:[0-9A-Fa-f]{1,4}){1,2})))|(([0-9A-Fa-f]{1,4}:)(:[0-9A-Fa-f]{1,4}){0,4}((:((25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3})?)|((:[0-9A-Fa-f]{1,4}){1,2})))|(:(:[0-9A-Fa-f]{1,4}){0,5}((:((25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3})?)|((:[0-9A-Fa-f]{1,4}){1,2})))|(((25[0-5]|2[0-4]\d|[01]?\d{1,2})(\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})){3})))(%.+)?\s*$"
        for i in ip:
            if not re.search(rep_ip, i) and not re.search(rep_ipv6, i):
                return public.returnMsg(True, "IP格式不正确")
        ip = ",".join(ip)
        jail_local_file = "/etc/fail2ban/jail.local"
        conf = self._read_conf_file(jail_local_file)
        rep = r"\nignoreip\s*=\s*(.*)"
        conf = re.sub(rep, "\nignoreip = {}".format(ip), conf)
        self._back_file(jail_local_file)
        public.writeFile(jail_local_file, conf)
        # 重载
        a, e = public.ExecShell("fail2ban-client reload")
        if "ERROR" not in a:
            return public.returnMsg(True, "添加成功")
        else:
            self._restore_file(jail_local_file)
            return public.returnMsg(True, "添加失败 {}".format(e))

    # 获取白名单列表
    def get_white_ip(self, get):
        conf = self._read_conf_file("/etc/fail2ban/jail.local")
        if not isinstance(conf, str):
            return False
        if not conf:
            return []
        ip_data = re.search(r"\nignoreip\s*=(?P<val>[^\n]*)\n", conf)
        if not ip_data:
            return []
        ip_data = ip_data.group("val").strip()
        ip_list = ip_data.split(",")
        return "\n".join(ip_list)

    # 判断规则是否已经存在
    def _check_mode_exist(self, mode):
        conf = self._read_conf(self._config)
        if mode in conf:
            return True
        return False

    # 获取信息
    def get_anti_info(self, get):
        """
        获取防护信息，按类型分类
        :param get:
        :return: {"site": [], "server": [], "custom": []}
        """
        self._check_main_conf()
        data = self._read_conf(self._config)
        if data:
            d = {"site": [], "server": [], "custom": []}
            for i in data:
                content = data[i]
                content["mode"] = i
                
                if "-scan" in i or "-cc" in i:
                    # 站点防护规则
                    d["site"].append(content)
                elif i.startswith("custom-"):
                    # 自定义防护规则
                    d["custom"].append(content)
                else:
                    # 服务器防护规则
                    d["server"].append(content)
            return d
        return {}
    # 判断配置是否存在
    def _check_conf_exist(self, conf, mode):
        jail_conf = self._read_conf_file(self._jail_local_file)
        self._back_file(self._jail_local_file)
        if '[{}]'.format(mode) in jail_conf:
            rep = "#{mode}-START(\n|.)+#{mode}-END".format(mode=mode)
            jail_conf = re.sub(rep, conf, jail_conf)
            public.writeFile(self._jail_local_file, jail_conf)
        else:
            public.writeFile(self._jail_local_file, conf, "a+")

    # 重载配置
    def _reload_fail2ban(self, values):
        a, e = public.ExecShell("fail2ban-client reload")
        if "ERROR" not in a:
            self._write_jail_conf(self._config, values)
            return public.returnMsg(True, "设置成功")
        else:
            self._restore_file(self._jail_local_file)
            return public.returnMsg(True, "设置失败 {}".format(e))

    def _check_log_exist(self, path):
        if not os.path.exists(path):
            return public.returnMsg(False, "[ {} ] 日志文件不存在，无法创建".format(path))

    # 设置ssh防爆破
    def set_sshd_anti(self, values):
        """
        get.port        端口
        get.maxretry    最大请求次数
        get.findtime    周期
        get.bantime     封锁时间
        get.act         开关
        :param get:
        :return:
        """
        if os.path.isfile('/var/log/secure'):
            logpath = 'logpath = /var/log/secure'
        elif os.path.isfile('/var/log/auth.log'):
            logpath = 'logpath = /var/log/auth.log'
        else:
            logpath = 'backend = systemd'
        conf = """
#sshd-START
[sshd]
enabled = {act}
filter = sshd
port = {port}
maxretry = {maxretry}
findtime = {findtime}
bantime = {bantime}
action = %(action_)s
{logpath}
#sshd-END
""".format(act=values["act"], port=values["port"], maxretry=values["maxretry"], findtime=values["findtime"],
           bantime=values["bantime"], logpath=logpath)
        # 判断配置是否存在
        self._check_conf_exist(conf, values["mode"])

        # 判断服务是否正常运行
        output, err = public.ExecShell("systemctl status fail2ban.service")

        # 临时解决放爆破服务冲突问题
        if "ERROR   Server already running" in output:
            public.print_log("服务重复运行")
            public.ExecShell("fail2ban-client stop")
            public.ExecShell("systemctl start fail2ban")

        # 重载
        return self._reload_fail2ban(values)

    # 设置ftp防爆破
    def set_ftpd_anti(self, values):
        tmp = self._check_log_exist('/var/log/messages')
        if tmp:
            return tmp
        ftp_conf_file = "/www/server/pure-ftpd/etc/pure-ftpd.conf"
        conf = self._read_conf_file(ftp_conf_file)
        if not conf:
            return public.returnMsg(True, "没有找到FTP配置文件，请确认ftp已经安装")
        conf = """
#ftpd-START
[ftpd]
enabled = {act}
filter = pure-ftpd
port = {port}
maxretry = {maxretry}
findtime = {findtime}
bantime = {bantime}
action = %(action_)s
logpath = /var/log/messages
#ftpd-END
""".format(act=values["act"], port=values["port"], maxretry=values["maxretry"], findtime=values["findtime"],
           bantime=values["bantime"])
        self._check_conf_exist(conf, values["mode"])
        return self._reload_fail2ban(values)

    # 设置dovecot防爆破
    def set_dovecot_anti(self, values):
        log_path = '/var/log/maillog'
        if not os.path.exists(log_path):
            log_path = '/var/log/mail.log'
        if not os.path.exists(log_path):
            return public.returnMsg(True, "没有找到邮件日志文件，请确认邮局已经安装，且配置了syslog管理邮局日志")
        dovecot_conf_file = "/etc/dovecot/dovecot.conf"
        conf = self._read_conf_file(dovecot_conf_file)
        if not conf:
            return public.returnMsg(True, "没有找到Dovecot配置文件，请确认邮局已经安装")
        conf = """
#dovecot-START
[dovecot]
enabled = {act}
filter = dovecot
maxretry = {maxretry}
findtime = {findtime}
bantime = {bantime}
action = %(action_)s
logpath = {log_path}
#dovecot-END
""".format(act=values["act"], maxretry=values["maxretry"], findtime=values["findtime"], bantime=values["bantime"], log_path=log_path)
        self._check_conf_exist(conf, "dovecot")
        return self._reload_fail2ban(values)

    # 设置postfix防爆破
    def set_postfix_anti(self, values):
        log_path = '/var/log/maillog'
        if not os.path.exists(log_path):
            log_path = '/var/log/mail.log'
        if not os.path.exists(log_path):
            return public.returnMsg(True, "没有找到邮件日志文件，请确认邮局已经安装，且配置了syslog管理邮局日志")
        postfix_conf_file = "/etc/postfix/main.cf"
        conf = self._read_conf_file(postfix_conf_file)
        if not conf:
            return public.returnMsg(True, "没有找到Postfix配置文件，请确认邮局已经安装")
        conf = """
#postfix-START
[postfix]
enabled = {act}
filter = aaP_postfix_1
maxretry = {maxretry}
findtime = {findtime}
bantime = {bantime}
action = %(action_)s
logpath = {log_path}
#postfix-END
""".format(act=values["act"], maxretry=values["maxretry"], findtime=values["findtime"], bantime=values["bantime"], log_path=log_path)
        self.set_filter(t="postfix")
        self._check_conf_exist(conf, values["mode"])
        return self._reload_fail2ban(values)

    def set_filter(self, values=None, sitename=None, t=None):
        if t == "postfix":
            regex = "failregex = (?i): warning: [-._\\w]+\\[<HOST>\\]: SASL (?:LOGIN|PLAIN|(?:CRAM|DIGEST)-MD5) authentication failed(:.*)$"
            sitename = "postfix"
            values = {}
            values["regex"] = "1"
        else:
            if values["regex"] == "scan":
                regex = r"failregex = ^<HOST> - - \[.*\] \"\S+ .*\" 444 [0-9]+".format(values["dir"])
            elif values["regex"] == "cc":
                regex = r"failregex = ^<HOST> - - \[.*\] \"(GET|POST) .*\" (429|401) [0-9]+"
            else:
                regex = values["regex"]
        conetnt = """
[Definition]
{regex}
ignoreregex =
""".format(regex=regex)
        f = "/etc/fail2ban/filter.d/aaP_{}_{}.conf".format(sitename, values["regex"])
        public.writeFile(f, conetnt)

    def _get_nginx_log_path(self, website):
        try:
            # 优先检查不带 "html_" 前缀的配置文件
            nginx_conffile = '/www/server/panel/vhost/nginx/{}.conf'.format(website)
            nginx_conf = public.readFile(nginx_conffile)
            
            if not nginx_conf:
                # 如果没有找到，再检查带 "html_" 前缀的配置文件
                nginx_conffile = '/www/server/panel/vhost/nginx/{}.conf'.format("html_" + website)
                nginx_conf = public.readFile(nginx_conffile)
                
            if not nginx_conf:
                # 如果没有找到，再检查带 "node_" 前缀的配置文件
                nginx_conffile = '/www/server/panel/vhost/nginx/{}.conf'.format("node_" + website)
                nginx_conf = public.readFile(nginx_conffile)            
                
            if not nginx_conf:
                raise FileNotFoundError("未找到Nginx配置文件")
            
            # 在配置文件中查找 access_log 的路径
            reg = r'access_log\s+(.*\.log)'
            log_path = re.search(reg, nginx_conf)
            nginx_log_path = ""
            if log_path:
                nginx_log_path = log_path.groups(1)[0]
            return nginx_log_path
        except:
            return ""

    def _get_apache_log_path(self, website):
        try:
            apache_conffile = '/www/server/panel/vhost/apache/{}.conf'.format(website)
            apache_conf = public.readFile(apache_conffile)
            reg = r'CustomLog\s+"(.*)"\s+combined'
            log_path = re.search(reg, apache_conf)
            apache_log_path = ""
            if log_path:
                apache_log_path = log_path.groups(1)[0]
            return apache_log_path
        except:
            return ""

    def _get_ols_log_path(self, website):
        try:
            ols_conffile = '/www/server/panel/vhost/openlitespeed/detail/{}.conf'.format(website)
            ols_conf = public.readFile(ols_conffile)
            reg = r'accesslog\s+(.*)\s+{'
            log_path = re.search(reg, ols_conf)
            ols_log_path = ""
            if log_path:
                ols_log_path = log_path.groups(1)[0].replace('$VH_NAME', website)
            return ols_log_path
        except:
            return ""

    def _get_website_log_path(self, website):
        try:
            from logsModel.siteModel import main as  site_log_main
            site_log = site_log_main()
            args = public.dict_obj()
            args.siteName = website
            log_file = site_log.get_site_log_file(args)["log_file"]
            return {
                "nginx": log_file,
                "apache": log_file,
                "openlitespeed": self._get_ols_log_path(website),
            }
        except:
            return {"nginx": self._get_nginx_log_path(website),
                    "apache": self._get_apache_log_path(website),
                    "openlitespeed": self._get_ols_log_path(website)
                    }

    # 设置站点目录防扫描
    def set_scan_anti(self, values):
        """
        get.sitename    站点名
        get.dir         不想被扫描的目录
        :param get:
        :return:
        """
        sitename = values["mode"].split("-")[:-1]
        sitename = "-".join(sitename)
        web_server = public.get_webserver()
        site_log_info = self._get_website_log_path(sitename)
        log_path = site_log_info[web_server]
        tmp = self._check_log_exist(log_path)
        if tmp:
            return tmp
        conf = """
#{sitename}-scan-START
[{sitename}-scan]
enabled = {act}
filter = aaP_{sitename}_scan
port = {port}
maxretry = {maxretry}
findtime = {findtime}
bantime = {bantime}
action = %(action_)s
logpath = {log_path}
#{sitename}-scan-END
""".format(act=values["act"], port=values["port"], maxretry=values["maxretry"], findtime=values["findtime"],
           bantime=values["bantime"], log_path=log_path, sitename=sitename)

        # mode = "{}-scan".format(get.sitename)
        self._check_conf_exist(conf, values["mode"])
        values["regex"] = "scan"
        self.set_filter(values, sitename)
        result = self._reload_fail2ban(values)
        if result["status"] == False:
            f = "/etc/fail2ban/filter.d/aaP_{}_scan.conf".format(sitename)
            if os.path.exists(f):
                os.remove(f)
        return result

    # 设置cc简单防御
    def set_cc_anti(self, values):
        sitename = values["mode"].split("-")[:-1]
        sitename = "-".join(sitename)
        web_server = public.get_webserver()
        site_log_info = self._get_website_log_path(sitename)
        log_path = site_log_info[web_server]
        tmp = self._check_log_exist(log_path)
        if tmp:
            return tmp
        conf = """
#{sitename}-cc-START
[{sitename}-cc]
enabled = {act}
filter = aaP_{sitename}_cc
port = {port}
maxretry = {maxretry}
findtime = {findtime}
bantime = {bantime}
action = %(action_)s
logpath = {log_path}
#{sitename}-cc-END
""".format(act=values["act"], port=values["port"], maxretry=values["maxretry"], findtime=values["findtime"],
           bantime=values["bantime"], log_path=log_path, sitename=sitename)

        self._check_conf_exist(conf, values["mode"])
        values["regex"] = "cc"
        self.set_filter(values, sitename)
        result = self._reload_fail2ban(values)
        if result["status"] == False:
            f = "/etc/fail2ban/filter.d/aaP_{}_cc.conf".format(sitename)
            if os.path.exists(f):
                os.remove(f)
        return result

    # 获取mysql数据目录
    def _get_mysql_storage_dir(self):
        data = {}
        try:
            public.CheckMyCnf()
            myfile = '/etc/my.cnf'
            mycnf = public.readFile(myfile)
            rep = r"datadir\s*=\s*(.+)\n"
            data['datadir'] = re.search(rep, mycnf).groups()[0]
        except:
            data['datadir'] = '/www/server/data'
        return data

    # mysql防爆破
    def set_mysql_anti(self, values):
        import socket
        hostname = socket.gethostname()
        postfix_conf_file = "/etc/my.cnf"
        conf = self._read_conf_file(postfix_conf_file)
        if not conf:
            return public.returnMsg(True, "没有找到Mysql配置文件，请确认邮局已经安装")
        datadir = self._get_mysql_storage_dir()
        tmp = self._check_log_exist("{}/{}.err".format(datadir["datadir"], hostname))
        if tmp:
            return tmp
        conf = """
#mysql-START
[mysql]
enabled = {act}
filter = mysqld-auth
maxretry = {maxretry}
findtime = {findtime}
bantime = {bantime}
action = %(action_)s
logpath = {datadir}/{hostname}.err
#mysql-END
""".format(act=values["act"], maxretry=values["maxretry"], findtime=values["findtime"], bantime=values["bantime"],
           datadir=datadir["datadir"], hostname=hostname)
        self._check_conf_exist(conf, values["mode"])
        return self._reload_fail2ban(values)

    def _detect_timestamp_pattern(self, text):
        """
        检测日志中的时间戳格式并返回相应的 datepattern 和正则匹配模式
        :param text: 日志文本
        :return: (datepattern, placeholder, timestamp_length, start_pos, end_pos)
        """
        # 定义常见的时间戳格式
        timestamp_formats = [
            # 1. 带中括号的 ISO 8601 (针对你提到的 [2025-12-30T03:35:37.932Z])
            {
                'regex': r'\[\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}\.\d{3,6}Z?\]',
                'datepattern': r'{^LN-BEG}\[%%Y-%%m-%%dT%%H:%%M:%%S\.%%f%%Z\]',
                'placeholder': r'\[\S+\]',
                'name': 'ISO8601_bracketed_ms'
            },
            # 2. 标准 ISO 8601 (带微秒和时区: 2025-12-30T03:35:37.932+08:00)
            {
                'regex': r'\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}\.\d{6}[+-]\d{2}:?\d{2}',
                'datepattern': '{^LN-BEG}', # 这种标准格式通常可以交给 fail2ban 自动识别
                'placeholder': r'\S+',
                'name': 'ISO8601_microsec_tz'
            },
            # 3. 标准 ISO 8601 (带毫秒: 2025-12-30 03:35:37.932)
            {
                'regex': r'\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}\.\d{3}',
                'datepattern': '{^LN-BEG}',
                'placeholder': r'\S+\s+\S+',
                'name': 'ISO8601_millisec'
            },
            # 4. 基础 ISO 8601 (无毫秒: 2025-12-30 03:35:37)
            {
                'regex': r'\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}',
                'datepattern': '{^LN-BEG}',
                'placeholder': r'\S+\s+\S+',
                'name': 'ISO8601'
            },
            # 5. Apache/Nginx 格式 (27/Oct/2023:10:00:00 +0800)
            {
                'regex': r'\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}\s+[+-]\d{4}',
                'datepattern': '{^LN-BEG}%%d/%%b/%%Y:%%H:%%M:%%S %%z',
                'placeholder': r'\S+\s+\S+',
                'name': 'apache'
            },
            # 6. Syslog 格式 (Oct 27 10:00:00)
            {
                'regex': r'[A-Za-z]{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}',
                'datepattern': '{^LN-BEG}',
                'placeholder': r'\S+\s+\d+\s+\S+',
                'name': 'syslog'
            },
            # 7. Unix 时间戳 (10位或13位)
            {
                'regex': r'\b1\d{9,12}\b', 
                'datepattern': '{^LN-BEG}EPOCH',
                'placeholder': r'\d+',
                'name': 'unix_timestamp'
            }
        ]

        for fmt in timestamp_formats:
            match = re.search(fmt['regex'], text)
            if match:
                # 如果匹配到的不是从行首开始，且我们指定了 {^LN-BEG}，
                # 需要考虑是否动态调整 datepattern
                start, end = match.start(), match.end()
                return (fmt['datepattern'], fmt['placeholder'], end - start, start, end)

        return (None, None, 0, -1, -1)
    
    def _generate_failregex_from_log(self, log_content, keyword, keyword_position):
        """
        根据日志内容和关键词生成精确的 failregex
        :param log_content: 具体日志行内容
        :param keyword: 关键词（未转义）
        :param keyword_position: 关键词位置 before/after/both
        :return: failregex 字符串（可能包含 datepattern）
        """
        if not log_content:
            # 如果没有提供日志内容，使用通用模式
            keyword_escaped = re.escape(keyword)
            if keyword_position == "before":
                return "failregex = ^.*{keyword}.*<HOST>.*$".format(keyword=keyword_escaped)
            elif keyword_position == "after":
                return "failregex = ^<HOST>.*{keyword}.*$".format(keyword=keyword_escaped)
            else:
                return """failregex = ^.*{keyword}.*<HOST>.*$
                    ^<HOST>.*{keyword}.*$
                    ^.*<HOST>.*{keyword}.*$""".format(keyword=keyword_escaped)
        
        # 检测时间戳格式
        datepattern, timestamp_placeholder, timestamp_len, ts_start, ts_end = self._detect_timestamp_pattern(log_content)
        
        # 从日志中提取 IP 地址
        ip_patterns = [
            r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',  # IPv4
            r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b',  # IPv6
            r'\b(?:[0-9a-fA-F]{1,4}:){1,7}:\b',  # IPv6 简写
        ]
        
        found_ip = None
        ip_start = -1
        ip_end = -1
        
        for pattern in ip_patterns:
            match = re.search(pattern, log_content)
            if match:
                found_ip = match.group()
                ip_start = match.start()
                ip_end = match.end()
                break
        
        if not found_ip:
            # 如果日志中没有找到IP，返回通用规则
            keyword_escaped = re.escape(keyword)
            result = ""
            if datepattern:
                result = "datepattern = {}\n".format(datepattern)
            if keyword_position == "before":
                result += "failregex = ^.*{keyword}.*<HOST>.*$".format(keyword=keyword_escaped)
            elif keyword_position == "after":
                result += "failregex = ^<HOST>.*{keyword}.*$".format(keyword=keyword_escaped)
            else:
                result += """failregex = ^.*{keyword}.*<HOST>.*$
                    ^<HOST>.*{keyword}.*$""".format(keyword=keyword_escaped)
            return result
        
        # 查找关键词位置
        keyword_index = log_content.find(keyword)
        if keyword_index == -1:
            # 关键词不在日志中，使用通用规则
            keyword_escaped = re.escape(keyword)
            result = ""
            if datepattern:
                result = "datepattern = {}\n".format(datepattern)
            if keyword_position == "before":
                result += "failregex = ^.*{keyword}.*<HOST>.*$".format(keyword=keyword_escaped)
            elif keyword_position == "after":
                result += "failregex = ^<HOST>.*{keyword}.*$".format(keyword=keyword_escaped)
            else:
                result += """failregex = ^.*{keyword}.*<HOST>.*$
                    ^<HOST>.*{keyword}.*$""".format(keyword=keyword_escaped)
            return result
        
        # 检测是否是 Nginx/Apache 标准日志格式
        def is_nginx_or_apache_log(log_line):
            """检测是否是 Nginx 或 Apache 标准访问日志"""
            # Nginx/Apache 典型特征：IP + - + - + [时间] + "请求" + 状态码
            pattern = r'^\S+\s+-\s+-\s+\[.+?\]\s+"[^"]*"\s+\d+\s+'
            return re.match(pattern, log_line) is not None
        
        # 如果是 Nginx/Apache 日志，使用简化的模板
        if is_nginx_or_apache_log(log_content):
            keyword_escaped = re.escape(keyword)
            result = ""
            if datepattern:
                result = "datepattern = {}\n".format(datepattern)
            
            # 根据关键词位置生成简化的规则
            if keyword_position == "before":
                # 关键词在IP前 - 通常不适用于标准 Nginx 日志，使用通用模式
                result += "failregex = ^.*{keyword}.*<HOST>.*$".format(keyword=keyword_escaped)
            elif keyword_position == "after":
                # IP在前，关键词在后 - Nginx 标准格式
                result += "failregex = ^<HOST>\\s+.*{keyword}.*$".format(keyword=keyword_escaped)
            else:
                # 两种都支持
                result += "failregex = ^<HOST>\\s+.*{keyword}.*$\n                    ^.*{keyword}.*<HOST>.*$".format(keyword=keyword_escaped)
            
            return result
        
        # 分析日志格式，生成正则表达式模式
        # 将日志分为三部分：IP前、IP、IP后
        before_ip = log_content[:ip_start]
        after_ip = log_content[ip_end:]
        
        # 转义特殊字符的辅助函数（改进版）
        def escape_and_generalize(text, aggressive=True):
            """
            转义文本并智能泛化某些模式
            :param text: 要处理的文本
            :param aggressive: 是否使用激进的泛化策略
            """
            if not text:
                return text
            
            # 如果开启激进模式，进行更多泛化
            if aggressive:
                # 替换双引号内的内容为通配符（保留引号结构）
                text = re.sub(r'"[^"]{20,}"', '".*?"', text)
                
                # 替换长字符串（超过15个字符的连续非空白字符）为通配符
                text = re.sub(r'\S{15,}', r'\\S+', text)
                
                # 替换版本号模式 (如 1.2.3.4)
                text = re.sub(r'\d+\.\d+(\.\d+)*', r'\\S+', text)
            
            result = []
            i = 0
            while i < len(text):
                # 检查是否是独立的数字
                num_match = re.match(r'\d+', text[i:])
                if num_match and (i == 0 or not text[i-1].isalnum()) and \
                   (i + num_match.end() >= len(text) or not text[i + num_match.end()].isalnum()):
                    result.append(r'\d+')
                    i += num_match.end()
                    continue
                
                # 检查是否是空白字符序列
                space_match = re.match(r'\s+', text[i:])
                if space_match:
                    result.append(r'\s+')
                    i += space_match.end()
                    continue
                
                # 转义正则特殊字符
                char = text[i]
                if char in '.()[]{}+?|$^*\\':
                    result.append('\\' + char)
                else:
                    result.append(char)
                i += 1
            
            return ''.join(result)
        
        keyword_escaped = re.escape(keyword)
        
        # 根据关键词和IP的相对位置生成规则
        failregex = ""
        
        # 如果有 datepattern，failregex 应该从时间戳之后开始
        # 因为 fail2ban 会自动处理 datepattern 匹配的部分
        failregex_start_pos = 0
        if datepattern and ts_start == 0:
            # 时间戳在行首，failregex 从时间戳之后开始
            failregex_start_pos = ts_end
        
        if keyword_position == "before":
            # 关键词在IP前面
            if keyword_index < ip_start:
                # 确实是 keyword ... IP 的顺序
                # 提取关键词到IP之间的模式
                between_pattern = log_content[keyword_index + len(keyword):ip_start]
                between_escaped = escape_and_generalize(between_pattern, aggressive=True)
                
                # 生成前缀模式（关键词之前的部分）
                prefix = log_content[failregex_start_pos:keyword_index]
                if datepattern and failregex_start_pos > 0:
                    # 使用 datepattern 时，不需要在 failregex 中包含时间戳
                    prefix_pattern = escape_and_generalize(prefix, aggressive=True) if prefix else ""
                    if prefix_pattern and not prefix_pattern.startswith('^'):
                        prefix_pattern = "^" + prefix_pattern
                    elif not prefix_pattern:
                        prefix_pattern = "^"
                else:
                    prefix_pattern = "^.*" if prefix else "^"
                
                # 生成后缀模式 - 对后缀使用通配符，避免过于具体
                if after_ip.strip():
                    # 后缀部分使用更宽松的匹配
                    suffix_pattern = ".*$"
                else:
                    suffix_pattern = ".*$"
                
                failregex = "failregex = {prefix}{keyword}{between}<HOST>{suffix}".format(
                    prefix=prefix_pattern,
                    keyword=keyword_escaped,
                    between=between_escaped,
                    suffix=suffix_pattern
                )
            else:
                # 实际顺序不匹配，使用通用规则
                failregex = "failregex = ^.*{keyword}.*<HOST>.*$".format(keyword=keyword_escaped)
                
        elif keyword_position == "after":
            # 关键词在IP后面
            if keyword_index > ip_end:
                # 确实是 IP ... keyword 的顺序
                # 提取IP到关键词之间的模式（使用温和的泛化，保留关键结构）
                between_pattern = log_content[ip_end:keyword_index]
                # 对于中间部分，使用较少的泛化以保留结构
                between_escaped = escape_and_generalize(between_pattern, aggressive=False)
                
                # 生成前缀模式
                prefix = log_content[failregex_start_pos:ip_start]
                if datepattern and failregex_start_pos > 0:
                    # 使用 datepattern 时，不需要在 failregex 中包含时间戳
                    prefix_pattern = escape_and_generalize(prefix, aggressive=False) if prefix else ""
                    if prefix_pattern and not prefix_pattern.startswith('^'):
                        prefix_pattern = "^" + prefix_pattern
                    elif not prefix_pattern:
                        prefix_pattern = "^"
                else:
                    prefix_pattern = escape_and_generalize(prefix, aggressive=False) if prefix else "^"
                    if prefix and not prefix_pattern.startswith('^'):
                        prefix_pattern = "^" + prefix_pattern
                
                # 生成后缀模式 - 使用通配符避免过于具体
                suffix = log_content[keyword_index + len(keyword):]
                if suffix.strip():
                    suffix_pattern = ".*$"
                else:
                    suffix_pattern = ".*$"
                
                failregex = "failregex = {prefix}<HOST>{between}{keyword}{suffix}".format(
                    prefix=prefix_pattern,
                    between=between_escaped,
                    keyword=keyword_escaped,
                    suffix=suffix_pattern
                )
            else:
                # 实际顺序不匹配，使用通用规则
                failregex = "failregex = ^<HOST>.*{keyword}.*$".format(keyword=keyword_escaped)
                
        else:  # both 或其他
            # 同时支持两种模式
            if keyword_index < ip_start:
                pattern1 = "^.*{keyword}.*<HOST>.*$".format(keyword=keyword_escaped)
            else:
                pattern1 = "^<HOST>.*{keyword}.*$".format(keyword=keyword_escaped)
            failregex = "failregex = {pattern1}\n                    ^.*<HOST>.*{keyword}.*$".format(
                pattern1=pattern1,
                keyword=keyword_escaped
            )
        
        # 组合 datepattern 和 failregex
        result = ""
        if datepattern:
            result = "datepattern = {}\n".format(datepattern)
        result += failregex
        
        return result

    # 自定义防护配置
    def set_custom_anti(self, values):
        """
        自定义防护规则（智能关键词模式）
        values.mode         规则名称（必须以 custom- 开头）
        values.logpath      日志路径
        values.port         端口
        values.maxretry     最大重试次数（出现频率）
        values.findtime     检测周期（秒）
        values.bantime      封锁时间（秒）
        values.keyword      关键词（自动匹配日志中包含关键词的行并提取IP）
        values.act          开关 true/false
        values.keyword_position 关键词位置 before/after/both
        values.log_id       可选：日志ID（用于获取具体日志内容）
        """
        # 验证必需参数

        if "logpath" not in values:
            return public.returnMsg(False, "缺少参数: logpath（日志路径）")
        if "keyword" not in values:
            return public.returnMsg(False, "缺少参数: keyword（关键词）")


        keyword_position = values.get("keyword_position", "both")
        keyword = values["keyword"]  # 原始关键词，不转义

        # 获取具体日志内容（如果提供了 log_id）
        log_content = ""
        log_id = values.get("log_id")
        if log_id:
            try:
                log_list_content = public.readFile(self._tmp_log_file)
                if log_list_content:
                    log_list = json.loads(log_list_content)
                    if isinstance(log_list, list) and len(log_list) >= log_id:
                        log_content = log_list[log_id-1]["log_content"]
            except Exception as e:
                public.print_log("获取日志内容失败: {}".format(str(e)))
        
        # 使用智能方法生成 failregex
        failregex_patterns = self._generate_failregex_from_log(log_content, keyword, keyword_position)

        # 检查日志文件是否存在（如果不是通配符）
        if '*' not in values["logpath"]:
            tmp = self._check_log_exist(values["logpath"])
            if tmp:
                return tmp
        
        # 使用 mode 作为 filter 名称
        filter_name = values["mode"]
        
        # 生成 jail 配置
        conf = """
#{mode}-START
[{mode}]
enabled = {act}
filter = custom_{filter_name}
port = {port}
maxretry = {maxretry}
findtime = {findtime}
bantime = {bantime}
action = %(action_)s
logpath = {logpath}
#{mode}-END
""".format(
            mode=values["mode"],
            act=values["act"],
            filter_name=filter_name,
            port=values["port"],
            maxretry=values["maxretry"],
            findtime=values["findtime"],
            bantime=values["bantime"],
            logpath=values["logpath"]
        )
        
        # 写入 jail 配置
        self._check_conf_exist(conf, values["mode"])
        
        # 创建自定义 filter（使用智能生成的 failregex）
        filter_content = """
[Definition]
# 智能关键词匹配模式（自动提取IP地址）
{failregex}
ignoreregex =
""".format(failregex=failregex_patterns)
        
        filter_file = "/etc/fail2ban/filter.d/custom_{}.conf".format(filter_name)
        public.writeFile(filter_file, filter_content)
        
        # 重载 fail2ban
        result = self._reload_fail2ban(values)
        
        # 如果失败，清理 filter 文件
        if result["status"] == False:
            if os.path.exists(filter_file):
                os.remove(filter_file)
        
        return result

    def set_anti(self, get):
        values = self._check_get_args(get)
        if "status" in values.keys():
            return values
        if values["type"] == "add":
            if self._check_mode_exist(values["mode"]):
                return public.returnMsg(False, "已经存在 {}".format(values["mode"]))
        default_filter = ["mysql", "postfix", "dovecot", "sshd", "ftpd"]
        if values["mode"] == "sshd_service":
            values["mode"] = "sshd"
        if values["mode"] == "ftpd_service":
            values["mode"] = "ftpd"
        # 添加自定义模式支持
        if values["mode"].startswith("custom-"):
            return self.set_custom_anti(values)
        if values["mode"] in default_filter:
            a = "self.set_" + values["mode"] + "_anti(values)"
            return eval(a)
        if "-cc" in values["mode"]:
            return self.set_cc_anti(values)
        if "-scan" in values["mode"]:
            return self.set_scan_anti(values)
        return public.returnMsg(False, "参数有误，请重新输入")

    # 删除防爆破
    def del_anti(self, get):
        values = self._check_get_args(get)
        if "status" in values.keys():
            return values
        conf = self._read_conf(self._config)
        if values["mode"] in conf:
            del (conf[values["mode"]])
            public.writeFile(self._config, json.dumps(conf))
        jail_conf = self._read_conf_file(self._jail_local_file)
        rep = "\n#{mode}-START(\n|.)+#{mode}-END".format(mode=values["mode"])
        jail_conf = re.sub(rep, "", jail_conf)
        public.writeFile(self._jail_local_file, jail_conf)
        
        # 如果是自定义规则，删除对应的 filter 文件
        if values["mode"].startswith("custom-"):
            filter_file = "/etc/fail2ban/filter.d/custom_{}.conf".format(values["mode"])
            if os.path.exists(filter_file):
                os.remove(filter_file)
        public.ExecShell("fail2ban-client reload")
        return public.returnMsg(True, "删除成功")

    # 更新fail2ban源码
    def update_fail2ban(self):
        # 备份旧fail2ban
        shell_str = """
fail2ban-client stop
mv /etc/fail2ban /etc/fail2ban_bak
git clone https://github.com/fail2ban/fail2ban.git
cd fail2ban
sudo python setup.py install
cp /etc/fail2ban_bak/jail.local /etc/fail2ban/jail.local
cp /etc/fail2ban_bak/filter.d/aaP_* /etc/fail2ban/filter.d/
"""
        os.system(shell_str)
        a, e = public.ExecShell("fail2ban-client start")
        if "ERROR" in a:
            return public.returnMsg(False, "升级失败 {}".format(a))
        return public.returnMsg(True, "升级成功")

    # 获取状态
    def get_status(self, get):
        values = self._check_get_args(get)
        if "status" in values.keys():
            return values
        conf = self.get_anti_info(get)
        for c in conf:
            for i in conf[c]:
                if values["mode"] == i["mode"]:
                    if i["act"] == "false":
                        return public.returnMsg(False, "防护已经关闭")

        a, e = public.ExecShell("/usr/bin/fail2ban-client status {}".format(values["mode"]))
        if "ERROR" not in a:
            data = {}
            currently_failed = re.search(r"Currently\s*failed:\s*(\d+)", a)
            total_failed = re.search(r"Total\s*failed:\s*(\d+)", a)
            file_list = re.search(r"File\s*list:\s*([\w/.]+)", a)
            if not file_list:
                file_list = "/tmp"
            currently_banned = re.search(r"Currently\s*banned:\s*(\d+)", a)
            total_banned = re.search(r"Total\s*banned:\s*(\d+)", a)
            banned_ip_list = re.search(r"Banned\s*IP\s*list:\s*([\w\s.:/]+)", a)

            if not (
                    currently_failed and total_failed and file_list and currently_banned and total_banned and banned_ip_list):
                return public.returnMsg(False, "此监控可能存在问题，请删除后重新创建")
            data["currently_failed"] = currently_failed.group(1)
            data["total_failed"] = total_failed.group(1)
            try:
                data["file_list"] = file_list.group(1)
            except:
                data["file_list"] = ""
            data["currently_banned"] = currently_banned.group(1)
            data["total_banned"] = total_banned.group(1)
            data["banned_ip_list"] = banned_ip_list.group(1).strip("\n").split()
            return public.returnMsg(True, data)
        else:
            return public.returnMsg(False, "获取失败，{}".format(a))

    # 解禁ip
    def ban_ip_release(self, get):
        """
        get.ip
        get.mode
        :param get:
        :return:
        """
        values = self._check_get_args(get)
        if "status" in values.keys():
            return values
        shell_str = "fail2ban-client set {mode} unbanip {ip}".format(mode=values["mode"], ip=values["ip"])
        os.system(shell_str)
        return public.returnMsg(True, "解锁成功")

    # 获取状态
    def get_fail2ban_status(self, get):
        sock = "/www/server/panel/plugin/fail2ban/fail2ban.sock"
        if os.path.exists(sock):
            return True
        return False

    # 设置fail2ban服务状态
    def set_fail2ban_status(self, get):
        if get.type == "reload":
            if not self.get_fail2ban_status(get):
                return public.returnMsg(False, "服务未开启，请先开启服务")
            a, e = public.ExecShell("fail2ban-client reload")
            if "ERROR" not in a:
                return public.returnMsg(True, "重载成功")
            else:
                self._restore_file(self._jail_local_file)
                return public.returnMsg(True, "重载失败 {}".format(e))
        if get.type == "start":
            if not self.get_fail2ban_status(get):
                a, e = public.ExecShell("fail2ban-client start")
                if "ERROR" in a:
                    return public.returnMsg(True, "启动失败")
                return public.returnMsg(True, "启动成功")
            return public.returnMsg(False, "服务已经开启")

        if get.type == "stop":
            if self.get_fail2ban_status(get):
                public.ExecShell("fail2ban-client stop")
                return public.returnMsg(True, "停止成功")
            return public.returnMsg(False, "服务已经停止")

        if get.type == "restart":
            public.ExecShell("fail2ban-client restart")
            return public.returnMsg(True, "重启成功")

    # 获取允许设置的模式列表
    def get_mode_list(self, get):
        mode_l = {
            "server": ["sshd", "mysql", "dovecot", "postfix", "ftpd"],
            "site": ["site-cc", "site-scan"],
            "custom": ["custom"]
        }
        return mode_l

    # 获取所有站点
    def get_all_sitename(self, get):
        site = {}
        site_list = public.M("sites").field("id,name").select()
        for i in site_list:
            domain_list = public.M("domain").where("pid=?", (i["id"],)).field("name").select()
            l = []
            for domain in domain_list:
                l.append(domain["name"])
            site[i["name"]] = l
        return site

    # def get_black_list(self,get):
    #     conf = self._read_conf(self._black_list,l=1)
    #     return conf
    # 获取黑名单列表
    def get_black_list(self, get):
        conf = self._read_conf(self._black_list, l=1)
        if not conf:
            return ''
        if not conf:
            return []
        return "\n".join(conf)

    # 设置黑名单
    def ban_ip(self, get):
        ip_list = self._read_conf(self._black_list, l=1)
        new_ip_list = list(set([i.strip() for i in get.black_ip.split('\n') if i.strip()]))
        add_ip_list = [new_ip for new_ip in new_ip_list if new_ip not in ip_list]
        del_ip_list = list(set([del_ip for del_ip in ip_list if del_ip not in new_ip_list]))
        data = self._read_conf(self._config)
        # 传入的IP为空时删除所有黑名单
        if not get.black_ip.strip():
            for d in data:
                for ip in ip_list:
                    public.ExecShell('fail2ban-client -vvv set {jail} unbanip {ip}'.format(jail=d, ip=ip))
            public.writeFile(self._black_list, json.dumps([]))
            return public.returnMsg(True, "删除IP黑名单成功")
        # 检查IP格式
        for ip in add_ip_list:
            if not self._is_ip_format(ip):
                return public.returnMsg(False, "IP格式错误 {}".format(ip))
        # 添加新域名到黑名单
        for d in data:
            for ip in add_ip_list:
                public.ExecShell('fail2ban-client -vvv set {jail} banip {ip}'.format(jail=d, ip=ip))
        # 检查是否有清理掉的IP
        for d in data:
            for ip in del_ip_list:
                public.ExecShell('fail2ban-client -vvv set {jail} unbanip {ip}'.format(jail=d, ip=ip))

        public.writeFile(self._black_list, json.dumps(new_ip_list))
        return public.returnMsg(True, "添加黑名单成功")

    # 删除黑名单
    def unban_ip(self, get):
        values = self._check_get_args(get)
        if "status" in values.keys():
            return values
        data = self._read_conf(self._config, l=1)
        for d in data:
            public.ExecShell('fail2ban-client set {jail} unbanip {ip}'.format(jail=d, ip=values["ip"]))
        conf = self._read_conf(self._black_list)
        conf.remove(values["ip"])
        public.writeFile(self._black_list, json.dumps(conf))
        return public.returnMsg(True, "删除黑名单成功")

    # 检查ssh端口
    def _check_ssh_port(self):
        rep = r"\nPort\s+(\d+)"
        c_file = "/etc/ssh/sshd_config"
        c = public.readFile(c_file)
        if not c:
            return False
        result = re.search(rep, c)
        if not c:
            return "22"
        return result.group(1)

    # 检查ftp端口
    def check_ftp_port(self):
        pass

    # 验证前端输入
    def _check_get_args(self, get):
        values = {}
        if hasattr(get, "type"):
            if get.type in ["edit", "add"]:
                values["type"] = get.type
            else:
                return public.ReturnMsg(False, "type 传入的类型错误")
        if hasattr(get, "act"):
            if get.act in ["true", "false"]:
                values["act"] = str(get.act)
            else:
                return public.ReturnMsg(False, "act 传入的类型错误")
        if hasattr(get, "findtime"):
            try:
                values["findtime"] = int(get.findtime)
            except:
                return public.ReturnMsg(False, "findtime 请传入正整数")
        if hasattr(get, "maxretry"):
            try:
                values["maxretry"] = int(get.maxretry)
            except:
                return public.ReturnMsg(False, "maxretry 请传入正整数")
        if hasattr(get, "bantime"):
            value = str(get.bantime).strip().lower()
            # 允许纯数字或带单位 s/m/h/d
            if not re.match(r'^\d+(s|m|h|d)?$', value):
                return public.returnMsg(False, "bantime 格式错误，请输入正整数或带单位 s/m/h/d")
            values["bantime"] = value
        if hasattr(get, "port"):
            try:
                port_l = get.port.split(",")
                for i in port_l:
                    if int(i) <= 0 or 65535 < int(i):
                        return public.ReturnMsg(False, "port:{} 请传入0-65535范围内的数字".format(i))
                values["port"] = get.port
            except:
                return public.ReturnMsg(False, "port:{} 请传入0-65535范围内的数字 error".format(port_l))
        if hasattr(get, "mode"):
            rep = r"[^\w\.\_\-]+"
            if re.search(rep, get.mode):
                return public.returnMsg(False, "mode 参数有特殊字符，请重新输入")
            values["mode"] = str(get.mode)
            if "null" in get.mode:
                return public.ReturnMsg(False, "请先创建网站后再创建站点保护！")
        if hasattr(get, "dir"):
            rep = r"[^\w\.\_\-\/]+"
            if re.search(rep, get.dir):
                return public.returnMsg(False, "dir 参数有特殊字符，请重新输入")
            values["dir"] = str(get.dir)
        if hasattr(get, "ip"):
            if not self._is_ip_format(get.ip.strip()):
                return public.returnMsg(False, "ip , wrong format")
            values["ip"] = str(get.ip.strip())
        #自定义设置    
        if hasattr(get, "logpath"):
            # 验证日志路径
            logpath = str(get.logpath).strip()
            if not logpath:
                return public.returnMsg(False, "logpath 日志路径不能为空")
            # 检查特殊字符（允许路径字符）
            rep = r"[^\w\.\_\-\/\*]+"
            if re.search(rep, logpath):
                return public.returnMsg(False, "logpath 参数有特殊字符，请重新输入")
            values["logpath"] = logpath
        if hasattr(get, "keyword"):
            # 验证关键词（智能模式）
            keyword = str(get.keyword).strip()
            if not keyword:
                return public.returnMsg(False, "keyword 关键词不能为空")
            values["keyword"] = keyword
        if hasattr(get, "keyword_position"):
            keyword_position = str(get.keyword_position).strip()
            if not keyword_position:
                return public.returnMsg(False, "keyword_position 关键词位置不能为空")
            values["keyword_position"] = keyword_position
        if hasattr(get, "log_id"):
            log_id = int(get.log_id)
            if log_id <= 0:
                return public.returnMsg(False, "log_id 请传入正整数")
            values["log_id"] = log_id
        return values

    @staticmethod
    def _is_ip_format(ip_val: str):
        if not ip_val or not isinstance(ip_val, str):
            return False
        try:
            ipaddress.ip_address(ip_val)
            return True
        except:
            pass
        try:
            ipaddress.ip_network(ip_val)
            return True
        except:
            return False

    def get_last_log(self, get=None):
        if get:
            log_path = get.log_path
        else:
            return public.returnMsg(False, "logpath 日志路径不能为空")

        search = getattr(get, 'search', None)
        if search:
            log_data=public.ExecShell("tail -n 1000 {} |grep '{}'".format(log_path, search))[0].split("\n")
        else:   
            log_data=public.ExecShell("tail -n 1000 {}".format(log_path))[0].split("\n")
        log_list = []
        
        for log_id, log_line in enumerate(log_data, start=1):
            if log_line.strip():
                log_list.append({
                    "log_id": log_id,
                    "log_content": log_line
                })
        public.writeFile(self._tmp_log_file, json.dumps(log_list))
        return log_list


