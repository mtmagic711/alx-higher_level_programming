#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    lists = dir(hidden_4)
    for i in lists:
        if i[:2] != "__":
            print(i)
