import time

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
greeting(friends)
give_candy(friends)
end = time.time()
print('Time taken {}'.format(end-start))
