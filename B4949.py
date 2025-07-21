while(True):
    문장 = input()
    if 문장 == '.':
        break
    스택 = []    
    for 글자 in 문장:
        if 글자 == '(':
            스택.append('(')
        elif 글자 == '[':
            스택.append('[')
        elif 글자 == ')':
            if len(스택) == 0 or 스택.pop() != '(':
                print('no')
                break
        elif 글자 == ']':
            if len(스택) == 0 or 스택.pop() != '[':
                print('no')
                break
    else:
        print('yes')