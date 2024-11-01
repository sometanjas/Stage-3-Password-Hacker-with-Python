import socket
import sys
import itertools
import logging
import string

class Logger:
    # STEP 1
    # create a logger object instance
    logger = logging.getLogger()

    # STEP 2
    # specify the lowest boundary for logging
    logger.setLevel(logging.DEBUG)

    # STEP 3
    # set a destination for your logs or a handler
    # here, we choose to print on console (a console handler)
    console_handler = logging.StreamHandler()

    # STEP 4
    # set the logging format for your handler
    log_format = '%(asctime)s | %(levelname)s: %(message)s'
    console_handler.setFormatter(logging.Formatter(log_format))

    # finally, add the handler to the logger
    logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

logger = Logger()

def connect_to_server(host, port, passwords):
    try:
        with socket.socket() as client_socket:
            logger.info(f"Attempting to connect to {host}:{port}")
            address = (host, port)
            client_socket.connect(address)

            for password in generate_case_combinations(passwords):
                encoded_password = password.encode()
                client_socket.send(encoded_password)
                response = client_socket.recv(1024).decode()
                logger.info("Connection successful.")
                if response == "Connection success!":
                    print(password)
                    break
    except ConnectionResetError:
        logger.error(f"{e.__class__.__name__} occurred: ConnectionResetError")
    except ConnectionAbortedError:
        logger.error(f"{e.__class__.__name__} occurred: ConnectionAbortedError")
    except socket.error as e:
        logger.error(f"Socket error occurred: {e}")


def open_file(file_path, mode='r'):
    """Open a file and log events."""
    try:
        logger.info(f"Attempting to open file: {file_path} in mode '{mode}'")
        with open(file_path, mode) as file:
            content = [x.rstrip() for x in file.readlines()]
            logger.info(f"File '{file_path}' opened and read successfully.")
            return content
    except FileNotFoundError:
        logger.error(f"File '{file_path}' not found.")
    except IOError as e:
        logger.error(f"I/O error occurred when handling the file '{file_path}': {e}")
    except Exception as e:
        logger.critical(f"Unexpected error occurred: {e}")


def generate_case_combinations(passwords):
    for word in passwords:
        for variant in itertools.product(*([letter.lower(), letter.upper()] for letter in word)):
            yield ''.join(variant)


def main():
    filepath = "/Users/tatjana/IdeaProjects/Password Hacker with Python/Password Hacker with Python/task/hacking/passwords.txt"
    passwords = open_file(filepath)

    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python hack.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    connect_to_server(host, port, passwords)


"""
# project phase #2
def generate_passwords():
    characters = string.ascii_lowercase + string.digits
    length = 1  # Start with length 1
    while True:  # Continue indefinitely until a password is found
        for password_tuple in itertools.product(characters, repeat=length):
            yield ''.join(password_tuple)  # Join tuple to form a string
        length += 1  # Increase length for the next iteration
"""


if __name__ == "__main__":
    main()
