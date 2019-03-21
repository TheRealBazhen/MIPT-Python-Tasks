import import_me


def get_all_functions():
    funcs = []
    for name in dir(import_me):
        if callable(getattr(import_me, name)):
            funcs.append(name)
    return funcs
