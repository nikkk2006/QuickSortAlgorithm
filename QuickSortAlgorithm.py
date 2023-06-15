# Quick Sort Algorithm


def QuickSort(myArr):
    if len(myArr) <= 1:
        return myArr

    main_numb = myArr[0]
    less_numbs = [numb for numb in myArr if numb < main_numb]
    bigger_numbs = [numb for numb in myArr if numb > main_numb]

    return QuickSort(less_numbs) + [main_numb] + QuickSort(bigger_numbs)


def main():
    my_list = [int(numb) for numb in input().split()]

    print(QuickSort(my_list))


if __name__ == '__main__':
    main()
