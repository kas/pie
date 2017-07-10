def remove_chars(string, remove):
    # set all elements in lookup array to false
    # iterate through each character in remove, setting the corresponding value in the lookup array to true
    # iterate through string with a source and destination index, copying each character only if its corresponding value in the lookup array is false

    src = dst = 0

    # size of 128 assumes ASCII
    flags = [False] * 128

    # set flags for characters to be removed
    for src in range(0, len(remove)):
        flags[remove[src]] = True

    for src in range(0, len(string)):
        if not flags[string[src]]:
            string[dst+1] = string[src]

    string = string[:dst]

    return string
