#! /usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# Simple TCP client and server that send receive 10 octets

import argparse, socket, sys

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length-len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received %d bytes before the '
                           'socket closed' % (length, len(data)))
        data += more
    return data


def server(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 45p
    sock.bind((host, port))
    sock.listen(1)  # listen方法决定了套接字是作为服务器使用，并且是不可撤销的
    print('Listen at', sock.getsockname())
    while True:
        sc, sockname = sock.accept()  # 监听套接字通过accept方法，生成一个连接套接字
        print('Process up to 1024 bytes at a time from', sockname)
        n = 0
        while True:
            data = sc.recv(1024)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sc.sendall(output)  # send it back uppercase
            n += len(data)
            print('\r %d bytes processed so far' % (n, ), end=' ')
            sys.stdout.flush()
        print()
        sc.close()
        print('  Socket closed')


def client(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = (bytecount + 15) // 16 * 16  # 四舍五入到16的倍数
    message = b'capitalize this!'   # 16-bytes message to repeat over and over

    print('Sending', bytecount, 'bytes of data, in chunks of 16 bytes')
    sock.connect((host, port))
    sent = 0
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print('\r %d bytes sent' % (sent, ), end='')
        sys.stdout.flush()

    print()
    sock.shutdown(socket.SHUT_WR)

    print('Receiving all the data the server sends back')

    recieved = 0
    while True:
        data = sock.recv(42)
        if not recieved:
            print('  The first data received says', repr(data))
        if not data:
            break
        recieved += len(data)
        print('\r %d bytes received' % (recieved, ), end='')

    print()
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Get deadlocked over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at; host the client sends to')
    parser.add_argument('bytecount', type=int, nargs='?', default=16,
                        help='number of bytes for client to send (default 16)')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port ('
                                                                           'default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p, args.bytecount)