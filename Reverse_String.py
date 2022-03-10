def rev_string(a):
    if a[0] == '-':
        a= '-' + a[:0:-1]

    else:
        a=a[::-1]

    return int(a)

print(rev_string('456'))
print(rev_string('-123'))