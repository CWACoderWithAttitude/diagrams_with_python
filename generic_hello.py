import json


def welcome(msg_file: str):

    with open(msg_file, 'r') as w:
        file_contents = json.load(w)
        print(f"Keys in {msg_file}: {file_contents.keys()}")
        print(f"Key values in {msg_file}: {file_contents.values()}")


def main() -> None:
    welcome('.devcontainer/devcontainer.json')


if __name__ == "__main__":
    main()
