# academy_captions_clean

### What is this repository for?

The team for the Xentral academy needed a way to get reliable subtitles and translations for their videos.
Previous options for this had such a low accuracy of the results that significant manual editing of the texts was necessary.
This repository provides a captions and translations into english of high quality and completely free of charge.

### How do I use it?

In the repository put the mp4-files in the folder named `videos` to process. Then run the script 'main'.
The results appear as [str-files](https://docs.fileformat.com/video/srt/) in the folder `srt_files`.
As these files are just couple 100 lines of plain text, they are pretty small. These files are ready to use.
![image](https://user-images.githubusercontent.com/115226411/215190980-b448ca16-40e1-44a2-8c74-0d8eac179c1c.png)

Processing 1 hour of video takes ~45minutes, so preferably let the script run over night with power connected. 

### How does it work behind the hood? :flushed:
- Extract audio from video
- Run audio through a [neural network](https://arxiv.org/pdf/2212.04356.pdf) from a project named *whisper* that generates text with timestamps. 
In case you run the script the first time, the neural network needs to be downloaded first, which may take a while, as it is ~3GB. The neural network is Transformer, which are for example also used in ChatGP**T**.
- The output of the network as post-processed (for example replacing "central" with "Xentral", as the network doesn't know about Xentral yet :unamused:),
then a file in the srt-format is written.
<img src="https://raw.githubusercontent.com/openai/whisper/main/approach.png" alt="drawing" width="500"/>


### What setup do I need to use it?

The setup-process is work-in-progress and will potentially be simplified in the future. For now, feel free to message me (*Moritz Groß*) on Slack.

Stuff needed:
- ffmpeg (easiest to install with homebrew, which in case you don't have it, can be found [here](https://brew.sh/)
- Python
- In Python, you need the following packages via `pip`
  - cachier (https://pypi.org/project/cachier/)
  - whisper (https://github.com/openai/whisper)
