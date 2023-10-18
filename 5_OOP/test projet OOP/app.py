from components.my_module import add, mul, balegoum
from components.data_sc import csv_clean
from components.create_model import create_model
from components.plot_the_beauty_of_ML import plotting
import numpy as np
import os

print(add(3,5))
print(mul(5,5))

print(np.arange(5))

print(balegoum('Balegoum'))

#Calling the cleaning csv module
DIR_PATH = os.path.abspath(os.path.dirname(__file__))
# print(DIR_PATH)
input_filepath = os.path.join(DIR_PATH,'data\\titanic.csv')
# print(filepath)
clean_file_path = csv_clean(input_filepath)
# print(os.path.dirname(filepath))

#Calling the create_model module
save_files_path = os.path.join(DIR_PATH,'ML\\')
create_model(clean_file_path, save_files_path)

#Calling plotting module 
image_save_path = os.path.join(DIR_PATH,'saved_plots\\')
plotting(clean_file_path, save_files_path, image_save_path)

