# scripts/send_command.py
import mcrcon
import argparse

def send_command(command):
    # Connect to the Minecraft server using RCON
    with mcrcon.MCRcon("localhost", "your-rcon-password") as mcr:
        response = mcr.command(command)
        print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send commands to Minecraft server")
    parser.add_argument("command", type=str, help="The command to send to the Minecraft server")
    args = parser.parse_args()

    send_command(args.command)
