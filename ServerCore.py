STATE_INTI = 0
STATE_STANBY = 1
STATE_CONNECTION_TO_NETWORK = 2
STATE_SHUTTING_DOWN = 3

class ServerCore:
    def __init__(self):
        self.server_state = STATE_INTI
        print('Initirazing server...')

    def start(self):
        self.server_state = STATE_STANBY

    def join_network(self):
        # 接続完了していないのにCONNECTEDになってるのは気にしない
        self.server_state = STATE_CONNECTION_TO_NETWORK
    
    def shutdown(self):
        self.server_state = STATE_SHUTTING_DOWN

    def get_my_current_state(self):
        return self.server_state

