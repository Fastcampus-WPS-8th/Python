#import game
from functions.game import *
from functions.shop import show_info as shop_info
from functions import shop
from friends.chat import send_message, send_message2

shop_info()

def turn_on():
    print('= Turn on game =')

    while True:
        choice = input('뭐할래?\n 1: 상점가기\n 2: 게임시작하기\n 3 or 4: 메시지 보내기\n 0: 종료\n  입력: ')
        if choice == '1':
            shop.buy_item()
        elif choice == '2':
            play_game()
        elif choice == '3':
            send_message()
        elif choice == '4':
            friend = input('친구명: ')
            message = input('메시지: ')
            send_message2(friend, message)
        elif choice == '0':
            break
        else:
            print('1, 2, 3중 하나를 입력해주세요')

if __name__ == '__main__':
    turn_on()

