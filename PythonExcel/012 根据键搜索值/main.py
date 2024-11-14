import load_file
import ini

key = input("key:")

json_data = load_file.load_json(ini.k_cheshi)
load_file.print_json(json_data,ini.k_cheshi,key)