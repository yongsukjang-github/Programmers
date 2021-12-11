#function
def solution(arr):
    output1 = arr[:-1]
    output2 = arr[1:]
    answer=[arr[0]]
    for idx, val in enumerate(output2):
        if output1[idx] != output2[idx]:
            answer.append(val)
    return answer

#test
print(solution(arr=[4,4,4,3,3]))