import pprint

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


async def send_response(send, status, body, content_type='text/plain'):
    await send({
        'type': 'http.response.start',
        'status': status,
        'headers': [
            [b'content-type', content_type.encode('utf-8')],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': body.encode('utf-8'),
    })

 
async def app(scope, receive, send):
    if scope['method'] != 'GET':
        response_body = 'Not Found'
        await send_response(send, 404, response_body)
    
    print(pprint.pprint(scope))
    path = scope['path'].strip('/').split('/')
    if len(path) == 2 and path[0] == 'fibonacci':
        # будем считать, что последовательность начинается с 0
        try:
            n = int(path[1])
            response_body = fib(n)
            await send_response(send, 200, response_body)
        except ValueError:
            await send_response(send, 400, 'Invalid number format')
    elif len(path) == 2 and path[0] == 'factorial':
        pass
    elif len(path) == 2 and path[0] == 'mean':
        pass
    else:
        response_body = 'Not Found'
        await send_response(send, 404, response_body)