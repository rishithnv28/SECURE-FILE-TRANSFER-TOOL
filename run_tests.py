import os
import subprocess
import tempfile

def run_tests():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b"Test data for secure transfer")
    temp_file.close()

    receiver_mac = "00:11:22:33:44:55"
    subprocess.run(["python", "secure_transfer.py", "send", temp_file.name, "testfile.txt", receiver_mac])
    received_file = temp_file.name + "_received"
    subprocess.run(["python", "secure_transfer.py", "receive", received_file])

    with open(temp_file.name, 'rb') as f1, open(received_file, 'rb') as f2:
        assert f1.read() == f2.read()

    os.remove(temp_file.name)
    os.remove(received_file)
    print("All tests passed successfully")

if __name__ == "__main__":
    run_tests()
