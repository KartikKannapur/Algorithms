"""
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return null.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: null # since there is no common slot whose duration is 12
Constraints:

[time limit] 5000ms

[input] array.array.integer slotsA

1 ≤ slotsA.length ≤ 100
slotsA[i].length = 2
[input] array.array.integer slotsB

1 ≤ slotsB.length ≤ 100
slotsB[i].length = 2
[input] integer

[output] array.integer


Test Case #1
Input: [[7,12]], [[2,11]], 5,Expected: [],Actual: []
Test Case #2
Input: [[6,12]], [[2,11]], 5,Expected: [6,11],Actual: [6, 11]
Test Case #3
Input: [[1,10]], [[2,3],[5,7]], 2,Expected: [5,7],Actual: [5, 7]
Test Case #4
Input: [[0,5],[50,70],[120,125]], [[0,50]], 8,Expected: [],Actual: []
Test Case #5
Input: [[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8,Expected: [60,68],Actual: [60, 68]
Test Case #6
Input: [[10,50],[60,120],[140,210]], [[0,15],[60,72]], 12,Expected: [60,72],Actual: [60, 72]
RUN CODE
"""


def meeting_planner(slotsA, slotsB, dur):
    i = 0
    j = 0

    while (i < len(slotsA)) and (j < len(slotsB)):

        start = max(slotsA[i][0], slotsB[j][0])
        end = min(slotsA[i][1], slotsB[j][1])
        if end - start >= dur:
            return [start, start + dur]

        if (slotsA[i][1] < slotsB[j][1]):
            i += 1
        else:
            j += 1

    return []

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8

meeting_planner(slotsA, slotsB, dur)