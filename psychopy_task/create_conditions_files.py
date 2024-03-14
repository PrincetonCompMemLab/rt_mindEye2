import random
import copy
import pandas as pd
import pdb
import os

n_participants = 10
images_paths = os.listdir("images/")[:750]
random.shuffle(images_paths)
images_paths_150 = images_paths[:150]
images_paths = (images_paths_150 + images_paths_150 + images_paths_150 + images_paths_150 + images_paths_150)
num_runs = 12
trials_per_run = 75
for p_id in range(n_participants):
    random.seed(p_id)
    # make dirs
    participant_path = "conditions_files/participant" + str(p_id) + "_"
    random.shuffle(images_paths)
    current_image_list = []
    is_repeat_list = []
    run_num_list = []
    is_new_run_list = []
    is_blank_trial_list = []
    trial_index_list = []
    image_index = 0
    for run_num in range(num_runs):
        blank_trial_indices = [10,20,30,40,50] if run_num % 2 != 0 else [10,20,30,40,50,60]
        for trial_index in range(trials_per_run):
            run_num_list.append(run_num)
            trial_index_list.append(trial_index)
            if trial_index == (trials_per_run - 1):
                is_new_run_list.append(1)
            else:
                is_new_run_list.append(0)

            if trial_index <= 2 or trial_index >= 71 or trial_index in blank_trial_indices:
                current_image_list.append("images/blank.jpg")
                is_blank_trial_list.append(1)
                is_repeat_list.append(0)
            else:
                print("len(images_paths): ",len(images_paths))
                print("image_index: ",image_index)
                image_path = images_paths[image_index]
                if image_path in current_image_list:
                    is_repeat_list.append(1)
                else:
                    is_repeat_list.append(0)
                current_image_list.append("images/" + image_path)
                is_blank_trial_list.append(0)

                image_index += 1
    # output study and test
    output_dict = {"current_image": current_image_list,
                   "is_repeat": is_repeat_list,
                   "trial_index": trial_index_list,
                   "is_blank_trial":is_blank_trial_list,
                   "is_new_run": is_new_run_list,
                   "run_num": run_num_list}
    output_df = pd.DataFrame(output_dict)
    study_test_file_path = participant_path + ".csv"
    output_df.to_csv(study_test_file_path, index = False)
