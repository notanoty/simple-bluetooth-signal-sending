import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

server.bind(("F8:B5:4D:40:F5:CD", 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Your message: ")
        client.send(message.encode("utf-8"))
except OSError:
    pass

client.close()
server.close()
