"""
bli bla
"""
import datetime
import os
from random import shuffle

import whisper
from cachier import cachier

from replacements import apply_replacements
from utils import format_float_to_time


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

    """
    bli bla
    """
    vid_path = source_folder + vid_name
    result = whisper_result_cached(vid_path, language='de', do_translation=do_translation)
    language_suffix = "_EN" if do_translation else "_DE"
    with open(
            f'{result_folder}{vid_name[:-4]}{language_suffix}.srt',
            mode='w',
            encoding='utf-8') as file_out:
        for segment in result['segments']:
            file_out.write(apply_replacements(segments_to_srt_format(segment)))


if __name__ == '__main__':
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
