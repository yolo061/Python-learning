import socket

socket_server = socket.socket()

# bind方法接收的是一个元组
socket_server.bind(("127.0.0.1",8080))

# 此处填写允许的连接数量，超出回等待，不填会预设一个合理值
socket_server.listen(1)

# 接收客户端连接，获得连接对象
conn, address = socket_server.accept()
print(f"客户端连接,连接来自:{address}")
'''
accept是阻塞方法，如果没有连接，会卡在当前这一行不向下执行代码
accept返回的是一个二元元组,可以使用上述形式,用两个变量接收二元元组的两个元素
'''
# 接收客户端信息,要使用客户端和服务器端的本次连接对象，而非socket_server对象
# 客户端连接后，通过recv方法，接收客户端发送的消息
while True:
    data = conn.recv(1024).decode("UTF-8")
    # recv方法的返回值是字节数组(Bytes)，可以通过decode使用UTF-8解码为字符串
    # recv方法的传参是buffsize，缓冲区大小，一般设置1024即可
    if data == "exit":
        break
    print("接收到发送来的数据:",data)
    print("数据类型为:",type(data))
    msg = input("请输入您要回复的信息:").encode("UTF-8")
    conn.send(msg)
'''
data: str = conn.recv(1024).decode("UTF-8")
print("接收到发送来的数据:",data)
# 通过conn(客户端当次连接对象),调用send方法可以回复信息
conn.send("hello socket".encode("UTF-8"))
'''


# conn(客户端当次连接对象)和socket_server对象调用close方法,关闭连接
conn.close()
socket_server.close()