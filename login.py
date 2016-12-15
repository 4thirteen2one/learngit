#! usr/bin/env python
# -*- coding: utf-8 -*-

'''
assume the content of accounts.txt is below:
username1 password1
username2 password2
username3 password3
assume the content of account_lock.txt is below:
locked1
locked2
locked3
'''

import os,sys,getpass

account_file = 'accounts.txt'

lock_file = 'account_lock.txt'

error_limit = 3

error_count = 0

while error_count < error_limit:    #只要用户登录异常不超过3次就不断循环

    username = input('\033[32;1mUsername: \033[0m')

    lock_list = open(lock_file, 'r').readlines()
    # 当用户输入用户名后，打开LOCK 文件 以检查是否此用户已经LOCK了

    for lock_line in lock_list:    # 循环LOCK文件

        lock_line = lock_line.strip('\n')
        # 去掉换行符

        if username == lock_line:    # 若LOCK了就直接退出

            sys.exit('\033[31;1mUser %s is locked!\033[0m' % username)

    user_list = open(account_file, 'r').readlines()
    # 打开帐号文件

    for user_line in user_list:    #对帐号文件进行遍历

        (user, passwd) = user_line.strip('\n').split()
        # 分别获取帐号和密码信息

        if user == username:    #如用户名正常匹配

            retry_limit = 3

            retry_count = 0

            while retry_count < retry_limit:    #只要输入密码错误不超过3次就不断循环

                password = getpass.getpass('\033[32;1mPassword: \033[0m')
                # 输入隐藏密码

                if passwd == password:    #密码正确，提示欢迎登录

                    print('Welcome login! %s' % username)

                    sys.exit(0)
                    # 正常退出

                elif retry_count < (retry_limit - 1):    #j=2时，是最后一次机会，不用在提示还剩余0次机会了

                    print('用户%s密码错误，请重新输入，你还有%d次机会' % (username, retry_limit - 1 - retry_count))

                retry_count += 1
                # 密码输入错误后，循环值增加1

            else:    #密码输入三次错误后，将该用户追加到LOCK文件

                add_lock = open(lock_file,'a')

                add_lock.write(username + '\n')

                sys.exit('\033[31;1m用户 %s 达到最大登录次数，将被锁定并退出\033[0m' % username)

        else:    #当用户没匹配时，跳过并继续循环

            pass

    else:    #i=2时，是最后一次机会，不用在提示还剩余0次机会了

        if error_count < error_limit - 1:

            print('用户 %s 不存在，请重新输入，还有 %d 次机会' % (username, error_limit - 1 - error_count))

    error_count += 1

else:    #用户输入异常三次后退出

    sys.exit('用户 %s 不存在，退出' % username)

lock_file.close()
#关闭LOCK文件

user_file.close()
#关闭帐号文件

