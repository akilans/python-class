import psutil

print(psutil.cpu_count()) # Number of CPUs
print(psutil.cpu_percent(3)) # Get the CPU usage in percentage