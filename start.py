import argparse
import pexpect

# read filename from args
parser = argparse.ArgumentParser(description = 'Basic launcher for ESEPP. Reads parameters from .ini config file.')
parser.add_argument('config_file')
args = parser.parse_args()
filename = args.config_file

# create a dictionary with parameters {'param_name': value}
parameters = {}

# open file
with open(filename, 'r') as file:
    # read raw text
    text = file.read()
    # split into lines
    lines = text.split('\n')
    for line in lines:
        # if not a comment line
        if line.strip() and line.strip()[0] != '#':
            key, value = [i.strip() for i in line.split('=')]
            parameters[key] = value

# full list of available parameters in the original ESEPP order
param_list = ['lepton_type', 'rosenbluth', 'proton_structure', 'bremsstrahlung', 'vacuum_polarization', 'two_photon', 'theta', 'min_theta', 'max_theta', 'phi', 'min_phi', 'max_phi', 'num_events', 'format', 'prefix']

# remove min_theta and max_theta if full range was selected
if parameters['theta'] == 1:
    param_list.pop(7)
    param_list.pop(7)

child = pexpect.spawn('./esepp')
for param in param_list:
    child.sendline(parameters[param])
