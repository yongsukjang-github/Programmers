# url
# https://programmers.co.kr/learn/courses/30/lessons/12906

# Function
def solution(arr):
    output1 = arr[:-1]
    output2 = arr[1:]
    answer=[arr[0]]
    for idx, val in enumerate(output2):
        if output1[idx] != output2[idx]:
            answer.append(val)
    return answer

# Test
print(solution(arr=[4,4,4,3,3]))

# Output
# [4,3]