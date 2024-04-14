import os
import sys
import logging
from datetime import datetime
from glob import glob
import re 

def setup_logging():
     log_directory = "logs"
     if not os.path.exists(log_directory):
          os.makedirs(log_directory)

     # Naming log files with a timestamp
     timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
     log_filename = f"{log_directory}/run_{timestamp}.log"

     # Setting up logging
     logging.basicConfig(filename=log_filename,
                         level=logging.DEBUG,
                         format='%(asctime)s - %(levelname)s - %(message)s')

     # Clean up old logs
     clean_old_logs(log_directory)

     return log_filename

def clean_old_logs(log_directory, keep=10):
     # Get all log files
     logs = sorted(glob(f"{log_directory}/run_*.log"))
     # Remove logs if there are more than 'keep' files
     if len(logs) > keep:
          for log in logs[:-keep]:
               try:
                    os.remove(log)
                    logging.info(f"Removed old log file: {log}")
               except Exception as e:
                    logging.error(f"Failed to remove old log file {log}: {e}")
                    
def process_emoji(code, qualification, symbol, version, friendly_name, variant, group, subgroup):
     # Further processing can be added here as needed
     try:
          emoji_char = chr(int(code.split()[0], 16))
          emoji_data = {
               'code': code,
               'qualification': qualification,
               'version': version,
               'variant': variant,
               'emoji': emoji_char,
               'friendly_name': friendly_name,
               'group': group,
               'subgroup': subgroup
          }
          return emoji_data
     except ValueError:
          logging.error(f"Failed to convert code to character: {code}")
          return None
     
def parse_emoji_data(file_path):
     emojis = []
     setup_logging()
     try:
          with open(file_path, 'r', encoding='utf-8') as file:
               current_group = None
               current_subgroup = None
               for line_number, line in enumerate(file, 1):
                    line = line.strip()
                    if "# group:" in line:
                         current_group = line.split("# group:")[1].strip()
                         logging.info(f"🔄 Changed group: {current_group}")
                    elif "# subgroup:" in line:
                         current_subgroup = line.split("# subgroup:")[1].strip()
                         logging.info(f"↪️ Changed subgroup: {current_subgroup}")
                    elif ";" in line and not line.startswith('#'):

                         stripped = re.sub(r'\s{2,}', ' ', line)
                         pattern = r'([^;]*?)\s*;\s*([^#]*?)\s*#\s*(\S+)\s+(\S+)\s+(.*)'
                         formatted_string = re.sub(pattern, r'\1,\2,\3,\4,\5', stripped)
                         parts_array = formatted_string.split(',')
                         # Check for colon in the description and adjust skin tone
                         # Adjust skin tone extraction
                         description, skin_tone = (parts_array[4].split(':', 1) + ['default'])[:2]
                         parts_array[4] = description.strip()
                         parts_array.append(skin_tone.replace(' skin tone', '').strip())
                         # if ':' in parts_array[4]:
                         #      description, skin_tone = parts_array[4].split(':', 1)
                         #      parts_array[4] = description.strip()
                         #      parts_array.append(skin_tone.replace(' skin tone', '').strip())
                              
                         # else:
                         #      parts_array.append('default')
          
                         logging.info(parts_array)
                         
                         if len(parts_array) == 6:
                              emoji = process_emoji(*parts_array[:5], parts_array[5], current_group, current_subgroup)
                              emojis.append(emoji) if emoji else logging.error(f"Failed to process emoji in line {line_number}: {line}")
                         else:
                              logging.error(f"Insufficient data parts in line {line_number}: {line}")
     except FileNotFoundError:
          logging.error(f"Error: The file '{file_path}' was not found.")
          return []
     except Exception as e:
          logging.error(f"Unexpected error while reading the file: {e}")
          return []

     return emojis


     # Example usage assuming file path
if __name__ == "__main__":
     log_filename = setup_logging()
     logging.info("Starting emoji parsing")
     emoji_list = parse_emoji_data('emoji-test.txt')
     for emoji in emoji_list:
          print(emoji)
     logging.info("Completed emoji parsing")
     logging.info(f"Logs are saved in {log_filename}")
