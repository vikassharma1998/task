a_dictionary = {"a": 1, "b": 2, "c": 3}
print(max(a_dictionary.items(),key =lambda i : i[1]))



a = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7}
b = {0:0, 1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 7:1}

print(max([k1 for (k1, v1), (k2, v2) in zip(a.items(), b.items()) if v1 == v2]))