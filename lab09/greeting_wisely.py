import time
from threading import Thread

friends = ['Aldo', 'Keti', 'Floralba', 'Flori', 'Kevin', 'Meri']

def greeting(friends):
    for i in friends:
        print('Hello Dear {}. How are you?'.format(i))
        time.sleep(1)

def give_candy(friends):
    for i in friends:
        print('Hey! {}, here is your candy.'.format(i))
        time.sleep(1)


start = time.time()
t1 = Thread(target=greeting, args=(friends,))
t2 = Thread(target=give_candy, args=(friends,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('Time taken {}'.format(end-start))

