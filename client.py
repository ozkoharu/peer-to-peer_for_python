import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 接続先IPは環境に合わせて
my_socket.connect(('192.168.1.100', 50030))
my_text = 'Hello! This is test message from my sample client!'
my_socket.sendall(my_text.encode('utf-8'))
