# ImageRecognition

:alien:
:alien:
:alien:
:alien:
:alien:

## Results

| # | model | options | dataset | split | # of pics |time to train | weight file | mAP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | mrcnn | epoch 30, layer = head | Google 3D, Google 2D | 80/20 | 202 | xx | link | 0.7739 |
| 02 | mrcnn | epoch 30, layer = head  | CARPK | 80/20 | 1.448 | 2h 21m | link | 0.8446 | 
| 03 | mrcnn | epoch 30, layer = head  | PUCPR+ | 80/20 | 125 | xx | link | 0.3353 |
| 04 | mrcnn | epoch 30, layer = head  | COWC | 80/20 | 1.683 | 53 min | link | 0.7831 |
| 05 | mrcnn | epoch 30, layer = head  | Google, CARPK, COWC | 80/20 | 3.333 | xx | link | 0.7729 |
| 06 | mrcnn | epoch 200, layer = head  | Google, CARPK, COWC | 80/20 | 3.333 | xx | link | 0.8015 |
| 07 | mrcnn | epoch 30, layer = all  | Google, CARPK, COWC | 80/20 | 3.333 | xx | link | 0.7831 |
| 08 | mrcnn | epoch 30, layer = 3+  | Google, CARPK, COWC | 80/20 | 3.333 | xx | link | 0.8278 |
| 09 | mrcnn | epoch 30, layer = 4+  | Google, CARPK, COWC | 80/20 | 3.333 | xx | link | 0.8573 |
| 10 | mrcnn | epoch 30, layer = 5+  | Google, CARPK, COWC | 80/20 | 3.333 | xx | link | 0.7511 |
| 08 | xxxx | xx | xx | xx | xx | xx | link | xx |
