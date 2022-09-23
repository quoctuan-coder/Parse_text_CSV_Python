#! /usr/bin/python -B
# -*- coding: utf-8 -*-

import sys
import os
import re

path_in_file = "log_4th_G2L_004"
path_out_file_clear = path_in_file + "clear_tc.txt"
path_out_file_group = path_in_file + "group_tc.txt"
path_out_file_remove= path_in_file + "remove_tc.txt"

lines = []
if os.path.isfile(path_in_file):
    with open(path_in_file) as file:
        lines = file.readlines()
else:
    sys.exit(1)

outfile_clear = open(path_out_file_clear,'w')
outfile_group = open(path_out_file_group,'w')

flag_start = False
flag_end = False
flag_record_group = False
ind_start = 0
ind_end = 0

tc = []
group_1 = "page https://web-platform.test:8443/testharness_runner.html failed"
group_2 = "pixels different, maximum difference per channel"
group_3 ="Test TIMEOUT"
other_tc = "group_other_tc"

group_tc = [group_1,group_2,group_3,other_tc]
dict_group_tc = {}
for group in group_tc:
    dict_group_tc[group] = []


# 1774 
for (cnt, line) in enumerate(lines):
    start_tc = re.search("test_start",line)
    end_tc = re.search("test_exit",line)
     
    if start_tc is not None:
        flag_record_group = True
        ind_start = cnt
        flag_start = True
        tc_name = str(start_tc.string)[12:]
        if (tc_name[-2:-1] == "]"):
            tc_name = tc_name[:-2] + "\n"
        
    elif end_tc is not None:
        ind_end = cnt
        flag_end = True
        flag_start = False
    
    else:
        pass

    if (flag_start):
        
        outfile_clear.write(line)

        if (flag_record_group):
            
            for group in group_tc:
                s_group = re.search(group,line)
                if (s_group is not None):
                    dict_group_tc[group].append(tc_name)
                    flag_record_group = False
              
        flag_end = False

    elif (flag_end):
        outfile_clear.write(line)

        if (flag_record_group):
            dict_group_tc[other_tc].append(tc_name)

        flag_start = False
        flag_end = False
        flag_record_group = False
        
        
    else:
        pass

for group in group_tc:
    outfile_group.write("{}\n".format(group))
    for item in dict_group_tc[group]:
        outfile_group.write("{}".format(item))
    
outfile_clear.close()
outfile_group.close()
        
    
