pass_list = ['*#*#', '123']

def login():
    pass_input = input('please enter\n')
    pass_right = pass_list[-1] == pass_input
    pass_rest = pass_list[0]  == pass_input
    if pass_right:
        print("login ok")
    elif pass_rest:
        new_input = input('please enter new pass\n')
        pass_list.append(new_input)
        print("modify password ok")
        login()
    else:
        print('failed')
        login()
login()