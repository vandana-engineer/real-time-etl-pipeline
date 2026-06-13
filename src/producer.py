def produce_event():
    event = {
        "order_id": 101,
        "customer_id": "C001",
        "amount": 250.75,
        "status": "created"
    }

    print("Produced event:", event)
    return event

if __name__ == "__main__":
    produce_event()
