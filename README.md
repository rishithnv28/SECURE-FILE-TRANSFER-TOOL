# Secure file transfer application

## Observation
This application securely transfers files over the web using AES encryption and custom encryption techniques based on recent research.

## features
- **AES-256 Encryption**: Uses AES-256 for file encryption.
- **Custom Encryption**: Applies additional encryption based on the checklist.
- **Checksum Validation**: Ensures file integrity using SHA-256 checksums.
- **MAC to IP Resolution**: Resolve MAC address to IP address for secure file transfer.

## lay
1. Cloning a repository:
    ```Sh
    git clone https://github.com/yourusername/secure_file_transfer.git
    cd secure_file_transfer
    ```

2. Run `setup.bat` with the necessary installation:
    ```Sh
    system.bat
    ```

## Survey
### Send the file
Use the following command to send the file.
```Sh
Send python secure_transfer.py <file_path> <filename> <client_mac>

file_path: Path of the file to be sent.
file_name: The name of the file to send.
receiver_mac: MAC address of the receiver.

Receiving the file
Use the following command to get the file.

Get python secure_transfer.py <save_path>

save_path: Path to save the received file.

For example

Sent by:

Send python secure_transfer.py C:\Users\Sender\Documents\Example.txt Example.txt 00:11:22:33:44:55

Customer:

python secure_transfer.py Get C:\Users\Recipients\Download

Examine

Run run_tests.py to create the basic test environment:
Python run_test.py
#This is a temporary file and sends it to the client and verifies it.

Encryption information:

AES Encryption: The file is encrypted using AES-256 with a key obtained from the password using PBKDF2.
Checksum verification: The SHA-256 checksum of the original file is calculated before encryption, and then compared to the checksum afterwards

