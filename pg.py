<<<<<<< main
import platform
import os

print(os.name)
print(platform.system())
=======
for i in range(10):
    for j in range(10):
        print(f'\033[{i*10+j}m{i*10+j:03d}\033[0m ', end='')
    print('')
>>>>>>> origin/main
