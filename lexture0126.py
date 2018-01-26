from csc131 import dictionaries


def main():
    print("main")
    d=dictionaries.get_personal_data()
    print(d)
    for key in sorted(d.keys()):
        print("%s: %s" % (key,d[key]))

def somethingelse():
    print('somethingelse')

if __name__ == '__main__':
    main()