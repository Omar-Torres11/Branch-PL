import Branch

while True:
    text = input('Branch > ')
    result, error = Branch.run(text)

    if error: print (error.as_string())
    else: print(result)