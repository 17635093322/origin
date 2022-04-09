# -*- encoding: utf-8 -*-
import random


game = '猜拳游戏'
game_title = f'{game:-^100}'
print(game_title)
print('{str1:-^97}'.format(str1='您会与电脑进行游戏'))
user_choice_difficulty = input('请你选择难度(简单，困难):')

i = 0
while i < 3:
    i += 1
    if user_choice_difficulty == '简单':
        user_choice = input('请输入你的选择(石头，剪刀，布):')  # 玩家开始输入
        choices_list = ['石头', '剪刀', '布']  # 电脑开始进行选择
        AI_choice = random.choice(choices_list)
        print('AI电脑的选择是' + AI_choice)  # 输出电脑的选择
        # 结果比较
        if user_choice == AI_choice:
            print('平局')
        elif (user_choice == '石头' and AI_choice == '布') or (user_choice == '布' and AI_choice == '剪刀') or (user_choice == '剪刀' and AI_choice == '石头'):
            print('你输了')
        else:
            print('你赢了')
            print('不玩了')
            break
    elif user_choice_difficulty == '困难':
        user_choice = input('请输入你的选择(石头，剪刀，布):')  # 玩家开始输入
        AI_choice = ''
        if user_choice == '石头':
            AI_choice = '布'
        elif user_choice == '剪刀':
            AI_choice = '石头'
        elif user_choice == '布':
            AI_choice = '剪刀'
        print(f'AI电脑的选择是{AI_choice}')
        print('你输给了人工智能')
        if i == 3:
            print('小废物')
