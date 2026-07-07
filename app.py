def track_shipment(shipment_id, status):
    return f"Shipment #{shipment_id} is: {status}"

if __name__ == "__main__":
    print(track_shipment(1001, "In Transit"))
    print(track_shipment(1002, "Delivered"))
    print(track_shipment(1003, "Pending"))
