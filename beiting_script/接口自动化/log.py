#-*- coding: UTF-8 -*-
import logging
import time
import os
from logging import handlers

# 获取本地时间，转换为设置的格式
rq = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
# log保存地址
folder_name = '\log\\'+ rq
root_directory = r'C:\Users\Administrator\Desktop\beiting_script'
site = root_directory + folder_name

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

def get_log(logger_name,level_relations=Logger.level_relations,level='info'):
        # 创建文件夹
        try:
            os.mkdir(root_directory + folder_name)
        except OSError:
            pass

        #创建一个logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        
        logger.setLevel(level_relations.get(level))#设置日志级别

        #设置日志文件名
        all_log_name = site + '\\all_log.html'
        error_log_name = site + '\error_log.html'
        
        #创建handler
        #创建一个handler写入所有日志
        fh = logging.FileHandler(all_log_name)
        fh.setLevel(logging.INFO)
        #创建一个handler写入错误日志
        eh = logging.FileHandler(error_log_name)
        eh.setLevel(logging.ERROR)
        #创建一个handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        #定义日志输出格式
        #以时间-日志器名称-日志级别-日志内容的形式展示
        all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s <br>')
        #以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        error_log_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s <br>')
               
        #将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)

        #设置日志格式，以时间-日志器名称[函数行号]-日志级别：日志内容
        format_str = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s <br>')
        
        #往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th = handlers.TimedRotatingFileHandler(filename=logger_name,when='D',backupCount=3,encoding='utf-8')
        
        #设置文件里写入的格式
        th.setFormatter(format_str)
        
        #给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(eh)
        logger.addHandler(ch)
        logger.addHandler(th)

        return logger
    
#直接在日志类创建了一个实例，括号里面的“操作日志”也可以自定义填项目名称表示哪个项目
#在调用日志类的时候，直接import这个myLog，不用在使用的时候再去初始化，一来避免重复去初始化，二来可以避免偶尔info日志重复打印的问题
myLog = get_log('操作日志_log.html')
