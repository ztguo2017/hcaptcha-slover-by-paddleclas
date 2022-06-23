if __name__ == '__main__':
    import os
    files = os.listdir('hcaptcha_labels')
    f1 = open('hcaptcha_labels/train.txt', 'a+', encoding='utf8')
    f2 = open('hcaptcha_labels/val.txt', 'a+', encoding='utf8')
    for index, name in enumerate(files):
        total = 1
        path = f'hcaptcha_labels/{name}'
        names = os.listdir(path)
        for n in names:
            if total / len(names) >= 0.2:
                f1.write(f'{name}/{n}' + ' ' + str(index) + '\n')
            else:
                f2.write(f'{name}/{n}' + ' ' + str(index) + '\n')
            total += 1