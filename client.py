import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # サーバを指定する
    sock.connect((socket.gethostname(), 6000))
    # サーバにメッセージを送信
    sock.sendall(b'Hello server!!')
    # サーバーからの返信を受け取る
    data = sock.recv(1024)
    print(data)
