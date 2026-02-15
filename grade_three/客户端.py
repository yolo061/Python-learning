import socket
# 创建客户端对象
socket_client = socket.socket()

# 连接到服务器
socket_client.connect(("127.0.0.1",8080))
# 发送消息
socket_client.send("hello socket".encode("UTF-8"))
# 接收返回消息
recv_data = socket_client.recv(1024)
print(f"服务端回复的消息是:{recv_data}")
# 关闭连接
socket_client.close()