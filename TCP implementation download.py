from socket import *

def send_file_to_climent(new_client_socket,client_addr):
    #1.接收客户端发送过来的文件名
    #接收哭护短发送过来的需要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)下载的文件是:%s" % (str(client_addr), file_name))
    file_content=None
    #2.打开这个文件
    try:
        f=open(file_name,"rb")
        file_content=f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件%s"%file_name)
    #3.发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)
def main():
    tcp_server_socket=tcp_server_socket=socket(AF_INET,SOCK_STREAM)
    tcp_server_socket.bind(("",2425))
    tcp_server_socket.listen(128)
    while True:
        new_client_socket,client_addr=tcp_server_socket.accept()
        send_file_to_climent(new_client_socket,client_addr)
        new_client_socket.close()
    tcp_server_socket.close()

if __name__=="__main__":
    main()