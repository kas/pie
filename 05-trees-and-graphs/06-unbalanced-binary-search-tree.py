def rotate_right(old_root):
    new_root = old_root.get_left()
    old_root.set_left(new_root.get_right())
    new_root.set_right(old_root)
    return new_root
