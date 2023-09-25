def get_record_at_index(index, filename):
    with open(filename, "rb") as file:
        offset = index * 21 + 4
        file.seek(offset)
        record = file.read(21)
        student_name = record[0:11].decode('utf-8').strip()
        student_id = str(record[11:21].decode('utf-8'))
    return student_name, int(student_id)


def find_student_by_id(database, id):
    OFFSET = 4
    LENGTH = 21

    id_int = int(id)

    file_in = open(database, 'rb')
    low = 0
    high = int.from_bytes(file_in.read(4))
    while low <= high:
        mid = (low + high) // 2
        file_in.seek((mid * LENGTH) + OFFSET)

        record = file_in.read(LENGTH)
        student_name = record[0:11].decode().strip()
        student_id = int(record[11:21].decode())

        if student_id == id_int:
            return student_name
        if student_id < id_int:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(find_student_by_id("student_data.bin", "0000000064"))  # output: Matthew
print(find_student_by_id("student_data.bin", "0000001447"))  # output: Timothy
print(find_student_by_id("student_data.bin", "0000030899"))  # output: Anthony
print(find_student_by_id("student_data.bin", "5049830265"))  # output: Steven
