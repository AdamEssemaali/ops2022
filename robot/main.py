from matplotlib.pyplot import plot, show
from enum import Enum
from rich import print
import re

def info(log): 
    print(f"[bold blue][INFO][/bold blue] {log}")

memory_heap = {

}

class Commands(Enum):
    FORWARD: str = "f",
    CLOCKWISE_TURN: str = "o"
    ANTICLOCKWISE_TURN: str = "a"

class Direction(Enum):
    NORD: str = "N"
    SUD: str  = "S"
    EST: str = "E"
    WEST: str = "W"

class LoadMemory:
    def __init__(self, var_name: str, var_value: str):
        self.var_name = var_name
        self.var_value = var_value
    def __repr__(self):
        return f"LoadMemory(var_name={self.var_name}, var_value={self.var_value})"

direction = [(Direction.EST, Direction.WEST), (Direction.NORD, Direction.SUD)]

def lex_commands_from_file(path: str) -> list:
    # read the commands from a file and convert the string value into a list
    commands: list = list(open(path, "r").read())

    # delete the curly braces
    commands.pop(0)
    commands.pop(-1)

    # transform the list into a string and then split for all the commas
    commands: list = "".join(commands).split(",")
    return commands

def clockwise_turn(initial_direction: Direction) -> Direction:
    dirs = [Direction.NORD, Direction.EST, Direction.SUD, Direction.WEST]
    dir_counter = dirs.index(initial_direction)

    if dir_counter == len(dirs) - 1:
        dir_counter = 0 

        return dirs[dir_counter]
    
    dir_counter += 1
    return dirs[dir_counter]
def anticlockwise_turn(initial_direction: Direction) -> Direction:
    dirs = [Direction.NORD, Direction.EST, Direction.SUD, Direction.WEST]
    dir_counter = dirs.index(initial_direction)

    if dir_counter == 0:
        dir_counter = len(dirs) -1
        return dirs[dir_counter]

    dir_counter -= 1


    return dirs[dir_counter]


def transform_from_string_to_command(command: str) -> Commands:
    if command == "f":
        return Commands.FORWARD
    if command == "o":
        return Commands.CLOCKWISE_TURN
    if command == "a":
        return Commands.ANTICLOCKWISE_TURN
    if command.startswith("c"):
        var_name = re.findall(r"\d+", command)[0]
        print(var_name)
        # check if the variable is in the memory heap 
        if var_name in memory_heap:
            return LoadMemory(var_name, memory_heap[var_name])


def parse_commands(command_list: list) -> list:
    buffer = []
    save_into_mem = None
    i = 0
    while i < len(command_list):
        if save_into_mem != None:

            if "|" in command_list[i]:
                memory_heap[save_into_mem].append(transform_from_string_to_command(command_list[i][0]))
                i+= 1
                save_into_mem = None
            else:
                memory_heap[save_into_mem].append(transform_from_string_to_command(command_list[i]))
        else:
            buffer.append(transform_from_string_to_command(command_list[i]))
        if command_list[i].startswith("s"):
            print("save")   
            var_name = re.findall(r"\d+", command_list[i])[0]
            save_into_mem = var_name

            var_value = command_list[i][-1]
            memory_heap[var_name] = []
            memory_heap[var_name].append(transform_from_string_to_command(var_value))
        i += 1
    return buffer


def execute_commands(command_list: list, robot_position: list) -> list:
    for cmd in command_list:
        if cmd == Commands.CLOCKWISE_TURN:
            new_direction = clockwise_turn(robot_position[1])
            info(f"CLOCKWISE TURN: {robot_position[1]} -> {new_direction}")


            robot_position[1] = new_direction
        if cmd == Commands.ANTICLOCKWISE_TURN:
            new_direction = anticlockwise_turn(robot_position[1])
            info(f"ANTICLOCKWISE TURN: {robot_position[1]} -> {new_direction}")

            robot_position[1] = new_direction
        if cmd == Commands.FORWARD:
            # get the current direction
            current_direction = robot_position[1]

            # get the current position
            current_position = robot_position[0]

            # control if modify the x or the y
            if current_direction == Direction.EST or current_direction == Direction.WEST:
                # modify the x
                if current_direction == Direction.EST:
                    current_position[0] += 1
                else:
                    current_position[0] -= 1
            else:
                # modify the y
                if current_direction == Direction.NORD:
                    current_position[1] += 1
                else:
                    current_position[1] -= 1

            info(f"FORWARD: {robot_position[0]} -> {current_position}")
        if isinstance(cmd, LoadMemory):
            execute_commands(memory_heap[cmd.var_name], robot_position)

        


commands_raw: list = lex_commands_from_file("command.txt")
commands_parsed: list = parse_commands(commands_raw)
for cmd in commands_parsed:
    if None in commands_parsed:
        commands_parsed.remove(None)



robot_position = [[8,7], Direction.NORD]
plot(robot_position[0][0], robot_position[0][1], "ro")

execute_commands(commands_parsed, robot_position)