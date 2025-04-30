from MessageManeger import MessageManager
from concurrent.futures import ThreadPoolExecutor
import socket

PING_INTERVAL = 1800

class ConnectionManager:
    def __init__(self, host, my_port):
        print('Initializing ConnectionManeger')
        self.host = host
        self.port = my_port
        self.core_node_set = set()
        self.__add_peer((host, my_port))
        self.mm = MessageManager()


    # 待ち受けを開始する際に呼び出される (ServerCore向け)
    def start(self):
        # メッセージ待機のために通信のための口を開く処理
        def __wait_for_access(self):
            self.socket = socket.socket(socket.AF_INTE, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen(0)
            executor = ThreadPoolExecutor(max_workers=10)

            while True:
                print('Waiting for the connection...')
                soc, addr = self.socket.accept()
                print('Connected by .. ', addr)
                data_sum = ''

                params = (soc, addr, data_sum)
                executor.submit(self.__handle_messages, params)
        # 他ノードから受け取ったメッセージを処理する
        def __handle_message(self, params):
            soc, addr, datasum = params
            while True:
                data = soc.recv(1024)
                data_sum = data_sum + data.decode('utf-8')

                if not data:
                    break
            if not data_sum:
                return
            result, reason, cmd, peer_port, payload = self.mm.parse(data_sum)
            print(result, reason, cmd, peer_port, payload)
            status = (result, reason)


    # ユーザーが指定したきちのCoreノードへの接続　(ServerCore向け)
    def join_network(self):
        print('未実装')
    
    # Coreノードリストに登録されているすべてのノードに対して
    # 同じメッセージをブロードキャストする
    def send_msg_all_peer(self):
        print('未実装')

    # 終了前の処理としてソケットを閉じる (ServerCore向け)
    def connection_close(self):
        print('未実装')
    
    # 受信したメッセージを確認して、内容に応じた処理を行う。クラスの外からは利用しない想定
    def __handle_message(self):
        print('未実装')
    
    # 新たに接続されたCoreノードをリストに追加する。クラスの外からは利用しない想定
    def __add_peer(self, peer):
        print('Adding peer :', peer)
        self.core_node_set.add((peer))
    
    # 離脱したCoreノードをリストから削除する。クラスのそとからは利用しない想定
    def __remove_peer(self, peer):
        if peer in self.core_node_set:
            print('Removing peer:', peer)
            self.core_node_set.remove(peer)
            print('Current Core list: ', self.core_node_set)

    # 接続されているCoreノードすべての接続状況確認を行う。クラスの外からは利用しない想定
    def __check_peers_connection(self):
        print('未実装')
