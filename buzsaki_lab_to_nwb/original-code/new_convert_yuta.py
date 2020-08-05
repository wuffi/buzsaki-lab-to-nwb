
from BuzsakiLabNWBConverter import BuzsakiLabNWBConverter
from datetime import datetime
from dateutil.parser import parse as dateparse

# usage
input_file_schema = BuzsakiLabNWBConverter.get_input_schema()

# construct input_args dict according to input schema, e.g.: 
input_args = {'NeuroscopeRecording': {'file_path': "D:/BuzsakiData/SenzaiY/YutaMouse41/YutaMouse41-150903/YutaMouse41-150903.dat"},
              'NeuroscopeSorting': {'file_path': "D:/BuzsakiData/SenzaiY/YutaMouse41/YutaMouse41-150903"}}

buzlab_converter = BuzsakiLabNWBConverter(**input_args)

expt_json_schema = buzlab_converter.get_metadata_schema()

# construct metadata_dict according to expt_json_schema, e.g. 
metadata_dict = {
    'NWBFile': {
            'session_description': 'mouse in open exploration and theta maze',
            'identifier': 'YutaMouse41-150903',
            'session_start_time': (dateparse('150903', yearfirst=True)).astimezone(),
            'file_create_date': datetime.now().astimezone(),
            'experimenter': 'Yuta Senzai',
            'session_id': 'YutaMouse41-150903',
            'institution': 'NYU',
            'lab': 'Buzsaki',
            'related_publications': 'DOI:10.1016/j.neuron.2016.12.011'
    },
    'Subject': {
            'subject_id': 'YutaMouse41',
            'age': '346 days',
            'genotype': 'POMC-Cre::Arch',
            'species': 'mouse' # should be Mus musculus?
    },
    'neuroscope': {
        'Device': {
            'name': 'implant',
            'description': 'no description'
        },
        'ElectrodeGroup': {
            'name': 'electrodes',
            'description': 'no description'
        },        
        'ElectricalSeries': {
            'name': 'ElectricalSeries',
            'description': 'no description'
        }
    }
}

nwbfile_path = 'D:/BuzsakiData/SenzaiY/YutaMouse41/YutaMouse41-150903_new_converter.nwb'
buzlab_converter.run_conversion(nwbfile_path, metadata_dict, stub_test=True)
