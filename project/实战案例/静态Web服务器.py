# -*- encoding: utf-8 -*-
import socket
import threading


class Listening():
    def __init__(self):
        self.server_side = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_side.bind(('', 8080))
        self.server_side.listen(100)

    def Response(self):
        while True:
            serve_sock, client_sock = self.server_side.accept()
            print('客户端已接入', client_sock)
            Reply_all = threading.Thread(target=self.Reply, args=(serve_sock,))
            Reply_all.start()

    def Reply(self, serve_sock):
        client_side = serve_sock.recv(1024).decode()
        client_side_list = client_side.split(' ')

        if len(client_side_list) == 1:
            serve_sock.close()
            print('client已经退出')
            return

        client_side_path = client_side_list[1]

        if client_side_path == '/':
            client_side_path = 'index.html'

        try:
            with open('../阿波/day04/' + client_side_path, 'rb') as file:
                html_data = file.read()

        except Exception as mistake:
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_header = 'Server: Wunai\r\n'
            # 空行
            response_body = 'sorry,mistake,mistake'
            response_all = (response_line + response_header + '\r\n' + response_body).encode()
            serve_sock.send(response_all)
        else:
            response_line = 'HTTP/1.1 200 OK\r\n'
            response_header = 'Server: Wunai\r\n'
            # 空行
            response_body = html_data
            response_all = (response_line + response_header + '\r\n').encode() + response_body
            serve_sock.send(response_all)

        finally:
            serve_sock.close()


if __name__ == '__main__':
    server = Listening()
    server.Response()
