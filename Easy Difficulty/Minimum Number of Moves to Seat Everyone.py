def minMovesToSeat(seats, students):
    """
    :type seats: List[int]
    :type students: List[int]
    :rtype: int
    """
    count = 0
    seatPos = 0
    studentPos = 0
    seats.sort()
    students.sort()
    for x in range(len(students)):
        count = count + abs(students[x]-seats[x])
    print(count)


answer = minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6])
print(answer)
