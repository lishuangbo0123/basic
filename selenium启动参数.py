#!/usr/bin/env bash
# (命令解释器位置)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   selenium启动参数
  Description :
  Author :    lee
  date：     2023/3/31
-------------------------------------------------
"""
__author__ = 'lee'

@staticmethod
    def get_chrome_start_args(local, headless, css, img, proxy, user_data_dir=config.CHROME_DATA_PATH_LOCAL):
        options = webdriver.ChromeOptions()
        chrome_conf = [
            '--ignore-certificate-error',   # 忽略证书认证出错
            '--ignore-ssl-errors',  # 忽略ssl出错                      ==========爬虫时候忽略这种证书报错不会出现爬不到数据的情况吗
            '--no-sandbox',  # 禁止沙箱运行，解决linux无头无法运行
            # 'lang=en_us.UTF-8',
            '--disable-dev-shm-usage',  # 解决linux无头无法运行
            # '--disable-software-rasterizer',   # 禁用浏览器GL锁         =====GL锁是啥
            # '--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"',
            '--disable-popup-blocking',  # 禁用弹出拦截
            '--disable-infobars',   # 禁止出现浏览器被控制
            '--ignore-certificate-errors',  # 忽略私密链接                =====就是不会抓取私密链接的数据了是吗？
        ]
        '''# 不开启无头，就开启无痕，（linux自动开启无头模式，无痕模式只有windows环境下启用）'''      ====无头的作用是什么？linux上只能用无头 无头无痕缓存分别什么时候使用
        if proxy:
            res = requests.get("http://thomas.suncentgroup.com/api/thomas_proxy/").json()
            chrome_conf.append(f'--proxy-server={res.get("host")}:{res.get("port")}')
        if headless or 'linux' == sys.platform:chrome_conf.append('--headless')    # 无头                 ====是不是linux必须得在无头模式才能运行
        elif not local and 'win32' == sys.platform: chrome_conf.append('--incognito')  # 无痕模式
        '''# 只有windows环境下才能开启本地缓存'''
        if local and 'win32' == sys.platform: chrome_conf.append(f'user-data-dir={user_data_dir}')      ====mac环境什么时候开缓存什么时候开无痕呢？跟linux一样？为什么要开启本地缓存，也用无痕不行吗？
        '''windows环境下自动禁用GPU'''     =======GPU是图形处理器，那这个是不是关闭图片加载
        for i in chrome_conf:options.add_argument(i)
        prefs = {
            'profile.managed_default_content_settings.images': 2,   # 禁止加载图片
            'permissions.default.stylesheet': 2,    # 禁止加载css
            'useAutomationExtension': False,    # 屏蔽自动化
            'directory_upgrade': True,
            'profile.default_content_setting_values': {'notifications': 2},
            'profile.default_content_settings.popups': 0,  # 防止下载保存弹窗
            'download.default_directory': config.DOWNLOAD_PATH,  # 设置默认下载路径
            "profile.default_content_setting_values.automatic_downloads": 1,    # 禁止下载文件弹窗
            'safebrowsing.enabled': False,  # 安全模式
        }
        if css:del prefs['permissions.default.stylesheet']
        if img:del prefs['profile.managed_default_content_settings.images']
        options.add_experimental_option("useAutomationExtension", False)  # 防止检测无头屏蔽自动化控制
        options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 防止检测无头屏蔽自动化控制
        options.add_experimental_option('prefs', prefs)  # 禁用浏览器弹窗
        return options

    @staticmethod
    def get_firefox_start_args(headless=False):
        save_to_disk = ','.join({
            'application/pdf',
            'application/x-executable',
            'text/csv',
            'application/javascript',
            'application/json',
            'binary/octet-stream',
            'application/octet-stream',
            'application/exe',
            'application/x-msexcel',
            'application/x-excel',
            'application/excel',
            'application/vnd.ms-excel',
            'image/png',
            'image/jpeg',
            'text/html',
            'text/plain',
            'application/msword',
            'application/xml',
            'text/x-c',
            'text/xml',
            'application/x-msdownload',
            'application/xhtml+xml',
            'image/avif',
            'image/webp',
            'image/apng',
            'image/gif',
            'application/atom+xml',
            'multipart/form-data',
        })
        # from common import check_exist,execute_cmd
        # if not check_exist('mitmdump'):
        #     execute_cmd('mitmdump -s C:\\crawler\\my_mitmdump.py -p 12525')
        # profile = webdriver.FirefoxProfile(config.FIREFOX_DATA_PATH)  # 创建一个FirefoxProfile实例
        profile = webdriver.FirefoxProfile()  # 创建一个FirefoxProfile实例
        profile.set_preference('intl.accept_languages', 'zh_CN')  # 设置浏览器语言 en-US
        # profile.set_preference('network.proxy.type', 0)  # selenium firefox设置代理(默认是0，就是直接连接；1就是手工配置代理)
        profile.set_preference('browser.download.dir', config.DOWNLOAD_PATH)  # 指定下载路径
        profile.set_preference('browser.download.folderList', 2)  # 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
        profile.set_preference('browser.download.manager.showWhenStarting', False)  # 在开始下载时是否显示下载管理器
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)  # 总是询问
        profile.set_preference("browser.download.manager.alertOnEXEOpen", False)  # 下载exe询问
        profile.set_preference("browser.download.manager.focusWhenStarting", False)  # 下载时获取焦点
        profile.set_preference("browser.download.manager.useWindow", False)  # 是否显示下载框
        profile.set_preference("browser.download.manager.showAlertOnComplete", False)  # 是否提示下载完成
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", save_to_disk)  # 设置正确的文件的Content_Type
        options = webdriver.FirefoxOptions()  # 驱动选项
        options.headless = headless
        # options.add_argument('--disable-gpu')  # 规避bug
        # options.add_argument('--no-sandbox')  # 禁止沙箱运行
        # options.add_argument('-ProfileManager') # 该命令将在启动Firefox或Thunderbird之前打开配置文件管理器：
        # options.add_argument('-venkman')  # 首先安装JavaScript调试器Venkman（如果已安装）
        options.add_argument('--safebrowsing-disable-extension-blacklist')
        options.add_argument('--safebrowsing-disable-download-protection')
        # options.add_argument('-edit https://sellercentral.amazon.com/home') # 启动给定<url>的编辑器
        # options.add_argument('-url https://sellercentral.amazon.com/home') # 在新选项卡或窗口中打开URL，具体取决于浏览器选项。-url可以省略。您可以列出多个URL，以空格分隔。
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument(
        #     '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0')
        options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        # options.add_argument('--console')  # console
        # options.add_argument('https://sellercentral.amazon.com/home')  # -new-tab URL 在新标签页中打开URL。仅限Firefox和SeaMonkey2.x
        # options.add_argument('-profile')  # -new-tab URL 在新标签页中打开URL。仅限Firefox和SeaMonkey2.x
        # options.add_argument('--kiosk https://sellercentral.amazon.com/home')  # --kiosk URL 全屏打开URL，没有用户界面。Firefox 71及更高版本。
        # options.add_argument("--disable-javascript")  # 禁用JavaScript
        return profile, options
@staticmethod
    def get_driver(local=False, headless=False, css=True, img=True, proxy=False):
        options = Common.get_chrome_start_args(local, headless, css, img, proxy)
        driver = webdriver.Chrome(executable_path=config.CHROME_EXECUTABLE_PATH, options=options)
        driver.execute_cdp_cmd("Network.enable", {})
        script_ls = [
            '''Object.defineProperty(navigator, 'webdriver', {get: () => undefined})''',
            '''window.navigator.chrome = {runtime: {},// etc.};''',
            # '''Object.defineProperty(navigator, 'plugins', {get: () => [5,4514,sfsded],});''',
            # '''Object.defineProperty(navigator, 'languages', {get: () => ['en', 'zh', 'und'],});''',
        ]
        for script in script_ls:
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
        driver.maximize_window()
        driver.implicitly_wait(1)
        driver.set_page_load_timeout(40)  # 全局请求页面超时时间
        driver.set_script_timeout(40)  # 全局请求页面js加载超时时间
        print('浏览器加载完毕')
        time.sleep(random.uniform(1, 2))
        return driver


账号与ip是一对一的，如果一个账号登录多个ip就会被封
