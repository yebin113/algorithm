def return_c(x, y, w):
    h1 = (x ** 2 - w ** 2) ** 0.5
    h2 = (y ** 2 - w ** 2) ** 0.5
    return h1 * h2 / (h1 + h2)


x, y, c = map(float, input().split())
start, end = 0, min(x, y)
res = 0
# end - start가 0.000001보다 클 때까지 반복
while end - start > 0.000001:
    middle = (start + end) / 2
    if return_c(x, y, middle) >= c:
        res = middle
        start = middle
    else:
        end = middle
print(f'{res:0.3f}')