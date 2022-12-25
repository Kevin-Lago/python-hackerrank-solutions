import re

if __name__ == '__main__':
    t = int(input())
    uids = [input() for i in range(t)]

    for uid in uids:
        if re.match(r"[a-zA-Z0-9]{10}", uid) \
                and len(set(uid)) == 10 \
                and len(re.findall("[A-Z]", uid)) >= 2 \
                and len(re.findall("[0-9]", uid)) >= 3:
            print("Valid")
            continue

        print("Invalid")
