#!/bin/bash 

youtube-dl -i --dateafter $(date -d "4 days ago" +"%Y%m%d") __play_list__

ex.

youtube-dl -i --dateafter $(date -d "4 days ago" +"%Y%m%d") https://www.youtube.com/watch?v=QH2-TGUlwu4
