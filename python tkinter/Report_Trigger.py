
import json
import pandas as pd
import streamlit as st
import os, string
import datetime


UTILITY_FILE = "USER_CONFIG.json"
CONFIG_DATA = dict()
CONFIG_DATA = dict()

PLACE_HOLDER_CONTAINER = st.empty()
CONFIGURATION_LAYOUT = st.empty()

def check_environment(drive = "PROD", **kaargs):
    return CONFIG_DATA.get('DRIVE_DATA').get(drive).get("DRIVE")
    

def read_file(file_path = "", file_type = "", path_prequel = "", **kaargs):
    file_source_path = path_prequel+file_path
    match file_type:
        case "csv":
            return pd.read_csv(file_source_path, sep=kaargs.get('sep'))
        case "json":
            return pd.read_json(file_source_path)
        case _:
            return None


def shared_drive_integrated(drive, **kaargs):
    #check path already exists for shared drive location
    return True


def execute_shared_drive_command(**kaargs):
    for env, env_details in CONFIG_DATA.get('DRIVE_DATA').items():
        if len((env_details.get('DRIVE'))) > 0 and shared_drive_integrated(env_details.get('DRIVE')):
            print(f"executing {env_details.get('COMMAND')}")


def configure_environments(env = 'PROD', check_env = 'TEST', drive_path = ''):
    CONFIG_DATA['DRIVE_DATA'][env]["DRIVE"] = drive_path
    with open("DRIVE_CONFIG.json", "w") as Drive_config:
        json.dump(CONFIG_DATA.get('DRIVE_DATA'), Drive_config)
    st.rerun()


def initialize_environments(**kaargs):
    with open("DRIVE_CONFIG.json") as Drive_config:
        CONFIG_DATA['DRIVE_DATA'] = json.load(Drive_config)
    st.session_state['CONFIG_DATA'] = CONFIG_DATA
    # for env, env_details in CONFIG_DATA.get('DRIVE_DATA').items():
    #     if len(check_environment(env_details.get('DRIVE'))) > 0:
    #         execute_shared_drive_command(env_details)
    

def fetchfile(env_path = '', **kaargs):
    with open(UTILITY_FILE) as configreader:
        # Has to be changed later for dynamic file paths
        # prequel_path = env_path
        prequel_path = ''
        CONFIG_PATHS_INFO = json.load(configreader)
        CONFIG_PATHS = CONFIG_PATHS_INFO.get("CONFIG_PATHS")
        for file_names, file_paths in CONFIG_PATHS.items():
            CONFIG_DATA[file_names] = read_file(file_paths, file_type=file_paths.split(".")[~0], path_prequel=prequel_path, sep = ',')
        st.session_state['CONFIG_DATA'] = CONFIG_DATA
        
        
def report_layout(**kaargs):
    with st.sidebar:
        report_list = list(CONFIG_DATA.get("REPORT_CONFIG").columns)
        box = st.multiselect("Select Your Reports", report_list)


def get_drive_list(**kaargs):
    available_drives = ['%s:' % d for d in string.ascii_uppercase if not os.path.exists('%s:' % d)]
    return available_drives


def drive_selection(**kaargs):
    drives_list = get_drive_list()
    selected_drive = st.selectbox("Configure one of the following drives", drives_list)
    return selected_drive


def load_environment(env = 'PROD', **kaargs):
    fetchfile(env_path = CONFIG_DATA.get('DRIVE_DATA').get(env).get("DRIVE"))
    st.session_state['LOADED_ENVIRONMENT'] = env
    load_environment_layout()


def report_checkbox_fields_instantiate(REPORT, values, report_name, attribute_name, actual_data_source, attribute_details, **kaargs):
    if "INCLUDE" in attribute_details:
        values = [val for val in values if val in attribute_details.get('INCLUDE')]

    if "EXCLUDE" in attribute_details:
        values = [val for val in values if val not in attribute_details.get('EXCLUDE')]

    REPORT[report_name][attribute_name] = {attribute_value_status:False for attribute_value_status in values}
    return REPORT


def update_data_source(actual_data_source, REPORT, report_name, filter_info, attribute_name_filter, **kaargs):
    if filter_info.get(attribute_name_filter).get('SELECTION_TYPE') != 'checkbox':
        return actual_data_source
    filtered_set = list()
    for attribute_name, attribute_values in REPORT.get(report_name).items():
        print(attribute_name, attribute_values)
        value_filter_set = list()
        for attribute_values, chosen in attribute_values.items():
            if chosen:
                value_filter_set.append(f"(actual_data_source['{filter_info.get(attribute_name).get('ATTRIBUTE')}'] == '{attribute_values}')")
                # updated_data_source = pd.concat([update_data_source, actual_data_source[actual_data_source[filter_info.get(attribute_name).get('ATTRIBUTE')] == attribute_values]])
        
        if len(value_filter_set) != 0:
            filtered_set.append(f"({' | '.join(value_filter_set)})")      
             
    if len(filtered_set) == 0:
        return actual_data_source
    else:
        return actual_data_source[eval(" & ".join(filtered_set))]



def prepare_report_layout(SELECTED_REPORT, report_name, REPORT_BUILDER, **kaargs):
    SELECTED_REPORT = CONFIG_DATA.get("REPORT_CONFIG").get(report_name)
    data_source_name = SELECTED_REPORT.pop('DATA_SOURCE')
    persistent_data_source = CONFIG_DATA.get(data_source_name)
    actual_data_source = persistent_data_source.copy()
    REPORT_BUILDER[report_name] = {}
    print("Fresh report")
    for filters, filter_info in SELECTED_REPORT.items():
        if type(filter_info) is not dict:            
            continue
        with st.form(f"Select the following Fields with {filters}"):

            for attributes_name, attribute_details in filter_info.items():
                st.subheader(attributes_name)  

                if attribute_details.get("SELECTION_TYPE") == 'checkbox':          
                    REPORT_BUILDER = report_checkbox_fields_instantiate(REPORT_BUILDER, actual_data_source[attribute_details.get("ATTRIBUTE")].unique(), report_name, attributes_name, actual_data_source, attribute_details)          
                    for attribute_values in list(REPORT_BUILDER.get(report_name).get(attributes_name).keys()):
                        REPORT_BUILDER[report_name][attributes_name][attribute_values] = st.checkbox(attribute_values, key=attribute_values)

                if attribute_details.get("SELECTION_TYPE") == 'multiselect':
                    set_values = list(actual_data_source[attribute_details.get("ATTRIBUTE")].unique())
                    REPORT_BUILDER[report_name][attributes_name] = st.multiselect("Select ",set_values)
                    print(REPORT_BUILDER[report_name][attributes_name])


                if attribute_details.get('SELECTION_TYPE') == 'date':
                    REPORT_BUILDER[report_name][attributes_name] = st.date_input("Select Date", datetime.datetime.now().date())
                   
                
            button = st.form_submit_button(f'SUBMIT {filters}')
            if button:
                st.info("Applied filter")
                st.session_state['REPORT_BUILDER'] = REPORT_BUILDER
                actual_data_source = update_data_source(actual_data_source=persistent_data_source, REPORT= REPORT_BUILDER, report_name=report_name, filter_info=filter_info, attribute_name_filter = attributes_name)
                # print(REPORT_BUILDER)
    report_submit = st.button(f"Submit {report_name}")
    # if report_submit:
    #     # print(REPORT_BUILDER)
    return REPORT_BUILDER



def load_environment_layout(**kaargs):

    with PLACE_HOLDER_CONTAINER.container():
        report_list = list(CONFIG_DATA.get("REPORT_CONFIG").columns)
        if "SELECTED_REPORT" not in st.session_state.keys():
            SELECTED_REPORT =  dict()
            REPORT_BUILDER = dict()
            st.session_state['SELECTED_REPORT'] = SELECTED_REPORT
            st.session_state['REPORT_BUILDER'] = REPORT_BUILDER
        else:
            SELECTED_REPORT = st.session_state['SELECTED_REPORT']
            REPORT_BUILDER = st.session_state['REPORT_BUILDER']

        report_name = st.selectbox("Select Your Reports", report_list, None)
        if report_name:
            REPORT_BUILDER = dict()
            SELECTED_REPORT =  dict()
            REPORT_BUILDER = prepare_report_layout(SELECTED_REPORT, report_name, REPORT_BUILDER)




def configlayout(**kaargs):
    
    with CONFIGURATION_LAYOUT.container():
        st.header(":blue[Configuration Window]")
        # test_container, prod_container = st.columns(2) 
        test_container = st.empty()
        prod_container = st.empty()
        environment_data = {
            "TEST":test_container,
            "PROD":prod_container
        }

        for env, container in environment_data.items():
            with container:
                st.header(f":blue[{env}]")
                # with st.container(height=200):
                with container.form(key = f"Configure {env} Drive"):
                    if len(check_environment(env)) == 0:
                        selected_drive = drive_selection()
                        submit_button = st.form_submit_button("Configure")
                        if submit_button:
                            configure_environments(env=env,drive_path=selected_drive)
                    else:
                        st.info(f"{env} ENVIRONMENT IS ALREADY CONFIGURED")
                        submit_button = st.form_submit_button("PROCEED")
                        if submit_button:
                            st.session_state['CONFIGURATION_PROCESS'] = True
                            load_environment(env=env)
                            st.rerun()
                                
        


if 'CONFIG_DATA' not in st.session_state.keys():   
    st.session_state['CONFIG_DATA'] = CONFIG_DATA
    initialize_environments()
else:
    CONFIG_DATA = st.session_state['CONFIG_DATA']

# if 'CONFIGURATION_PROCESS' in st.session_state.keys():
    


execute_shared_drive_command()

if 'CONFIGURATION_PROCESS' not in st.session_state.keys():
    configlayout()
else:
    print("Reloading after sumissions ")
    CONFIGURATION_LAYOUT.empty()
    load_environment(st.session_state['LOADED_ENVIRONMENT'])
