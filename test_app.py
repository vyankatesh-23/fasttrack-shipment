from app import track_shipment

def test_in_transit():
    assert track_shipment(1001, "In Transit") == "Shipment #1001 is: In Transit"

def test_delivered():
    assert track_shipment(1002, "Delivered") == "Shipment #1002 is: Delivered"

def test_pending():
    assert track_shipment(1003, "Pending") == "Shipment #1003 is: Pending"
