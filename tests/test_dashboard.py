from main import snapshot

def test_snapshot():
    data = snapshot()
    assert {"cpu_percent","memory_percent","disk_percent","processes"} <= data.keys()
