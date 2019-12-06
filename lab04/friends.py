with open('friends.txt') as file:
    friends = file.readlines()

    friend = input('Enter another friend: ')
    friends.append(friend)
    print(friends)
    print(len(friends), 'friends')
