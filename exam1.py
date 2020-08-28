# coding = utf-8

K, N = map(int, input().split())
d = list(map(int, input().split()))

final_index, return_num = K, 0
if final_index == 0:
    print("paradox")
else:
    flag = True
    for i, d_ in enumerate(d):
        if d_ == final_index:
            if i != N - 1:
                flag = False
                print("paradox")
                break
            else:
                final_index -= d_

        elif d_ < final_index: 
            final_index -= d_
        else:
            final_index = d_ - final_index
            return_num += 1

    if flag:
        print(str(final_index) + ' ' + str(return_num))
