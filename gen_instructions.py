import random
import pickle
def gen_instructions(max_process, max_ask, num_instructions):
    instructions = list()
    for i in range(num_instructions):
        name = random.randint(0,max_process)
        instruction = random.randint(0,max_ask)
        process = [name,instruction]
        instructions.append(process)

    pickle.dump(instructions, open("input.prod", "wb"))



if __name__ == "__main__":
    gen_instructions(5,8,100)
