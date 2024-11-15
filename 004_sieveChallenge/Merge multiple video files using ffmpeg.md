```bash
ffmpeg -f concat -i videos.txt -c copy output8.mp4
```
(ref: [Merge videos using FFmpeg concat — Shotstack](https://shotstack.io/learn/use-ffmpeg-to-concatenate-video/)) 

- first create a text file with a list of videos according to the order you want to join. Below is an example file `videos.txt` 
```bash
# videos.txt
file 'input1.mp4'
file 'input2.mp4'
file 'input3.mp4'
```

OR:

```bash
ffmpeg -i "concat:input1.mp4|input2.mp4|input3.mp4|input4.mp4" -c copy output10.mp4
```
