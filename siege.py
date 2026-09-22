"""Тикет 0: парсер лога осады.

Запуск: python3 siege.py siege_log.txt
"""

import sys


def main(path: str) -> None:
    with open('siege_log.txt', encoding='utf-8') as log:
        skip=list(log)
        for i in skip[2:]:
            if not i.strip():
                nick,gild,damage=0,0,0
            else:
                line=i.strip().split('|')
                baf2=1
                baf1=1
                first=line[0]
                second=line[1]
                if len(line)>2:
                      cond=line[2]
                      if len(line)>3:
                            baf1=line[3]
                      elif len(line)>4:
                            baf2=line[4]
                if len(line)<=2:
                      cond='fgf'
                if first.startswith('[') and ']' in first:
                      poisk=first.find(']')
                      if not first.startswith('['):
                                  first=first[first.find('['):]                
                      gild=first[1:poisk]
                      gild=gild.replace('[','')
                      if gild=='' or gild==' ':
                            gild=0
                      nick=first[poisk+1:]
                      nick=nick.replace('[','_').replace(']','')
                elif not '[' in first:
                      gild=0
                      nick=first
    
    
                try:
                      a=float(cond)
                      if True:
                            if len(line)>2:
                                  baf1=line[4]
                                  cond=line[3]
                                  nick=nick+'_'+second
                
                except ValueError:
                      pass
    
    
    
                if 'Active' in cond:
                      mn=1.5
                elif 'Broken' in cond:
                      mn=0.5
                elif 'Repairing' in cond:
                      mn=1
                elif 'Destroyed' in cond:
                      mn=0
                elif 'Overheated' in cond:
                      mn=0.8
                else: 
                      mn=1
    
                second=second.replace(',','.').replace(' ','')
    
    
    
                try:
                      a=float(second)
                      if True:
                            dam=float(second)
                            if dam>100000:
                                  dam=100000
                            if dam<0:
                                  dam=0
                except ValueError:
                      if 'inf' in second:
                            dam=100000
                      try:
                            a=float(cond)
                            if True:
                                  dam=float(cond)
                                  nick=nick+'_'+second
    
                      except ValueError:
                            dam=0
    
                      try:
                            a=float(cond)
                            if True:
                                  dam=float(cond)
                                  nick=nick+'_'+second
                      
                      except ValueError:
                            dam=0
    
                baf1=str(baf1).replace('N/A','0')
                if baf1=='':
                      baf1=0
                elif float(baf1)<0:
                      baf1=0
                damage=round(dam*mn*(1+0.15*float(baf1)*float(baf2)),2)
                nick=str(nick).strip().replace(' ','_')
                #Если нужна именно проверка но будто выше лучше:
                #if ' ' in str(nick).strip():
                #      nick=str(nick).strip().replace(' ','_')
                h=''
                for i in nick:
                    if ('a'<=i<='z')or('A'<=i<='Z') or i=='_':
                        h+=i
                nick=h
                if len(nick)<=1:
                    nick=0
                
                
                gild=str(gild).upper()
            print(f'Игрок {nick} из гильдии {gild} нанес {damage} по воротам')
    pass


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "siege_log.txt")
