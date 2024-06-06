import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("F8:B5:4D:40:F5:CD", 4))

try:
    while True:
        message = input()
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break
        print(f"The answer is: {data.decode('utf-8')}")

except OSError as e:
    pass

client.close()
