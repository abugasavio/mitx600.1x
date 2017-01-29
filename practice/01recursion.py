def hello_world(count):
    if count < 1:
        return
    print('Hello world')
    hello_world(count - 1)


hello_world(0)
