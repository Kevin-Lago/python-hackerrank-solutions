import re

if __name__ == '__main__':
    m = re.findall(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]*([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]", input())

    if len(m) > 0:
        for group in m:
            print(group)
    else:
        print("-1")
