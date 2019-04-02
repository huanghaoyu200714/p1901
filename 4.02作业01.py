import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41904)
server.bind(server_addr)
print('服务器已经开启')
server.listen(10)
while 1:
    try:
        conn, conn_addr = server.accept()
    except Exception:
        break
    while 1:
        try:
            msg = conn.recv(65535)
            if not msg:
                break
            msg = msg.decode()
            print('收到{}的消息:{}'.format(conn_addr, msg))
            return_msg = 'http://localhost:63342/P1901python/作业/baidu.html?_ijt=i54ec1v4vniqbde9fkkua4gra6'
            conn.send(return_msg.encode())
        except Exception:
            break
    conn.close()
    print('{}的链接已经断开'.format(conn_addr))
server.close()
print('服务器已经结束')