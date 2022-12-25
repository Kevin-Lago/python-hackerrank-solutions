| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/set_mutations)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/sets/check_subset)</img> |
|:---|:---:|---:|

# The Captain's Room

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.

The tourists consist of:

-> A Captain.

-> An unknown group of families consisting of ___k___ members per group where $k != 1$.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has n unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear ___k___ time per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.

The total number of tourists or the total number of groups of families is not known to you.

You only know the value of ___k___ and the room number list.

__Input Format__

The first line consists of an integer, ___k___, the size of each group.

The second line contains the unordered elements of the room number list.

__Constraints__

$1 < k < 1000$

__Output Format__

Output the Captain's room number.

__Sample Input__

```
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
```

__Sample Output__

```
8
```

__Explanation__

The list of room numbers contains __31__ elements. Since ___k___ is __5__, there must be __6__ groups of families. In the given list, all of the numbers repeat __5__ times except for the room number __8__.

Hence, __8__ is the Captain's room number.

---

<details><summary>Solution</summary>
    
```python

```
</details>