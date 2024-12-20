import websocket
import ssl
import rel
import os
from dotenv import load_dotenv
from event import decode_hid_event, replay_event

load_dotenv()

APP_NAME = os.environ['APP_NAME']

def on_message(ws, message):
    hid_event = decode_hid_event(message)
    replay_event(hid_event)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    ws.send_text(f'dest/{APP_NAME}')

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(f"wss://streamlineanalytics.net:10010",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE}, dispatcher=rel, reconnect=5, ping_interval=10)

    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()