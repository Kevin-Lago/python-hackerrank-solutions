# if __name__ == '__main__':
#     s = input()
#     hasalnum = False
#     hasalpha = False
#     hasdigit = False
#     haslower = False
#     hasupper = False
#
#     for i in range(len(s)):
#         if (hasalnum and hasalpha and hasdigit and haslower and hasupper):
#             break
#         if (s[i:i + 1].isalnum()):
#             hasalnum = True
#         if (s[i:i + 1].isalpha()):
#             hasalpha = True
#         if (s[i:i + 1].isdigit()):
#             hasdigit = True
#         if (s[i:i + 1].islower()):
#             haslower = True
#         if (s[i:i + 1].isupper()):
#             hasupper = True
#
#     print(hasalnum)
#     print(hasalpha)
#     print(hasdigit)
#     print(haslower)
#     print(hasupper)


# def check(s, func_list):
#     res = []
#     for f in func_list:
#         res.append(any([getattr(str(l), f)() for l in s]))
#     return res
#
#
# if __name__ == '__main__':
#     s = input()
#     res = check(s, ["isalnum", "isalpha", "isdigit", "islower", "isupper"])
#     for r in res:
#         print(r)


if __name__ == '__main__':
    s = input()
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))
