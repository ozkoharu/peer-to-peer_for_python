from MessageManeger import MessageManager

PING_INTERVAL = 1800

class ConnectionManager:
    def __init__(self):
        print('未実装')

    # 待ち受けを開始する際に呼び出される (ServerCore向け)
    def start(self):
        print('未実装')

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
    def __add_peer(self):
        print('未実装')
    
    # 離脱したCoreノードをリストから削除する。クラスのそとからは利用しない想定
    def __remove_peer(self):
        print('未実装')

    # 接続されているCoreノードすべての接続状況確認を行う。クラスの外からは利用しない想定
    def __check_peers_connection(self):
        print('未実装')
