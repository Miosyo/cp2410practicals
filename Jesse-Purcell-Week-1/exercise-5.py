# import random

import os


def main():
    # output: Ryan
    assert (find_student_by_id(os.getcwd() + '\\student_data.txt', 53) == 'Ryan')
    # output: Paul
    assert (find_student_by_id(os.getcwd() + '\\student_data.txt', 100) == 'Paul')
    # output: Jennifer
    assert (find_student_by_id(os.getcwd() +
            '\\student_data.txt', 800) == 'Jennifer')
    # output: Laura
    assert (find_student_by_id(os.getcwd() +
            '\\student_data.txt', 5050066078) == 'Laura')

    student_id = input("Input student ID: ")
    if student_id.isdigit():
        print(find_student_by_id(os.getcwd() +
              '\\student_data.txt', int(student_id)))
    else:
        print("Invalid id")
    # for i in range(0, 1000):
    #     print(find_student_by_id_binary_search('Jesse-Purcell-Week-1\student_data.txt', random.randint(0, 100000)))


def find_student_by_id(database, student_id):
    file_in = open(database)
    low = 0
    file_in.seek(0, 2)
    high = file_in.tell()
    while low < high:
        mid = (low + high) // 2
        file_in.seek(mid)
        line_length = len(file_in.readline())
        # print(f"low: {low}\nmid: {mid}\nhigh: {high}")
        guess = file_in.readline().strip().split(',')

        if int(guess[1]) == student_id:
            return guess[0]
        if (int(guess[1]) > student_id):
            high = mid - len(guess)
        else:
            low = mid + len(guess)
    # print('Item not found')
    return None


main()
