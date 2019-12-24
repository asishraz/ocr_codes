import sys 
import os
# inp =open(r'C:\Users\Asish.Asish\Desktop\pdf_extraction\Member_1\56B_member_1\sample.pdf','r') 
# out =open(r'C:\Users\Asish.Asish\Desktop\pdf_extraction\Member_1\56B_member_1\sample_2.pdf','w') 
# n=inp.read() 
# out.write(n)
# out.close()
# inp.close()

'''
pseudo code

1. take a file as an input inside the function
2. focus on the path, where the file is located
3. and print the document type

'''

# def file_present(absolute_path_or_relative_path):
# 	cwd = os.getcwd()
# 	root_dir = cwd[:cwd.rfind('/')+1]
# 	if 'B' in complete_path or absolute_path:
# 		print('this document belongs to B')
# 	elif 'F' in complete_path or absolute_path:
# 		print('this document belongs to F')
# 	elif 'G' in complete_path or absolute_path:
# 		print('this document belongs to G')
# 	else:
# 		print("new type of document")


# import os
# parent = r'C:\Users\Asish.Asish\Desktop\pdf_extraction'
# for i in os.listdir(parent):
# 	print(i)


# import os
# parent = r'C:\Users\Asish.Asish\Desktop\pdf_extraction'
# for i in os.listdir(parent):
#     for f in os.listdir(os.path.join(parent,i)):
#         print(f)
#         for m in os.listdir(os.path.join(parent,i,f)):
#             print('FileName:'+m+' ,Folder: '+f)

'''

def take_a_file(file_name):
	full_path = os.path.abspath(file_name)
	


file_func = take_a_file("sample.pdf")
'''
import os


# directory name should be given for the current working directory level
def change_dir(complete_path_or_dir_name):
	cwd = os.getcwd()
	root_dir = cwd[:cwd.rfind('/')+1]
	if '/' in complete_path_or_dir_name:
		os.chdir(complete_path_or_dir_name)
	else:
		os.chdir(root_dir + '%s' % dir_name)
	changed_cwd = os.getcwd()

	print('cwd=>',cwd)
	print('changed_cwd=>',changed_cwd)

# insert a correct absolute path , e.g :- /home/asish/Desktop/mediff_coding_challenge/A
change_dir(r'C:\Users\Asish.Asish\Desktop\pdf_extraction')
