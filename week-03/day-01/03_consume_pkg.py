import my_package.durga_pkg.durga
import my_package.akilan
import my_package.inba

# Import only function and variable
from my_package.durga_pkg.durga import hello_durga
from my_package.akilan import hello_akilan
print(hello_durga())
print(hello_akilan())


greeting_akilan = my_package.akilan.hello_akilan()
print(greeting_akilan)

greeting_inba = my_package.inba.hello_inba()
print(greeting_inba)

greeting_durga = my_package.durga_pkg.durga.hello_durga()
print(greeting_durga)
