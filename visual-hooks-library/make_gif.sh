#!/bin/bash
# make_gif.sh <in.mp4> <out.gif>  : first 3.0s, 12fps, 360px wide, optimized palette
in=$1; out=$2
ffmpeg -v error -y -t 3.0 -i "$in" -vf "fps=12,scale=360:-2:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" -loop 0 "$out"
