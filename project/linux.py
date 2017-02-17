# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import subprocess
import re

keydic = {"MemTotal": "总内存(单位G)",
          "MemFree": "剩余内存(单位G)",
          "MemAvailable": "可用内存(单位G)",
          "Cached": "缓存内存(单位G)"}


def command(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    resultDic = {}
    for line in p.stdout.readlines():
        line = str(line, encoding="utf-8")
        result = re.split("\s*", line)
        if result[0][:-1] in keydic:
            resultDic[keydic[result[0][:-1]]] = "%.2f" % (int(result[1]) / (1024 ** 2))
    return resultDic


if __name__ == "__main__":
    print(command("cat /proc/meminfo"))









# if __name__ == '__main__':