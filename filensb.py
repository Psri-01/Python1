# Class Assignment = File_Name, File_Ext = docx, 17875 = Bytes
# File_Ext is nothing but Extention of the file 1 KB = 1024 Bytes
def file_size(file_info):
	file_name, file_ext, bytes = file_info
	return("{:.2f}".format(bytes / 1024))
print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
