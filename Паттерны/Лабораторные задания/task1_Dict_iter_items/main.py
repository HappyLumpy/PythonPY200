from typing import Iterator, Tuple, Hashable, Any


class MyDict(dict):
    def __iter__(self):
        for keys, values in self.items():
            print(keys,values)



if __name__ == "__main__":
    my_dict = MyDict({
        1: "a",
        2: "b",
        3: "c"
    })
    for key, value in my_dict:
        print(key, value)
