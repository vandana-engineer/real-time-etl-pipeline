def transform_data(data):
    data["processed"] = True
    return data

if __name__ == "__main__":
    sample = {"order_id": 101, "amount": 250.75}
    print(transform_data(sample))
