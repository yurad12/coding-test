def solution(n,direction):
    direc_dict = {'R':1, 'L':-1, 'U':-1, 'D':1}
    current = [1,1]

    for i in direction:
        if (0<current[0]<6) & (0<current[1]<6):
            before = current.copy()
            if i in ['R','L']:
                current[1] += direc_dict[i]
            elif i in ['U','D']:
                current[0] += direc_dict[i]
            print('>>>',current)
        else:
            current = before.copy()
            if i in ['R','L']:
                current[1] += direc_dict[i]
            elif i in ['U','D']:
                current[0] += direc_dict[i]
            print('<<<',current)
    current = tuple(current)
    print(current)
    return current

solution(5,['R','R','R','U','D','D'])