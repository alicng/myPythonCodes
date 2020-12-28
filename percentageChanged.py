def percentage_changed(old, new):

    return f"{int(abs(int(old[1:]) - int(new[1:]))*0.1)}% {'decrease' if int(old[1:]) > int(new[1:]) else 'increase'}"

a=percentage_changed("$100", "$840")
print(a)