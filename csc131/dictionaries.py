import string
def get_personal_data() -> dict:
    """return: return a dict of personal information"""


    personal_data = {"name": "Jim", "A_role": "teacher"}

    return personal_data

def main()->int:
    default_dict=dict()
    print(default_dict)
    initialized_dict = dict([('name', 'Jim'),('a_role','joker')])
    print(initialized_dict)
    simple_init_dict = dict(name='Jim', a_role = 'teacher')
    print(simple_init_dict)
    simple_init_dict['a_role']='joker'
    print(simple_init_dict)
    my_comprehension={x:x**2 for x in range(5)}
    print(my_comprehension)

    s="little,".translate({ord(i): None for i in  string.punctuation})
    print(s)
    return 0

if __name__ == '__main__':
    main()
