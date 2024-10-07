import inquirer
import numpy as np

def get_user_input():
    questions = [
        inquirer.Text("Clump", message="Clump Thickness"),
        inquirer.Text("UnifSize", message="Uniformity of Cell Size"),
        inquirer.Text("Unifshape", message="Unifshape"),
        inquirer.Text("MargAdh", message="MargAdh"),
        inquirer.Text("SignEpiSize", message="SignEpiSize"),
        inquirer.Text("BareNuc", message="BareNuc"),
        inquirer.Text("BlandChrom", message="BlandChrom"),
        inquirer.Text("Normnucl", message="Normnucl"),
        inquirer.Text("Mit", message="Mit"),
    ]
    
    # Promt
    answers = inquirer.prompt(questions)

    # Convert the answer
    new_data = np.array(
        [[
            int(answers['Clump']),
            int(answers['UnifSize']),
            int(answers['Unifshape']),
            int(answers['MargAdh']),
            int(answers['SignEpiSize']),
            int(answers['BareNuc']),
            int(answers['BlandChrom']),
            int(answers['Normnucl']),
            int(answers['Mit']),
        ]]
    )

    return new_data
