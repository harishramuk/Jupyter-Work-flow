from imp import reload
import time
import module1

module1.add(10,20)
print('befor sleeping time..')
time.sleep(30)
print('after sleep..')
import module1
module1.product(10,20)
