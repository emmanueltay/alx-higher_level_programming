#!/usr/bin/python3
if _name_ == "_main_":
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if name[0:2] != "_":
            print("{}".format(name))
