import socket

def main():
    #创建udp变量
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        print("------聊天器--------")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出系统")
        op=input("请输入数字:")
        if op=="1":
            send_msg(udp_socket)
        elif op=="2":
            recv_msg(udp_socket)
        elif op=="0":
            break
        else:
            print("输入有误")
    #关闭变量
    udp_socket.close()
def send_msg(udp_socket):
    dest_ip = "192.168.0.183"
    dest_port=int(2425)
    # dest_ip = input("请输入对方IP:")
    # dest_port = int(input("请输入对方port:"))
    # 从键盘获取数据
    send_data = input("请输入要发送的数据:")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def recv_msg(udp_socket):
    # 接收回来的数据
    recv_data = udp_socket.recvfrom(1024)
    # 变量是可以同时收发数据
    print("%s:%s"%(recv_data[1],recv_data[0].decode("utf-8")))
if __name__=="__main__":
    main()