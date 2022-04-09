# -*- encoding: utf-8 -*-
import socket


if __name__ == '__main__':

    # 创建客户端socket对象 socket.AF_INET --- IPv4，socket.SOCK_STREAM --- TCP流式传输协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 和服务器socket进行连接
    tcp_client_socket.connect(('10.255.254.1', 9090))

    # 传输数据的循环


        # 用户输入数据
    content = input('请输入您的反馈：')

        # 发送数据
    tcp_client_socket.send(content.encode('utf-8'))

        # 接收数据 1024 --- 单词接受数据的最大值
    recv_data = tcp_client_socket.recv(99999).decode('utf-8')
    print(recv_data)

        # 判断是否继续传输


    # 关闭客户端socket
    tcp_client_socket.close()
