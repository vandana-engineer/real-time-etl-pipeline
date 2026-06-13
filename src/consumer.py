def consume_event():
    event = {
        "order_id": 101,
        "customer_id": "C001",
        "amount": 250.75,
        "status": "created"
    }

    print("Consumed event:", event)

if __name__ == "__main__":
    consume_event()
