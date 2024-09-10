import time
import pyautogui
import inquirer
from pynput import mouse

plate_options = {'GreenPlate1':[1.964	,	1.957	,	1.971	,	1.988	,	0.9591	,	0.9513	,	0.9541	,	0.9606,
                                3.927	,	3.915	,	3.943	,	3.977	,	1.918	,	1.903	,	1.908	,	1.921,
                                7.855	,	7.829	,	7.885	,	7.953	,	3.936	,	3.805	,	3.816	,	3.842,
                                39.19	,	39.03	,	39.36	,	39.71	,	19.07	,	18.93	,	18.99	,	19.12],
                'GreenPlate2':  [1.961	,	1.955	,	1.961	,	1.965	,	0.948	,	0.9503	,	0.9493	,	0.9474,
                                3.921	,	3.911	,	3.922	,	3.929	,	1.896	,	1.901	,	1.899	,	1.895,
                                7.842	,	7.822	,	7.843	,	7.859	,	3.792	,	3.801	,	3.797	,	3.79,
                                39.09	,	38.97	,	39.14	,	39.22	,	18.85	,	18.9	,	18.89	,	18.84],
                'OrangePlate1': [1.97	,	1.978	,	1.98	,	1.974	,	0.9506	,	0.947	,	0.9472	,	0.9553,
                                3.939	,	3.956	,	3.96	,	3.948	,	1.901	,	1.894	,	1.894	,	1.911,
                                7.878	,	7.912	,	7.919	,	7.897	,	3.802	,	3.788	,	3.789	,	3.821,
                                39.27	,	39.39	,	39.54	,	39.36	,	18.93	,	18.84	,	18.85	,	19.02,],
                'OrangePlate2': [1.97	,	1.981	,	1.977	,	1.977	,	0.9518	,	0.9484	,	0.9514	,	0.9505,
                                3.939	,	3.962	,	3.955	,	3.955	,	1.904	,	1.897	,	1.903	,	1.901,
                                7.879	,	7.923	,	7.909	,	7.909	,	3.807	,	3.793	,	3.806	,	3.802,
                                39.26	,	39.48	,	39.53	,	39.45	,	18.93	,	18.86	,	18.91	,	18.9,],
                'YellowPlate1': [1.968	,	1.977	,	1.965	,	1.967	,	0.937	,	0.939	,	0.946	,	0.941,
                                3.935	,	3.954	,	3.931	,	3.933	,	1.875	,	1.879	,	1.893	,	1.822,
                                7.87	,	7.908	,	7.862	,	7.866	,	3.75	,	3.757	,	3.785	,	3.763,
                                39.214	,	39.427	,	39.064	,	39.056	,	18.677	,	18.723	,	18.855	,	18.746,],
                'YellowPlate2': [1.954	,	1.969	,	1.958	,	1.964	,	0.94	,	0.94	,	0.941	,	0.943,
                                3.909	,	3.939	,	3.916	,	3.929	,	1.88	,	1.88	,	1.882	,	1.886,
                                7.817	,	7.877	,	7.823	,	7.858	,	3.76	,	3.76	,	3.764	,	3.772,
                                38.874	,	39.188	,	38.906	,	39.055	,	18.712	,	18.72	,	18.727	,	18.761,]
                }


# Variable to control if the input process should continue
continue_input = False
last_click_time = 0
double_click_threshold = 0.3  # seconds

def on_click(x, y, button, pressed):
    global continue_input, last_click_time
    if pressed:
        if button == mouse.Button.left:
            current_time = time.time()
            # Check if this click is within the double-click threshold
            if current_time - last_click_time < double_click_threshold:
                continue_input = True  # Start the process on a double click
            else:
                if continue_input:
                    # Stop the process if it's running and a single click occurs
                    continue_input = False
            # Update the time of the last click
            last_click_time = current_time

# Create a mouse listener
listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
    questions = [
        inquirer.List('plates',
                      message="Which plate's sensitivities do you want to input?",
                      choices=list(plate_options.keys()))
    ]
    answers = inquirer.prompt(questions)
    selected_plate_name = answers["plates"]  # The name of the selected plate
    selectedplate = plate_options[answers["plates"]]

    print(f"Selected Plate: {selected_plate_name}")

    # Wait for double-click to start the process
    print("Double-click in first field to start the input process.\n")
    while not continue_input:
        time.sleep(0.1)
    time.sleep(2.0)
    print("Input process started. Single-click to interrupt.\n")

    # Start input process
    for x in selectedplate:
        if not continue_input:
            print("Process interrupted by a single click.\n")
            break
        pyautogui.write(str(x))
        pyautogui.press('tab')


    # Wait for single click to potentially interrupt
    while continue_input:
        time.sleep(0.1)

listener.stop()