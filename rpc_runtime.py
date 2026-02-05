import socket
import json


def send_msg(sock, data):
    message = json.dumps(data).encode("utf-8")
    sock.sendall(message)


def recv_msg(sock):
    data = sock.recv(4096).decode("utf-8")
    if not data:
        return None
    return json.loads(data)


#TYPE VALIDATION

def validate_types(profile):

    if not isinstance(profile, dict):
        raise TypeError("StudentProfile must be a dictionary")

    if not isinstance(profile.get("name"), str):
        raise TypeError("name must be a string")

    if not isinstance(profile.get("id"), int):
        raise TypeError("id must be an integer")

    grades = profile.get("grades")

    if not isinstance(grades, list):
        raise TypeError("grades must be a list")

    for g in grades:
        if not isinstance(g, int):
            raise TypeError("grades must contain only integers")
