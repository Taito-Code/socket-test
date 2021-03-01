import socket

# TCP/IPv4でのソケット作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # IPアドレスとポート番号をソケットに割り当てる
    sock.bind((socket.gethostname(), 6000))

    # 接続待ち:接続数1
    sock.listen(1)

    while True:
        # 接続受信したらコネクションとアドレスを格納
        connect, address = sock.accept()
        with connect:
            while True:
                # データの受信
                data = connect.recv(1024)
                if not data:
                    break

                # データをバイト型で返す
                print('data:{}, address:{}'.format(data, address))
                connect.sendall(b"Welcome to the server! " +
                                b"Your msg:" + data)
