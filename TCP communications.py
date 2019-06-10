from socket import *
def main():
    #创建一个套接字 socket
    tcp_server_socket=tcp_server_socket=socket(AF_INET,SOCK_STREAM)
    #绑定本地信息
    tcp_server_socket.bind(("",2425))
    #让默认的套接字变为主动变为被动
    tcp_server_socket.listen(128)
    while True:
        print("-----1")
        #等待客户端的连接accept
        new_client_socket,client_addr=tcp_server_socket.accept()
        print("-----2")

        print("等待一个新的客户端%s"%str(client_addr))
        while True:
            #接收客户端发送过来的请求
            recv_data=new_client_socket.recv(1024)
            print("客户端发送的信息是%s" %recv_data.decode("utf-8"))
            #如果recv解堵塞那么有两种方式,
            #1.那么客户端发送过来数据,
            #2.客户端调用了close导致而了,这里recv解堵塞
            if recv_data:
                #回送一部分数据给客户端
                new_client_socket.send("hhh".encode("utf-8"))
            else:
                break
        #关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()

if __name__=="__main__":
    main()