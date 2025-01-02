# File handling basics
def read_config_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read all lines into a list
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []

def write_log(filename, message):
    # Append mode ('a') for logging
    with open(filename, 'a') as file:
        file.write(f"{message}\n")

# Usage
config_lines = read_config_file('config.txt')
write_log('security.log', 'Security scan started')
