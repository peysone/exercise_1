"""Za pomocą odpowiednich operacji, na podstawie przykładowej listy, stwórz listę,
w której będą tylko unikalne wartości.
przyklad = ["aaa", "bbb", "aaa", "ccc", "ddd", "aaa", "bbb", "ccc", "ddd", "eee"]"""

not_unique_list = ["aaa", "bbb", "aaa", "ccc", "ddd", "aaa", "bbb", "ccc", "ddd", "eee"]

unique_list = []
for u in not_unique_list:
    if u not in unique_list:
        unique_list.append(u)

print(unique_list)
