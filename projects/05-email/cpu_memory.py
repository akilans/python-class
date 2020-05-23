import psutil
from email_agent import send_mail

max_cpu_usage = 30
max_mem_usage = 30
max_disk_usage = 10
'''
dir(psutil.virtual_memory())
psutil.cpu_count()
psutil.cpu_freq()
psutil.disk_partitions()
'''
cpu_usage = psutil.cpu_percent(interval=3)
memory_usage = psutil.virtual_memory()._asdict()
disk_usage = psutil.disk_usage("/")._asdict()
'''
print(type(cpu_usage))
print(type(memory_usage))
print(type(disk_usage))
'''

print(cpu_usage)
print(memory_usage["percent"])
print(disk_usage["percent"])

alert_msg = ""

if cpu_usage > max_cpu_usage:
    alert_msg = alert_msg+"<h1>"+"CPU usage exceeded - "+str(cpu_usage)+"%"+"</h1>"
if memory_usage["percent"] > max_mem_usage:
    alert_msg = alert_msg+"<h1>Memory usage exceeded - "+str(memory_usage["percent"])+"%"+"</h1>"
if disk_usage["percent"] > max_disk_usage:
    alert_msg = alert_msg+"<h1>Disk usage exceeded - "+str(disk_usage["percent"])+"%"+"</h1>"

if alert_msg != "":
    send_mail(alert_msg)
    print(alert_msg)
