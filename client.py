import socket
from rpc_runtime import send_msg, recv_msg


def rpc_call(profile):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 5000))

    send_msg(sock, {
        "method": "calculate_grade_average",
        "params": [profile]
    })

    response = recv_msg(sock)
    sock.close()
    return response


#VALID INPUT
print(rpc_call({
    "name": "Alice",
    "id": 1,
    "grades": [80, 90, 100]
}))

#TYPE ERROR
print(rpc_call({
    "name": "Bob",
    "id": "two",
    "grades": [70, 80]
}))
