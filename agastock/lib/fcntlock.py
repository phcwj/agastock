import os
import win32con
import pywintypes
import win32file
"""
from: https://www.jianshu.com/p/4a0fa333c562
1. 先pip安装pywin32 ：

pip install pywin32
pip list  #查看是否在已安装列表中

安装完成之后，需要将C:\Python27\Lib\site-packages\pywin32_system32目录下的.dll文件复制到C:\Windows\System32目录下，这样便可以引用一下三个模块了：
import win32con \\ import pywintypes \\ import win32file

2. 设计fcntl()函数代码

复制以下代码段，保存为fcntlock.py文件，将其放到引用的目录下，通过import fcntlock as fcntl 引入模块即可，亲测有效。
"""
LOCK_EX = win32con.LOCKFILE_EXCLUSIVE_LOCK
LOCK_SH = 0  # The default value
LOCK_NB = win32con.LOCKFILE_FAIL_IMMEDIATELY
__overlapped = pywintypes.OVERLAPPED()

def flock(file, flags):
    hfile = win32file._get_osfhandle(file.fileno())
    win32file.LockFileEx(hfile, flags, 0, 0xffff0000, __overlapped)
def unlock(file):
    hfile = win32file._get_osfhandle(file.fileno())
    win32file.UnlockFileEx(hfile, 0, 0xffff0000, __overlapped)