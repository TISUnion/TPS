# -*- coding: utf-8 -*-

from time import sleep

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!tps'):
      args = info.content.split(' ')
      if args[0] == '!!tps':
        if (len(args) == 1):
          server.execute('debug start')
          sleep(1)
          server.execute('debug stop')
        elif (len(args) == 2) and (args[1]=='help'):
          server.tell(info.player, '使用 !!tps [秒数] 指定获取多少秒内的tps')
        elif (len(args) == 2) and (args[1].isdigit()) and (float(args[1]) >= 1.0 ) and (float(args[1]) <= 60):
          server.execute('debug start')
          sleep(float(args[1]))
          server.execute('debug stop')
        elif (len(args) == 2) and (args[1].isdigit()) and (float(args[1]) < 1.0 ):
          server.say(info.player + '甘霖娘!')
        elif (len(args) == 2) and (args[1].isdigit()) and (float(args[1]) > 60 ):
          server.say(info.player+'滚出克!')
        else:
          server.say('输入无效')
      else:
        pass
  elif info.content.startswith('Stopped debug profiling after'):
    server.say(info.content.replace('Stopped debug profiling after ', '', 1))
