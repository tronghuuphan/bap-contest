def clean_path(path):
    path = path.split('/')
    i = 0
    while True:
        if path[i] in ['','.']:
            path.pop(i)
            i -= 1
        elif path[i] == '..':
            path.pop(i)
            if i > 0:
                path.pop(i-1)
                i -= 1
            i -= 1
        i += 1
        if i == len(path):
            break
    return '/'+'/'.join(path)

if __name__ == '__main__':
    path4 = '/home/./ubuntu/../../bob/alice'
    path3 = '/home//ubuntu'
    path2 = '/../'
    path1 = '/home/'
    print(clean_path(path1))
    print(clean_path(path2))
    print(clean_path(path3))
    print(clean_path(path4))
