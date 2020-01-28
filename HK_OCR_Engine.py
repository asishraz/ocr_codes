
import re

import asyncio
import pandas as pd
import os
import datetime
import shutil
from xlrd import open_workbook

from Data_Extrcact.OCR_Engine_Data_Extract_56B import processDataExtraction_56B
from Data_Extrcact.OCR_Engine_Data_Extract_56F import processDataExtraction_56F
from Data_Extrcact.OCR_Engine_Data_Extract_56G import processDataExtraction_56G

cwd = os.getcwd()
workflow_Excel_path = os.path.join(cwd, "Config.xlsx")

workbook = open_workbook(workflow_Excel_path)
sheet = workbook.sheet_by_index(0)
final_output_path = sheet.cell_value(2, 1)

movdir= sheet.cell_value(0, 1)
basedir = sheet.cell_value(1, 1)


#         return sheet.cell_value(1, 1)


response_list = []

tasks = ['56B', '56F', '56G']
async def get_nlp_task(nlp_task):


    if nlp_task == '56B':
            print("56B")
            res_56B = processDataExtraction_56B()
            response_list.append(res_56B)

    elif nlp_task == '56F':
            print("56F")
            res_56F = processDataExtraction_56F()
            response_list.append(res_56F)

    else:
        print("56G")
        res_56G = processDataExtraction_56G()
        response_list.append(res_56G)

    return response_list


async def call_nlp_task(task):
    response = await get_nlp_task(task)

    return response


def OCR_parallel_processing():

        res_list = []
        response_data = ''

        futures = [call_nlp_task(task) for task in tasks]
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        res_datas, b = loop.run_until_complete(asyncio.wait(futures))
        if res_datas:
            for res_data in res_datas:
                res_list.append(res_data.result())

        loop.close()

        if res_list:
            response_data = res_list[-1]
            if response_data:
                result=pd.concat(response_data, axis=0, join='inner', ignore_index=True, keys=None,
                          levels=None, names=None, verify_integrity=False, copy=True)
            timestamp = datetime.datetime.now()
            dt = str(timestamp.year) + str(timestamp.month) + str(timestamp.day) + str(timestamp.hour) + str(
                timestamp.minute)
            newname = 'HK_IR_' + str(dt) + '_Output.xlsx'
            current_directory = os.getcwd()

            # output_path = os.path.join(current_directory + '/Output_File', newname)
            output_path = os.path.join(final_output_path + '\\', newname)
            print("Generate output excel to ", output_path)
            result.to_excel(output_path, index=False)



            # Walk through all files in the directory that contains the files to copy
            root_src_dir = sheet.cell_value(0, 1)
            root_dst_dir = sheet.cell_value(1, 1)
            try:
                for src_dir, dirs, files in os.walk(root_src_dir):
                    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
                    if not os.path.exists(dst_dir):
                        os.makedirs(dst_dir)
                    for file_ in files:
                        src_file = os.path.join(src_dir, file_)
                        dst_file = os.path.join(dst_dir, file_)
                        if os.path.exists(dst_file):
                            # in case of the src and dst are the same file
                            if os.path.samefile(src_file, dst_file):
                                continue
                            os.remove(dst_file)
                        shutil.move(src_file, dst_dir)
            except:
                print("Error in file Moving")



OCR_parallel_processing()