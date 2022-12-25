| <img width=1000>[Previous Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/date_and_time/calendar_module)</img> | <img width=1000>[Home](https://github.com/Kevin-Lago/python-hackerrank-solutions)</img> | <img width=1000>[Next Question](https://github.com/Kevin-Lago/python-hackerrank-solutions/tree/main/src/python/errors_and_exceptions/exceptions)</img> |
|:---|:---:|---:|

# Time Delta

When users post an update on social media, such as a URL, image, status update ect., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e., how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

```Day dd Mon yyyy hh:mm:ss +xxxx```

Here +xxxx represent the time zone. Your task is to print the absolute difference (in seconds) between them.

__Input Format__

The first line contains ___t___, the number of test cases.

Each testcase contains __2__ lines, representing time ___t_<sub>1</sub>__ and time ___t_<sub>2</sub>__.

__Constraints__

- Input contains only valid timestamps

- $year \le 3000$

__Output Format__

Print the absolute difference __(_t_<sub>1</sub> - _t_<sub>2</sub>)__

__Sample Input__

```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```

__Sample Output__

```
25200
88200
```

__Explanation__

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours.

which is __7 x 3600__ seconds or __25200__ seconds.

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for the we have a difference of 1 day and 30 minutes. Or __24 x 3600 + 30 x 60 = 88200__

---

<details><summary>Solution</summary>
    
```python
import datetime


def time_delta(t1, t2):
    t1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    td = t1 - t2 if t1 > t2 else t2 - t1

    return int(td.total_seconds())


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
```
</details>