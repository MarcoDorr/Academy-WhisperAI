import datetime
import os
import time
from random import shuffle
import shutil

import whisper
from cachier import cachier

from replacements import apply_replacements
from utils import format_float_to_time

import warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

""" 
    Converts all mp4-files of the folder 'videos' to English SRT-files in the folder 'srt_files'. So German to English and English to English.
    It moves all videos from the folder 'videos' to the folder 'videos_finished'.
    it uses the 'replacements.py' file to convert 'Central' to 'Xentral'.
    It uses the 'utils.py' for some format changes.
"""

@cachier(stale_after=datetime.timedelta(days=100))
def whisper_result_cached(path, language: str, do_translation=True):
    """bla"""
    model = whisper.load_model('large')
    print("Starting transcription...")
    result = model.transcribe(
        audio=path,
        language=language,
        verbose=True,
        task='translate' if do_translation else 'transcribe',
    )
    return result


def segments_to_srt_format(segment):
    """bla"""

    text = segment['text']
    segment_id = segment['id'] + 1

    temp = f"{segment_id}\n{format_float_to_time(segment['start'])} --> " \
           f"{format_float_to_time(segment['end'])}\n{text[1:] if text[0] == ' ' else text}\n\n"
    return temp


def write_captions_to_srt_file(vid_name,
                               do_translation: bool,
                               source_folder: str,
                               result_folder: str):

    if vid_name[-4:] != '.mp4': # Überprüfung der Dateierweiterung auf .mp4
        print(f"Skipping {vid_name}")
        return
    vid_path = source_folder + vid_name
    result = whisper_result_cached(vid_path, language='de', do_translation=do_translation)
    language_suffix = "_EN" if do_translation else "_DE"
    srt_filename = f'{vid_name[:-4]}{language_suffix}.srt'
    srt_filepath = f'{result_folder}{srt_filename}'
    source_filepath = f'{source_folder}{vid_name}'
    destination_filepath = f'../videos_finished/{vid_name}'
    with open(srt_filepath, mode='w', encoding='utf-8') as file_out:
        for segment in result['segments']:
            file_out.write(apply_replacements(segments_to_srt_format(segment)))
    shutil.move(source_filepath, destination_filepath)


if __name__ == '__main__':
    start_time = time.time()
    source_folder = '../videos/'
    dir_list = os.listdir(source_folder)
    shuffle(dir_list)
    for d in dir_list:
        print('#' * 50)
        print(d, '\n')
        write_captions_to_srt_file(vid_name=d,
                                   do_translation=True,
                                   source_folder=source_folder,
                                   result_folder='../srt_files/')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {int(elapsed_time // 60)}:{int(elapsed_time % 60):02d}")
