# n = int(input())
# n_users = [input() for _ in range(n)]
# m = int(input())
# m_users = [input() for _ in range(m)]
# n_users_dict = {}
# res = []
#
# for i in n_users:
#     for j in range(len(i.split("@")[0]) - 1, 0, -1):
#         index = 0
#         if i[j].isdigit():
#             pass
#         else:
#             name = i.split("@")[0][:j + 1]
#             if i.split("@")[0][j + 1:]:
#                 index = i.split("@")[0][j + 1:]
#             break
#     n_users_dict.setdefault(name, set()).add(int(index))
#
# for user in m_users:
#     if user in n_users_dict:
#         for l in range(len(n_users_dict[user]) + 1):
#             if l in n_users_dict[user]:
#                 pass
#             else:
#                 n_users_dict[user].add(l)
#                 if l == 0:
#                     print(f"{user}@beegeek.bzz")
#                 else:
#                     print(f"{user}{l}@beegeek.bzz")
#                 break
#     else:
#         n_users_dict.setdefault(user, set()).add(0)
#         print(f"{user}@beegeek.bzz")

emails = set(input() for _ in range(int(input())))
for _ in range(int(input())):
    user = input()
    email = f"{user}@beegeek.bzz"
    count = 0
    while email in emails:
        count += 1
        email = f"{user}{count}@beegeek.bzz"
    emails.add(email)
    print(email)