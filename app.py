def get_user(user_id):
    return {"id": user_id, "name": "User"}

def process_order(order_id, amount):
    return {"order_id": order_id, "amount": amount, "status": "pending"}

def send_notification(user_id, message):
    print(f"Notify {user_id}: {message}")
