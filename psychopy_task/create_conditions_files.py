import random
import copy
import pandas as pd
import pdb
import os

n_participants = 1000
no_repeat_images = os.listdir("face_triangles/")
for p_id in range(n_participants):
    random.seed(p_id)
    # make dirs
    participant_path = "conditions_files/participant" + str(p_id) + "_"
    random.shuffle(no_repeat_images)
    # output study and test
    output_dict = {"current_image": ["face_triangles/" + x for x in no_repeat_images],
                    "is_repeat": [0 for x in range(len(no_repeat_images))]}
    output_df = pd.DataFrame(output_dict)
    study_test_file_path = participant_path + ".csv"
    output_df.to_csv(study_test_file_path, index = False)
