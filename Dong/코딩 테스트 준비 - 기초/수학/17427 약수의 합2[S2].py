# 약수의 합 2
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.5 초 (추가 시간 없음)	512 MB	4144	1712	1453	41.633%
# 문제
# 두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

# 자연수 N이 주어졌을 때, g(N)을 구해보자.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 g(N)를 출력한다.

# 예제 입력 1 
# 1
# 예제 출력 1 
# 1
# 예제 입력 2 
# 2
# 예제 출력 2 
# 4
# 예제 입력 3 
# 10
# 예제 출력 3 
# 87
# 예제 입력 4 
# 70
# 예제 출력 4 
# 4065
# 예제 입력 5 
# 10000
# 예제 출력 5 
# 82256014

N = int(input())

# 시간 초과
# sumAll = [0] * (N + 1)

# def sumDivisor(N) :
#     if N == 1 :
#         return 1
#     divisor = [1, N]
#     for i in range(2, int(N ** 1 / 2) + 1) :
#         if N % i == 0 :
#             divisor.append(i)
#             if int(N ** 1 / 2) + 1 < N // i :
#                 divisor.append(N // i)
#     return sum(divisor)

# for j in range(1, N + 1) :
#     sumAll[j] = sumDivisor(j)

# print(sum(sumAll))

sum = 0

for i in range(1, N + 1) :
    sum += (N // i) * i

print(sum)