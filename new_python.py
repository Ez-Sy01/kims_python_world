import time

t = time.time()
local_time = time.gmtime(t)
print("{0}년{1}월{2}일에 생성되었습니다.".format(local_time.tm_year,local_time.tm_mon,local_time.tm_day))