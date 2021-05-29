def reverse_linked_list(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next

def evaluate_rpn(expression):
    inter_results = []
    delimiter = ','
    operators = {
        '+':lambda y, x: x + y,'-':lambda y,x:x-y,
        '*':lambda y,x:x*y,'/':lambda y,x:x //y
    }
    
    for token in expression.split(delimiter):
        if token in operators:
            inter_results.append(operators[token](inter_results.pop(),inter_results.pop()))
        else:
            inter_results.append(int(token))
    return inter_results[-1]


expression = "3,4,+,2,*,1,+"
evaluate_rpn(expression)
# 15

def shortest_path(path):
    if not path:
        raise ValueError("パスが与えられていません")
        
    path_names = []
    if path[0] == '/':
        path_names.append("/")
    for token in (token for token in path.split("/") if token not in ['.','']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError("パスエラー")
        else:
            path_names.append(token)
            
    result = '/'.join(path_names)
    return result[result.startswith('//'):]


path = "/usr/lib/../appication/../bin/"
shortest_path(path)
# '/usr/lib/appication/bin'  

# Commentary on below article.
# https://www.kueharx.com/2021/05/python.html
