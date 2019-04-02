import socket
import webbrowser
# 因为主机是ip4和tcp所以客户端一样需要使用ip4和tcp
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 41902)
client.connect(server_addr)
while 1:
    try:
        msg = input('请输入消息:')
        client.send(msg.encode())
        msg = client.recv(1460)
        print('收到服务器发送过来的消息:', msg.decode())
        webbrowser.open(msg.decode())
    except Exception:
        break
client.close()
print('链接已经完成')