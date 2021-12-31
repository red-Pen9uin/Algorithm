# 문제
# 예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
#
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
#
# 입력
# 첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
# 0 없음 주의
# 출력
# 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
x = int(input())
y = int(input())

if x > 0 :
    if y > 0:
        print(1)
    if y < 0:
        print(4)
else :
    if y > 0:
        print(2)
    if y < 0:
        print(3)
