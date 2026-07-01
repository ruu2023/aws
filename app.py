def get_user(user_id):
    return {"id": user_id, "name": "User"}

def update_user(user_id, data):
    return {"id": user_id, **data}

def delete_user(user_id):
    # 小さな改修1 (旧構造に適応): ユーザー削除機能 (by Alice)
    print(f"Deleting user {user_id}")
    return {"deleted": user_id}

def process_order(order_id, amount):
    return {"order_id": order_id, "amount": amount, "status": "pending"}

def cancel_order(order_id):
    # 小さな改修2 (旧構造に適応): 注文キャンセル機能 (by Bob)
    return {"order_id": order_id, "status": "cancelled"}

def send_notification(user_id, message):
    print(f"Notify {user_id}: {message}")

def send_bulk_notification(user_ids, message):
    # 小さな改修3 (旧構造に適応): 一括通知機能 (by Carol)
    for uid in user_ids:
        send_notification(uid, message)
