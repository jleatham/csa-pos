#!/usr/bin/python3
#----------#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3   #for work laptop

## crontab -e
## * * * * * /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 /Users/jleatham/Documents/Programming/Python/automation/POS/v3_pos_automation.py
## if it doesn't edit, type 'export EDITOR=VIM' in terminal
## make python file executable with chmod a+x
## Example crontab :
##    ###Every 10 minutes, check for new CSV by running filter python program
##    */10 * * * * /usr/bin/python3 /home/cisco/houston-pos/v9_POS_filter.py
##    ###first of every month, move CSV data to monthly csv, remove old POS files
##    0 0 1 * * /usr/bin/python3 /home/cisco/houston-pos/v9_POS_upload.py
##    ###makesure http-server is running after reboot
##    @reboot http-server /home/cisco/houston-pos/

from POS_automation import * #includes list of accounts and am names to search, as well as variables to import
global op_list


#################Start main



def process_new_csv_files():

    file_index = []    
    for file in glob.glob(home_file_path + '/*.[Cc][Ss][Vv]'):
        file_index.append(file)


    #create html table using csvtotable, installed on ubuntu server
    if file_index:
        #print("processing csv files")
        to_csv_from_json_v2(file_index,all_data_csv_filename, non_error_pos_data_filename)
        print ("all files processed")
        #to_html_v1(all_data_csv_filename,all_data_html_filename)
        create_area_reports(all_data_csv_filename,non_error_pos_data_filename,op_list)
        #create_monthly_csv(all_data_csv_filename) #moved to area_report function
        create_html_tables()

    else:
        #print('no files to process')
        pass
    return



def purge_logs_of_static():
    search_strings_to_remove = ["127.0.0.1",
                                "foundation.css",
                                "app.css",
                                "foundation-icons.css",
                                "jquery.js",
                                "what-input.js",
                                "app.js",
                                "favicon.ico",
                                "dynatable.css",
                                "foundation.js",
                                "dynatable.js",
                                "WARNING:csvtotable",
                                "Virtual scroll is enabled",
                                "SettingWithCopyWarning",
                                "slice from a DataFrame",
                                "See the caveats in the documentation",
                                "Try using .loc",
                                "] = EMAIL",
                                "No parser was explicitly specified",
                                "The code that caused this warning",
                                "BeautifulSoup",
                                "to this:",
                                "markup_type=",
                                "editdistance.bycython.eval",
                                "TypeError: object of type"
                                ]   
    f = open(home_file_path +"pos_log.out","r")
    lines = f.readlines()
    f.close()
    f = open(home_file_path +"pos_log.out","w")
    #print("starting loop")
    for line in lines:
        found_string = False
        for search_string in search_strings_to_remove:
            if search_string in line:
                found_string = True
        if not found_string:
            f.write(line)
    f.close()    


    ####################End main