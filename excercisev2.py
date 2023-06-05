"""Za pomocą odpowiednich operacji, na podstawie przykładowej listy, stwórz listę,
w której będą tylko unikalne wartości.
przyklad = ["aaa", "bbb", "aaa", "ccc", "ddd", "aaa", "bbb", "ccc", "ddd", "eee"]"""

not_unique_list = ["aaa", "bbb", "aaa", "ccc", "ddd", "aaa", "bbb", "ccc", "ddd", "eee"]
print(not_unique_list)
print(100 * "-")

unique_list = [i for u, i in enumerate(not_unique_list)
               if i not in not_unique_list[:u]
               ]
print(unique_list)
