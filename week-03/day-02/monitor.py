import psutil
import email_module

try:
    if psutil.cpu_percent(3) > 30:
        email_module.send_email_function()
except Exception as e:
    print(e)