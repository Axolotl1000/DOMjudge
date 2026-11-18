precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
tokens = input().split() 
stack = []
output = []

for token in tokens:
    if token.isalnum():
        output.append(token)
    elif token == '(':
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            output.append(stack.pop())
        if stack and stack[-1] == '(':
            stack.pop()
    elif token in precedence:
        while (stack and stack[-1] in precedence and 
                precedence[stack[-1]] >= precedence[token]):
            output.append(stack.pop())
        stack.append(token)
        
while stack:
    output.append(stack.pop())
    
print(" ".join(output))