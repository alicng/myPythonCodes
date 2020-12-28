def has_syncopation(s):

    return any([i=='#' for i in s[1::2]])

a=has_syncopation("#.###.#.")
print(a)
#return '#' in s[1::2]