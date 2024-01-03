import random
import sys
from my_module import hello
from demo_pkg import greet

coin = random.choice(["head","tail"])
print(coin)

rand_int = random.randint(1,10)
print(rand_int)

cards = ["king","queen","jack"]
random.shuffle(cards)
for card in cards:
    print(card)

if len(sys.argv) > 1:
    for name in sys.argv[1:]:
        print(name)
else:
    sys.exit("Few arguments")

hello("Inba")
greet.hello("Akilan")

'''
python 05_library.py Akilan Alex Jegan Kumar
Output:
head
4
queen
king
jack
Akilan
Alex
Jegan
Kumar
| Hello Inba |
  ==========
          \
           \
             ^__^
             (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
Hello Akilan, Welcome to demo_pkg
'''