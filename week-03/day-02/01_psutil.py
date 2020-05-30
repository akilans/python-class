import psutil

print(psutil.cpu_count())
print(psutil.cpu_percent(3))
print(psutil.virtual_memory())
#print(psutil.test())