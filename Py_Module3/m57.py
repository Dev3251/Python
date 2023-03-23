import random
def random_line(fname):
    f=open(fname).read().splitlines()
    print(random.choice(f))

random_line("m57File.txt")