# url
# https://programmers.co.kr/learn/courses/30/lessons/67256

# Function
def solution(numbers, hand):

    # arg setting
    if hand == 'right':
        hand = 'R'
    elif hand == 'left':
        hand = 'L'

    # 전화번호 dictionary형태로 저장
    phone_dic={
        1: [0,3], 2: [1,3], 3: [2,3],
        4: [0,2], 5: [1,2], 6: [2,2],
        7: [0,1], 8: [1,1],9: [2,1],
        '*': [0,0], 0: [1,0], '#': [2,0]
    }

    # initial value
    IL=phone_dic['*']
    IR=phone_dic['#']

    # 최종 답 저장(left/right)
    answer=[]

    # main loop
    for idx, val in enumerate(numbers):
        if val in [1,4,7]:
            # 1,4,7 일경우 L
            answer.append('L')
            IL=phone_dic[val]
        elif val in [3,6,9]:
            # 3,6,9 일경우 R
            answer.append('R')
            IR=phone_dic[val]
        elif val in [2,5,8,0]:
            # 2,5,8,0 이 첫번째일 경우 선호손잡이로 표시
            if idx == 0:
                answer.append(hand)
                if hand == 'L':
                    IL=phone_dic[val]
                elif hand == 'R':
                    IR=phone_dic[val]
            # 2,5,8,0 이 첫번째가 아닐 경우 거리계산
            elif idx != 0:
                if (abs(phone_dic[val][0]-IL[0]) + abs(phone_dic[val][1]-IL[1])) - (abs(phone_dic[val][0]-IR[0]) + abs(phone_dic[val][1]-IR[1])) < 0:
                    answer.append('L')
                    IL=phone_dic[val]
                elif (abs(phone_dic[val][0]-IL[0]) + abs(phone_dic[val][1]-IL[1])) - (abs(phone_dic[val][0]-IR[0]) + abs(phone_dic[val][1]-IR[1])) > 0:
                    answer.append('R')
                    IR=phone_dic[val]
                elif (abs(phone_dic[val][0]-IL[0]) + abs(phone_dic[val][1]-IL[1])) - (abs(phone_dic[val][0]-IR[0]) + abs(phone_dic[val][1]-IR[1])) == 0:
                    answer.append(hand)
                    if hand == 'L':
                        IL=phone_dic[val]
                    elif hand == 'R':
                        IR=phone_dic[val]

    return ''.join(answer)

# Test
print(solution(numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],hand='left'))

# Output
# LRLLRRLLLRR