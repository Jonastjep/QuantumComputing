# This file stores the values from the grover iteration
import numpy as np

M = 2**17

snrs_ = np.load('SNRs_signal_spins.npy')
if len(snrs_)>M:
    snrs = snrs_[::len(snrs_)//M]
    if len(snrs)>M:
        snrs = snrs[:M]
    elif len(snrs)<M:
        snrs__ = snrs_[1:][::len(snrs)//M][:M-len(snrs)]
        snrs = np.concatenate((snrs,snrs__))
else:
    snrs = snrs_

nb_break = 2**4 #size of blocks
broken_snrs = [snrs[i:i + nb_break] for i in range(0, len(snrs), nb_break)]
dict_val = {
0:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 469}], # Indices 0 to 16
1:[], # Indices 16 to 32
2:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 487}], # Indices 32 to 48
3:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 484}], # Indices 48 to 64
4:[], # Indices 64 to 80
5:[], # Indices 80 to 96
6:[], # Indices 96 to 112
7:[], # Indices 112 to 128
8:[], # Indices 128 to 144
9:[], # Indices 144 to 160
10:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 427}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 380}], # Indices 160 to 176
11:[], # Indices 176 to 192
12:[], # Indices 192 to 208
13:[], # Indices 208 to 224
14:[], # Indices 224 to 240
15:[], # Indices 240 to 256
16:[], # Indices 256 to 272
17:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 477}], # Indices 272 to 288
18:[], # Indices 288 to 304
19:[], # Indices 304 to 320
20:[], # Indices 320 to 336
21:[], # Indices 336 to 352
22:[], # Indices 352 to 368
23:[], # Indices 368 to 384
24:[], # Indices 384 to 400
25:[], # Indices 400 to 416
26:[], # Indices 416 to 432
27:[], # Indices 432 to 448
28:[], # Indices 448 to 464
29:[], # Indices 464 to 480
30:[], # Indices 480 to 496
31:[], # Indices 496 to 512
32:[], # Indices 512 to 528
33:[], # Indices 528 to 544
34:[], # Indices 544 to 560
35:[], # Indices 560 to 576
36:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 500}], # Indices 576 to 592
37:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 482}], # Indices 592 to 608
38:[], # Indices 608 to 624
39:[], # Indices 624 to 640
40:[], # Indices 640 to 656
41:[], # Indices 656 to 672
42:[], # Indices 672 to 688
43:[], # Indices 688 to 704
44:[], # Indices 704 to 720
45:[], # Indices 720 to 736
46:[], # Indices 736 to 752
47:[], # Indices 752 to 768
48:[], # Indices 768 to 784
49:[], # Indices 784 to 800
50:[], # Indices 800 to 816
51:[], # Indices 816 to 832
52:[], # Indices 832 to 848
53:[], # Indices 848 to 864
54:[], # Indices 864 to 880
55:[], # Indices 880 to 896
56:[], # Indices 896 to 912
57:[{'index_dec': 2, 'index_bin': '0010', 'val': 13, 'counts': 505}], # Indices 912 to 928
58:[], # Indices 928 to 944
59:[], # Indices 944 to 960
60:[], # Indices 960 to 976
61:[], # Indices 976 to 992
62:[], # Indices 992 to 1008
63:[], # Indices 1008 to 1024
64:[], # Indices 1024 to 1040
65:[], # Indices 1040 to 1056
66:[], # Indices 1056 to 1072
67:[], # Indices 1072 to 1088
68:[], # Indices 1088 to 1104
69:[], # Indices 1104 to 1120
70:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 313}, {'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 326}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 336}], # Indices 1120 to 1136
71:[], # Indices 1136 to 1152
72:[], # Indices 1152 to 1168
73:[], # Indices 1168 to 1184
74:[], # Indices 1184 to 1200
75:[], # Indices 1200 to 1216
76:[], # Indices 1216 to 1232
77:[], # Indices 1232 to 1248
78:[], # Indices 1248 to 1264
79:[], # Indices 1264 to 1280
80:[], # Indices 1280 to 1296
81:[], # Indices 1296 to 1312
82:[], # Indices 1312 to 1328
83:[], # Indices 1328 to 1344
84:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 358}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 305}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 315}], # Indices 1344 to 1360
85:[], # Indices 1360 to 1376
86:[], # Indices 1376 to 1392
87:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 474}], # Indices 1392 to 1408
88:[], # Indices 1408 to 1424
89:[], # Indices 1424 to 1440
90:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 473}], # Indices 1440 to 1456
91:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 460}], # Indices 1456 to 1472
92:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 492}], # Indices 1472 to 1488
93:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 452}], # Indices 1488 to 1504
94:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 494}], # Indices 1504 to 1520
95:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 484}], # Indices 1520 to 1536
96:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 326}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 333}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 295}], # Indices 1536 to 1552
97:[], # Indices 1552 to 1568
98:[], # Indices 1568 to 1584
99:[], # Indices 1584 to 1600
100:[], # Indices 1600 to 1616
101:[], # Indices 1616 to 1632
102:[], # Indices 1632 to 1648
103:[], # Indices 1648 to 1664
104:[], # Indices 1664 to 1680
105:[], # Indices 1680 to 1696
106:[], # Indices 1696 to 1712
107:[], # Indices 1712 to 1728
108:[], # Indices 1728 to 1744
109:[], # Indices 1744 to 1760
110:[], # Indices 1760 to 1776
111:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 483}], # Indices 1776 to 1792
112:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 384}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 395}], # Indices 1792 to 1808
113:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 507}], # Indices 1808 to 1824
114:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 244}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 266}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 256}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 258}], # Indices 1824 to 1840
115:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 330}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 311}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 331}], # Indices 1840 to 1856
116:[], # Indices 1856 to 1872
117:[], # Indices 1872 to 1888
118:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 489}], # Indices 1888 to 1904
119:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 421}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 368}], # Indices 1904 to 1920
120:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 406}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 405}], # Indices 1920 to 1936
121:[], # Indices 1936 to 1952
122:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 479}], # Indices 1952 to 1968
123:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 460}], # Indices 1968 to 1984
124:[], # Indices 1984 to 2000
125:[], # Indices 2000 to 2016
126:[], # Indices 2016 to 2032
127:[], # Indices 2032 to 2048
128:[], # Indices 2048 to 2064
129:[], # Indices 2064 to 2080
130:[], # Indices 2080 to 2096
131:[], # Indices 2096 to 2112
132:[], # Indices 2112 to 2128
133:[], # Indices 2128 to 2144
134:[], # Indices 2144 to 2160
135:[], # Indices 2160 to 2176
136:[], # Indices 2176 to 2192
137:[], # Indices 2192 to 2208
138:[], # Indices 2208 to 2224
139:[], # Indices 2224 to 2240
140:[], # Indices 2240 to 2256
141:[], # Indices 2256 to 2272
142:[], # Indices 2272 to 2288
143:[], # Indices 2288 to 2304
144:[], # Indices 2304 to 2320
145:[], # Indices 2320 to 2336
146:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 390}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 393}], # Indices 2336 to 2352
147:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 455}], # Indices 2352 to 2368
148:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 300}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 328}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 341}], # Indices 2368 to 2384
149:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 508}], # Indices 2384 to 2400
150:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 482}], # Indices 2400 to 2416
151:[{'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 482}], # Indices 2416 to 2432
152:[], # Indices 2432 to 2448
153:[], # Indices 2448 to 2464
154:[], # Indices 2464 to 2480
155:[], # Indices 2480 to 2496
156:[], # Indices 2496 to 2512
157:[], # Indices 2512 to 2528
158:[], # Indices 2528 to 2544
159:[], # Indices 2544 to 2560
160:[], # Indices 2560 to 2576
161:[], # Indices 2576 to 2592
162:[], # Indices 2592 to 2608
163:[], # Indices 2608 to 2624
164:[], # Indices 2624 to 2640
165:[], # Indices 2640 to 2656
166:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 486}], # Indices 2656 to 2672
167:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 469}], # Indices 2672 to 2688
168:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 494}], # Indices 2688 to 2704
169:[], # Indices 2704 to 2720
170:[], # Indices 2720 to 2736
171:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 472}], # Indices 2736 to 2752
172:[], # Indices 2752 to 2768
173:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 503}], # Indices 2768 to 2784
174:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 477}], # Indices 2784 to 2800
175:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 500}], # Indices 2800 to 2816
176:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 381}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 422}], # Indices 2816 to 2832
177:[{'index_dec': 6, 'index_bin': '0110', 'val': 13, 'counts': 403}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 428}], # Indices 2832 to 2848
178:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 487}], # Indices 2848 to 2864
179:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 487}], # Indices 2864 to 2880
180:[{'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 416}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 397}], # Indices 2880 to 2896
181:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 490}], # Indices 2896 to 2912
182:[], # Indices 2912 to 2928
183:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 484}], # Indices 2928 to 2944
184:[], # Indices 2944 to 2960
185:[], # Indices 2960 to 2976
186:[], # Indices 2976 to 2992
187:[], # Indices 2992 to 3008
188:[], # Indices 3008 to 3024
189:[], # Indices 3024 to 3040
190:[], # Indices 3040 to 3056
191:[], # Indices 3056 to 3072
192:[], # Indices 3072 to 3088
193:[], # Indices 3088 to 3104
194:[], # Indices 3104 to 3120
195:[], # Indices 3120 to 3136
196:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 485}], # Indices 3136 to 3152
197:[], # Indices 3152 to 3168
198:[], # Indices 3168 to 3184
199:[], # Indices 3184 to 3200
200:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 491}], # Indices 3200 to 3216
201:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 310}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 306}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 358}], # Indices 3216 to 3232
202:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 481}], # Indices 3232 to 3248
203:[{'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 492}], # Indices 3248 to 3264
204:[{'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 480}], # Indices 3264 to 3280
205:[], # Indices 3280 to 3296
206:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 323}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 365}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 291}], # Indices 3296 to 3312
207:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 482}], # Indices 3312 to 3328
208:[], # Indices 3328 to 3344
209:[], # Indices 3344 to 3360
210:[], # Indices 3360 to 3376
211:[], # Indices 3376 to 3392
212:[], # Indices 3392 to 3408
213:[], # Indices 3408 to 3424
214:[], # Indices 3424 to 3440
215:[], # Indices 3440 to 3456
216:[], # Indices 3456 to 3472
217:[], # Indices 3472 to 3488
218:[], # Indices 3488 to 3504
219:[], # Indices 3504 to 3520
220:[], # Indices 3520 to 3536
221:[], # Indices 3536 to 3552
222:[], # Indices 3552 to 3568
223:[], # Indices 3568 to 3584
224:[], # Indices 3584 to 3600
225:[], # Indices 3600 to 3616
226:[], # Indices 3616 to 3632
227:[], # Indices 3632 to 3648
228:[], # Indices 3648 to 3664
229:[], # Indices 3664 to 3680
230:[], # Indices 3680 to 3696
231:[], # Indices 3696 to 3712
232:[], # Indices 3712 to 3728
233:[], # Indices 3728 to 3744
234:[], # Indices 3744 to 3760
235:[], # Indices 3760 to 3776
236:[], # Indices 3776 to 3792
237:[], # Indices 3792 to 3808
238:[], # Indices 3808 to 3824
239:[], # Indices 3824 to 3840
240:[], # Indices 3840 to 3856
241:[], # Indices 3856 to 3872
242:[], # Indices 3872 to 3888
243:[], # Indices 3888 to 3904
244:[], # Indices 3904 to 3920
245:[], # Indices 3920 to 3936
246:[], # Indices 3936 to 3952
247:[], # Indices 3952 to 3968
248:[], # Indices 3968 to 3984
249:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 314}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 342}, {'index_dec': 7, 'index_bin': '0111', 'val': 14, 'counts': 323}], # Indices 3984 to 4000
250:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 411}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 399}], # Indices 4000 to 4016
251:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 420}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 381}], # Indices 4016 to 4032
252:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 319}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 313}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 346}], # Indices 4032 to 4048
253:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 193}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 215}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 195}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 176}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 191}], # Indices 4048 to 4064
254:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 268}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 273}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 247}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 236}], # Indices 4064 to 4080
255:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 371}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 415}], # Indices 4080 to 4096
256:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 259}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 275}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 254}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 236}], # Indices 4096 to 4112
257:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 328}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 334}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 319}], # Indices 4112 to 4128
258:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 378}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 420}], # Indices 4128 to 4144
259:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 508}], # Indices 4144 to 4160
260:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 493}], # Indices 4160 to 4176
261:[], # Indices 4176 to 4192
262:[], # Indices 4192 to 4208
263:[], # Indices 4208 to 4224
264:[], # Indices 4224 to 4240
265:[], # Indices 4240 to 4256
266:[], # Indices 4256 to 4272
267:[], # Indices 4272 to 4288
268:[], # Indices 4288 to 4304
269:[], # Indices 4304 to 4320
270:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 332}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 328}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 322}], # Indices 4320 to 4336
271:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 470}], # Indices 4336 to 4352
272:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 470}], # Indices 4352 to 4368
273:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 499}], # Indices 4368 to 4384
274:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 489}], # Indices 4384 to 4400
275:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 477}], # Indices 4400 to 4416
276:[], # Indices 4416 to 4432
277:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 411}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 368}], # Indices 4432 to 4448
278:[], # Indices 4448 to 4464
279:[{'index_dec': 8, 'index_bin': '1000', 'val': 12, 'counts': 448}], # Indices 4464 to 4480
280:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 447}], # Indices 4480 to 4496
281:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 391}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 401}], # Indices 4496 to 4512
282:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 316}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 330}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 317}], # Indices 4512 to 4528
283:[{'index_dec': 14, 'index_bin': '1110', 'val': 16, 'counts': 474}], # Indices 4528 to 4544
284:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 328}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 328}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 315}], # Indices 4544 to 4560
285:[{'index_dec': 1, 'index_bin': '0001', 'val': 13, 'counts': 344}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 324}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 316}], # Indices 4560 to 4576
286:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 461}], # Indices 4576 to 4592
287:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 472}], # Indices 4592 to 4608
288:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 374}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 407}], # Indices 4608 to 4624
289:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 343}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 311}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 312}], # Indices 4624 to 4640
290:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 395}, {'index_dec': 2, 'index_bin': '0010', 'val': 13, 'counts': 397}], # Indices 4640 to 4656
291:[], # Indices 4656 to 4672
292:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 405}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 416}], # Indices 4672 to 4688
293:[], # Indices 4688 to 4704
294:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 475}], # Indices 4704 to 4720
295:[], # Indices 4720 to 4736
296:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 470}], # Indices 4736 to 4752
297:[{'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 517}], # Indices 4752 to 4768
298:[], # Indices 4768 to 4784
299:[{'index_dec': 14, 'index_bin': '1110', 'val': 14, 'counts': 484}], # Indices 4784 to 4800
300:[], # Indices 4800 to 4816
301:[], # Indices 4816 to 4832
302:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 407}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 389}], # Indices 4832 to 4848
303:[{'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 460}], # Indices 4848 to 4864
304:[], # Indices 4864 to 4880
305:[], # Indices 4880 to 4896
306:[], # Indices 4896 to 4912
307:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 488}], # Indices 4912 to 4928
308:[{'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 387}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 415}], # Indices 4928 to 4944
309:[], # Indices 4944 to 4960
310:[], # Indices 4960 to 4976
311:[], # Indices 4976 to 4992
312:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 337}, {'index_dec': 5, 'index_bin': '0101', 'val': 12, 'counts': 343}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 294}], # Indices 4992 to 5008
313:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 483}], # Indices 5008 to 5024
314:[], # Indices 5024 to 5040
315:[], # Indices 5040 to 5056
316:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 511}], # Indices 5056 to 5072
317:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 411}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 392}], # Indices 5072 to 5088
318:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 502}], # Indices 5088 to 5104
319:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 507}], # Indices 5104 to 5120
320:[{'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 469}], # Indices 5120 to 5136
321:[], # Indices 5136 to 5152
322:[], # Indices 5152 to 5168
323:[{'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 499}], # Indices 5168 to 5184
324:[], # Indices 5184 to 5200
325:[], # Indices 5200 to 5216
326:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 485}], # Indices 5216 to 5232
327:[{'index_dec': 8, 'index_bin': '1000', 'val': 14, 'counts': 340}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 318}, {'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 317}], # Indices 5232 to 5248
328:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 319}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 333}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 319}], # Indices 5248 to 5264
329:[], # Indices 5264 to 5280
330:[], # Indices 5280 to 5296
331:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 311}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 326}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 327}], # Indices 5296 to 5312
332:[], # Indices 5312 to 5328
333:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 472}], # Indices 5328 to 5344
334:[], # Indices 5344 to 5360
335:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 400}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 400}], # Indices 5360 to 5376
336:[{'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 463}], # Indices 5376 to 5392
337:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 391}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 412}], # Indices 5392 to 5408
338:[{'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 361}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 298}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 307}], # Indices 5408 to 5424
339:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 475}], # Indices 5424 to 5440
340:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 501}], # Indices 5440 to 5456
341:[{'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 399}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 415}], # Indices 5456 to 5472
342:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 405}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 403}], # Indices 5472 to 5488
343:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 477}], # Indices 5488 to 5504
344:[], # Indices 5504 to 5520
345:[], # Indices 5520 to 5536
346:[{'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 501}], # Indices 5536 to 5552
347:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 257}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 279}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 239}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 249}], # Indices 5552 to 5568
348:[], # Indices 5568 to 5584
349:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 376}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 401}], # Indices 5584 to 5600
350:[], # Indices 5600 to 5616
351:[{'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 492}], # Indices 5616 to 5632
352:[{'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 482}], # Indices 5632 to 5648
353:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 374}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 413}], # Indices 5648 to 5664
354:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 353}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 308}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 316}], # Indices 5664 to 5680
355:[], # Indices 5680 to 5696
356:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 486}], # Indices 5696 to 5712
357:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 506}], # Indices 5712 to 5728
358:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 330}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 323}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 316}], # Indices 5728 to 5744
359:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 491}], # Indices 5744 to 5760
360:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 392}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 405}], # Indices 5760 to 5776
361:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 481}], # Indices 5776 to 5792
362:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 418}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 392}], # Indices 5792 to 5808
363:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 478}], # Indices 5808 to 5824
364:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 455}], # Indices 5824 to 5840
365:[], # Indices 5840 to 5856
366:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 473}], # Indices 5856 to 5872
367:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 485}], # Indices 5872 to 5888
368:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 487}], # Indices 5888 to 5904
369:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 412}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 405}], # Indices 5904 to 5920
370:[], # Indices 5920 to 5936
371:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 329}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 317}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 330}], # Indices 5936 to 5952
372:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 405}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 409}], # Indices 5952 to 5968
373:[], # Indices 5968 to 5984
374:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 390}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 420}], # Indices 5984 to 6000
375:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 508}], # Indices 6000 to 6016
376:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 484}], # Indices 6016 to 6032
377:[], # Indices 6032 to 6048
378:[], # Indices 6048 to 6064
379:[], # Indices 6064 to 6080
380:[], # Indices 6080 to 6096
381:[], # Indices 6096 to 6112
382:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 419}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 379}], # Indices 6112 to 6128
383:[], # Indices 6128 to 6144
384:[], # Indices 6144 to 6160
385:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 476}], # Indices 6160 to 6176
386:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 465}], # Indices 6176 to 6192
387:[], # Indices 6192 to 6208
388:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 470}], # Indices 6208 to 6224
389:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 477}], # Indices 6224 to 6240
390:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 384}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 407}], # Indices 6240 to 6256
391:[], # Indices 6256 to 6272
392:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 400}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 402}], # Indices 6272 to 6288
393:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 435}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 385}], # Indices 6288 to 6304
394:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 500}], # Indices 6304 to 6320
395:[], # Indices 6320 to 6336
396:[], # Indices 6336 to 6352
397:[], # Indices 6352 to 6368
398:[], # Indices 6368 to 6384
399:[], # Indices 6384 to 6400
400:[], # Indices 6400 to 6416
401:[], # Indices 6416 to 6432
402:[], # Indices 6432 to 6448
403:[], # Indices 6448 to 6464
404:[], # Indices 6464 to 6480
405:[], # Indices 6480 to 6496
406:[], # Indices 6496 to 6512
407:[], # Indices 6512 to 6528
408:[], # Indices 6528 to 6544
409:[], # Indices 6544 to 6560
410:[], # Indices 6560 to 6576
411:[], # Indices 6576 to 6592
412:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 486}], # Indices 6592 to 6608
413:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 309}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 341}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 321}], # Indices 6608 to 6624
414:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 462}], # Indices 6624 to 6640
415:[], # Indices 6640 to 6656
416:[], # Indices 6656 to 6672
417:[], # Indices 6672 to 6688
418:[], # Indices 6688 to 6704
419:[], # Indices 6704 to 6720
420:[], # Indices 6720 to 6736
421:[], # Indices 6736 to 6752
422:[], # Indices 6752 to 6768
423:[], # Indices 6768 to 6784
424:[], # Indices 6784 to 6800
425:[], # Indices 6800 to 6816
426:[], # Indices 6816 to 6832
427:[], # Indices 6832 to 6848
428:[], # Indices 6848 to 6864
429:[], # Indices 6864 to 6880
430:[], # Indices 6880 to 6896
431:[], # Indices 6896 to 6912
432:[], # Indices 6912 to 6928
433:[], # Indices 6928 to 6944
434:[], # Indices 6944 to 6960
435:[], # Indices 6960 to 6976
436:[], # Indices 6976 to 6992
437:[{'index_dec': 1, 'index_bin': '0001', 'val': 5, 'counts': 91}], # Indices 6992 to 7008
438:[], # Indices 7008 to 7024
439:[], # Indices 7024 to 7040
440:[], # Indices 7040 to 7056
441:[], # Indices 7056 to 7072
442:[], # Indices 7072 to 7088
443:[], # Indices 7088 to 7104
444:[], # Indices 7104 to 7120
445:[], # Indices 7120 to 7136
446:[], # Indices 7136 to 7152
447:[], # Indices 7152 to 7168
448:[], # Indices 7168 to 7184
449:[], # Indices 7184 to 7200
450:[], # Indices 7200 to 7216
451:[], # Indices 7216 to 7232
452:[], # Indices 7232 to 7248
453:[], # Indices 7248 to 7264
454:[], # Indices 7264 to 7280
455:[], # Indices 7280 to 7296
456:[], # Indices 7296 to 7312
457:[], # Indices 7312 to 7328
458:[], # Indices 7328 to 7344
459:[], # Indices 7344 to 7360
460:[], # Indices 7360 to 7376
461:[], # Indices 7376 to 7392
462:[], # Indices 7392 to 7408
463:[], # Indices 7408 to 7424
464:[], # Indices 7424 to 7440
465:[], # Indices 7440 to 7456
466:[], # Indices 7456 to 7472
467:[], # Indices 7472 to 7488
468:[], # Indices 7488 to 7504
469:[], # Indices 7504 to 7520
470:[], # Indices 7520 to 7536
471:[], # Indices 7536 to 7552
472:[], # Indices 7552 to 7568
473:[], # Indices 7568 to 7584
474:[], # Indices 7584 to 7600
475:[], # Indices 7600 to 7616
476:[], # Indices 7616 to 7632
477:[], # Indices 7632 to 7648
478:[], # Indices 7648 to 7664
479:[], # Indices 7664 to 7680
480:[], # Indices 7680 to 7696
481:[], # Indices 7696 to 7712
482:[], # Indices 7712 to 7728
483:[], # Indices 7728 to 7744
484:[], # Indices 7744 to 7760
485:[], # Indices 7760 to 7776
486:[], # Indices 7776 to 7792
487:[], # Indices 7792 to 7808
488:[], # Indices 7808 to 7824
489:[], # Indices 7824 to 7840
490:[], # Indices 7840 to 7856
491:[], # Indices 7856 to 7872
492:[], # Indices 7872 to 7888
493:[], # Indices 7888 to 7904
494:[], # Indices 7904 to 7920
495:[], # Indices 7920 to 7936
496:[], # Indices 7936 to 7952
497:[], # Indices 7952 to 7968
498:[], # Indices 7968 to 7984
499:[], # Indices 7984 to 8000
500:[], # Indices 8000 to 8016
501:[], # Indices 8016 to 8032
502:[], # Indices 8032 to 8048
503:[], # Indices 8048 to 8064
504:[], # Indices 8064 to 8080
505:[], # Indices 8080 to 8096
506:[], # Indices 8096 to 8112
507:[], # Indices 8112 to 8128
508:[], # Indices 8128 to 8144
509:[], # Indices 8144 to 8160
510:[], # Indices 8160 to 8176
511:[], # Indices 8176 to 8192
512:[], # Indices 8192 to 8208
513:[], # Indices 8208 to 8224
514:[], # Indices 8224 to 8240
515:[], # Indices 8240 to 8256
516:[], # Indices 8256 to 8272
517:[], # Indices 8272 to 8288
518:[], # Indices 8288 to 8304
519:[], # Indices 8304 to 8320
520:[], # Indices 8320 to 8336
521:[], # Indices 8336 to 8352
522:[], # Indices 8352 to 8368
523:[], # Indices 8368 to 8384
524:[], # Indices 8384 to 8400
525:[], # Indices 8400 to 8416
526:[], # Indices 8416 to 8432
527:[], # Indices 8432 to 8448
528:[], # Indices 8448 to 8464
529:[], # Indices 8464 to 8480
530:[], # Indices 8480 to 8496
531:[], # Indices 8496 to 8512
532:[], # Indices 8512 to 8528
533:[], # Indices 8528 to 8544
534:[], # Indices 8544 to 8560
535:[], # Indices 8560 to 8576
536:[], # Indices 8576 to 8592
537:[], # Indices 8592 to 8608
538:[], # Indices 8608 to 8624
539:[], # Indices 8624 to 8640
540:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 405}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 394}], # Indices 8640 to 8656
541:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 211}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 186}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 178}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 212}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 194}], # Indices 8656 to 8672
542:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 140}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 146}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 138}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 152}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 151}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 131}], # Indices 8672 to 8688
543:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 254}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 251}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 250}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 269}], # Indices 8688 to 8704
544:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 423}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 392}], # Indices 8704 to 8720
545:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 267}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 246}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 253}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 258}], # Indices 8720 to 8736
546:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 258}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 258}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 245}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 263}], # Indices 8736 to 8752
547:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 371}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 405}], # Indices 8752 to 8768
548:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 282}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 245}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 233}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 264}], # Indices 8768 to 8784
549:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 183}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 186}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 188}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 208}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 210}], # Indices 8784 to 8800
550:[{'index_dec': 0, 'index_bin': '0000', 'val': 12, 'counts': 197}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 177}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 216}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 196}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 196}], # Indices 8800 to 8816
551:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 323}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 321}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 320}], # Indices 8816 to 8832
552:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 280}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 242}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 255}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 247}], # Indices 8832 to 8848
553:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 206}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 194}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 204}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 212}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 173}], # Indices 8848 to 8864
554:[{'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 315}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 356}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 298}], # Indices 8864 to 8880
555:[], # Indices 8880 to 8896
556:[], # Indices 8896 to 8912
557:[], # Indices 8912 to 8928
558:[], # Indices 8928 to 8944
559:[], # Indices 8944 to 8960
560:[], # Indices 8960 to 8976
561:[], # Indices 8976 to 8992
562:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 371}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 426}], # Indices 8992 to 9008
563:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 333}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 310}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 331}], # Indices 9008 to 9024
564:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 449}], # Indices 9024 to 9040
565:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 244}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 267}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 255}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 258}], # Indices 9040 to 9056
566:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 488}], # Indices 9056 to 9072
567:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 320}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 347}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 304}], # Indices 9072 to 9088
568:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 308}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 324}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 340}], # Indices 9088 to 9104
569:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 309}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 304}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 354}], # Indices 9104 to 9120
570:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 244}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 260}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 244}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 276}], # Indices 9120 to 9136
571:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 471}], # Indices 9136 to 9152
572:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 270}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 264}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 237}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 253}], # Indices 9152 to 9168
573:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 495}], # Indices 9168 to 9184
574:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 411}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 384}], # Indices 9184 to 9200
575:[{'index_dec': 4, 'index_bin': '0100', 'val': 14, 'counts': 248}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 250}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 267}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 259}], # Indices 9200 to 9216
576:[], # Indices 9216 to 9232
577:[{'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 235}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 263}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 285}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 241}], # Indices 9232 to 9248
578:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 314}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 343}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 317}], # Indices 9248 to 9264
579:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 405}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 394}], # Indices 9264 to 9280
580:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 403}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 389}], # Indices 9280 to 9296
581:[{'index_dec': 0, 'index_bin': '0000', 'val': 16, 'counts': 188}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 195}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 181}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 209}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 207}], # Indices 9296 to 9312
582:[{'index_dec': 2, 'index_bin': '0010', 'val': 14, 'counts': 326}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 326}, {'index_dec': 6, 'index_bin': '0110', 'val': 15, 'counts': 308}], # Indices 9312 to 9328
583:[], # Indices 9328 to 9344
584:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 414}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 388}], # Indices 9344 to 9360
585:[{'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 466}], # Indices 9360 to 9376
586:[], # Indices 9376 to 9392
587:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 505}], # Indices 9392 to 9408
588:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 478}], # Indices 9408 to 9424
589:[], # Indices 9424 to 9440
590:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 383}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 391}], # Indices 9440 to 9456
591:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 475}], # Indices 9456 to 9472
592:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 487}], # Indices 9472 to 9488
593:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 502}], # Indices 9488 to 9504
594:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 487}], # Indices 9504 to 9520
595:[{'index_dec': 4, 'index_bin': '0100', 'val': 15, 'counts': 496}], # Indices 9520 to 9536
596:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 385}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 391}], # Indices 9536 to 9552
597:[{'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 480}], # Indices 9552 to 9568
598:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 421}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 384}], # Indices 9568 to 9584
599:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 337}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 325}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 309}], # Indices 9584 to 9600
600:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 434}], # Indices 9600 to 9616
601:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 505}], # Indices 9616 to 9632
602:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 428}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 387}], # Indices 9632 to 9648
603:[], # Indices 9648 to 9664
604:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 490}], # Indices 9664 to 9680
605:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 411}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 403}], # Indices 9680 to 9696
606:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 490}], # Indices 9696 to 9712
607:[], # Indices 9712 to 9728
608:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 403}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 389}], # Indices 9728 to 9744
609:[], # Indices 9744 to 9760
610:[{'index_dec': 0, 'index_bin': '0000', 'val': 14, 'counts': 395}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 406}], # Indices 9760 to 9776
611:[{'index_dec': 15, 'index_bin': '1111', 'val': 13, 'counts': 477}], # Indices 9776 to 9792
612:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 497}], # Indices 9792 to 9808
613:[], # Indices 9808 to 9824
614:[], # Indices 9824 to 9840
615:[{'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 466}], # Indices 9840 to 9856
616:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 488}], # Indices 9856 to 9872
617:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 458}], # Indices 9872 to 9888
618:[], # Indices 9888 to 9904
619:[{'index_dec': 10, 'index_bin': '1010', 'val': 13, 'counts': 491}], # Indices 9904 to 9920
620:[], # Indices 9920 to 9936
621:[{'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 463}], # Indices 9936 to 9952
622:[], # Indices 9952 to 9968
623:[{'index_dec': 5, 'index_bin': '0101', 'val': 13, 'counts': 364}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 419}], # Indices 9968 to 9984
624:[], # Indices 9984 to 10000
625:[{'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 397}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 393}], # Indices 10000 to 10016
626:[], # Indices 10016 to 10032
627:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 320}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 312}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 339}], # Indices 10032 to 10048
628:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 486}], # Indices 10048 to 10064
629:[{'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 507}], # Indices 10064 to 10080
630:[], # Indices 10080 to 10096
631:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 508}], # Indices 10096 to 10112
632:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 443}], # Indices 10112 to 10128
633:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 502}], # Indices 10128 to 10144
634:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 396}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 399}], # Indices 10144 to 10160
635:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 415}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 394}], # Indices 10160 to 10176
636:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 380}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 410}], # Indices 10176 to 10192
637:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 388}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 401}], # Indices 10192 to 10208
638:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 491}], # Indices 10208 to 10224
639:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 412}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 404}], # Indices 10224 to 10240
640:[{'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 495}], # Indices 10240 to 10256
641:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 385}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 432}], # Indices 10256 to 10272
642:[], # Indices 10272 to 10288
643:[], # Indices 10288 to 10304
644:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 326}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 318}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 331}], # Indices 10304 to 10320
645:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 504}], # Indices 10320 to 10336
646:[], # Indices 10336 to 10352
647:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 494}], # Indices 10352 to 10368
648:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 377}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 415}], # Indices 10368 to 10384
649:[], # Indices 10384 to 10400
650:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 490}], # Indices 10400 to 10416
651:[], # Indices 10416 to 10432
652:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 501}], # Indices 10432 to 10448
653:[], # Indices 10448 to 10464
654:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 382}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 420}], # Indices 10464 to 10480
655:[], # Indices 10480 to 10496
656:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 397}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 413}], # Indices 10496 to 10512
657:[{'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 460}], # Indices 10512 to 10528
658:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 303}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 319}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 348}], # Indices 10528 to 10544
659:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 250}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 264}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 252}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 258}], # Indices 10544 to 10560
660:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 500}], # Indices 10560 to 10576
661:[{'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 477}], # Indices 10576 to 10592
662:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 492}], # Indices 10592 to 10608
663:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 406}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 402}], # Indices 10608 to 10624
664:[], # Indices 10624 to 10640
665:[], # Indices 10640 to 10656
666:[], # Indices 10656 to 10672
667:[], # Indices 10672 to 10688
668:[], # Indices 10688 to 10704
669:[], # Indices 10704 to 10720
670:[], # Indices 10720 to 10736
671:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 491}], # Indices 10736 to 10752
672:[], # Indices 10752 to 10768
673:[], # Indices 10768 to 10784
674:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 485}], # Indices 10784 to 10800
675:[], # Indices 10800 to 10816
676:[], # Indices 10816 to 10832
677:[], # Indices 10832 to 10848
678:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 495}], # Indices 10848 to 10864
679:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 493}], # Indices 10864 to 10880
680:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 531}], # Indices 10880 to 10896
681:[], # Indices 10896 to 10912
682:[], # Indices 10912 to 10928
683:[], # Indices 10928 to 10944
684:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 394}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 419}], # Indices 10944 to 10960
685:[], # Indices 10960 to 10976
686:[], # Indices 10976 to 10992
687:[], # Indices 10992 to 11008
688:[], # Indices 11008 to 11024
689:[], # Indices 11024 to 11040
690:[], # Indices 11040 to 11056
691:[], # Indices 11056 to 11072
692:[], # Indices 11072 to 11088
693:[], # Indices 11088 to 11104
694:[], # Indices 11104 to 11120
695:[], # Indices 11120 to 11136
696:[], # Indices 11136 to 11152
697:[], # Indices 11152 to 11168
698:[], # Indices 11168 to 11184
699:[], # Indices 11184 to 11200
700:[], # Indices 11200 to 11216
701:[], # Indices 11216 to 11232
702:[], # Indices 11232 to 11248
703:[], # Indices 11248 to 11264
704:[], # Indices 11264 to 11280
705:[], # Indices 11280 to 11296
706:[], # Indices 11296 to 11312
707:[], # Indices 11312 to 11328
708:[], # Indices 11328 to 11344
709:[], # Indices 11344 to 11360
710:[], # Indices 11360 to 11376
711:[], # Indices 11376 to 11392
712:[], # Indices 11392 to 11408
713:[], # Indices 11408 to 11424
714:[], # Indices 11424 to 11440
715:[], # Indices 11440 to 11456
716:[], # Indices 11456 to 11472
717:[], # Indices 11472 to 11488
718:[], # Indices 11488 to 11504
719:[], # Indices 11504 to 11520
720:[], # Indices 11520 to 11536
721:[], # Indices 11536 to 11552
722:[], # Indices 11552 to 11568
723:[], # Indices 11568 to 11584
724:[], # Indices 11584 to 11600
725:[], # Indices 11600 to 11616
726:[], # Indices 11616 to 11632
727:[], # Indices 11632 to 11648
728:[], # Indices 11648 to 11664
729:[], # Indices 11664 to 11680
730:[], # Indices 11680 to 11696
731:[], # Indices 11696 to 11712
732:[], # Indices 11712 to 11728
733:[], # Indices 11728 to 11744
734:[], # Indices 11744 to 11760
735:[], # Indices 11760 to 11776
736:[], # Indices 11776 to 11792
737:[], # Indices 11792 to 11808
738:[], # Indices 11808 to 11824
739:[], # Indices 11824 to 11840
740:[], # Indices 11840 to 11856
741:[], # Indices 11856 to 11872
742:[], # Indices 11872 to 11888
743:[], # Indices 11888 to 11904
744:[], # Indices 11904 to 11920
745:[], # Indices 11920 to 11936
746:[], # Indices 11936 to 11952
747:[], # Indices 11952 to 11968
748:[], # Indices 11968 to 11984
749:[], # Indices 11984 to 12000
750:[], # Indices 12000 to 12016
751:[], # Indices 12016 to 12032
752:[], # Indices 12032 to 12048
753:[], # Indices 12048 to 12064
754:[], # Indices 12064 to 12080
755:[], # Indices 12080 to 12096
756:[], # Indices 12096 to 12112
757:[], # Indices 12112 to 12128
758:[], # Indices 12128 to 12144
759:[], # Indices 12144 to 12160
760:[], # Indices 12160 to 12176
761:[], # Indices 12176 to 12192
762:[], # Indices 12192 to 12208
763:[], # Indices 12208 to 12224
764:[], # Indices 12224 to 12240
765:[], # Indices 12240 to 12256
766:[], # Indices 12256 to 12272
767:[], # Indices 12272 to 12288
768:[], # Indices 12288 to 12304
769:[], # Indices 12304 to 12320
770:[{'index_dec': 5, 'index_bin': '0101', 'val': 16, 'counts': 181}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 185}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 182}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 221}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 215}], # Indices 12320 to 12336
771:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 495}], # Indices 12336 to 12352
772:[{'index_dec': 0, 'index_bin': '0000', 'val': 16, 'counts': 144}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 142}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 172}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 140}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 148}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 130}], # Indices 12352 to 12368
773:[{'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 467}], # Indices 12368 to 12384
774:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 483}], # Indices 12384 to 12400
775:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 179}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 204}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 198}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 195}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 204}], # Indices 12400 to 12416
776:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 486}], # Indices 12416 to 12432
777:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 250}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 253}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 247}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 274}], # Indices 12432 to 12448
778:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 209}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 185}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 201}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 209}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 185}], # Indices 12448 to 12464
779:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 141}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 136}, {'index_dec': 6, 'index_bin': '0110', 'val': 13, 'counts': 151}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 146}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 175}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 120}], # Indices 12464 to 12480
780:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 319}, {'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 314}, {'index_dec': 14, 'index_bin': '1110', 'val': 13, 'counts': 319}], # Indices 12480 to 12496
781:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 141}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 163}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 133}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 151}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 151}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 129}], # Indices 12496 to 12512
782:[{'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 471}], # Indices 12512 to 12528
783:[], # Indices 12528 to 12544
784:[], # Indices 12544 to 12560
785:[], # Indices 12560 to 12576
786:[], # Indices 12576 to 12592
787:[], # Indices 12592 to 12608
788:[], # Indices 12608 to 12624
789:[], # Indices 12624 to 12640
790:[], # Indices 12640 to 12656
791:[{'index_dec': 8, 'index_bin': '1000', 'val': 14, 'counts': 378}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 421}], # Indices 12656 to 12672
792:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 407}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 390}], # Indices 12672 to 12688
793:[], # Indices 12688 to 12704
794:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 399}, {'index_dec': 8, 'index_bin': '1000', 'val': 15, 'counts': 405}], # Indices 12704 to 12720
795:[], # Indices 12720 to 12736
796:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 497}], # Indices 12736 to 12752
797:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 406}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 397}], # Indices 12752 to 12768
798:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 461}], # Indices 12768 to 12784
799:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 305}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 315}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 351}], # Indices 12784 to 12800
800:[], # Indices 12800 to 12816
801:[], # Indices 12816 to 12832
802:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 385}, {'index_dec': 15, 'index_bin': '1111', 'val': 14, 'counts': 412}], # Indices 12832 to 12848
803:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 395}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 391}], # Indices 12848 to 12864
804:[], # Indices 12864 to 12880
805:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 336}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 319}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 310}], # Indices 12880 to 12896
806:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 336}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 312}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 335}], # Indices 12896 to 12912
807:[{'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 455}], # Indices 12912 to 12928
808:[{'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 254}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 275}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 225}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 270}], # Indices 12928 to 12944
809:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 319}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 322}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 327}], # Indices 12944 to 12960
810:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 260}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 253}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 262}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 249}], # Indices 12960 to 12976
811:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 351}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 316}, {'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 302}], # Indices 12976 to 12992
812:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 478}], # Indices 12992 to 13008
813:[], # Indices 13008 to 13024
814:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 465}], # Indices 13024 to 13040
815:[], # Indices 13040 to 13056
816:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 499}], # Indices 13056 to 13072
817:[], # Indices 13072 to 13088
818:[], # Indices 13088 to 13104
819:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 501}], # Indices 13104 to 13120
820:[], # Indices 13120 to 13136
821:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 383}, {'index_dec': 7, 'index_bin': '0111', 'val': 13, 'counts': 412}], # Indices 13136 to 13152
822:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 484}], # Indices 13152 to 13168
823:[], # Indices 13168 to 13184
824:[{'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 328}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 330}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 324}], # Indices 13184 to 13200
825:[], # Indices 13200 to 13216
826:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 495}], # Indices 13216 to 13232
827:[{'index_dec': 2, 'index_bin': '0010', 'val': 15, 'counts': 510}], # Indices 13232 to 13248
828:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 496}], # Indices 13248 to 13264
829:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 497}], # Indices 13264 to 13280
830:[{'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 500}], # Indices 13280 to 13296
831:[{'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 491}], # Indices 13296 to 13312
832:[{'index_dec': 2, 'index_bin': '0010', 'val': 15, 'counts': 479}], # Indices 13312 to 13328
833:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 521}], # Indices 13328 to 13344
834:[], # Indices 13344 to 13360
835:[], # Indices 13360 to 13376
836:[], # Indices 13376 to 13392
837:[], # Indices 13392 to 13408
838:[{'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 495}], # Indices 13408 to 13424
839:[], # Indices 13424 to 13440
840:[], # Indices 13440 to 13456
841:[], # Indices 13456 to 13472
842:[], # Indices 13472 to 13488
843:[], # Indices 13488 to 13504
844:[], # Indices 13504 to 13520
845:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 490}], # Indices 13520 to 13536
846:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 321}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 327}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 327}], # Indices 13536 to 13552
847:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 202}, {'index_dec': 7, 'index_bin': '0111', 'val': 13, 'counts': 198}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 182}, {'index_dec': 10, 'index_bin': '1010', 'val': 13, 'counts': 182}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 197}], # Indices 13552 to 13568
848:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 435}], # Indices 13568 to 13584
849:[], # Indices 13584 to 13600
850:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 500}], # Indices 13600 to 13616
851:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 394}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 391}], # Indices 13616 to 13632
852:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 391}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 413}], # Indices 13632 to 13648
853:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 407}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 395}], # Indices 13648 to 13664
854:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 416}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 387}], # Indices 13664 to 13680
855:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 454}], # Indices 13680 to 13696
856:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 412}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 410}], # Indices 13696 to 13712
857:[{'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 506}], # Indices 13712 to 13728
858:[{'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 404}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 385}], # Indices 13728 to 13744
859:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 470}], # Indices 13744 to 13760
860:[], # Indices 13760 to 13776
861:[], # Indices 13776 to 13792
862:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 384}, {'index_dec': 12, 'index_bin': '1100', 'val': 12, 'counts': 406}], # Indices 13792 to 13808
863:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 476}], # Indices 13808 to 13824
864:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 417}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 377}], # Indices 13824 to 13840
865:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 483}], # Indices 13840 to 13856
866:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 489}], # Indices 13856 to 13872
867:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 473}], # Indices 13872 to 13888
868:[], # Indices 13888 to 13904
869:[{'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 312}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 334}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 324}], # Indices 13904 to 13920
870:[], # Indices 13920 to 13936
871:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 482}], # Indices 13936 to 13952
872:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 491}], # Indices 13952 to 13968
873:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 416}, {'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 403}], # Indices 13968 to 13984
874:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 464}], # Indices 13984 to 14000
875:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 491}], # Indices 14000 to 14016
876:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 496}], # Indices 14016 to 14032
877:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 347}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 311}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 302}], # Indices 14032 to 14048
878:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 409}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 373}], # Indices 14048 to 14064
879:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 414}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 382}], # Indices 14064 to 14080
880:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 471}], # Indices 14080 to 14096
881:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 490}], # Indices 14096 to 14112
882:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 480}], # Indices 14112 to 14128
883:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 499}], # Indices 14128 to 14144
884:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 406}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 404}], # Indices 14144 to 14160
885:[{'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 499}], # Indices 14160 to 14176
886:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 318}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 319}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 330}], # Indices 14176 to 14192
887:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 491}], # Indices 14192 to 14208
888:[{'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 482}], # Indices 14208 to 14224
889:[], # Indices 14224 to 14240
890:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 494}], # Indices 14240 to 14256
891:[], # Indices 14256 to 14272
892:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 490}], # Indices 14272 to 14288
893:[], # Indices 14288 to 14304
894:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 495}], # Indices 14304 to 14320
895:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 390}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 419}], # Indices 14320 to 14336
896:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 472}], # Indices 14336 to 14352
897:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 397}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 397}], # Indices 14352 to 14368
898:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 473}], # Indices 14368 to 14384
899:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 315}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 359}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 305}], # Indices 14384 to 14400
900:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 426}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 393}], # Indices 14400 to 14416
901:[], # Indices 14416 to 14432
902:[{'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 396}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 396}], # Indices 14432 to 14448
903:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 324}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 341}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 325}], # Indices 14448 to 14464
904:[], # Indices 14464 to 14480
905:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 485}], # Indices 14480 to 14496
906:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 516}], # Indices 14496 to 14512
907:[], # Indices 14512 to 14528
908:[], # Indices 14528 to 14544
909:[], # Indices 14544 to 14560
910:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 266}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 247}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 296}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 215}], # Indices 14560 to 14576
911:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 493}], # Indices 14576 to 14592
912:[], # Indices 14592 to 14608
913:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 498}], # Indices 14608 to 14624
914:[], # Indices 14624 to 14640
915:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 469}], # Indices 14640 to 14656
916:[{'index_dec': 2, 'index_bin': '0010', 'val': 13, 'counts': 431}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 383}], # Indices 14656 to 14672
917:[], # Indices 14672 to 14688
918:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 322}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 311}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 336}], # Indices 14688 to 14704
919:[], # Indices 14704 to 14720
920:[], # Indices 14720 to 14736
921:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 309}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 333}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 314}], # Indices 14736 to 14752
922:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 346}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 329}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 315}], # Indices 14752 to 14768
923:[], # Indices 14768 to 14784
924:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 517}], # Indices 14784 to 14800
925:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 251}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 254}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 254}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 265}], # Indices 14800 to 14816
926:[], # Indices 14816 to 14832
927:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 405}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 421}], # Indices 14832 to 14848
928:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 400}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 394}], # Indices 14848 to 14864
929:[], # Indices 14864 to 14880
930:[], # Indices 14880 to 14896
931:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 280}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 241}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 238}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 265}], # Indices 14896 to 14912
932:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 483}], # Indices 14912 to 14928
933:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 471}], # Indices 14928 to 14944
934:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 259}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 259}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 265}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 241}], # Indices 14944 to 14960
935:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 318}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 346}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 311}], # Indices 14960 to 14976
936:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 320}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 334}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 330}], # Indices 14976 to 14992
937:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 512}], # Indices 14992 to 15008
938:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 413}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 379}], # Indices 15008 to 15024
939:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 313}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 332}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 327}], # Indices 15024 to 15040
940:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 489}], # Indices 15040 to 15056
941:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 490}], # Indices 15056 to 15072
942:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 241}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 240}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 258}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 285}], # Indices 15072 to 15088
943:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 469}], # Indices 15088 to 15104
944:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 482}], # Indices 15104 to 15120
945:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 415}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 392}], # Indices 15120 to 15136
946:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 327}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 319}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 319}], # Indices 15136 to 15152
947:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 458}], # Indices 15152 to 15168
948:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 318}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 314}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 327}], # Indices 15168 to 15184
949:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 398}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 403}], # Indices 15184 to 15200
950:[], # Indices 15200 to 15216
951:[], # Indices 15216 to 15232
952:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 480}], # Indices 15232 to 15248
953:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 480}], # Indices 15248 to 15264
954:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 376}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 420}], # Indices 15264 to 15280
955:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 469}], # Indices 15280 to 15296
956:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 250}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 265}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 265}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 244}], # Indices 15296 to 15312
957:[], # Indices 15312 to 15328
958:[], # Indices 15328 to 15344
959:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 322}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 349}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 303}], # Indices 15344 to 15360
960:[], # Indices 15360 to 15376
961:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 458}], # Indices 15376 to 15392
962:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 180}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 196}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 190}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 195}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 214}], # Indices 15392 to 15408
963:[], # Indices 15408 to 15424
964:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 383}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 407}], # Indices 15424 to 15440
965:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 480}], # Indices 15440 to 15456
966:[], # Indices 15456 to 15472
967:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 401}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 415}], # Indices 15472 to 15488
968:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 468}], # Indices 15488 to 15504
969:[], # Indices 15504 to 15520
970:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 484}], # Indices 15520 to 15536
971:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 407}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 403}], # Indices 15536 to 15552
972:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 419}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 402}], # Indices 15552 to 15568
973:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 403}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 411}], # Indices 15568 to 15584
974:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 398}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 393}], # Indices 15584 to 15600
975:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 484}], # Indices 15600 to 15616
976:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 483}], # Indices 15616 to 15632
977:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 448}], # Indices 15632 to 15648
978:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 396}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 411}], # Indices 15648 to 15664
979:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 498}], # Indices 15664 to 15680
980:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 473}], # Indices 15680 to 15696
981:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 488}], # Indices 15696 to 15712
982:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 335}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 340}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 308}], # Indices 15712 to 15728
983:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 416}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 395}], # Indices 15728 to 15744
984:[], # Indices 15744 to 15760
985:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 468}], # Indices 15760 to 15776
986:[], # Indices 15776 to 15792
987:[], # Indices 15792 to 15808
988:[], # Indices 15808 to 15824
989:[], # Indices 15824 to 15840
990:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 401}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 412}], # Indices 15840 to 15856
991:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 302}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 341}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 325}], # Indices 15856 to 15872
992:[], # Indices 15872 to 15888
993:[], # Indices 15888 to 15904
994:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 476}], # Indices 15904 to 15920
995:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 312}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 353}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 313}], # Indices 15920 to 15936
996:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 413}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 397}], # Indices 15936 to 15952
997:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 404}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 396}], # Indices 15952 to 15968
998:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 487}], # Indices 15968 to 15984
999:[], # Indices 15984 to 16000
1000:[], # Indices 16000 to 16016
1001:[], # Indices 16016 to 16032
1002:[], # Indices 16032 to 16048
1003:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 405}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 411}], # Indices 16048 to 16064
1004:[], # Indices 16064 to 16080
1005:[], # Indices 16080 to 16096
1006:[], # Indices 16096 to 16112
1007:[], # Indices 16112 to 16128
1008:[], # Indices 16128 to 16144
1009:[], # Indices 16144 to 16160
1010:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 481}], # Indices 16160 to 16176
1011:[], # Indices 16176 to 16192
1012:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 504}], # Indices 16192 to 16208
1013:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 518}], # Indices 16208 to 16224
1014:[], # Indices 16224 to 16240
1015:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 333}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 320}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 325}], # Indices 16240 to 16256
1016:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 462}], # Indices 16256 to 16272
1017:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 465}], # Indices 16272 to 16288
1018:[], # Indices 16288 to 16304
1019:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 406}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 389}], # Indices 16304 to 16320
1020:[], # Indices 16320 to 16336
1021:[], # Indices 16336 to 16352
1022:[], # Indices 16352 to 16368
1023:[], # Indices 16368 to 16384
1024:[], # Indices 16384 to 16400
1025:[], # Indices 16400 to 16416
1026:[], # Indices 16416 to 16432
1027:[], # Indices 16432 to 16448
1028:[{'index_dec': 0, 'index_bin': '0000', 'val': 4, 'counts': 93}], # Indices 16448 to 16464
1029:[], # Indices 16464 to 16480
1030:[], # Indices 16480 to 16496
1031:[], # Indices 16496 to 16512
1032:[], # Indices 16512 to 16528
1033:[], # Indices 16528 to 16544
1034:[], # Indices 16544 to 16560
1035:[], # Indices 16560 to 16576
1036:[], # Indices 16576 to 16592
1037:[], # Indices 16592 to 16608
1038:[], # Indices 16608 to 16624
1039:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 512}], # Indices 16624 to 16640
1040:[], # Indices 16640 to 16656
1041:[], # Indices 16656 to 16672
1042:[], # Indices 16672 to 16688
1043:[], # Indices 16688 to 16704
1044:[], # Indices 16704 to 16720
1045:[], # Indices 16720 to 16736
1046:[], # Indices 16736 to 16752
1047:[], # Indices 16752 to 16768
1048:[], # Indices 16768 to 16784
1049:[], # Indices 16784 to 16800
1050:[], # Indices 16800 to 16816
1051:[], # Indices 16816 to 16832
1052:[], # Indices 16832 to 16848
1053:[], # Indices 16848 to 16864
1054:[], # Indices 16864 to 16880
1055:[], # Indices 16880 to 16896
1056:[], # Indices 16896 to 16912
1057:[], # Indices 16912 to 16928
1058:[], # Indices 16928 to 16944
1059:[], # Indices 16944 to 16960
1060:[], # Indices 16960 to 16976
1061:[], # Indices 16976 to 16992
1062:[], # Indices 16992 to 17008
1063:[], # Indices 17008 to 17024
1064:[], # Indices 17024 to 17040
1065:[], # Indices 17040 to 17056
1066:[], # Indices 17056 to 17072
1067:[], # Indices 17072 to 17088
1068:[], # Indices 17088 to 17104
1069:[], # Indices 17104 to 17120
1070:[], # Indices 17120 to 17136
1071:[], # Indices 17136 to 17152
1072:[], # Indices 17152 to 17168
1073:[], # Indices 17168 to 17184
1074:[], # Indices 17184 to 17200
1075:[], # Indices 17200 to 17216
1076:[], # Indices 17216 to 17232
1077:[], # Indices 17232 to 17248
1078:[], # Indices 17248 to 17264
1079:[], # Indices 17264 to 17280
1080:[], # Indices 17280 to 17296
1081:[], # Indices 17296 to 17312
1082:[], # Indices 17312 to 17328
1083:[], # Indices 17328 to 17344
1084:[], # Indices 17344 to 17360
1085:[], # Indices 17360 to 17376
1086:[], # Indices 17376 to 17392
1087:[], # Indices 17392 to 17408
1088:[], # Indices 17408 to 17424
1089:[], # Indices 17424 to 17440
1090:[], # Indices 17440 to 17456
1091:[], # Indices 17456 to 17472
1092:[], # Indices 17472 to 17488
1093:[], # Indices 17488 to 17504
1094:[], # Indices 17504 to 17520
1095:[], # Indices 17520 to 17536
1096:[], # Indices 17536 to 17552
1097:[], # Indices 17552 to 17568
1098:[], # Indices 17568 to 17584
1099:[], # Indices 17584 to 17600
1100:[], # Indices 17600 to 17616
1101:[], # Indices 17616 to 17632
1102:[], # Indices 17632 to 17648
1103:[], # Indices 17648 to 17664
1104:[], # Indices 17664 to 17680
1105:[], # Indices 17680 to 17696
1106:[], # Indices 17696 to 17712
1107:[], # Indices 17712 to 17728
1108:[], # Indices 17728 to 17744
1109:[], # Indices 17744 to 17760
1110:[], # Indices 17760 to 17776
1111:[], # Indices 17776 to 17792
1112:[], # Indices 17792 to 17808
1113:[], # Indices 17808 to 17824
1114:[], # Indices 17824 to 17840
1115:[{'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 91}], # Indices 17840 to 17856
1116:[], # Indices 17856 to 17872
1117:[], # Indices 17872 to 17888
1118:[], # Indices 17888 to 17904
1119:[], # Indices 17904 to 17920
1120:[], # Indices 17920 to 17936
1121:[], # Indices 17936 to 17952
1122:[], # Indices 17952 to 17968
1123:[], # Indices 17968 to 17984
1124:[], # Indices 17984 to 18000
1125:[], # Indices 18000 to 18016
1126:[], # Indices 18016 to 18032
1127:[], # Indices 18032 to 18048
1128:[], # Indices 18048 to 18064
1129:[], # Indices 18064 to 18080
1130:[], # Indices 18080 to 18096
1131:[], # Indices 18096 to 18112
1132:[], # Indices 18112 to 18128
1133:[], # Indices 18128 to 18144
1134:[], # Indices 18144 to 18160
1135:[], # Indices 18160 to 18176
1136:[], # Indices 18176 to 18192
1137:[], # Indices 18192 to 18208
1138:[], # Indices 18208 to 18224
1139:[], # Indices 18224 to 18240
1140:[], # Indices 18240 to 18256
1141:[], # Indices 18256 to 18272
1142:[], # Indices 18272 to 18288
1143:[], # Indices 18288 to 18304
1144:[], # Indices 18304 to 18320
1145:[], # Indices 18320 to 18336
1146:[], # Indices 18336 to 18352
1147:[], # Indices 18352 to 18368
1148:[], # Indices 18368 to 18384
1149:[], # Indices 18384 to 18400
1150:[], # Indices 18400 to 18416
1151:[], # Indices 18416 to 18432
1152:[], # Indices 18432 to 18448
1153:[], # Indices 18448 to 18464
1154:[], # Indices 18464 to 18480
1155:[{'index_dec': 0, 'index_bin': '0000', 'val': 4, 'counts': 96}], # Indices 18480 to 18496
1156:[], # Indices 18496 to 18512
1157:[], # Indices 18512 to 18528
1158:[], # Indices 18528 to 18544
1159:[], # Indices 18544 to 18560
1160:[], # Indices 18560 to 18576
1161:[], # Indices 18576 to 18592
1162:[], # Indices 18592 to 18608
1163:[], # Indices 18608 to 18624
1164:[], # Indices 18624 to 18640
1165:[], # Indices 18640 to 18656
1166:[], # Indices 18656 to 18672
1167:[], # Indices 18672 to 18688
1168:[], # Indices 18688 to 18704
1169:[], # Indices 18704 to 18720
1170:[], # Indices 18720 to 18736
1171:[], # Indices 18736 to 18752
1172:[], # Indices 18752 to 18768
1173:[], # Indices 18768 to 18784
1174:[], # Indices 18784 to 18800
1175:[], # Indices 18800 to 18816
1176:[], # Indices 18816 to 18832
1177:[], # Indices 18832 to 18848
1178:[], # Indices 18848 to 18864
1179:[], # Indices 18864 to 18880
1180:[], # Indices 18880 to 18896
1181:[], # Indices 18896 to 18912
1182:[], # Indices 18912 to 18928
1183:[], # Indices 18928 to 18944
1184:[], # Indices 18944 to 18960
1185:[], # Indices 18960 to 18976
1186:[], # Indices 18976 to 18992
1187:[], # Indices 18992 to 19008
1188:[], # Indices 19008 to 19024
1189:[], # Indices 19024 to 19040
1190:[], # Indices 19040 to 19056
1191:[], # Indices 19056 to 19072
1192:[], # Indices 19072 to 19088
1193:[], # Indices 19088 to 19104
1194:[], # Indices 19104 to 19120
1195:[], # Indices 19120 to 19136
1196:[], # Indices 19136 to 19152
1197:[], # Indices 19152 to 19168
1198:[], # Indices 19168 to 19184
1199:[], # Indices 19184 to 19200
1200:[], # Indices 19200 to 19216
1201:[], # Indices 19216 to 19232
1202:[], # Indices 19232 to 19248
1203:[], # Indices 19248 to 19264
1204:[], # Indices 19264 to 19280
1205:[], # Indices 19280 to 19296
1206:[], # Indices 19296 to 19312
1207:[], # Indices 19312 to 19328
1208:[], # Indices 19328 to 19344
1209:[], # Indices 19344 to 19360
1210:[], # Indices 19360 to 19376
1211:[], # Indices 19376 to 19392
1212:[], # Indices 19392 to 19408
1213:[], # Indices 19408 to 19424
1214:[], # Indices 19424 to 19440
1215:[], # Indices 19440 to 19456
1216:[], # Indices 19456 to 19472
1217:[{'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 91}], # Indices 19472 to 19488
1218:[], # Indices 19488 to 19504
1219:[], # Indices 19504 to 19520
1220:[], # Indices 19520 to 19536
1221:[], # Indices 19536 to 19552
1222:[], # Indices 19552 to 19568
1223:[], # Indices 19568 to 19584
1224:[], # Indices 19584 to 19600
1225:[], # Indices 19600 to 19616
1226:[], # Indices 19616 to 19632
1227:[], # Indices 19632 to 19648
1228:[], # Indices 19648 to 19664
1229:[], # Indices 19664 to 19680
1230:[], # Indices 19680 to 19696
1231:[], # Indices 19696 to 19712
1232:[], # Indices 19712 to 19728
1233:[], # Indices 19728 to 19744
1234:[], # Indices 19744 to 19760
1235:[], # Indices 19760 to 19776
1236:[], # Indices 19776 to 19792
1237:[], # Indices 19792 to 19808
1238:[], # Indices 19808 to 19824
1239:[], # Indices 19824 to 19840
1240:[], # Indices 19840 to 19856
1241:[], # Indices 19856 to 19872
1242:[], # Indices 19872 to 19888
1243:[], # Indices 19888 to 19904
1244:[], # Indices 19904 to 19920
1245:[], # Indices 19920 to 19936
1246:[], # Indices 19936 to 19952
1247:[], # Indices 19952 to 19968
1248:[], # Indices 19968 to 19984
1249:[{'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 95}], # Indices 19984 to 20000
1250:[], # Indices 20000 to 20016
1251:[], # Indices 20016 to 20032
1252:[], # Indices 20032 to 20048
1253:[], # Indices 20048 to 20064
1254:[], # Indices 20064 to 20080
1255:[], # Indices 20080 to 20096
1256:[], # Indices 20096 to 20112
1257:[], # Indices 20112 to 20128
1258:[], # Indices 20128 to 20144
1259:[], # Indices 20144 to 20160
1260:[], # Indices 20160 to 20176
1261:[], # Indices 20176 to 20192
1262:[], # Indices 20192 to 20208
1263:[], # Indices 20208 to 20224
1264:[], # Indices 20224 to 20240
1265:[], # Indices 20240 to 20256
1266:[], # Indices 20256 to 20272
1267:[], # Indices 20272 to 20288
1268:[], # Indices 20288 to 20304
1269:[], # Indices 20304 to 20320
1270:[], # Indices 20320 to 20336
1271:[], # Indices 20336 to 20352
1272:[], # Indices 20352 to 20368
1273:[], # Indices 20368 to 20384
1274:[], # Indices 20384 to 20400
1275:[], # Indices 20400 to 20416
1276:[], # Indices 20416 to 20432
1277:[], # Indices 20432 to 20448
1278:[], # Indices 20448 to 20464
1279:[], # Indices 20464 to 20480
1280:[], # Indices 20480 to 20496
1281:[], # Indices 20496 to 20512
1282:[], # Indices 20512 to 20528
1283:[], # Indices 20528 to 20544
1284:[], # Indices 20544 to 20560
1285:[], # Indices 20560 to 20576
1286:[], # Indices 20576 to 20592
1287:[], # Indices 20592 to 20608
1288:[], # Indices 20608 to 20624
1289:[], # Indices 20624 to 20640
1290:[], # Indices 20640 to 20656
1291:[], # Indices 20656 to 20672
1292:[], # Indices 20672 to 20688
1293:[], # Indices 20688 to 20704
1294:[], # Indices 20704 to 20720
1295:[], # Indices 20720 to 20736
1296:[], # Indices 20736 to 20752
1297:[], # Indices 20752 to 20768
1298:[], # Indices 20768 to 20784
1299:[], # Indices 20784 to 20800
1300:[], # Indices 20800 to 20816
1301:[], # Indices 20816 to 20832
1302:[], # Indices 20832 to 20848
1303:[], # Indices 20848 to 20864
1304:[], # Indices 20864 to 20880
1305:[], # Indices 20880 to 20896
1306:[], # Indices 20896 to 20912
1307:[], # Indices 20912 to 20928
1308:[], # Indices 20928 to 20944
1309:[], # Indices 20944 to 20960
1310:[], # Indices 20960 to 20976
1311:[], # Indices 20976 to 20992
1312:[], # Indices 20992 to 21008
1313:[], # Indices 21008 to 21024
1314:[], # Indices 21024 to 21040
1315:[], # Indices 21040 to 21056
1316:[], # Indices 21056 to 21072
1317:[], # Indices 21072 to 21088
1318:[], # Indices 21088 to 21104
1319:[], # Indices 21104 to 21120
1320:[], # Indices 21120 to 21136
1321:[], # Indices 21136 to 21152
1322:[], # Indices 21152 to 21168
1323:[], # Indices 21168 to 21184
1324:[], # Indices 21184 to 21200
1325:[], # Indices 21200 to 21216
1326:[], # Indices 21216 to 21232
1327:[], # Indices 21232 to 21248
1328:[], # Indices 21248 to 21264
1329:[], # Indices 21264 to 21280
1330:[], # Indices 21280 to 21296
1331:[], # Indices 21296 to 21312
1332:[], # Indices 21312 to 21328
1333:[], # Indices 21328 to 21344
1334:[], # Indices 21344 to 21360
1335:[], # Indices 21360 to 21376
1336:[{'index_dec': 3, 'index_bin': '0011', 'val': 4, 'counts': 92}], # Indices 21376 to 21392
1337:[], # Indices 21392 to 21408
1338:[{'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 92}], # Indices 21408 to 21424
1339:[], # Indices 21424 to 21440
1340:[], # Indices 21440 to 21456
1341:[], # Indices 21456 to 21472
1342:[], # Indices 21472 to 21488
1343:[], # Indices 21488 to 21504
1344:[], # Indices 21504 to 21520
1345:[], # Indices 21520 to 21536
1346:[], # Indices 21536 to 21552
1347:[], # Indices 21552 to 21568
1348:[], # Indices 21568 to 21584
1349:[], # Indices 21584 to 21600
1350:[], # Indices 21600 to 21616
1351:[], # Indices 21616 to 21632
1352:[], # Indices 21632 to 21648
1353:[], # Indices 21648 to 21664
1354:[], # Indices 21664 to 21680
1355:[], # Indices 21680 to 21696
1356:[], # Indices 21696 to 21712
1357:[], # Indices 21712 to 21728
1358:[], # Indices 21728 to 21744
1359:[], # Indices 21744 to 21760
1360:[], # Indices 21760 to 21776
1361:[], # Indices 21776 to 21792
1362:[], # Indices 21792 to 21808
1363:[], # Indices 21808 to 21824
1364:[], # Indices 21824 to 21840
1365:[], # Indices 21840 to 21856
1366:[], # Indices 21856 to 21872
1367:[], # Indices 21872 to 21888
1368:[], # Indices 21888 to 21904
1369:[], # Indices 21904 to 21920
1370:[], # Indices 21920 to 21936
1371:[], # Indices 21936 to 21952
1372:[], # Indices 21952 to 21968
1373:[], # Indices 21968 to 21984
1374:[], # Indices 21984 to 22000
1375:[], # Indices 22000 to 22016
1376:[], # Indices 22016 to 22032
1377:[], # Indices 22032 to 22048
1378:[], # Indices 22048 to 22064
1379:[], # Indices 22064 to 22080
1380:[], # Indices 22080 to 22096
1381:[], # Indices 22096 to 22112
1382:[], # Indices 22112 to 22128
1383:[], # Indices 22128 to 22144
1384:[], # Indices 22144 to 22160
1385:[], # Indices 22160 to 22176
1386:[], # Indices 22176 to 22192
1387:[], # Indices 22192 to 22208
1388:[], # Indices 22208 to 22224
1389:[], # Indices 22224 to 22240
1390:[], # Indices 22240 to 22256
1391:[], # Indices 22256 to 22272
1392:[], # Indices 22272 to 22288
1393:[], # Indices 22288 to 22304
1394:[], # Indices 22304 to 22320
1395:[], # Indices 22320 to 22336
1396:[], # Indices 22336 to 22352
1397:[], # Indices 22352 to 22368
1398:[], # Indices 22368 to 22384
1399:[], # Indices 22384 to 22400
1400:[], # Indices 22400 to 22416
1401:[], # Indices 22416 to 22432
1402:[], # Indices 22432 to 22448
1403:[], # Indices 22448 to 22464
1404:[], # Indices 22464 to 22480
1405:[], # Indices 22480 to 22496
1406:[], # Indices 22496 to 22512
1407:[], # Indices 22512 to 22528
1408:[], # Indices 22528 to 22544
1409:[], # Indices 22544 to 22560
1410:[], # Indices 22560 to 22576
1411:[], # Indices 22576 to 22592
1412:[], # Indices 22592 to 22608
1413:[], # Indices 22608 to 22624
1414:[], # Indices 22624 to 22640
1415:[{'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 478}], # Indices 22640 to 22656
1416:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 145}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 148}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 142}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 138}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 155}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 132}], # Indices 22656 to 22672
1417:[], # Indices 22672 to 22688
1418:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 248}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 251}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 246}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 279}], # Indices 22688 to 22704
1419:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 260}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 253}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 266}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 245}], # Indices 22704 to 22720
1420:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 116}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 139}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 144}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 150}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 151}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 143}], # Indices 22720 to 22736
1421:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 243}, {'index_dec': 4, 'index_bin': '0100', 'val': 14, 'counts': 255}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 286}, {'index_dec': 10, 'index_bin': '1010', 'val': 13, 'counts': 240}], # Indices 22736 to 22752
1422:[], # Indices 22752 to 22768
1423:[], # Indices 22768 to 22784
1424:[], # Indices 22784 to 22800
1425:[], # Indices 22800 to 22816
1426:[], # Indices 22816 to 22832
1427:[], # Indices 22832 to 22848
1428:[], # Indices 22848 to 22864
1429:[], # Indices 22864 to 22880
1430:[], # Indices 22880 to 22896
1431:[], # Indices 22896 to 22912
1432:[], # Indices 22912 to 22928
1433:[], # Indices 22928 to 22944
1434:[], # Indices 22944 to 22960
1435:[], # Indices 22960 to 22976
1436:[], # Indices 22976 to 22992
1437:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 163}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 142}, {'index_dec': 7, 'index_bin': '0111', 'val': 16, 'counts': 143}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 138}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 136}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 131}], # Indices 22992 to 23008
1438:[{'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 270}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 217}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 275}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 262}], # Indices 23008 to 23024
1439:[], # Indices 23024 to 23040
1440:[], # Indices 23040 to 23056
1441:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 177}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 180}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 221}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 192}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 204}], # Indices 23056 to 23072
1442:[{'index_dec': 0, 'index_bin': '0000', 'val': 16, 'counts': 209}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 192}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 190}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 174}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 215}], # Indices 23072 to 23088
1443:[{'index_dec': 9, 'index_bin': '1001', 'val': 15, 'counts': 456}], # Indices 23088 to 23104
1444:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 398}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 384}], # Indices 23104 to 23120
1445:[{'index_dec': 4, 'index_bin': '0100', 'val': 17, 'counts': 267}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 247}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 255}, {'index_dec': 11, 'index_bin': '1011', 'val': 15, 'counts': 255}], # Indices 23120 to 23136
1446:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 207}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 203}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 188}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 203}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 185}], # Indices 23136 to 23152
1447:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 201}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 190}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 186}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 201}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 207}], # Indices 23152 to 23168
1448:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 479}], # Indices 23168 to 23184
1449:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 338}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 311}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 329}], # Indices 23184 to 23200
1450:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 102}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 97}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 92}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 101}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 92}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 100}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 107}], # Indices 23200 to 23216
1451:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 267}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 242}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 264}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 251}], # Indices 23216 to 23232
1452:[], # Indices 23232 to 23248
1453:[], # Indices 23248 to 23264
1454:[], # Indices 23264 to 23280
1455:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 242}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 257}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 261}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 264}], # Indices 23280 to 23296
1456:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 109}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 95}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 113}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 96}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 96}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 95}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 106}], # Indices 23296 to 23312
1457:[{'index_dec': 0, 'index_bin': '0000', 'val': 12, 'counts': 205}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 198}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 180}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 193}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 209}], # Indices 23312 to 23328
1458:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 497}], # Indices 23328 to 23344
1459:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 398}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 411}], # Indices 23344 to 23360
1460:[{'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 297}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 346}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 320}], # Indices 23360 to 23376
1461:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 322}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 330}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 331}], # Indices 23376 to 23392
1462:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 405}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 393}], # Indices 23392 to 23408
1463:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 485}], # Indices 23408 to 23424
1464:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 380}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 437}], # Indices 23424 to 23440
1465:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 221}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 167}, {'index_dec': 4, 'index_bin': '0100', 'val': 15, 'counts': 191}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 203}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 198}], # Indices 23440 to 23456
1466:[{'index_dec': 3, 'index_bin': '0011', 'val': 15, 'counts': 490}], # Indices 23456 to 23472
1467:[{'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 258}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 237}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 254}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 275}], # Indices 23472 to 23488
1468:[{'index_dec': 10, 'index_bin': '1010', 'val': 15, 'counts': 376}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 414}], # Indices 23488 to 23504
1469:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 307}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 319}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 343}], # Indices 23504 to 23520
1470:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 282}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 236}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 237}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 269}], # Indices 23520 to 23536
1471:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 388}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 402}], # Indices 23536 to 23552
1472:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 465}], # Indices 23552 to 23568
1473:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 483}], # Indices 23568 to 23584
1474:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 146}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 147}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 131}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 145}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 146}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 130}], # Indices 23584 to 23600
1475:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 241}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 265}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 268}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 250}], # Indices 23600 to 23616
1476:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 187}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 182}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 194}, {'index_dec': 12, 'index_bin': '1100', 'val': 14, 'counts': 211}, {'index_dec': 15, 'index_bin': '1111', 'val': 16, 'counts': 201}], # Indices 23616 to 23632
1477:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 417}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 409}], # Indices 23632 to 23648
1478:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 481}], # Indices 23648 to 23664
1479:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 458}], # Indices 23664 to 23680
1480:[], # Indices 23680 to 23696
1481:[], # Indices 23696 to 23712
1482:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 491}], # Indices 23712 to 23728
1483:[], # Indices 23728 to 23744
1484:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 403}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 396}], # Indices 23744 to 23760
1485:[{'index_dec': 6, 'index_bin': '0110', 'val': 15, 'counts': 493}], # Indices 23760 to 23776
1486:[{'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 468}], # Indices 23776 to 23792
1487:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 369}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 436}], # Indices 23792 to 23808
1488:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 261}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 251}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 262}, {'index_dec': 12, 'index_bin': '1100', 'val': 14, 'counts': 250}], # Indices 23808 to 23824
1489:[], # Indices 23824 to 23840
1490:[{'index_dec': 14, 'index_bin': '1110', 'val': 13, 'counts': 507}], # Indices 23840 to 23856
1491:[{'index_dec': 13, 'index_bin': '1101', 'val': 13, 'counts': 490}], # Indices 23856 to 23872
1492:[], # Indices 23872 to 23888
1493:[], # Indices 23888 to 23904
1494:[{'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 466}], # Indices 23904 to 23920
1495:[{'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 497}], # Indices 23920 to 23936
1496:[], # Indices 23936 to 23952
1497:[], # Indices 23952 to 23968
1498:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 475}], # Indices 23968 to 23984
1499:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 496}], # Indices 23984 to 24000
1500:[{'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 470}], # Indices 24000 to 24016
1501:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 465}], # Indices 24016 to 24032
1502:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 336}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 316}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 328}], # Indices 24032 to 24048
1503:[], # Indices 24048 to 24064
1504:[], # Indices 24064 to 24080
1505:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 406}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 407}], # Indices 24080 to 24096
1506:[], # Indices 24096 to 24112
1507:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 329}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 344}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 306}], # Indices 24112 to 24128
1508:[], # Indices 24128 to 24144
1509:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 412}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 390}], # Indices 24144 to 24160
1510:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 478}], # Indices 24160 to 24176
1511:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 492}], # Indices 24176 to 24192
1512:[{'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 313}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 317}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 342}], # Indices 24192 to 24208
1513:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 411}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 408}], # Indices 24208 to 24224
1514:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 303}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 323}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 343}], # Indices 24224 to 24240
1515:[], # Indices 24240 to 24256
1516:[], # Indices 24256 to 24272
1517:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 420}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 380}], # Indices 24272 to 24288
1518:[{'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 392}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 415}], # Indices 24288 to 24304
1519:[{'index_dec': 5, 'index_bin': '0101', 'val': 15, 'counts': 516}], # Indices 24304 to 24320
1520:[], # Indices 24320 to 24336
1521:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 243}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 265}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 255}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 261}], # Indices 24336 to 24352
1522:[{'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 315}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 337}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 323}], # Indices 24352 to 24368
1523:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 457}], # Indices 24368 to 24384
1524:[{'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 498}], # Indices 24384 to 24400
1525:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 427}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 407}], # Indices 24400 to 24416
1526:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 242}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 276}, {'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 268}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 238}], # Indices 24416 to 24432
1527:[{'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 499}], # Indices 24432 to 24448
1528:[], # Indices 24448 to 24464
1529:[], # Indices 24464 to 24480
1530:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 388}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 419}], # Indices 24480 to 24496
1531:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 478}], # Indices 24496 to 24512
1532:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 407}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 388}], # Indices 24512 to 24528
1533:[{'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 479}], # Indices 24528 to 24544
1534:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 490}], # Indices 24544 to 24560
1535:[{'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 495}], # Indices 24560 to 24576
1536:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 385}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 420}], # Indices 24576 to 24592
1537:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 460}], # Indices 24592 to 24608
1538:[], # Indices 24608 to 24624
1539:[{'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 488}], # Indices 24624 to 24640
1540:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 491}], # Indices 24640 to 24656
1541:[{'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 386}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 421}], # Indices 24656 to 24672
1542:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 380}, {'index_dec': 9, 'index_bin': '1001', 'val': 15, 'counts': 397}], # Indices 24672 to 24688
1543:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 476}], # Indices 24688 to 24704
1544:[], # Indices 24704 to 24720
1545:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 402}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 392}], # Indices 24720 to 24736
1546:[], # Indices 24736 to 24752
1547:[{'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 396}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 405}], # Indices 24752 to 24768
1548:[], # Indices 24768 to 24784
1549:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 398}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 413}], # Indices 24784 to 24800
1550:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 491}], # Indices 24800 to 24816
1551:[{'index_dec': 15, 'index_bin': '1111', 'val': 13, 'counts': 489}], # Indices 24816 to 24832
1552:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 479}], # Indices 24832 to 24848
1553:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 404}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 403}], # Indices 24848 to 24864
1554:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 413}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 396}], # Indices 24864 to 24880
1555:[{'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 472}], # Indices 24880 to 24896
1556:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 503}], # Indices 24896 to 24912
1557:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 494}], # Indices 24912 to 24928
1558:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 520}], # Indices 24928 to 24944
1559:[], # Indices 24944 to 24960
1560:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 492}], # Indices 24960 to 24976
1561:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 403}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 380}], # Indices 24976 to 24992
1562:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 472}], # Indices 24992 to 25008
1563:[], # Indices 25008 to 25024
1564:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 303}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 321}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 338}], # Indices 25024 to 25040
1565:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 314}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 339}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 309}], # Indices 25040 to 25056
1566:[], # Indices 25056 to 25072
1567:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 380}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 401}], # Indices 25072 to 25088
1568:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 500}], # Indices 25088 to 25104
1569:[], # Indices 25104 to 25120
1570:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 472}], # Indices 25120 to 25136
1571:[], # Indices 25136 to 25152
1572:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 491}], # Indices 25152 to 25168
1573:[], # Indices 25168 to 25184
1574:[], # Indices 25184 to 25200
1575:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 467}], # Indices 25200 to 25216
1576:[{'index_dec': 8, 'index_bin': '1000', 'val': 12, 'counts': 409}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 387}], # Indices 25216 to 25232
1577:[{'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 457}], # Indices 25232 to 25248
1578:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 378}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 431}], # Indices 25248 to 25264
1579:[], # Indices 25264 to 25280
1580:[], # Indices 25280 to 25296
1581:[{'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 495}], # Indices 25296 to 25312
1582:[], # Indices 25312 to 25328
1583:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 495}], # Indices 25328 to 25344
1584:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 400}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 403}], # Indices 25344 to 25360
1585:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 363}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 434}], # Indices 25360 to 25376
1586:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 275}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 264}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 245}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 240}], # Indices 25376 to 25392
1587:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 499}], # Indices 25392 to 25408
1588:[], # Indices 25408 to 25424
1589:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 471}], # Indices 25424 to 25440
1590:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 395}, {'index_dec': 12, 'index_bin': '1100', 'val': 12, 'counts': 404}], # Indices 25440 to 25456
1591:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 500}], # Indices 25456 to 25472
1592:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 395}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 404}], # Indices 25472 to 25488
1593:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 481}], # Indices 25488 to 25504
1594:[{'index_dec': 11, 'index_bin': '1011', 'val': 13, 'counts': 496}], # Indices 25504 to 25520
1595:[{'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 479}], # Indices 25520 to 25536
1596:[], # Indices 25536 to 25552
1597:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 429}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 374}], # Indices 25552 to 25568
1598:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 451}], # Indices 25568 to 25584
1599:[], # Indices 25584 to 25600
1600:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 446}], # Indices 25600 to 25616
1601:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 398}, {'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 407}], # Indices 25616 to 25632
1602:[{'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 498}], # Indices 25632 to 25648
1603:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 476}], # Indices 25648 to 25664
1604:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 306}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 327}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 334}], # Indices 25664 to 25680
1605:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 319}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 307}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 340}], # Indices 25680 to 25696
1606:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 479}], # Indices 25696 to 25712
1607:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 398}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 388}], # Indices 25712 to 25728
1608:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 460}], # Indices 25728 to 25744
1609:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 267}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 263}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 251}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 243}], # Indices 25744 to 25760
1610:[], # Indices 25760 to 25776
1611:[], # Indices 25776 to 25792
1612:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 503}], # Indices 25792 to 25808
1613:[], # Indices 25808 to 25824
1614:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 403}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 390}], # Indices 25824 to 25840
1615:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 323}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 308}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 350}], # Indices 25840 to 25856
1616:[{'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 482}], # Indices 25856 to 25872
1617:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 429}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 355}], # Indices 25872 to 25888
1618:[{'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 368}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 409}], # Indices 25888 to 25904
1619:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 494}], # Indices 25904 to 25920
1620:[{'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 518}], # Indices 25920 to 25936
1621:[], # Indices 25936 to 25952
1622:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 466}], # Indices 25952 to 25968
1623:[], # Indices 25968 to 25984
1624:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 368}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 401}], # Indices 25984 to 26000
1625:[], # Indices 26000 to 26016
1626:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 197}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 221}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 185}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 192}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 198}], # Indices 26016 to 26032
1627:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 480}], # Indices 26032 to 26048
1628:[{'index_dec': 4, 'index_bin': '0100', 'val': 14, 'counts': 385}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 406}], # Indices 26048 to 26064
1629:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 499}], # Indices 26064 to 26080
1630:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 465}], # Indices 26080 to 26096
1631:[], # Indices 26096 to 26112
1632:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 270}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 241}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 255}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 258}], # Indices 26112 to 26128
1633:[{'index_dec': 1, 'index_bin': '0001', 'val': 14, 'counts': 334}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 332}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 298}], # Indices 26128 to 26144
1634:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 474}], # Indices 26144 to 26160
1635:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 462}], # Indices 26160 to 26176
1636:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 476}], # Indices 26176 to 26192
1637:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 488}], # Indices 26192 to 26208
1638:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 474}], # Indices 26208 to 26224
1639:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 451}], # Indices 26224 to 26240
1640:[], # Indices 26240 to 26256
1641:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 476}], # Indices 26256 to 26272
1642:[{'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 466}], # Indices 26272 to 26288
1643:[{'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 375}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 434}], # Indices 26288 to 26304
1644:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 484}], # Indices 26304 to 26320
1645:[], # Indices 26320 to 26336
1646:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 460}], # Indices 26336 to 26352
1647:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 393}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 404}], # Indices 26352 to 26368
1648:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 390}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 404}], # Indices 26368 to 26384
1649:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 289}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 374}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 322}], # Indices 26384 to 26400
1650:[], # Indices 26400 to 26416
1651:[], # Indices 26416 to 26432
1652:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 495}], # Indices 26432 to 26448
1653:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 485}], # Indices 26448 to 26464
1654:[{'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 495}], # Indices 26464 to 26480
1655:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 495}], # Indices 26480 to 26496
1656:[], # Indices 26496 to 26512
1657:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 478}], # Indices 26512 to 26528
1658:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 480}], # Indices 26528 to 26544
1659:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 438}], # Indices 26544 to 26560
1660:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 413}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 408}], # Indices 26560 to 26576
1661:[{'index_dec': 4, 'index_bin': '0100', 'val': 12, 'counts': 481}], # Indices 26576 to 26592
1662:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 470}], # Indices 26592 to 26608
1663:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 419}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 380}], # Indices 26608 to 26624
1664:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 472}], # Indices 26624 to 26640
1665:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 415}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 379}], # Indices 26640 to 26656
1666:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 448}], # Indices 26656 to 26672
1667:[], # Indices 26672 to 26688
1668:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 328}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 322}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 317}], # Indices 26688 to 26704
1669:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 399}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 428}], # Indices 26704 to 26720
1670:[], # Indices 26720 to 26736
1671:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 350}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 299}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 325}], # Indices 26736 to 26752
1672:[], # Indices 26752 to 26768
1673:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 488}], # Indices 26768 to 26784
1674:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 320}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 322}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 335}], # Indices 26784 to 26800
1675:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 502}], # Indices 26800 to 26816
1676:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 500}], # Indices 26816 to 26832
1677:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 482}], # Indices 26832 to 26848
1678:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 501}], # Indices 26848 to 26864
1679:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 456}], # Indices 26864 to 26880
1680:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 198}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 199}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 207}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 182}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 194}], # Indices 26880 to 26896
1681:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 411}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 373}], # Indices 26896 to 26912
1682:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 387}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 408}], # Indices 26912 to 26928
1683:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 393}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 415}], # Indices 26928 to 26944
1684:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 498}], # Indices 26944 to 26960
1685:[{'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 458}], # Indices 26960 to 26976
1686:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 307}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 312}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 358}], # Indices 26976 to 26992
1687:[], # Indices 26992 to 27008
1688:[], # Indices 27008 to 27024
1689:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 486}], # Indices 27024 to 27040
1690:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 415}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 406}], # Indices 27040 to 27056
1691:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 517}], # Indices 27056 to 27072
1692:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 395}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 387}], # Indices 27072 to 27088
1693:[], # Indices 27088 to 27104
1694:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 486}], # Indices 27104 to 27120
1695:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 405}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 419}], # Indices 27120 to 27136
1696:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 332}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 355}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 283}], # Indices 27136 to 27152
1697:[], # Indices 27152 to 27168
1698:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 338}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 320}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 317}], # Indices 27168 to 27184
1699:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 491}], # Indices 27184 to 27200
1700:[{'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 405}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 390}], # Indices 27200 to 27216
1701:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 315}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 312}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 346}], # Indices 27216 to 27232
1702:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 389}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 414}], # Indices 27232 to 27248
1703:[], # Indices 27248 to 27264
1704:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 336}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 338}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 309}], # Indices 27264 to 27280
1705:[], # Indices 27280 to 27296
1706:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 350}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 300}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 330}], # Indices 27296 to 27312
1707:[], # Indices 27312 to 27328
1708:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 491}], # Indices 27328 to 27344
1709:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 358}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 309}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 314}], # Indices 27344 to 27360
1710:[{'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 334}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 323}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 312}], # Indices 27360 to 27376
1711:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 314}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 336}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 318}], # Indices 27376 to 27392
1712:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 337}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 321}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 305}], # Indices 27392 to 27408
1713:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 409}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 387}], # Indices 27408 to 27424
1714:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 478}], # Indices 27424 to 27440
1715:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 472}], # Indices 27440 to 27456
1716:[], # Indices 27456 to 27472
1717:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 484}], # Indices 27472 to 27488
1718:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 401}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 412}], # Indices 27488 to 27504
1719:[], # Indices 27504 to 27520
1720:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 334}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 303}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 336}], # Indices 27520 to 27536
1721:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 334}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 331}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 308}], # Indices 27536 to 27552
1722:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 489}], # Indices 27552 to 27568
1723:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 423}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 386}], # Indices 27568 to 27584
1724:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 406}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 393}], # Indices 27584 to 27600
1725:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 489}], # Indices 27600 to 27616
1726:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 490}], # Indices 27616 to 27632
1727:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 416}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 397}], # Indices 27632 to 27648
1728:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 478}], # Indices 27648 to 27664
1729:[], # Indices 27664 to 27680
1730:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 331}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 313}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 326}], # Indices 27680 to 27696
1731:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 480}], # Indices 27696 to 27712
1732:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 500}], # Indices 27712 to 27728
1733:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 498}], # Indices 27728 to 27744
1734:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 460}], # Indices 27744 to 27760
1735:[{'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 494}], # Indices 27760 to 27776
1736:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 244}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 271}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 251}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 258}], # Indices 27776 to 27792
1737:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 456}], # Indices 27792 to 27808
1738:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 311}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 341}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 321}], # Indices 27808 to 27824
1739:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 416}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 388}], # Indices 27824 to 27840
1740:[], # Indices 27840 to 27856
1741:[], # Indices 27856 to 27872
1742:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 338}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 334}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 298}], # Indices 27872 to 27888
1743:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 391}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 409}], # Indices 27888 to 27904
1744:[{'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 404}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 394}], # Indices 27904 to 27920
1745:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 295}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 330}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 340}], # Indices 27920 to 27936
1746:[{'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 450}], # Indices 27936 to 27952
1747:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 199}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 195}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 193}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 201}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 194}], # Indices 27952 to 27968
1748:[], # Indices 27968 to 27984
1749:[], # Indices 27984 to 28000
1750:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 495}], # Indices 28000 to 28016
1751:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 503}], # Indices 28016 to 28032
1752:[], # Indices 28032 to 28048
1753:[], # Indices 28048 to 28064
1754:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 505}], # Indices 28064 to 28080
1755:[], # Indices 28080 to 28096
1756:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 472}], # Indices 28096 to 28112
1757:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 397}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 404}], # Indices 28112 to 28128
1758:[], # Indices 28128 to 28144
1759:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 485}], # Indices 28144 to 28160
1760:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 465}], # Indices 28160 to 28176
1761:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 481}], # Indices 28176 to 28192
1762:[], # Indices 28192 to 28208
1763:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 396}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 419}], # Indices 28208 to 28224
1764:[], # Indices 28224 to 28240
1765:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 182}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 197}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 206}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 190}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 201}], # Indices 28240 to 28256
1766:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 398}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 406}], # Indices 28256 to 28272
1767:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 478}], # Indices 28272 to 28288
1768:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 387}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 424}], # Indices 28288 to 28304
1769:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 472}], # Indices 28304 to 28320
1770:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 497}], # Indices 28320 to 28336
1771:[], # Indices 28336 to 28352
1772:[], # Indices 28352 to 28368
1773:[], # Indices 28368 to 28384
1774:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 402}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 403}], # Indices 28384 to 28400
1775:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 484}], # Indices 28400 to 28416
1776:[], # Indices 28416 to 28432
1777:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 483}], # Indices 28432 to 28448
1778:[], # Indices 28448 to 28464
1779:[], # Indices 28464 to 28480
1780:[], # Indices 28480 to 28496
1781:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 504}], # Indices 28496 to 28512
1782:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 439}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 377}], # Indices 28512 to 28528
1783:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 389}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 414}], # Indices 28528 to 28544
1784:[], # Indices 28544 to 28560
1785:[], # Indices 28560 to 28576
1786:[], # Indices 28576 to 28592
1787:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 394}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 419}], # Indices 28592 to 28608
1788:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 467}], # Indices 28608 to 28624
1789:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 502}], # Indices 28624 to 28640
1790:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 493}], # Indices 28640 to 28656
1791:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 468}], # Indices 28656 to 28672
1792:[], # Indices 28672 to 28688
1793:[], # Indices 28688 to 28704
1794:[], # Indices 28704 to 28720
1795:[], # Indices 28720 to 28736
1796:[], # Indices 28736 to 28752
1797:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 488}], # Indices 28752 to 28768
1798:[], # Indices 28768 to 28784
1799:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 479}], # Indices 28784 to 28800
1800:[], # Indices 28800 to 28816
1801:[], # Indices 28816 to 28832
1802:[], # Indices 28832 to 28848
1803:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 476}], # Indices 28848 to 28864
1804:[], # Indices 28864 to 28880
1805:[], # Indices 28880 to 28896
1806:[], # Indices 28896 to 28912
1807:[], # Indices 28912 to 28928
1808:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 459}], # Indices 28928 to 28944
1809:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 475}], # Indices 28944 to 28960
1810:[], # Indices 28960 to 28976
1811:[], # Indices 28976 to 28992
1812:[], # Indices 28992 to 29008
1813:[], # Indices 29008 to 29024
1814:[], # Indices 29024 to 29040
1815:[], # Indices 29040 to 29056
1816:[], # Indices 29056 to 29072
1817:[], # Indices 29072 to 29088
1818:[], # Indices 29088 to 29104
1819:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 458}], # Indices 29104 to 29120
1820:[], # Indices 29120 to 29136
1821:[], # Indices 29136 to 29152
1822:[], # Indices 29152 to 29168
1823:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 503}], # Indices 29168 to 29184
1824:[], # Indices 29184 to 29200
1825:[], # Indices 29200 to 29216
1826:[], # Indices 29216 to 29232
1827:[], # Indices 29232 to 29248
1828:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 472}], # Indices 29248 to 29264
1829:[], # Indices 29264 to 29280
1830:[], # Indices 29280 to 29296
1831:[], # Indices 29296 to 29312
1832:[], # Indices 29312 to 29328
1833:[], # Indices 29328 to 29344
1834:[], # Indices 29344 to 29360
1835:[], # Indices 29360 to 29376
1836:[], # Indices 29376 to 29392
1837:[], # Indices 29392 to 29408
1838:[], # Indices 29408 to 29424
1839:[], # Indices 29424 to 29440
1840:[], # Indices 29440 to 29456
1841:[], # Indices 29456 to 29472
1842:[], # Indices 29472 to 29488
1843:[], # Indices 29488 to 29504
1844:[], # Indices 29504 to 29520
1845:[], # Indices 29520 to 29536
1846:[], # Indices 29536 to 29552
1847:[], # Indices 29552 to 29568
1848:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 502}], # Indices 29568 to 29584
1849:[], # Indices 29584 to 29600
1850:[], # Indices 29600 to 29616
1851:[], # Indices 29616 to 29632
1852:[], # Indices 29632 to 29648
1853:[{'index_dec': 14, 'index_bin': '1110', 'val': 5, 'counts': 98}], # Indices 29648 to 29664
1854:[], # Indices 29664 to 29680
1855:[], # Indices 29680 to 29696
1856:[], # Indices 29696 to 29712
1857:[], # Indices 29712 to 29728
1858:[], # Indices 29728 to 29744
1859:[], # Indices 29744 to 29760
1860:[], # Indices 29760 to 29776
1861:[], # Indices 29776 to 29792
1862:[], # Indices 29792 to 29808
1863:[], # Indices 29808 to 29824
1864:[], # Indices 29824 to 29840
1865:[], # Indices 29840 to 29856
1866:[], # Indices 29856 to 29872
1867:[], # Indices 29872 to 29888
1868:[], # Indices 29888 to 29904
1869:[], # Indices 29904 to 29920
1870:[], # Indices 29920 to 29936
1871:[], # Indices 29936 to 29952
1872:[], # Indices 29952 to 29968
1873:[], # Indices 29968 to 29984
1874:[], # Indices 29984 to 30000
1875:[], # Indices 30000 to 30016
1876:[], # Indices 30016 to 30032
1877:[], # Indices 30032 to 30048
1878:[], # Indices 30048 to 30064
1879:[], # Indices 30064 to 30080
1880:[], # Indices 30080 to 30096
1881:[], # Indices 30096 to 30112
1882:[], # Indices 30112 to 30128
1883:[], # Indices 30128 to 30144
1884:[], # Indices 30144 to 30160
1885:[], # Indices 30160 to 30176
1886:[], # Indices 30176 to 30192
1887:[], # Indices 30192 to 30208
1888:[], # Indices 30208 to 30224
1889:[], # Indices 30224 to 30240
1890:[], # Indices 30240 to 30256
1891:[], # Indices 30256 to 30272
1892:[], # Indices 30272 to 30288
1893:[], # Indices 30288 to 30304
1894:[], # Indices 30304 to 30320
1895:[], # Indices 30320 to 30336
1896:[], # Indices 30336 to 30352
1897:[], # Indices 30352 to 30368
1898:[], # Indices 30368 to 30384
1899:[], # Indices 30384 to 30400
1900:[], # Indices 30400 to 30416
1901:[], # Indices 30416 to 30432
1902:[], # Indices 30432 to 30448
1903:[], # Indices 30448 to 30464
1904:[], # Indices 30464 to 30480
1905:[], # Indices 30480 to 30496
1906:[], # Indices 30496 to 30512
1907:[], # Indices 30512 to 30528
1908:[], # Indices 30528 to 30544
1909:[], # Indices 30544 to 30560
1910:[], # Indices 30560 to 30576
1911:[], # Indices 30576 to 30592
1912:[], # Indices 30592 to 30608
1913:[], # Indices 30608 to 30624
1914:[], # Indices 30624 to 30640
1915:[], # Indices 30640 to 30656
1916:[], # Indices 30656 to 30672
1917:[], # Indices 30672 to 30688
1918:[], # Indices 30688 to 30704
1919:[], # Indices 30704 to 30720
1920:[], # Indices 30720 to 30736
1921:[], # Indices 30736 to 30752
1922:[], # Indices 30752 to 30768
1923:[], # Indices 30768 to 30784
1924:[], # Indices 30784 to 30800
1925:[], # Indices 30800 to 30816
1926:[], # Indices 30816 to 30832
1927:[], # Indices 30832 to 30848
1928:[], # Indices 30848 to 30864
1929:[], # Indices 30864 to 30880
1930:[], # Indices 30880 to 30896
1931:[], # Indices 30896 to 30912
1932:[], # Indices 30912 to 30928
1933:[{'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 94}], # Indices 30928 to 30944
1934:[], # Indices 30944 to 30960
1935:[], # Indices 30960 to 30976
1936:[], # Indices 30976 to 30992
1937:[], # Indices 30992 to 31008
1938:[], # Indices 31008 to 31024
1939:[], # Indices 31024 to 31040
1940:[], # Indices 31040 to 31056
1941:[], # Indices 31056 to 31072
1942:[], # Indices 31072 to 31088
1943:[], # Indices 31088 to 31104
1944:[], # Indices 31104 to 31120
1945:[], # Indices 31120 to 31136
1946:[], # Indices 31136 to 31152
1947:[], # Indices 31152 to 31168
1948:[], # Indices 31168 to 31184
1949:[], # Indices 31184 to 31200
1950:[], # Indices 31200 to 31216
1951:[], # Indices 31216 to 31232
1952:[], # Indices 31232 to 31248
1953:[], # Indices 31248 to 31264
1954:[], # Indices 31264 to 31280
1955:[], # Indices 31280 to 31296
1956:[], # Indices 31296 to 31312
1957:[], # Indices 31312 to 31328
1958:[], # Indices 31328 to 31344
1959:[], # Indices 31344 to 31360
1960:[], # Indices 31360 to 31376
1961:[], # Indices 31376 to 31392
1962:[], # Indices 31392 to 31408
1963:[], # Indices 31408 to 31424
1964:[], # Indices 31424 to 31440
1965:[], # Indices 31440 to 31456
1966:[], # Indices 31456 to 31472
1967:[], # Indices 31472 to 31488
1968:[], # Indices 31488 to 31504
1969:[], # Indices 31504 to 31520
1970:[], # Indices 31520 to 31536
1971:[], # Indices 31536 to 31552
1972:[], # Indices 31552 to 31568
1973:[], # Indices 31568 to 31584
1974:[], # Indices 31584 to 31600
1975:[], # Indices 31600 to 31616
1976:[], # Indices 31616 to 31632
1977:[], # Indices 31632 to 31648
1978:[], # Indices 31648 to 31664
1979:[], # Indices 31664 to 31680
1980:[], # Indices 31680 to 31696
1981:[], # Indices 31696 to 31712
1982:[], # Indices 31712 to 31728
1983:[], # Indices 31728 to 31744
1984:[], # Indices 31744 to 31760
1985:[], # Indices 31760 to 31776
1986:[], # Indices 31776 to 31792
1987:[], # Indices 31792 to 31808
1988:[], # Indices 31808 to 31824
1989:[], # Indices 31824 to 31840
1990:[], # Indices 31840 to 31856
1991:[], # Indices 31856 to 31872
1992:[], # Indices 31872 to 31888
1993:[], # Indices 31888 to 31904
1994:[], # Indices 31904 to 31920
1995:[], # Indices 31920 to 31936
1996:[], # Indices 31936 to 31952
1997:[], # Indices 31952 to 31968
1998:[], # Indices 31968 to 31984
1999:[], # Indices 31984 to 32000
2000:[], # Indices 32000 to 32016
2001:[], # Indices 32016 to 32032
2002:[], # Indices 32032 to 32048
2003:[], # Indices 32048 to 32064
2004:[], # Indices 32064 to 32080
2005:[], # Indices 32080 to 32096
2006:[], # Indices 32096 to 32112
2007:[], # Indices 32112 to 32128
2008:[], # Indices 32128 to 32144
2009:[], # Indices 32144 to 32160
2010:[], # Indices 32160 to 32176
2011:[], # Indices 32176 to 32192
2012:[], # Indices 32192 to 32208
2013:[], # Indices 32208 to 32224
2014:[], # Indices 32224 to 32240
2015:[], # Indices 32240 to 32256
2016:[], # Indices 32256 to 32272
2017:[], # Indices 32272 to 32288
2018:[], # Indices 32288 to 32304
2019:[{'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 449}], # Indices 32304 to 32320
2020:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 121}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 93}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 108}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 99}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 102}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 104}], # Indices 32320 to 32336
2021:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 204}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 186}, {'index_dec': 12, 'index_bin': '1100', 'val': 12, 'counts': 209}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 179}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 200}], # Indices 32336 to 32352
2022:[], # Indices 32352 to 32368
2023:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 320}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 334}, {'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 304}], # Indices 32368 to 32384
2024:[], # Indices 32384 to 32400
2025:[], # Indices 32400 to 32416
2026:[], # Indices 32416 to 32432
2027:[], # Indices 32432 to 32448
2028:[], # Indices 32448 to 32464
2029:[], # Indices 32464 to 32480
2030:[], # Indices 32480 to 32496
2031:[], # Indices 32496 to 32512
2032:[], # Indices 32512 to 32528
2033:[], # Indices 32528 to 32544
2034:[], # Indices 32544 to 32560
2035:[], # Indices 32560 to 32576
2036:[], # Indices 32576 to 32592
2037:[], # Indices 32592 to 32608
2038:[], # Indices 32608 to 32624
2039:[], # Indices 32624 to 32640
2040:[{'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 488}], # Indices 32640 to 32656
2041:[{'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 491}], # Indices 32656 to 32672
2042:[{'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 467}], # Indices 32672 to 32688
2043:[{'index_dec': 1, 'index_bin': '0001', 'val': 16, 'counts': 381}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 417}], # Indices 32688 to 32704
2044:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 340}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 323}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 308}], # Indices 32704 to 32720
2045:[{'index_dec': 0, 'index_bin': '0000', 'val': 12, 'counts': 373}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 413}], # Indices 32720 to 32736
2046:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 484}], # Indices 32736 to 32752
2047:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 386}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 414}], # Indices 32752 to 32768
2048:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 415}, {'index_dec': 5, 'index_bin': '0101', 'val': 14, 'counts': 394}], # Indices 32768 to 32784
2049:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 382}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 410}], # Indices 32784 to 32800
2050:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 243}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 267}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 246}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 268}], # Indices 32800 to 32816
2051:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 315}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 336}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 339}], # Indices 32816 to 32832
2052:[{'index_dec': 0, 'index_bin': '0000', 'val': 14, 'counts': 256}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 267}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 262}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 239}], # Indices 32832 to 32848
2053:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 146}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 135}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 157}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 130}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 129}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 163}], # Indices 32848 to 32864
2054:[{'index_dec': 3, 'index_bin': '0011', 'val': 16, 'counts': 325}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 326}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 317}], # Indices 32864 to 32880
2055:[], # Indices 32880 to 32896
2056:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 186}, {'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 191}, {'index_dec': 7, 'index_bin': '0111', 'val': 17, 'counts': 193}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 203}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 210}], # Indices 32896 to 32912
2057:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 246}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 262}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 262}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 254}], # Indices 32912 to 32928
2058:[{'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 475}], # Indices 32928 to 32944
2059:[{'index_dec': 9, 'index_bin': '1001', 'val': 17, 'counts': 324}, {'index_dec': 10, 'index_bin': '1010', 'val': 17, 'counts': 323}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 333}], # Indices 32944 to 32960
2060:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 344}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 335}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 300}], # Indices 32960 to 32976
2061:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 325}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 343}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 306}], # Indices 32976 to 32992
2062:[{'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 487}], # Indices 32992 to 33008
2063:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 307}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 326}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 335}], # Indices 33008 to 33024
2064:[{'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 475}], # Indices 33024 to 33040
2065:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 510}], # Indices 33040 to 33056
2066:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 410}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 392}], # Indices 33056 to 33072
2067:[{'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 491}], # Indices 33072 to 33088
2068:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 494}], # Indices 33088 to 33104
2069:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 326}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 322}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 320}], # Indices 33104 to 33120
2070:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 321}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 334}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 313}], # Indices 33120 to 33136
2071:[{'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 478}], # Indices 33136 to 33152
2072:[{'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 401}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 393}], # Indices 33152 to 33168
2073:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 386}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 412}], # Indices 33168 to 33184
2074:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 393}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 414}], # Indices 33184 to 33200
2075:[{'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 331}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 306}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 322}], # Indices 33200 to 33216
2076:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 478}], # Indices 33216 to 33232
2077:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 418}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 404}], # Indices 33232 to 33248
2078:[], # Indices 33248 to 33264
2079:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 400}, {'index_dec': 7, 'index_bin': '0111', 'val': 14, 'counts': 419}], # Indices 33264 to 33280
2080:[{'index_dec': 5, 'index_bin': '0101', 'val': 15, 'counts': 383}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 419}], # Indices 33280 to 33296
2081:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 490}], # Indices 33296 to 33312
2082:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 516}], # Indices 33312 to 33328
2083:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 475}], # Indices 33328 to 33344
2084:[], # Indices 33344 to 33360
2085:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 503}], # Indices 33360 to 33376
2086:[], # Indices 33376 to 33392
2087:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 480}], # Indices 33392 to 33408
2088:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 394}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 407}], # Indices 33408 to 33424
2089:[{'index_dec': 5, 'index_bin': '0101', 'val': 14, 'counts': 236}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 257}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 248}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 283}], # Indices 33424 to 33440
2090:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 286}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 251}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 243}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 244}], # Indices 33440 to 33456
2091:[{'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 387}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 411}], # Indices 33456 to 33472
2092:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 395}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 394}], # Indices 33472 to 33488
2093:[], # Indices 33488 to 33504
2094:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 407}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 404}], # Indices 33504 to 33520
2095:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 473}], # Indices 33520 to 33536
2096:[], # Indices 33536 to 33552
2097:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 385}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 417}], # Indices 33552 to 33568
2098:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 465}], # Indices 33568 to 33584
2099:[{'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 409}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 393}], # Indices 33584 to 33600
2100:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 404}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 385}], # Indices 33600 to 33616
2101:[], # Indices 33616 to 33632
2102:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 326}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 329}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 324}], # Indices 33632 to 33648
2103:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 476}], # Indices 33648 to 33664
2104:[{'index_dec': 7, 'index_bin': '0111', 'val': 14, 'counts': 418}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 382}], # Indices 33664 to 33680
2105:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 146}, {'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 142}, {'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 133}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 152}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 135}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 157}], # Indices 33680 to 33696
2106:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 187}, {'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 189}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 206}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 203}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 187}], # Indices 33696 to 33712
2107:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 317}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 317}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 322}], # Indices 33712 to 33728
2108:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 302}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 323}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 357}], # Indices 33728 to 33744
2109:[{'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 355}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 323}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 302}], # Indices 33744 to 33760
2110:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 390}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 430}], # Indices 33760 to 33776
2111:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 345}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 311}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 325}], # Indices 33776 to 33792
2112:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 500}], # Indices 33792 to 33808
2113:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 426}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 369}], # Indices 33808 to 33824
2114:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 396}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 390}], # Indices 33824 to 33840
2115:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 474}], # Indices 33840 to 33856
2116:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 466}], # Indices 33856 to 33872
2117:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 332}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 297}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 335}], # Indices 33872 to 33888
2118:[], # Indices 33888 to 33904
2119:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 387}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 403}], # Indices 33904 to 33920
2120:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 503}], # Indices 33920 to 33936
2121:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 279}, {'index_dec': 2, 'index_bin': '0010', 'val': 14, 'counts': 252}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 247}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 246}], # Indices 33936 to 33952
2122:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 296}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 343}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 332}], # Indices 33952 to 33968
2123:[], # Indices 33968 to 33984
2124:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 173}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 208}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 213}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 195}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 194}], # Indices 33984 to 34000
2125:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 417}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 377}], # Indices 34000 to 34016
2126:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 480}], # Indices 34016 to 34032
2127:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 316}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 319}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 334}], # Indices 34032 to 34048
2128:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 376}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 430}], # Indices 34048 to 34064
2129:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 472}], # Indices 34064 to 34080
2130:[{'index_dec': 14, 'index_bin': '1110', 'val': 13, 'counts': 498}], # Indices 34080 to 34096
2131:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 488}], # Indices 34096 to 34112
2132:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 498}], # Indices 34112 to 34128
2133:[{'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 489}], # Indices 34128 to 34144
2134:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 495}], # Indices 34144 to 34160
2135:[], # Indices 34160 to 34176
2136:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 400}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 376}], # Indices 34176 to 34192
2137:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 497}], # Indices 34192 to 34208
2138:[], # Indices 34208 to 34224
2139:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 328}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 312}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 336}], # Indices 34224 to 34240
2140:[{'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 503}], # Indices 34240 to 34256
2141:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 323}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 339}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 307}], # Indices 34256 to 34272
2142:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 424}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 398}], # Indices 34272 to 34288
2143:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 322}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 322}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 326}], # Indices 34288 to 34304
2144:[], # Indices 34304 to 34320
2145:[], # Indices 34320 to 34336
2146:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 430}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 375}], # Indices 34336 to 34352
2147:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 404}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 390}], # Indices 34352 to 34368
2148:[], # Indices 34368 to 34384
2149:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 414}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 397}], # Indices 34384 to 34400
2150:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 524}], # Indices 34400 to 34416
2151:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 405}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 399}], # Indices 34416 to 34432
2152:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 503}], # Indices 34432 to 34448
2153:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 476}], # Indices 34448 to 34464
2154:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 418}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 371}], # Indices 34464 to 34480
2155:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 389}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 413}], # Indices 34480 to 34496
2156:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 490}], # Indices 34496 to 34512
2157:[{'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 331}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 333}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 319}], # Indices 34512 to 34528
2158:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 412}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 396}], # Indices 34528 to 34544
2159:[], # Indices 34544 to 34560
2160:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 493}], # Indices 34560 to 34576
2161:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 409}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 409}], # Indices 34576 to 34592
2162:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 252}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 265}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 277}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 230}], # Indices 34592 to 34608
2163:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 251}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 256}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 258}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 259}], # Indices 34608 to 34624
2164:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 508}], # Indices 34624 to 34640
2165:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 495}], # Indices 34640 to 34656
2166:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 395}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 402}], # Indices 34656 to 34672
2167:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 347}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 324}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 298}], # Indices 34672 to 34688
2168:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 404}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 378}], # Indices 34688 to 34704
2169:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 458}], # Indices 34704 to 34720
2170:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 307}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 311}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 348}], # Indices 34720 to 34736
2171:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 323}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 338}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 312}], # Indices 34736 to 34752
2172:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 328}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 334}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 307}], # Indices 34752 to 34768
2173:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 504}], # Indices 34768 to 34784
2174:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 412}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 386}], # Indices 34784 to 34800
2175:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 463}], # Indices 34800 to 34816
2176:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 360}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 423}], # Indices 34816 to 34832
2177:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 420}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 392}], # Indices 34832 to 34848
2178:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 418}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 363}], # Indices 34848 to 34864
2179:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 384}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 410}], # Indices 34864 to 34880
2180:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 476}], # Indices 34880 to 34896
2181:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 413}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 384}], # Indices 34896 to 34912
2182:[{'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 416}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 363}], # Indices 34912 to 34928
2183:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 321}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 340}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 309}], # Indices 34928 to 34944
2184:[], # Indices 34944 to 34960
2185:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 313}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 326}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 327}], # Indices 34960 to 34976
2186:[{'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 446}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 373}], # Indices 34976 to 34992
2187:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 319}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 328}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 329}], # Indices 34992 to 35008
2188:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 393}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 407}], # Indices 35008 to 35024
2189:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 502}], # Indices 35024 to 35040
2190:[], # Indices 35040 to 35056
2191:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 398}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 410}], # Indices 35056 to 35072
2192:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 311}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 319}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 338}], # Indices 35072 to 35088
2193:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 319}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 295}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 360}], # Indices 35088 to 35104
2194:[], # Indices 35104 to 35120
2195:[], # Indices 35120 to 35136
2196:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 411}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 388}], # Indices 35136 to 35152
2197:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 509}], # Indices 35152 to 35168
2198:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 395}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 390}], # Indices 35168 to 35184
2199:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 345}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 324}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 304}], # Indices 35184 to 35200
2200:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 458}], # Indices 35200 to 35216
2201:[], # Indices 35216 to 35232
2202:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 425}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 375}], # Indices 35232 to 35248
2203:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 381}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 422}], # Indices 35248 to 35264
2204:[], # Indices 35264 to 35280
2205:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 338}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 346}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 288}], # Indices 35280 to 35296
2206:[], # Indices 35296 to 35312
2207:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 409}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 413}], # Indices 35312 to 35328
2208:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 507}], # Indices 35328 to 35344
2209:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 481}], # Indices 35344 to 35360
2210:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 494}], # Indices 35360 to 35376
2211:[], # Indices 35376 to 35392
2212:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 468}], # Indices 35392 to 35408
2213:[], # Indices 35408 to 35424
2214:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 463}], # Indices 35424 to 35440
2215:[], # Indices 35440 to 35456
2216:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 354}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 312}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 311}], # Indices 35456 to 35472
2217:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 461}], # Indices 35472 to 35488
2218:[{'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 469}], # Indices 35488 to 35504
2219:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 488}], # Indices 35504 to 35520
2220:[], # Indices 35520 to 35536
2221:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 473}], # Indices 35536 to 35552
2222:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 486}], # Indices 35552 to 35568
2223:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 491}], # Indices 35568 to 35584
2224:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 479}], # Indices 35584 to 35600
2225:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 477}], # Indices 35600 to 35616
2226:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 467}], # Indices 35616 to 35632
2227:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 414}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 397}], # Indices 35632 to 35648
2228:[], # Indices 35648 to 35664
2229:[], # Indices 35664 to 35680
2230:[], # Indices 35680 to 35696
2231:[], # Indices 35696 to 35712
2232:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 464}], # Indices 35712 to 35728
2233:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 500}], # Indices 35728 to 35744
2234:[], # Indices 35744 to 35760
2235:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 483}], # Indices 35760 to 35776
2236:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 385}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 412}], # Indices 35776 to 35792
2237:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 485}], # Indices 35792 to 35808
2238:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 403}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 376}], # Indices 35808 to 35824
2239:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 474}], # Indices 35824 to 35840
2240:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 479}], # Indices 35840 to 35856
2241:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 492}], # Indices 35856 to 35872
2242:[], # Indices 35872 to 35888
2243:[], # Indices 35888 to 35904
2244:[], # Indices 35904 to 35920
2245:[], # Indices 35920 to 35936
2246:[], # Indices 35936 to 35952
2247:[{'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 384}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 377}], # Indices 35952 to 35968
2248:[], # Indices 35968 to 35984
2249:[], # Indices 35984 to 36000
2250:[], # Indices 36000 to 36016
2251:[], # Indices 36016 to 36032
2252:[], # Indices 36032 to 36048
2253:[], # Indices 36048 to 36064
2254:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 455}], # Indices 36064 to 36080
2255:[], # Indices 36080 to 36096
2256:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 472}], # Indices 36096 to 36112
2257:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 484}], # Indices 36112 to 36128
2258:[], # Indices 36128 to 36144
2259:[], # Indices 36144 to 36160
2260:[], # Indices 36160 to 36176
2261:[], # Indices 36176 to 36192
2262:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 467}], # Indices 36192 to 36208
2263:[], # Indices 36208 to 36224
2264:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 396}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 382}], # Indices 36224 to 36240
2265:[], # Indices 36240 to 36256
2266:[], # Indices 36256 to 36272
2267:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 483}], # Indices 36272 to 36288
2268:[], # Indices 36288 to 36304
2269:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 492}], # Indices 36304 to 36320
2270:[], # Indices 36320 to 36336
2271:[], # Indices 36336 to 36352
2272:[], # Indices 36352 to 36368
2273:[], # Indices 36368 to 36384
2274:[], # Indices 36384 to 36400
2275:[], # Indices 36400 to 36416
2276:[], # Indices 36416 to 36432
2277:[], # Indices 36432 to 36448
2278:[], # Indices 36448 to 36464
2279:[], # Indices 36464 to 36480
2280:[], # Indices 36480 to 36496
2281:[], # Indices 36496 to 36512
2282:[], # Indices 36512 to 36528
2283:[], # Indices 36528 to 36544
2284:[], # Indices 36544 to 36560
2285:[], # Indices 36560 to 36576
2286:[], # Indices 36576 to 36592
2287:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 494}], # Indices 36592 to 36608
2288:[], # Indices 36608 to 36624
2289:[], # Indices 36624 to 36640
2290:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 507}], # Indices 36640 to 36656
2291:[], # Indices 36656 to 36672
2292:[], # Indices 36672 to 36688
2293:[], # Indices 36688 to 36704
2294:[], # Indices 36704 to 36720
2295:[], # Indices 36720 to 36736
2296:[], # Indices 36736 to 36752
2297:[], # Indices 36752 to 36768
2298:[], # Indices 36768 to 36784
2299:[], # Indices 36784 to 36800
2300:[{'index_dec': 2, 'index_bin': '0010', 'val': 4, 'counts': 92}], # Indices 36800 to 36816
2301:[], # Indices 36816 to 36832
2302:[], # Indices 36832 to 36848
2303:[], # Indices 36848 to 36864
2304:[], # Indices 36864 to 36880
2305:[], # Indices 36880 to 36896
2306:[], # Indices 36896 to 36912
2307:[], # Indices 36912 to 36928
2308:[], # Indices 36928 to 36944
2309:[], # Indices 36944 to 36960
2310:[], # Indices 36960 to 36976
2311:[], # Indices 36976 to 36992
2312:[], # Indices 36992 to 37008
2313:[], # Indices 37008 to 37024
2314:[], # Indices 37024 to 37040
2315:[], # Indices 37040 to 37056
2316:[], # Indices 37056 to 37072
2317:[], # Indices 37072 to 37088
2318:[], # Indices 37088 to 37104
2319:[], # Indices 37104 to 37120
2320:[], # Indices 37120 to 37136
2321:[], # Indices 37136 to 37152
2322:[], # Indices 37152 to 37168
2323:[], # Indices 37168 to 37184
2324:[], # Indices 37184 to 37200
2325:[], # Indices 37200 to 37216
2326:[], # Indices 37216 to 37232
2327:[], # Indices 37232 to 37248
2328:[], # Indices 37248 to 37264
2329:[], # Indices 37264 to 37280
2330:[], # Indices 37280 to 37296
2331:[], # Indices 37296 to 37312
2332:[], # Indices 37312 to 37328
2333:[], # Indices 37328 to 37344
2334:[], # Indices 37344 to 37360
2335:[], # Indices 37360 to 37376
2336:[], # Indices 37376 to 37392
2337:[], # Indices 37392 to 37408
2338:[], # Indices 37408 to 37424
2339:[], # Indices 37424 to 37440
2340:[], # Indices 37440 to 37456
2341:[], # Indices 37456 to 37472
2342:[], # Indices 37472 to 37488
2343:[], # Indices 37488 to 37504
2344:[], # Indices 37504 to 37520
2345:[], # Indices 37520 to 37536
2346:[], # Indices 37536 to 37552
2347:[], # Indices 37552 to 37568
2348:[], # Indices 37568 to 37584
2349:[], # Indices 37584 to 37600
2350:[], # Indices 37600 to 37616
2351:[], # Indices 37616 to 37632
2352:[], # Indices 37632 to 37648
2353:[], # Indices 37648 to 37664
2354:[{'index_dec': 3, 'index_bin': '0011', 'val': 4, 'counts': 92}], # Indices 37664 to 37680
2355:[], # Indices 37680 to 37696
2356:[], # Indices 37696 to 37712
2357:[], # Indices 37712 to 37728
2358:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 92}], # Indices 37728 to 37744
2359:[], # Indices 37744 to 37760
2360:[], # Indices 37760 to 37776
2361:[], # Indices 37776 to 37792
2362:[], # Indices 37792 to 37808
2363:[], # Indices 37808 to 37824
2364:[], # Indices 37824 to 37840
2365:[], # Indices 37840 to 37856
2366:[], # Indices 37856 to 37872
2367:[], # Indices 37872 to 37888
2368:[], # Indices 37888 to 37904
2369:[], # Indices 37904 to 37920
2370:[], # Indices 37920 to 37936
2371:[], # Indices 37936 to 37952
2372:[], # Indices 37952 to 37968
2373:[], # Indices 37968 to 37984
2374:[], # Indices 37984 to 38000
2375:[], # Indices 38000 to 38016
2376:[], # Indices 38016 to 38032
2377:[], # Indices 38032 to 38048
2378:[], # Indices 38048 to 38064
2379:[], # Indices 38064 to 38080
2380:[], # Indices 38080 to 38096
2381:[], # Indices 38096 to 38112
2382:[], # Indices 38112 to 38128
2383:[], # Indices 38128 to 38144
2384:[], # Indices 38144 to 38160
2385:[], # Indices 38160 to 38176
2386:[], # Indices 38176 to 38192
2387:[], # Indices 38192 to 38208
2388:[], # Indices 38208 to 38224
2389:[], # Indices 38224 to 38240
2390:[], # Indices 38240 to 38256
2391:[], # Indices 38256 to 38272
2392:[], # Indices 38272 to 38288
2393:[], # Indices 38288 to 38304
2394:[], # Indices 38304 to 38320
2395:[], # Indices 38320 to 38336
2396:[], # Indices 38336 to 38352
2397:[], # Indices 38352 to 38368
2398:[], # Indices 38368 to 38384
2399:[], # Indices 38384 to 38400
2400:[], # Indices 38400 to 38416
2401:[], # Indices 38416 to 38432
2402:[], # Indices 38432 to 38448
2403:[], # Indices 38448 to 38464
2404:[{'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 93}], # Indices 38464 to 38480
2405:[], # Indices 38480 to 38496
2406:[], # Indices 38496 to 38512
2407:[], # Indices 38512 to 38528
2408:[], # Indices 38528 to 38544
2409:[], # Indices 38544 to 38560
2410:[], # Indices 38560 to 38576
2411:[], # Indices 38576 to 38592
2412:[], # Indices 38592 to 38608
2413:[], # Indices 38608 to 38624
2414:[], # Indices 38624 to 38640
2415:[], # Indices 38640 to 38656
2416:[], # Indices 38656 to 38672
2417:[], # Indices 38672 to 38688
2418:[], # Indices 38688 to 38704
2419:[], # Indices 38704 to 38720
2420:[], # Indices 38720 to 38736
2421:[], # Indices 38736 to 38752
2422:[], # Indices 38752 to 38768
2423:[], # Indices 38768 to 38784
2424:[], # Indices 38784 to 38800
2425:[], # Indices 38800 to 38816
2426:[], # Indices 38816 to 38832
2427:[], # Indices 38832 to 38848
2428:[], # Indices 38848 to 38864
2429:[], # Indices 38864 to 38880
2430:[], # Indices 38880 to 38896
2431:[], # Indices 38896 to 38912
2432:[], # Indices 38912 to 38928
2433:[], # Indices 38928 to 38944
2434:[], # Indices 38944 to 38960
2435:[], # Indices 38960 to 38976
2436:[], # Indices 38976 to 38992
2437:[], # Indices 38992 to 39008
2438:[], # Indices 39008 to 39024
2439:[], # Indices 39024 to 39040
2440:[{'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 92}], # Indices 39040 to 39056
2441:[], # Indices 39056 to 39072
2442:[], # Indices 39072 to 39088
2443:[], # Indices 39088 to 39104
2444:[], # Indices 39104 to 39120
2445:[], # Indices 39120 to 39136
2446:[], # Indices 39136 to 39152
2447:[], # Indices 39152 to 39168
2448:[], # Indices 39168 to 39184
2449:[], # Indices 39184 to 39200
2450:[], # Indices 39200 to 39216
2451:[], # Indices 39216 to 39232
2452:[], # Indices 39232 to 39248
2453:[], # Indices 39248 to 39264
2454:[], # Indices 39264 to 39280
2455:[], # Indices 39280 to 39296
2456:[], # Indices 39296 to 39312
2457:[], # Indices 39312 to 39328
2458:[], # Indices 39328 to 39344
2459:[], # Indices 39344 to 39360
2460:[], # Indices 39360 to 39376
2461:[], # Indices 39376 to 39392
2462:[], # Indices 39392 to 39408
2463:[], # Indices 39408 to 39424
2464:[], # Indices 39424 to 39440
2465:[], # Indices 39440 to 39456
2466:[], # Indices 39456 to 39472
2467:[], # Indices 39472 to 39488
2468:[], # Indices 39488 to 39504
2469:[], # Indices 39504 to 39520
2470:[], # Indices 39520 to 39536
2471:[], # Indices 39536 to 39552
2472:[], # Indices 39552 to 39568
2473:[], # Indices 39568 to 39584
2474:[], # Indices 39584 to 39600
2475:[], # Indices 39600 to 39616
2476:[], # Indices 39616 to 39632
2477:[], # Indices 39632 to 39648
2478:[], # Indices 39648 to 39664
2479:[], # Indices 39664 to 39680
2480:[], # Indices 39680 to 39696
2481:[], # Indices 39696 to 39712
2482:[], # Indices 39712 to 39728
2483:[], # Indices 39728 to 39744
2484:[], # Indices 39744 to 39760
2485:[], # Indices 39760 to 39776
2486:[], # Indices 39776 to 39792
2487:[], # Indices 39792 to 39808
2488:[], # Indices 39808 to 39824
2489:[], # Indices 39824 to 39840
2490:[], # Indices 39840 to 39856
2491:[], # Indices 39856 to 39872
2492:[], # Indices 39872 to 39888
2493:[], # Indices 39888 to 39904
2494:[], # Indices 39904 to 39920
2495:[], # Indices 39920 to 39936
2496:[], # Indices 39936 to 39952
2497:[], # Indices 39952 to 39968
2498:[], # Indices 39968 to 39984
2499:[], # Indices 39984 to 40000
2500:[], # Indices 40000 to 40016
2501:[], # Indices 40016 to 40032
2502:[], # Indices 40032 to 40048
2503:[], # Indices 40048 to 40064
2504:[], # Indices 40064 to 40080
2505:[], # Indices 40080 to 40096
2506:[], # Indices 40096 to 40112
2507:[], # Indices 40112 to 40128
2508:[], # Indices 40128 to 40144
2509:[], # Indices 40144 to 40160
2510:[], # Indices 40160 to 40176
2511:[], # Indices 40176 to 40192
2512:[], # Indices 40192 to 40208
2513:[], # Indices 40208 to 40224
2514:[], # Indices 40224 to 40240
2515:[], # Indices 40240 to 40256
2516:[], # Indices 40256 to 40272
2517:[], # Indices 40272 to 40288
2518:[], # Indices 40288 to 40304
2519:[], # Indices 40304 to 40320
2520:[], # Indices 40320 to 40336
2521:[], # Indices 40336 to 40352
2522:[], # Indices 40352 to 40368
2523:[], # Indices 40368 to 40384
2524:[], # Indices 40384 to 40400
2525:[], # Indices 40400 to 40416
2526:[], # Indices 40416 to 40432
2527:[], # Indices 40432 to 40448
2528:[], # Indices 40448 to 40464
2529:[], # Indices 40464 to 40480
2530:[], # Indices 40480 to 40496
2531:[], # Indices 40496 to 40512
2532:[], # Indices 40512 to 40528
2533:[], # Indices 40528 to 40544
2534:[], # Indices 40544 to 40560
2535:[], # Indices 40560 to 40576
2536:[], # Indices 40576 to 40592
2537:[], # Indices 40592 to 40608
2538:[], # Indices 40608 to 40624
2539:[], # Indices 40624 to 40640
2540:[{'index_dec': 13, 'index_bin': '1101', 'val': 13, 'counts': 336}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 322}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 306}], # Indices 40640 to 40656
2541:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 202}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 194}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 201}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 197}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 180}], # Indices 40656 to 40672
2542:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 310}, {'index_dec': 7, 'index_bin': '0111', 'val': 15, 'counts': 330}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 326}], # Indices 40672 to 40688
2543:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 144}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 135}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 140}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 139}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 119}, {'index_dec': 15, 'index_bin': '1111', 'val': 14, 'counts': 170}], # Indices 40688 to 40704
2544:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 118}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 100}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 95}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 103}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 107}], # Indices 40704 to 40720
2545:[], # Indices 40720 to 40736
2546:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 271}, {'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 266}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 244}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 243}], # Indices 40736 to 40752
2547:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 482}], # Indices 40752 to 40768
2548:[], # Indices 40768 to 40784
2549:[], # Indices 40784 to 40800
2550:[], # Indices 40800 to 40816
2551:[], # Indices 40816 to 40832
2552:[], # Indices 40832 to 40848
2553:[], # Indices 40848 to 40864
2554:[], # Indices 40864 to 40880
2555:[], # Indices 40880 to 40896
2556:[], # Indices 40896 to 40912
2557:[], # Indices 40912 to 40928
2558:[], # Indices 40928 to 40944
2559:[], # Indices 40944 to 40960
2560:[], # Indices 40960 to 40976
2561:[{'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 464}], # Indices 40976 to 40992
2562:[{'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 466}], # Indices 40992 to 41008
2563:[{'index_dec': 1, 'index_bin': '0001', 'val': 15, 'counts': 388}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 396}], # Indices 41008 to 41024
2564:[{'index_dec': 0, 'index_bin': '0000', 'val': 15, 'counts': 250}, {'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 260}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 250}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 264}], # Indices 41024 to 41040
2565:[], # Indices 41040 to 41056
2566:[{'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 520}], # Indices 41056 to 41072
2567:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 481}], # Indices 41072 to 41088
2568:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 357}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 317}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 304}], # Indices 41088 to 41104
2569:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 182}, {'index_dec': 3, 'index_bin': '0011', 'val': 15, 'counts': 195}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 208}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 202}, {'index_dec': 13, 'index_bin': '1101', 'val': 14, 'counts': 196}], # Indices 41104 to 41120
2570:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 476}], # Indices 41120 to 41136
2571:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 205}, {'index_dec': 2, 'index_bin': '0010', 'val': 13, 'counts': 190}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 201}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 195}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 187}], # Indices 41136 to 41152
2572:[{'index_dec': 0, 'index_bin': '0000', 'val': 16, 'counts': 317}, {'index_dec': 4, 'index_bin': '0100', 'val': 12, 'counts': 309}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 337}], # Indices 41152 to 41168
2573:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 314}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 331}, {'index_dec': 13, 'index_bin': '1101', 'val': 17, 'counts': 334}], # Indices 41168 to 41184
2574:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 212}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 201}, {'index_dec': 4, 'index_bin': '0100', 'val': 12, 'counts': 183}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 195}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 188}], # Indices 41184 to 41200
2575:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 383}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 415}], # Indices 41200 to 41216
2576:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 180}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 181}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 202}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 204}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 208}], # Indices 41216 to 41232
2577:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 249}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 248}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 248}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 279}], # Indices 41232 to 41248
2578:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 492}], # Indices 41248 to 41264
2579:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 262}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 245}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 251}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 266}], # Indices 41264 to 41280
2580:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 250}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 271}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 256}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 247}], # Indices 41280 to 41296
2581:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 179}, {'index_dec': 6, 'index_bin': '0110', 'val': 15, 'counts': 208}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 211}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 192}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 182}], # Indices 41296 to 41312
2582:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 420}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 384}], # Indices 41312 to 41328
2583:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 421}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 348}], # Indices 41328 to 41344
2584:[{'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 385}, {'index_dec': 15, 'index_bin': '1111', 'val': 14, 'counts': 396}], # Indices 41344 to 41360
2585:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 512}], # Indices 41360 to 41376
2586:[{'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 193}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 201}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 194}, {'index_dec': 13, 'index_bin': '1101', 'val': 14, 'counts': 192}, {'index_dec': 15, 'index_bin': '1111', 'val': 14, 'counts': 201}], # Indices 41376 to 41392
2587:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 414}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 402}], # Indices 41392 to 41408
2588:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 336}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 333}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 308}], # Indices 41408 to 41424
2589:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 458}], # Indices 41424 to 41440
2590:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 388}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 423}], # Indices 41440 to 41456
2591:[], # Indices 41456 to 41472
2592:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 236}, {'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 261}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 256}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 271}], # Indices 41472 to 41488
2593:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 385}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 437}], # Indices 41488 to 41504
2594:[{'index_dec': 3, 'index_bin': '0011', 'val': 15, 'counts': 355}, {'index_dec': 4, 'index_bin': '0100', 'val': 12, 'counts': 283}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 342}], # Indices 41504 to 41520
2595:[{'index_dec': 2, 'index_bin': '0010', 'val': 13, 'counts': 332}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 338}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 311}], # Indices 41520 to 41536
2596:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 149}, {'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 132}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 133}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 143}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 165}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 151}], # Indices 41536 to 41552
2597:[{'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 328}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 347}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 312}], # Indices 41552 to 41568
2598:[], # Indices 41568 to 41584
2599:[{'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 379}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 420}], # Indices 41584 to 41600
2600:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 299}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 358}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 313}], # Indices 41600 to 41616
2601:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 274}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 258}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 242}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 250}], # Indices 41616 to 41632
2602:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 273}, {'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 253}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 244}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 254}], # Indices 41632 to 41648
2603:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 260}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 249}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 254}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 261}], # Indices 41648 to 41664
2604:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 498}], # Indices 41664 to 41680
2605:[{'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 324}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 358}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 299}], # Indices 41680 to 41696
2606:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 429}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 367}], # Indices 41696 to 41712
2607:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 405}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 392}], # Indices 41712 to 41728
2608:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 496}], # Indices 41728 to 41744
2609:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 394}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 407}], # Indices 41744 to 41760
2610:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 313}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 343}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 322}], # Indices 41760 to 41776
2611:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 489}], # Indices 41776 to 41792
2612:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 402}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 418}], # Indices 41792 to 41808
2613:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 183}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 210}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 196}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 190}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 200}], # Indices 41808 to 41824
2614:[{'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 402}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 391}], # Indices 41824 to 41840
2615:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 240}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 255}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 232}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 297}], # Indices 41840 to 41856
2616:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 379}, {'index_dec': 12, 'index_bin': '1100', 'val': 14, 'counts': 397}], # Indices 41856 to 41872
2617:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 327}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 322}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 324}], # Indices 41872 to 41888
2618:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 496}], # Indices 41888 to 41904
2619:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 403}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 405}], # Indices 41904 to 41920
2620:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 421}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 388}], # Indices 41920 to 41936
2621:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 299}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 324}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 344}], # Indices 41936 to 41952
2622:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 325}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 317}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 330}], # Indices 41952 to 41968
2623:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 339}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 320}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 322}], # Indices 41968 to 41984
2624:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 425}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 370}], # Indices 41984 to 42000
2625:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 246}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 267}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 267}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 244}], # Indices 42000 to 42016
2626:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 379}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 422}], # Indices 42016 to 42032
2627:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 322}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 335}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 309}], # Indices 42032 to 42048
2628:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 344}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 314}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 315}], # Indices 42048 to 42064
2629:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 353}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 315}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 308}], # Indices 42064 to 42080
2630:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 310}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 310}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 342}], # Indices 42080 to 42096
2631:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 316}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 344}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 313}], # Indices 42096 to 42112
2632:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 270}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 273}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 249}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 232}], # Indices 42112 to 42128
2633:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 369}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 343}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 274}], # Indices 42128 to 42144
2634:[], # Indices 42144 to 42160
2635:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 253}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 257}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 257}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 257}], # Indices 42160 to 42176
2636:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 460}], # Indices 42176 to 42192
2637:[{'index_dec': 1, 'index_bin': '0001', 'val': 13, 'counts': 279}, {'index_dec': 5, 'index_bin': '0101', 'val': 15, 'counts': 254}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 243}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 248}], # Indices 42192 to 42208
2638:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 489}], # Indices 42208 to 42224
2639:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 434}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 388}], # Indices 42224 to 42240
2640:[{'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 362}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 418}], # Indices 42240 to 42256
2641:[{'index_dec': 2, 'index_bin': '0010', 'val': 14, 'counts': 334}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 336}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 307}], # Indices 42256 to 42272
2642:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 450}], # Indices 42272 to 42288
2643:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 350}, {'index_dec': 8, 'index_bin': '1000', 'val': 12, 'counts': 314}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 305}], # Indices 42288 to 42304
2644:[{'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 472}], # Indices 42304 to 42320
2645:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 387}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 405}], # Indices 42320 to 42336
2646:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 391}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 420}], # Indices 42336 to 42352
2647:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 490}], # Indices 42352 to 42368
2648:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 387}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 395}], # Indices 42368 to 42384
2649:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 412}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 420}], # Indices 42384 to 42400
2650:[{'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 495}], # Indices 42400 to 42416
2651:[], # Indices 42416 to 42432
2652:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 479}], # Indices 42432 to 42448
2653:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 201}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 187}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 205}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 186}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 187}], # Indices 42448 to 42464
2654:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 390}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 409}], # Indices 42464 to 42480
2655:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 401}, {'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 393}], # Indices 42480 to 42496
2656:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 303}, {'index_dec': 11, 'index_bin': '1011', 'val': 15, 'counts': 350}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 312}], # Indices 42496 to 42512
2657:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 462}], # Indices 42512 to 42528
2658:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 246}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 240}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 267}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 271}], # Indices 42528 to 42544
2659:[], # Indices 42544 to 42560
2660:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 391}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 408}], # Indices 42560 to 42576
2661:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 477}], # Indices 42576 to 42592
2662:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 309}, {'index_dec': 3, 'index_bin': '0011', 'val': 15, 'counts': 329}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 336}], # Indices 42592 to 42608
2663:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 253}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 255}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 268}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 248}], # Indices 42608 to 42624
2664:[{'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 401}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 392}], # Indices 42624 to 42640
2665:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 383}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 410}], # Indices 42640 to 42656
2666:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 387}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 421}], # Indices 42656 to 42672
2667:[], # Indices 42672 to 42688
2668:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 398}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 387}], # Indices 42688 to 42704
2669:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 295}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 351}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 324}], # Indices 42704 to 42720
2670:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 331}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 309}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 344}], # Indices 42720 to 42736
2671:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 489}], # Indices 42736 to 42752
2672:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 311}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 329}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 337}], # Indices 42752 to 42768
2673:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 471}], # Indices 42768 to 42784
2674:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 487}], # Indices 42784 to 42800
2675:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 273}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 257}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 259}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 235}], # Indices 42800 to 42816
2676:[], # Indices 42816 to 42832
2677:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 405}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 415}], # Indices 42832 to 42848
2678:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 327}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 299}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 342}], # Indices 42848 to 42864
2679:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 247}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 271}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 257}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 249}], # Indices 42864 to 42880
2680:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 347}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 324}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 304}], # Indices 42880 to 42896
2681:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 395}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 409}], # Indices 42896 to 42912
2682:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 480}], # Indices 42912 to 42928
2683:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 511}], # Indices 42928 to 42944
2684:[], # Indices 42944 to 42960
2685:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 189}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 191}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 209}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 207}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 184}], # Indices 42960 to 42976
2686:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 152}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 144}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 136}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 145}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 143}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 148}], # Indices 42976 to 42992
2687:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 339}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 306}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 325}], # Indices 42992 to 43008
2688:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 371}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 417}], # Indices 43008 to 43024
2689:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 302}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 348}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 307}], # Indices 43024 to 43040
2690:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 489}], # Indices 43040 to 43056
2691:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 393}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 406}], # Indices 43056 to 43072
2692:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 485}], # Indices 43072 to 43088
2693:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 403}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 414}], # Indices 43088 to 43104
2694:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 391}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 396}], # Indices 43104 to 43120
2695:[], # Indices 43120 to 43136
2696:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 400}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 409}], # Indices 43136 to 43152
2697:[], # Indices 43152 to 43168
2698:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 388}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 397}], # Indices 43168 to 43184
2699:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 375}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 436}], # Indices 43184 to 43200
2700:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 329}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 302}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 347}], # Indices 43200 to 43216
2701:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 474}], # Indices 43216 to 43232
2702:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 313}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 330}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 340}], # Indices 43232 to 43248
2703:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 409}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 381}], # Indices 43248 to 43264
2704:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 259}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 224}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 275}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 266}], # Indices 43264 to 43280
2705:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 403}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 405}], # Indices 43280 to 43296
2706:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 500}], # Indices 43296 to 43312
2707:[], # Indices 43312 to 43328
2708:[], # Indices 43328 to 43344
2709:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 411}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 400}], # Indices 43344 to 43360
2710:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 325}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 330}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 330}], # Indices 43360 to 43376
2711:[], # Indices 43376 to 43392
2712:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 482}], # Indices 43392 to 43408
2713:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 320}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 321}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 319}], # Indices 43408 to 43424
2714:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 440}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 375}], # Indices 43424 to 43440
2715:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 462}], # Indices 43440 to 43456
2716:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 480}], # Indices 43456 to 43472
2717:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 489}], # Indices 43472 to 43488
2718:[], # Indices 43488 to 43504
2719:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 414}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 405}], # Indices 43504 to 43520
2720:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 463}], # Indices 43520 to 43536
2721:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 480}], # Indices 43536 to 43552
2722:[], # Indices 43552 to 43568
2723:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 322}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 326}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 325}], # Indices 43568 to 43584
2724:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 462}], # Indices 43584 to 43600
2725:[], # Indices 43600 to 43616
2726:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 373}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 416}], # Indices 43616 to 43632
2727:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 383}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 422}], # Indices 43632 to 43648
2728:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 313}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 305}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 329}], # Indices 43648 to 43664
2729:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 482}], # Indices 43664 to 43680
2730:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 473}], # Indices 43680 to 43696
2731:[], # Indices 43696 to 43712
2732:[], # Indices 43712 to 43728
2733:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 466}], # Indices 43728 to 43744
2734:[], # Indices 43744 to 43760
2735:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 385}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 397}], # Indices 43760 to 43776
2736:[], # Indices 43776 to 43792
2737:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 481}], # Indices 43792 to 43808
2738:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 476}], # Indices 43808 to 43824
2739:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 478}], # Indices 43824 to 43840
2740:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 487}], # Indices 43840 to 43856
2741:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 462}], # Indices 43856 to 43872
2742:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 462}], # Indices 43872 to 43888
2743:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 487}], # Indices 43888 to 43904
2744:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 509}], # Indices 43904 to 43920
2745:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 409}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 391}], # Indices 43920 to 43936
2746:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 475}], # Indices 43936 to 43952
2747:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 335}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 324}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 311}], # Indices 43952 to 43968
2748:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 422}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 378}], # Indices 43968 to 43984
2749:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 488}], # Indices 43984 to 44000
2750:[], # Indices 44000 to 44016
2751:[], # Indices 44016 to 44032
2752:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 405}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 418}], # Indices 44032 to 44048
2753:[], # Indices 44048 to 44064
2754:[], # Indices 44064 to 44080
2755:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 492}], # Indices 44080 to 44096
2756:[], # Indices 44096 to 44112
2757:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 464}], # Indices 44112 to 44128
2758:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 456}], # Indices 44128 to 44144
2759:[], # Indices 44144 to 44160
2760:[], # Indices 44160 to 44176
2761:[], # Indices 44176 to 44192
2762:[], # Indices 44192 to 44208
2763:[], # Indices 44208 to 44224
2764:[], # Indices 44224 to 44240
2765:[], # Indices 44240 to 44256
2766:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 417}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 365}], # Indices 44256 to 44272
2767:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 494}], # Indices 44272 to 44288
2768:[], # Indices 44288 to 44304
2769:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 469}], # Indices 44304 to 44320
2770:[], # Indices 44320 to 44336
2771:[], # Indices 44336 to 44352
2772:[], # Indices 44352 to 44368
2773:[], # Indices 44368 to 44384
2774:[], # Indices 44384 to 44400
2775:[], # Indices 44400 to 44416
2776:[], # Indices 44416 to 44432
2777:[], # Indices 44432 to 44448
2778:[], # Indices 44448 to 44464
2779:[], # Indices 44464 to 44480
2780:[], # Indices 44480 to 44496
2781:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 460}], # Indices 44496 to 44512
2782:[], # Indices 44512 to 44528
2783:[], # Indices 44528 to 44544
2784:[], # Indices 44544 to 44560
2785:[], # Indices 44560 to 44576
2786:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 477}], # Indices 44576 to 44592
2787:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 468}], # Indices 44592 to 44608
2788:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 463}], # Indices 44608 to 44624
2789:[], # Indices 44624 to 44640
2790:[], # Indices 44640 to 44656
2791:[], # Indices 44656 to 44672
2792:[], # Indices 44672 to 44688
2793:[], # Indices 44688 to 44704
2794:[], # Indices 44704 to 44720
2795:[], # Indices 44720 to 44736
2796:[], # Indices 44736 to 44752
2797:[], # Indices 44752 to 44768
2798:[], # Indices 44768 to 44784
2799:[], # Indices 44784 to 44800
2800:[], # Indices 44800 to 44816
2801:[], # Indices 44816 to 44832
2802:[], # Indices 44832 to 44848
2803:[], # Indices 44848 to 44864
2804:[], # Indices 44864 to 44880
2805:[], # Indices 44880 to 44896
2806:[], # Indices 44896 to 44912
2807:[], # Indices 44912 to 44928
2808:[], # Indices 44928 to 44944
2809:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 467}], # Indices 44944 to 44960
2810:[], # Indices 44960 to 44976
2811:[], # Indices 44976 to 44992
2812:[], # Indices 44992 to 45008
2813:[], # Indices 45008 to 45024
2814:[], # Indices 45024 to 45040
2815:[], # Indices 45040 to 45056
2816:[], # Indices 45056 to 45072
2817:[], # Indices 45072 to 45088
2818:[], # Indices 45088 to 45104
2819:[], # Indices 45104 to 45120
2820:[], # Indices 45120 to 45136
2821:[], # Indices 45136 to 45152
2822:[], # Indices 45152 to 45168
2823:[], # Indices 45168 to 45184
2824:[], # Indices 45184 to 45200
2825:[], # Indices 45200 to 45216
2826:[], # Indices 45216 to 45232
2827:[], # Indices 45232 to 45248
2828:[], # Indices 45248 to 45264
2829:[], # Indices 45264 to 45280
2830:[], # Indices 45280 to 45296
2831:[], # Indices 45296 to 45312
2832:[], # Indices 45312 to 45328
2833:[], # Indices 45328 to 45344
2834:[], # Indices 45344 to 45360
2835:[], # Indices 45360 to 45376
2836:[], # Indices 45376 to 45392
2837:[], # Indices 45392 to 45408
2838:[], # Indices 45408 to 45424
2839:[], # Indices 45424 to 45440
2840:[], # Indices 45440 to 45456
2841:[], # Indices 45456 to 45472
2842:[], # Indices 45472 to 45488
2843:[], # Indices 45488 to 45504
2844:[], # Indices 45504 to 45520
2845:[], # Indices 45520 to 45536
2846:[], # Indices 45536 to 45552
2847:[], # Indices 45552 to 45568
2848:[], # Indices 45568 to 45584
2849:[], # Indices 45584 to 45600
2850:[], # Indices 45600 to 45616
2851:[], # Indices 45616 to 45632
2852:[], # Indices 45632 to 45648
2853:[], # Indices 45648 to 45664
2854:[], # Indices 45664 to 45680
2855:[], # Indices 45680 to 45696
2856:[], # Indices 45696 to 45712
2857:[], # Indices 45712 to 45728
2858:[], # Indices 45728 to 45744
2859:[], # Indices 45744 to 45760
2860:[], # Indices 45760 to 45776
2861:[], # Indices 45776 to 45792
2862:[], # Indices 45792 to 45808
2863:[], # Indices 45808 to 45824
2864:[], # Indices 45824 to 45840
2865:[], # Indices 45840 to 45856
2866:[], # Indices 45856 to 45872
2867:[], # Indices 45872 to 45888
2868:[], # Indices 45888 to 45904
2869:[], # Indices 45904 to 45920
2870:[], # Indices 45920 to 45936
2871:[], # Indices 45936 to 45952
2872:[{'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 91}], # Indices 45952 to 45968
2873:[], # Indices 45968 to 45984
2874:[], # Indices 45984 to 46000
2875:[], # Indices 46000 to 46016
2876:[], # Indices 46016 to 46032
2877:[], # Indices 46032 to 46048
2878:[], # Indices 46048 to 46064
2879:[], # Indices 46064 to 46080
2880:[], # Indices 46080 to 46096
2881:[], # Indices 46096 to 46112
2882:[], # Indices 46112 to 46128
2883:[], # Indices 46128 to 46144
2884:[], # Indices 46144 to 46160
2885:[], # Indices 46160 to 46176
2886:[], # Indices 46176 to 46192
2887:[], # Indices 46192 to 46208
2888:[], # Indices 46208 to 46224
2889:[], # Indices 46224 to 46240
2890:[], # Indices 46240 to 46256
2891:[], # Indices 46256 to 46272
2892:[], # Indices 46272 to 46288
2893:[], # Indices 46288 to 46304
2894:[], # Indices 46304 to 46320
2895:[], # Indices 46320 to 46336
2896:[], # Indices 46336 to 46352
2897:[], # Indices 46352 to 46368
2898:[], # Indices 46368 to 46384
2899:[], # Indices 46384 to 46400
2900:[], # Indices 46400 to 46416
2901:[], # Indices 46416 to 46432
2902:[], # Indices 46432 to 46448
2903:[], # Indices 46448 to 46464
2904:[], # Indices 46464 to 46480
2905:[], # Indices 46480 to 46496
2906:[], # Indices 46496 to 46512
2907:[], # Indices 46512 to 46528
2908:[], # Indices 46528 to 46544
2909:[], # Indices 46544 to 46560
2910:[], # Indices 46560 to 46576
2911:[{'index_dec': 1, 'index_bin': '0001', 'val': 4, 'counts': 94}], # Indices 46576 to 46592
2912:[], # Indices 46592 to 46608
2913:[], # Indices 46608 to 46624
2914:[], # Indices 46624 to 46640
2915:[], # Indices 46640 to 46656
2916:[], # Indices 46656 to 46672
2917:[], # Indices 46672 to 46688
2918:[], # Indices 46688 to 46704
2919:[], # Indices 46704 to 46720
2920:[], # Indices 46720 to 46736
2921:[], # Indices 46736 to 46752
2922:[], # Indices 46752 to 46768
2923:[], # Indices 46768 to 46784
2924:[], # Indices 46784 to 46800
2925:[], # Indices 46800 to 46816
2926:[], # Indices 46816 to 46832
2927:[], # Indices 46832 to 46848
2928:[], # Indices 46848 to 46864
2929:[], # Indices 46864 to 46880
2930:[], # Indices 46880 to 46896
2931:[], # Indices 46896 to 46912
2932:[], # Indices 46912 to 46928
2933:[], # Indices 46928 to 46944
2934:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 92}], # Indices 46944 to 46960
2935:[], # Indices 46960 to 46976
2936:[], # Indices 46976 to 46992
2937:[], # Indices 46992 to 47008
2938:[], # Indices 47008 to 47024
2939:[], # Indices 47024 to 47040
2940:[], # Indices 47040 to 47056
2941:[], # Indices 47056 to 47072
2942:[], # Indices 47072 to 47088
2943:[], # Indices 47088 to 47104
2944:[], # Indices 47104 to 47120
2945:[], # Indices 47120 to 47136
2946:[], # Indices 47136 to 47152
2947:[], # Indices 47152 to 47168
2948:[], # Indices 47168 to 47184
2949:[], # Indices 47184 to 47200
2950:[], # Indices 47200 to 47216
2951:[], # Indices 47216 to 47232
2952:[], # Indices 47232 to 47248
2953:[], # Indices 47248 to 47264
2954:[], # Indices 47264 to 47280
2955:[], # Indices 47280 to 47296
2956:[], # Indices 47296 to 47312
2957:[], # Indices 47312 to 47328
2958:[], # Indices 47328 to 47344
2959:[], # Indices 47344 to 47360
2960:[], # Indices 47360 to 47376
2961:[], # Indices 47376 to 47392
2962:[], # Indices 47392 to 47408
2963:[], # Indices 47408 to 47424
2964:[], # Indices 47424 to 47440
2965:[], # Indices 47440 to 47456
2966:[], # Indices 47456 to 47472
2967:[], # Indices 47472 to 47488
2968:[], # Indices 47488 to 47504
2969:[], # Indices 47504 to 47520
2970:[], # Indices 47520 to 47536
2971:[], # Indices 47536 to 47552
2972:[], # Indices 47552 to 47568
2973:[], # Indices 47568 to 47584
2974:[], # Indices 47584 to 47600
2975:[], # Indices 47600 to 47616
2976:[], # Indices 47616 to 47632
2977:[], # Indices 47632 to 47648
2978:[], # Indices 47648 to 47664
2979:[], # Indices 47664 to 47680
2980:[], # Indices 47680 to 47696
2981:[], # Indices 47696 to 47712
2982:[], # Indices 47712 to 47728
2983:[], # Indices 47728 to 47744
2984:[], # Indices 47744 to 47760
2985:[], # Indices 47760 to 47776
2986:[], # Indices 47776 to 47792
2987:[], # Indices 47792 to 47808
2988:[], # Indices 47808 to 47824
2989:[], # Indices 47824 to 47840
2990:[], # Indices 47840 to 47856
2991:[{'index_dec': 3, 'index_bin': '0011', 'val': 4, 'counts': 91}], # Indices 47856 to 47872
2992:[], # Indices 47872 to 47888
2993:[], # Indices 47888 to 47904
2994:[], # Indices 47904 to 47920
2995:[], # Indices 47920 to 47936
2996:[], # Indices 47936 to 47952
2997:[], # Indices 47952 to 47968
2998:[], # Indices 47968 to 47984
2999:[], # Indices 47984 to 48000
3000:[], # Indices 48000 to 48016
3001:[], # Indices 48016 to 48032
3002:[], # Indices 48032 to 48048
3003:[], # Indices 48048 to 48064
3004:[], # Indices 48064 to 48080
3005:[], # Indices 48080 to 48096
3006:[], # Indices 48096 to 48112
3007:[], # Indices 48112 to 48128
3008:[], # Indices 48128 to 48144
3009:[], # Indices 48144 to 48160
3010:[], # Indices 48160 to 48176
3011:[], # Indices 48176 to 48192
3012:[], # Indices 48192 to 48208
3013:[], # Indices 48208 to 48224
3014:[], # Indices 48224 to 48240
3015:[], # Indices 48240 to 48256
3016:[], # Indices 48256 to 48272
3017:[], # Indices 48272 to 48288
3018:[], # Indices 48288 to 48304
3019:[], # Indices 48304 to 48320
3020:[], # Indices 48320 to 48336
3021:[], # Indices 48336 to 48352
3022:[], # Indices 48352 to 48368
3023:[], # Indices 48368 to 48384
3024:[], # Indices 48384 to 48400
3025:[], # Indices 48400 to 48416
3026:[], # Indices 48416 to 48432
3027:[], # Indices 48432 to 48448
3028:[], # Indices 48448 to 48464
3029:[], # Indices 48464 to 48480
3030:[], # Indices 48480 to 48496
3031:[], # Indices 48496 to 48512
3032:[], # Indices 48512 to 48528
3033:[], # Indices 48528 to 48544
3034:[], # Indices 48544 to 48560
3035:[], # Indices 48560 to 48576
3036:[], # Indices 48576 to 48592
3037:[], # Indices 48592 to 48608
3038:[], # Indices 48608 to 48624
3039:[], # Indices 48624 to 48640
3040:[], # Indices 48640 to 48656
3041:[], # Indices 48656 to 48672
3042:[], # Indices 48672 to 48688
3043:[], # Indices 48688 to 48704
3044:[], # Indices 48704 to 48720
3045:[], # Indices 48720 to 48736
3046:[], # Indices 48736 to 48752
3047:[], # Indices 48752 to 48768
3048:[], # Indices 48768 to 48784
3049:[], # Indices 48784 to 48800
3050:[], # Indices 48800 to 48816
3051:[], # Indices 48816 to 48832
3052:[], # Indices 48832 to 48848
3053:[], # Indices 48848 to 48864
3054:[], # Indices 48864 to 48880
3055:[], # Indices 48880 to 48896
3056:[], # Indices 48896 to 48912
3057:[], # Indices 48912 to 48928
3058:[], # Indices 48928 to 48944
3059:[], # Indices 48944 to 48960
3060:[], # Indices 48960 to 48976
3061:[], # Indices 48976 to 48992
3062:[], # Indices 48992 to 49008
3063:[], # Indices 49008 to 49024
3064:[], # Indices 49024 to 49040
3065:[], # Indices 49040 to 49056
3066:[], # Indices 49056 to 49072
3067:[], # Indices 49072 to 49088
3068:[], # Indices 49088 to 49104
3069:[], # Indices 49104 to 49120
3070:[], # Indices 49120 to 49136
3071:[], # Indices 49136 to 49152
3072:[], # Indices 49152 to 49168
3073:[], # Indices 49168 to 49184
3074:[], # Indices 49184 to 49200
3075:[], # Indices 49200 to 49216
3076:[], # Indices 49216 to 49232
3077:[], # Indices 49232 to 49248
3078:[], # Indices 49248 to 49264
3079:[], # Indices 49264 to 49280
3080:[], # Indices 49280 to 49296
3081:[], # Indices 49296 to 49312
3082:[], # Indices 49312 to 49328
3083:[], # Indices 49328 to 49344
3084:[], # Indices 49344 to 49360
3085:[], # Indices 49360 to 49376
3086:[], # Indices 49376 to 49392
3087:[], # Indices 49392 to 49408
3088:[], # Indices 49408 to 49424
3089:[], # Indices 49424 to 49440
3090:[], # Indices 49440 to 49456
3091:[], # Indices 49456 to 49472
3092:[], # Indices 49472 to 49488
3093:[], # Indices 49488 to 49504
3094:[], # Indices 49504 to 49520
3095:[], # Indices 49520 to 49536
3096:[], # Indices 49536 to 49552
3097:[], # Indices 49552 to 49568
3098:[], # Indices 49568 to 49584
3099:[], # Indices 49584 to 49600
3100:[], # Indices 49600 to 49616
3101:[], # Indices 49616 to 49632
3102:[], # Indices 49632 to 49648
3103:[], # Indices 49648 to 49664
3104:[], # Indices 49664 to 49680
3105:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 93}], # Indices 49680 to 49696
3106:[], # Indices 49696 to 49712
3107:[], # Indices 49712 to 49728
3108:[], # Indices 49728 to 49744
3109:[], # Indices 49744 to 49760
3110:[], # Indices 49760 to 49776
3111:[], # Indices 49776 to 49792
3112:[], # Indices 49792 to 49808
3113:[], # Indices 49808 to 49824
3114:[], # Indices 49824 to 49840
3115:[], # Indices 49840 to 49856
3116:[], # Indices 49856 to 49872
3117:[], # Indices 49872 to 49888
3118:[], # Indices 49888 to 49904
3119:[], # Indices 49904 to 49920
3120:[], # Indices 49920 to 49936
3121:[], # Indices 49936 to 49952
3122:[], # Indices 49952 to 49968
3123:[], # Indices 49968 to 49984
3124:[], # Indices 49984 to 50000
3125:[], # Indices 50000 to 50016
3126:[], # Indices 50016 to 50032
3127:[], # Indices 50032 to 50048
3128:[], # Indices 50048 to 50064
3129:[], # Indices 50064 to 50080
3130:[], # Indices 50080 to 50096
3131:[], # Indices 50096 to 50112
3132:[], # Indices 50112 to 50128
3133:[{'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 95}], # Indices 50128 to 50144
3134:[], # Indices 50144 to 50160
3135:[], # Indices 50160 to 50176
3136:[], # Indices 50176 to 50192
3137:[], # Indices 50192 to 50208
3138:[], # Indices 50208 to 50224
3139:[], # Indices 50224 to 50240
3140:[], # Indices 50240 to 50256
3141:[], # Indices 50256 to 50272
3142:[], # Indices 50272 to 50288
3143:[], # Indices 50288 to 50304
3144:[], # Indices 50304 to 50320
3145:[], # Indices 50320 to 50336
3146:[], # Indices 50336 to 50352
3147:[], # Indices 50352 to 50368
3148:[], # Indices 50368 to 50384
3149:[], # Indices 50384 to 50400
3150:[], # Indices 50400 to 50416
3151:[], # Indices 50416 to 50432
3152:[], # Indices 50432 to 50448
3153:[], # Indices 50448 to 50464
3154:[], # Indices 50464 to 50480
3155:[], # Indices 50480 to 50496
3156:[], # Indices 50496 to 50512
3157:[], # Indices 50512 to 50528
3158:[], # Indices 50528 to 50544
3159:[], # Indices 50544 to 50560
3160:[], # Indices 50560 to 50576
3161:[], # Indices 50576 to 50592
3162:[], # Indices 50592 to 50608
3163:[], # Indices 50608 to 50624
3164:[], # Indices 50624 to 50640
3165:[], # Indices 50640 to 50656
3166:[], # Indices 50656 to 50672
3167:[], # Indices 50672 to 50688
3168:[], # Indices 50688 to 50704
3169:[], # Indices 50704 to 50720
3170:[], # Indices 50720 to 50736
3171:[], # Indices 50736 to 50752
3172:[], # Indices 50752 to 50768
3173:[], # Indices 50768 to 50784
3174:[], # Indices 50784 to 50800
3175:[], # Indices 50800 to 50816
3176:[], # Indices 50816 to 50832
3177:[], # Indices 50832 to 50848
3178:[], # Indices 50848 to 50864
3179:[], # Indices 50864 to 50880
3180:[], # Indices 50880 to 50896
3181:[], # Indices 50896 to 50912
3182:[], # Indices 50912 to 50928
3183:[], # Indices 50928 to 50944
3184:[], # Indices 50944 to 50960
3185:[], # Indices 50960 to 50976
3186:[], # Indices 50976 to 50992
3187:[], # Indices 50992 to 51008
3188:[], # Indices 51008 to 51024
3189:[], # Indices 51024 to 51040
3190:[], # Indices 51040 to 51056
3191:[], # Indices 51056 to 51072
3192:[], # Indices 51072 to 51088
3193:[], # Indices 51088 to 51104
3194:[], # Indices 51104 to 51120
3195:[], # Indices 51120 to 51136
3196:[], # Indices 51136 to 51152
3197:[], # Indices 51152 to 51168
3198:[], # Indices 51168 to 51184
3199:[], # Indices 51184 to 51200
3200:[], # Indices 51200 to 51216
3201:[], # Indices 51216 to 51232
3202:[], # Indices 51232 to 51248
3203:[], # Indices 51248 to 51264
3204:[], # Indices 51264 to 51280
3205:[], # Indices 51280 to 51296
3206:[], # Indices 51296 to 51312
3207:[], # Indices 51312 to 51328
3208:[], # Indices 51328 to 51344
3209:[], # Indices 51344 to 51360
3210:[], # Indices 51360 to 51376
3211:[], # Indices 51376 to 51392
3212:[], # Indices 51392 to 51408
3213:[], # Indices 51408 to 51424
3214:[], # Indices 51424 to 51440
3215:[], # Indices 51440 to 51456
3216:[], # Indices 51456 to 51472
3217:[], # Indices 51472 to 51488
3218:[], # Indices 51488 to 51504
3219:[], # Indices 51504 to 51520
3220:[], # Indices 51520 to 51536
3221:[], # Indices 51536 to 51552
3222:[], # Indices 51552 to 51568
3223:[], # Indices 51568 to 51584
3224:[], # Indices 51584 to 51600
3225:[], # Indices 51600 to 51616
3226:[], # Indices 51616 to 51632
3227:[], # Indices 51632 to 51648
3228:[], # Indices 51648 to 51664
3229:[], # Indices 51664 to 51680
3230:[], # Indices 51680 to 51696
3231:[], # Indices 51696 to 51712
3232:[], # Indices 51712 to 51728
3233:[{'index_dec': 2, 'index_bin': '0010', 'val': 4, 'counts': 91}], # Indices 51728 to 51744
3234:[], # Indices 51744 to 51760
3235:[], # Indices 51760 to 51776
3236:[], # Indices 51776 to 51792
3237:[], # Indices 51792 to 51808
3238:[], # Indices 51808 to 51824
3239:[], # Indices 51824 to 51840
3240:[], # Indices 51840 to 51856
3241:[], # Indices 51856 to 51872
3242:[], # Indices 51872 to 51888
3243:[], # Indices 51888 to 51904
3244:[], # Indices 51904 to 51920
3245:[], # Indices 51920 to 51936
3246:[], # Indices 51936 to 51952
3247:[], # Indices 51952 to 51968
3248:[], # Indices 51968 to 51984
3249:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 314}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 345}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 320}], # Indices 51984 to 52000
3250:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 487}], # Indices 52000 to 52016
3251:[], # Indices 52016 to 52032
3252:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 244}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 249}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 267}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 264}], # Indices 52032 to 52048
3253:[], # Indices 52048 to 52064
3254:[], # Indices 52064 to 52080
3255:[], # Indices 52080 to 52096
3256:[], # Indices 52096 to 52112
3257:[], # Indices 52112 to 52128
3258:[], # Indices 52128 to 52144
3259:[], # Indices 52144 to 52160
3260:[], # Indices 52160 to 52176
3261:[], # Indices 52176 to 52192
3262:[], # Indices 52192 to 52208
3263:[], # Indices 52208 to 52224
3264:[], # Indices 52224 to 52240
3265:[], # Indices 52240 to 52256
3266:[], # Indices 52256 to 52272
3267:[], # Indices 52272 to 52288
3268:[], # Indices 52288 to 52304
3269:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 513}], # Indices 52304 to 52320
3270:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 390}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 411}], # Indices 52320 to 52336
3271:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 248}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 277}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 235}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 264}], # Indices 52336 to 52352
3272:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 494}], # Indices 52352 to 52368
3273:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 278}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 250}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 237}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 259}], # Indices 52368 to 52384
3274:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 262}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 254}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 257}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 251}], # Indices 52384 to 52400
3275:[], # Indices 52400 to 52416
3276:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 376}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 414}], # Indices 52416 to 52432
3277:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 382}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 429}], # Indices 52432 to 52448
3278:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 252}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 255}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 264}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 253}], # Indices 52448 to 52464
3279:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 265}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 234}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 268}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 257}], # Indices 52464 to 52480
3280:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 385}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 430}], # Indices 52480 to 52496
3281:[], # Indices 52496 to 52512
3282:[{'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 497}], # Indices 52512 to 52528
3283:[{'index_dec': 4, 'index_bin': '0100', 'val': 12, 'counts': 426}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 371}], # Indices 52528 to 52544
3284:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 240}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 264}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 259}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 261}], # Indices 52544 to 52560
3285:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 325}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 336}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 308}], # Indices 52560 to 52576
3286:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 198}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 208}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 191}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 192}, {'index_dec': 14, 'index_bin': '1110', 'val': 13, 'counts': 190}], # Indices 52576 to 52592
3287:[{'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 323}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 321}, {'index_dec': 14, 'index_bin': '1110', 'val': 13, 'counts': 335}], # Indices 52592 to 52608
3288:[{'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 420}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 395}], # Indices 52608 to 52624
3289:[{'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 485}], # Indices 52624 to 52640
3290:[{'index_dec': 1, 'index_bin': '0001', 'val': 13, 'counts': 426}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 393}], # Indices 52640 to 52656
3291:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 412}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 379}], # Indices 52656 to 52672
3292:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 477}], # Indices 52672 to 52688
3293:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 477}], # Indices 52688 to 52704
3294:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 500}], # Indices 52704 to 52720
3295:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 362}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 307}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 301}], # Indices 52720 to 52736
3296:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 395}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 388}], # Indices 52736 to 52752
3297:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 502}], # Indices 52752 to 52768
3298:[{'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 461}], # Indices 52768 to 52784
3299:[], # Indices 52784 to 52800
3300:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 308}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 323}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 340}], # Indices 52800 to 52816
3301:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 514}], # Indices 52816 to 52832
3302:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 510}], # Indices 52832 to 52848
3303:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 469}], # Indices 52848 to 52864
3304:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 394}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 407}], # Indices 52864 to 52880
3305:[], # Indices 52880 to 52896
3306:[], # Indices 52896 to 52912
3307:[], # Indices 52912 to 52928
3308:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 469}], # Indices 52928 to 52944
3309:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 394}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 397}], # Indices 52944 to 52960
3310:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 414}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 388}], # Indices 52960 to 52976
3311:[], # Indices 52976 to 52992
3312:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 474}], # Indices 52992 to 53008
3313:[], # Indices 53008 to 53024
3314:[], # Indices 53024 to 53040
3315:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 312}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 304}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 349}], # Indices 53040 to 53056
3316:[{'index_dec': 6, 'index_bin': '0110', 'val': 6, 'counts': 91}], # Indices 53056 to 53072
3317:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 334}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 342}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 299}], # Indices 53072 to 53088
3318:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 484}], # Indices 53088 to 53104
3319:[], # Indices 53104 to 53120
3320:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 481}], # Indices 53120 to 53136
3321:[], # Indices 53136 to 53152
3322:[], # Indices 53152 to 53168
3323:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 482}], # Indices 53168 to 53184
3324:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 490}], # Indices 53184 to 53200
3325:[], # Indices 53200 to 53216
3326:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 331}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 319}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 326}], # Indices 53216 to 53232
3327:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 485}], # Indices 53232 to 53248
3328:[], # Indices 53248 to 53264
3329:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 503}], # Indices 53264 to 53280
3330:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 405}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 407}], # Indices 53280 to 53296
3331:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 468}], # Indices 53296 to 53312
3332:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 382}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 402}], # Indices 53312 to 53328
3333:[], # Indices 53328 to 53344
3334:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 527}], # Indices 53344 to 53360
3335:[], # Indices 53360 to 53376
3336:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 475}], # Indices 53376 to 53392
3337:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 501}], # Indices 53392 to 53408
3338:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 337}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 329}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 314}], # Indices 53408 to 53424
3339:[], # Indices 53424 to 53440
3340:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 388}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 428}], # Indices 53440 to 53456
3341:[], # Indices 53456 to 53472
3342:[], # Indices 53472 to 53488
3343:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 508}], # Indices 53488 to 53504
3344:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 475}], # Indices 53504 to 53520
3345:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 463}], # Indices 53520 to 53536
3346:[], # Indices 53536 to 53552
3347:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 405}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 380}], # Indices 53552 to 53568
3348:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 417}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 380}], # Indices 53568 to 53584
3349:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 467}], # Indices 53584 to 53600
3350:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 451}], # Indices 53600 to 53616
3351:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 266}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 242}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 254}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 262}], # Indices 53616 to 53632
3352:[], # Indices 53632 to 53648
3353:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 462}], # Indices 53648 to 53664
3354:[], # Indices 53664 to 53680
3355:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 375}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 399}], # Indices 53680 to 53696
3356:[], # Indices 53696 to 53712
3357:[], # Indices 53712 to 53728
3358:[], # Indices 53728 to 53744
3359:[], # Indices 53744 to 53760
3360:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 367}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 432}], # Indices 53760 to 53776
3361:[], # Indices 53776 to 53792
3362:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 467}], # Indices 53792 to 53808
3363:[], # Indices 53808 to 53824
3364:[], # Indices 53824 to 53840
3365:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 468}], # Indices 53840 to 53856
3366:[], # Indices 53856 to 53872
3367:[], # Indices 53872 to 53888
3368:[], # Indices 53888 to 53904
3369:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 496}], # Indices 53904 to 53920
3370:[], # Indices 53920 to 53936
3371:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 485}], # Indices 53936 to 53952
3372:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 497}], # Indices 53952 to 53968
3373:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 470}], # Indices 53968 to 53984
3374:[], # Indices 53984 to 54000
3375:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 464}], # Indices 54000 to 54016
3376:[], # Indices 54016 to 54032
3377:[], # Indices 54032 to 54048
3378:[], # Indices 54048 to 54064
3379:[], # Indices 54064 to 54080
3380:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 497}], # Indices 54080 to 54096
3381:[], # Indices 54096 to 54112
3382:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 485}], # Indices 54112 to 54128
3383:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 423}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 377}], # Indices 54128 to 54144
3384:[], # Indices 54144 to 54160
3385:[], # Indices 54160 to 54176
3386:[], # Indices 54176 to 54192
3387:[], # Indices 54192 to 54208
3388:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 464}], # Indices 54208 to 54224
3389:[], # Indices 54224 to 54240
3390:[], # Indices 54240 to 54256
3391:[], # Indices 54256 to 54272
3392:[], # Indices 54272 to 54288
3393:[], # Indices 54288 to 54304
3394:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 475}], # Indices 54304 to 54320
3395:[], # Indices 54320 to 54336
3396:[], # Indices 54336 to 54352
3397:[], # Indices 54352 to 54368
3398:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 473}], # Indices 54368 to 54384
3399:[], # Indices 54384 to 54400
3400:[], # Indices 54400 to 54416
3401:[], # Indices 54416 to 54432
3402:[], # Indices 54432 to 54448
3403:[], # Indices 54448 to 54464
3404:[], # Indices 54464 to 54480
3405:[], # Indices 54480 to 54496
3406:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 481}], # Indices 54496 to 54512
3407:[], # Indices 54512 to 54528
3408:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 489}], # Indices 54528 to 54544
3409:[], # Indices 54544 to 54560
3410:[], # Indices 54560 to 54576
3411:[], # Indices 54576 to 54592
3412:[], # Indices 54592 to 54608
3413:[], # Indices 54608 to 54624
3414:[], # Indices 54624 to 54640
3415:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 427}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 389}], # Indices 54640 to 54656
3416:[], # Indices 54656 to 54672
3417:[], # Indices 54672 to 54688
3418:[], # Indices 54688 to 54704
3419:[{'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 92}], # Indices 54704 to 54720
3420:[], # Indices 54720 to 54736
3421:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 483}], # Indices 54736 to 54752
3422:[], # Indices 54752 to 54768
3423:[], # Indices 54768 to 54784
3424:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 481}], # Indices 54784 to 54800
3425:[], # Indices 54800 to 54816
3426:[], # Indices 54816 to 54832
3427:[], # Indices 54832 to 54848
3428:[], # Indices 54848 to 54864
3429:[], # Indices 54864 to 54880
3430:[], # Indices 54880 to 54896
3431:[], # Indices 54896 to 54912
3432:[], # Indices 54912 to 54928
3433:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 365}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 416}], # Indices 54928 to 54944
3434:[], # Indices 54944 to 54960
3435:[], # Indices 54960 to 54976
3436:[], # Indices 54976 to 54992
3437:[], # Indices 54992 to 55008
3438:[], # Indices 55008 to 55024
3439:[], # Indices 55024 to 55040
3440:[], # Indices 55040 to 55056
3441:[], # Indices 55056 to 55072
3442:[], # Indices 55072 to 55088
3443:[], # Indices 55088 to 55104
3444:[], # Indices 55104 to 55120
3445:[], # Indices 55120 to 55136
3446:[], # Indices 55136 to 55152
3447:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 487}], # Indices 55152 to 55168
3448:[], # Indices 55168 to 55184
3449:[], # Indices 55184 to 55200
3450:[], # Indices 55200 to 55216
3451:[], # Indices 55216 to 55232
3452:[], # Indices 55232 to 55248
3453:[], # Indices 55248 to 55264
3454:[], # Indices 55264 to 55280
3455:[], # Indices 55280 to 55296
3456:[], # Indices 55296 to 55312
3457:[], # Indices 55312 to 55328
3458:[], # Indices 55328 to 55344
3459:[], # Indices 55344 to 55360
3460:[], # Indices 55360 to 55376
3461:[], # Indices 55376 to 55392
3462:[], # Indices 55392 to 55408
3463:[], # Indices 55408 to 55424
3464:[], # Indices 55424 to 55440
3465:[], # Indices 55440 to 55456
3466:[], # Indices 55456 to 55472
3467:[], # Indices 55472 to 55488
3468:[], # Indices 55488 to 55504
3469:[], # Indices 55504 to 55520
3470:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 493}], # Indices 55520 to 55536
3471:[], # Indices 55536 to 55552
3472:[], # Indices 55552 to 55568
3473:[], # Indices 55568 to 55584
3474:[], # Indices 55584 to 55600
3475:[], # Indices 55600 to 55616
3476:[], # Indices 55616 to 55632
3477:[], # Indices 55632 to 55648
3478:[], # Indices 55648 to 55664
3479:[], # Indices 55664 to 55680
3480:[], # Indices 55680 to 55696
3481:[], # Indices 55696 to 55712
3482:[], # Indices 55712 to 55728
3483:[], # Indices 55728 to 55744
3484:[], # Indices 55744 to 55760
3485:[], # Indices 55760 to 55776
3486:[], # Indices 55776 to 55792
3487:[], # Indices 55792 to 55808
3488:[], # Indices 55808 to 55824
3489:[], # Indices 55824 to 55840
3490:[], # Indices 55840 to 55856
3491:[], # Indices 55856 to 55872
3492:[], # Indices 55872 to 55888
3493:[], # Indices 55888 to 55904
3494:[], # Indices 55904 to 55920
3495:[], # Indices 55920 to 55936
3496:[], # Indices 55936 to 55952
3497:[], # Indices 55952 to 55968
3498:[], # Indices 55968 to 55984
3499:[], # Indices 55984 to 56000
3500:[], # Indices 56000 to 56016
3501:[], # Indices 56016 to 56032
3502:[], # Indices 56032 to 56048
3503:[], # Indices 56048 to 56064
3504:[], # Indices 56064 to 56080
3505:[], # Indices 56080 to 56096
3506:[], # Indices 56096 to 56112
3507:[], # Indices 56112 to 56128
3508:[], # Indices 56128 to 56144
3509:[], # Indices 56144 to 56160
3510:[], # Indices 56160 to 56176
3511:[], # Indices 56176 to 56192
3512:[], # Indices 56192 to 56208
3513:[], # Indices 56208 to 56224
3514:[], # Indices 56224 to 56240
3515:[], # Indices 56240 to 56256
3516:[], # Indices 56256 to 56272
3517:[], # Indices 56272 to 56288
3518:[], # Indices 56288 to 56304
3519:[], # Indices 56304 to 56320
3520:[], # Indices 56320 to 56336
3521:[], # Indices 56336 to 56352
3522:[], # Indices 56352 to 56368
3523:[], # Indices 56368 to 56384
3524:[], # Indices 56384 to 56400
3525:[], # Indices 56400 to 56416
3526:[], # Indices 56416 to 56432
3527:[], # Indices 56432 to 56448
3528:[], # Indices 56448 to 56464
3529:[], # Indices 56464 to 56480
3530:[], # Indices 56480 to 56496
3531:[], # Indices 56496 to 56512
3532:[], # Indices 56512 to 56528
3533:[], # Indices 56528 to 56544
3534:[], # Indices 56544 to 56560
3535:[], # Indices 56560 to 56576
3536:[], # Indices 56576 to 56592
3537:[], # Indices 56592 to 56608
3538:[], # Indices 56608 to 56624
3539:[], # Indices 56624 to 56640
3540:[], # Indices 56640 to 56656
3541:[], # Indices 56656 to 56672
3542:[], # Indices 56672 to 56688
3543:[], # Indices 56688 to 56704
3544:[], # Indices 56704 to 56720
3545:[], # Indices 56720 to 56736
3546:[], # Indices 56736 to 56752
3547:[], # Indices 56752 to 56768
3548:[], # Indices 56768 to 56784
3549:[], # Indices 56784 to 56800
3550:[], # Indices 56800 to 56816
3551:[], # Indices 56816 to 56832
3552:[], # Indices 56832 to 56848
3553:[], # Indices 56848 to 56864
3554:[], # Indices 56864 to 56880
3555:[], # Indices 56880 to 56896
3556:[], # Indices 56896 to 56912
3557:[], # Indices 56912 to 56928
3558:[], # Indices 56928 to 56944
3559:[], # Indices 56944 to 56960
3560:[], # Indices 56960 to 56976
3561:[], # Indices 56976 to 56992
3562:[], # Indices 56992 to 57008
3563:[], # Indices 57008 to 57024
3564:[], # Indices 57024 to 57040
3565:[], # Indices 57040 to 57056
3566:[], # Indices 57056 to 57072
3567:[], # Indices 57072 to 57088
3568:[], # Indices 57088 to 57104
3569:[], # Indices 57104 to 57120
3570:[], # Indices 57120 to 57136
3571:[], # Indices 57136 to 57152
3572:[], # Indices 57152 to 57168
3573:[], # Indices 57168 to 57184
3574:[], # Indices 57184 to 57200
3575:[], # Indices 57200 to 57216
3576:[], # Indices 57216 to 57232
3577:[], # Indices 57232 to 57248
3578:[], # Indices 57248 to 57264
3579:[], # Indices 57264 to 57280
3580:[], # Indices 57280 to 57296
3581:[], # Indices 57296 to 57312
3582:[], # Indices 57312 to 57328
3583:[], # Indices 57328 to 57344
3584:[], # Indices 57344 to 57360
3585:[], # Indices 57360 to 57376
3586:[], # Indices 57376 to 57392
3587:[], # Indices 57392 to 57408
3588:[], # Indices 57408 to 57424
3589:[], # Indices 57424 to 57440
3590:[], # Indices 57440 to 57456
3591:[], # Indices 57456 to 57472
3592:[], # Indices 57472 to 57488
3593:[], # Indices 57488 to 57504
3594:[], # Indices 57504 to 57520
3595:[], # Indices 57520 to 57536
3596:[], # Indices 57536 to 57552
3597:[], # Indices 57552 to 57568
3598:[], # Indices 57568 to 57584
3599:[], # Indices 57584 to 57600
3600:[], # Indices 57600 to 57616
3601:[], # Indices 57616 to 57632
3602:[], # Indices 57632 to 57648
3603:[], # Indices 57648 to 57664
3604:[], # Indices 57664 to 57680
3605:[], # Indices 57680 to 57696
3606:[], # Indices 57696 to 57712
3607:[], # Indices 57712 to 57728
3608:[], # Indices 57728 to 57744
3609:[], # Indices 57744 to 57760
3610:[], # Indices 57760 to 57776
3611:[], # Indices 57776 to 57792
3612:[], # Indices 57792 to 57808
3613:[], # Indices 57808 to 57824
3614:[], # Indices 57824 to 57840
3615:[], # Indices 57840 to 57856
3616:[], # Indices 57856 to 57872
3617:[], # Indices 57872 to 57888
3618:[], # Indices 57888 to 57904
3619:[], # Indices 57904 to 57920
3620:[], # Indices 57920 to 57936
3621:[], # Indices 57936 to 57952
3622:[], # Indices 57952 to 57968
3623:[], # Indices 57968 to 57984
3624:[], # Indices 57984 to 58000
3625:[], # Indices 58000 to 58016
3626:[], # Indices 58016 to 58032
3627:[], # Indices 58032 to 58048
3628:[], # Indices 58048 to 58064
3629:[], # Indices 58064 to 58080
3630:[], # Indices 58080 to 58096
3631:[], # Indices 58096 to 58112
3632:[], # Indices 58112 to 58128
3633:[], # Indices 58128 to 58144
3634:[], # Indices 58144 to 58160
3635:[], # Indices 58160 to 58176
3636:[], # Indices 58176 to 58192
3637:[], # Indices 58192 to 58208
3638:[], # Indices 58208 to 58224
3639:[], # Indices 58224 to 58240
3640:[], # Indices 58240 to 58256
3641:[], # Indices 58256 to 58272
3642:[], # Indices 58272 to 58288
3643:[], # Indices 58288 to 58304
3644:[], # Indices 58304 to 58320
3645:[], # Indices 58320 to 58336
3646:[], # Indices 58336 to 58352
3647:[], # Indices 58352 to 58368
3648:[], # Indices 58368 to 58384
3649:[], # Indices 58384 to 58400
3650:[], # Indices 58400 to 58416
3651:[], # Indices 58416 to 58432
3652:[], # Indices 58432 to 58448
3653:[], # Indices 58448 to 58464
3654:[], # Indices 58464 to 58480
3655:[], # Indices 58480 to 58496
3656:[], # Indices 58496 to 58512
3657:[], # Indices 58512 to 58528
3658:[], # Indices 58528 to 58544
3659:[], # Indices 58544 to 58560
3660:[], # Indices 58560 to 58576
3661:[], # Indices 58576 to 58592
3662:[], # Indices 58592 to 58608
3663:[], # Indices 58608 to 58624
3664:[], # Indices 58624 to 58640
3665:[], # Indices 58640 to 58656
3666:[], # Indices 58656 to 58672
3667:[], # Indices 58672 to 58688
3668:[], # Indices 58688 to 58704
3669:[], # Indices 58704 to 58720
3670:[], # Indices 58720 to 58736
3671:[], # Indices 58736 to 58752
3672:[], # Indices 58752 to 58768
3673:[], # Indices 58768 to 58784
3674:[], # Indices 58784 to 58800
3675:[], # Indices 58800 to 58816
3676:[], # Indices 58816 to 58832
3677:[], # Indices 58832 to 58848
3678:[], # Indices 58848 to 58864
3679:[], # Indices 58864 to 58880
3680:[], # Indices 58880 to 58896
3681:[], # Indices 58896 to 58912
3682:[], # Indices 58912 to 58928
3683:[], # Indices 58928 to 58944
3684:[], # Indices 58944 to 58960
3685:[], # Indices 58960 to 58976
3686:[], # Indices 58976 to 58992
3687:[], # Indices 58992 to 59008
3688:[], # Indices 59008 to 59024
3689:[], # Indices 59024 to 59040
3690:[], # Indices 59040 to 59056
3691:[], # Indices 59056 to 59072
3692:[], # Indices 59072 to 59088
3693:[], # Indices 59088 to 59104
3694:[], # Indices 59104 to 59120
3695:[], # Indices 59120 to 59136
3696:[], # Indices 59136 to 59152
3697:[], # Indices 59152 to 59168
3698:[], # Indices 59168 to 59184
3699:[], # Indices 59184 to 59200
3700:[], # Indices 59200 to 59216
3701:[], # Indices 59216 to 59232
3702:[], # Indices 59232 to 59248
3703:[], # Indices 59248 to 59264
3704:[], # Indices 59264 to 59280
3705:[], # Indices 59280 to 59296
3706:[], # Indices 59296 to 59312
3707:[], # Indices 59312 to 59328
3708:[], # Indices 59328 to 59344
3709:[], # Indices 59344 to 59360
3710:[], # Indices 59360 to 59376
3711:[], # Indices 59376 to 59392
3712:[], # Indices 59392 to 59408
3713:[], # Indices 59408 to 59424
3714:[], # Indices 59424 to 59440
3715:[], # Indices 59440 to 59456
3716:[], # Indices 59456 to 59472
3717:[], # Indices 59472 to 59488
3718:[], # Indices 59488 to 59504
3719:[], # Indices 59504 to 59520
3720:[], # Indices 59520 to 59536
3721:[], # Indices 59536 to 59552
3722:[], # Indices 59552 to 59568
3723:[], # Indices 59568 to 59584
3724:[], # Indices 59584 to 59600
3725:[], # Indices 59600 to 59616
3726:[], # Indices 59616 to 59632
3727:[], # Indices 59632 to 59648
3728:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 416}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 381}], # Indices 59648 to 59664
3729:[{'index_dec': 0, 'index_bin': '0000', 'val': 14, 'counts': 203}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 191}, {'index_dec': 12, 'index_bin': '1100', 'val': 12, 'counts': 190}, {'index_dec': 13, 'index_bin': '1101', 'val': 15, 'counts': 211}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 184}], # Indices 59664 to 59680
3730:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 379}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 415}], # Indices 59680 to 59696
3731:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 242}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 253}, {'index_dec': 7, 'index_bin': '0111', 'val': 15, 'counts': 286}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 243}], # Indices 59696 to 59712
3732:[], # Indices 59712 to 59728
3733:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 470}], # Indices 59728 to 59744
3734:[], # Indices 59744 to 59760
3735:[], # Indices 59760 to 59776
3736:[], # Indices 59776 to 59792
3737:[], # Indices 59792 to 59808
3738:[], # Indices 59808 to 59824
3739:[], # Indices 59824 to 59840
3740:[], # Indices 59840 to 59856
3741:[], # Indices 59856 to 59872
3742:[], # Indices 59872 to 59888
3743:[], # Indices 59888 to 59904
3744:[], # Indices 59904 to 59920
3745:[], # Indices 59920 to 59936
3746:[], # Indices 59936 to 59952
3747:[], # Indices 59952 to 59968
3748:[], # Indices 59968 to 59984
3749:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 243}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 239}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 269}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 273}], # Indices 59984 to 60000
3750:[{'index_dec': 1, 'index_bin': '0001', 'val': 13, 'counts': 151}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 147}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 138}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 154}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 140}, {'index_dec': 14, 'index_bin': '1110', 'val': 14, 'counts': 157}], # Indices 60000 to 60016
3751:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 252}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 272}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 255}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 245}], # Indices 60016 to 60032
3752:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 285}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 349}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 352}], # Indices 60032 to 60048
3753:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 484}], # Indices 60048 to 60064
3754:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 308}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 330}, {'index_dec': 11, 'index_bin': '1011', 'val': 13, 'counts': 324}], # Indices 60064 to 60080
3755:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 405}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 372}], # Indices 60080 to 60096
3756:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 348}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 312}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 314}], # Indices 60096 to 60112
3757:[{'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 419}, {'index_dec': 13, 'index_bin': '1101', 'val': 14, 'counts': 382}], # Indices 60112 to 60128
3758:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 402}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 417}], # Indices 60128 to 60144
3759:[{'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 397}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 405}], # Indices 60144 to 60160
3760:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 390}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 411}], # Indices 60160 to 60176
3761:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 132}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 144}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 142}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 152}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 141}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 154}], # Indices 60176 to 60192
3762:[{'index_dec': 2, 'index_bin': '0010', 'val': 15, 'counts': 392}, {'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 400}], # Indices 60192 to 60208
3763:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 506}], # Indices 60208 to 60224
3764:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 295}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 361}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 308}], # Indices 60224 to 60240
3765:[], # Indices 60240 to 60256
3766:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 338}, {'index_dec': 7, 'index_bin': '0111', 'val': 15, 'counts': 311}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 323}], # Indices 60256 to 60272
3767:[], # Indices 60272 to 60288
3768:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 455}], # Indices 60288 to 60304
3769:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 266}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 253}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 244}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 261}], # Indices 60304 to 60320
3770:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 401}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 393}], # Indices 60320 to 60336
3771:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 234}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 263}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 284}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 243}], # Indices 60336 to 60352
3772:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 197}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 213}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 214}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 172}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 189}], # Indices 60352 to 60368
3773:[{'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 241}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 270}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 262}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 251}], # Indices 60368 to 60384
3774:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 377}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 420}], # Indices 60384 to 60400
3775:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 314}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 330}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 337}], # Indices 60400 to 60416
3776:[{'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 437}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 374}], # Indices 60416 to 60432
3777:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 246}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 252}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 255}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 271}], # Indices 60432 to 60448
3778:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 405}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 394}], # Indices 60448 to 60464
3779:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 422}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 391}], # Indices 60464 to 60480
3780:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 412}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 396}], # Indices 60480 to 60496
3781:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 375}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 409}], # Indices 60496 to 60512
3782:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 512}], # Indices 60512 to 60528
3783:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 324}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 322}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 325}], # Indices 60528 to 60544
3784:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 317}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 332}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 326}], # Indices 60544 to 60560
3785:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 341}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 330}, {'index_dec': 13, 'index_bin': '1101', 'val': 13, 'counts': 315}], # Indices 60560 to 60576
3786:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 139}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 164}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 141}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 143}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 155}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 140}], # Indices 60576 to 60592
3787:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 188}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 179}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 213}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 186}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 206}], # Indices 60592 to 60608
3788:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 265}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 253}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 229}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 277}], # Indices 60608 to 60624
3789:[], # Indices 60624 to 60640
3790:[], # Indices 60640 to 60656
3791:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 337}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 303}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 312}], # Indices 60656 to 60672
3792:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 381}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 424}], # Indices 60672 to 60688
3793:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 391}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 415}], # Indices 60688 to 60704
3794:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 397}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 394}], # Indices 60704 to 60720
3795:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 480}], # Indices 60720 to 60736
3796:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 249}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 270}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 261}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 244}], # Indices 60736 to 60752
3797:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 260}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 258}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 255}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 251}], # Indices 60752 to 60768
3798:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 196}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 193}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 195}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 198}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 211}], # Indices 60768 to 60784
3799:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 342}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 324}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 313}], # Indices 60784 to 60800
3800:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 399}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 395}], # Indices 60800 to 60816
3801:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 391}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 434}], # Indices 60816 to 60832
3802:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 421}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 371}], # Indices 60832 to 60848
3803:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 474}], # Indices 60848 to 60864
3804:[{'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 478}], # Indices 60864 to 60880
3805:[], # Indices 60880 to 60896
3806:[], # Indices 60896 to 60912
3807:[], # Indices 60912 to 60928
3808:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 311}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 299}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 360}], # Indices 60928 to 60944
3809:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 494}], # Indices 60944 to 60960
3810:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 348}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 318}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 302}], # Indices 60960 to 60976
3811:[{'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 317}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 343}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 319}], # Indices 60976 to 60992
3812:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 475}], # Indices 60992 to 61008
3813:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 465}], # Indices 61008 to 61024
3814:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 415}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 393}], # Indices 61024 to 61040
3815:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 479}], # Indices 61040 to 61056
3816:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 399}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 403}], # Indices 61056 to 61072
3817:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 267}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 258}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 249}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 250}], # Indices 61072 to 61088
3818:[], # Indices 61088 to 61104
3819:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 494}], # Indices 61104 to 61120
3820:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 484}], # Indices 61120 to 61136
3821:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 473}], # Indices 61136 to 61152
3822:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 467}], # Indices 61152 to 61168
3823:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 395}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 383}], # Indices 61168 to 61184
3824:[], # Indices 61184 to 61200
3825:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 501}], # Indices 61200 to 61216
3826:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 347}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 293}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 329}], # Indices 61216 to 61232
3827:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 302}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 328}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 348}], # Indices 61232 to 61248
3828:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 257}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 243}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 251}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 273}], # Indices 61248 to 61264
3829:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 316}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 344}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 319}], # Indices 61264 to 61280
3830:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 420}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 366}], # Indices 61280 to 61296
3831:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 473}], # Indices 61296 to 61312
3832:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 257}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 250}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 256}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 261}], # Indices 61312 to 61328
3833:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 477}], # Indices 61328 to 61344
3834:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 492}], # Indices 61344 to 61360
3835:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 415}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 380}], # Indices 61360 to 61376
3836:[], # Indices 61376 to 61392
3837:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 406}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 398}], # Indices 61392 to 61408
3838:[], # Indices 61408 to 61424
3839:[], # Indices 61424 to 61440
3840:[], # Indices 61440 to 61456
3841:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 380}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 418}], # Indices 61456 to 61472
3842:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 393}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 407}], # Indices 61472 to 61488
3843:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 478}], # Indices 61488 to 61504
3844:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 398}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 396}], # Indices 61504 to 61520
3845:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 488}], # Indices 61520 to 61536
3846:[], # Indices 61536 to 61552
3847:[], # Indices 61552 to 61568
3848:[], # Indices 61568 to 61584
3849:[], # Indices 61584 to 61600
3850:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 317}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 324}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 318}], # Indices 61600 to 61616
3851:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 459}], # Indices 61616 to 61632
3852:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 324}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 300}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 348}], # Indices 61632 to 61648
3853:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 414}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 372}], # Indices 61648 to 61664
3854:[], # Indices 61664 to 61680
3855:[], # Indices 61680 to 61696
3856:[], # Indices 61696 to 61712
3857:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 480}], # Indices 61712 to 61728
3858:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 470}], # Indices 61728 to 61744
3859:[], # Indices 61744 to 61760
3860:[], # Indices 61760 to 61776
3861:[], # Indices 61776 to 61792
3862:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 484}], # Indices 61792 to 61808
3863:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 451}], # Indices 61808 to 61824
3864:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 396}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 395}], # Indices 61824 to 61840
3865:[], # Indices 61840 to 61856
3866:[], # Indices 61856 to 61872
3867:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 511}], # Indices 61872 to 61888
3868:[], # Indices 61888 to 61904
3869:[], # Indices 61904 to 61920
3870:[], # Indices 61920 to 61936
3871:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 205}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 186}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 213}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 175}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 196}], # Indices 61936 to 61952
3872:[], # Indices 61952 to 61968
3873:[], # Indices 61968 to 61984
3874:[], # Indices 61984 to 62000
3875:[], # Indices 62000 to 62016
3876:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 456}], # Indices 62016 to 62032
3877:[], # Indices 62032 to 62048
3878:[], # Indices 62048 to 62064
3879:[], # Indices 62064 to 62080
3880:[], # Indices 62080 to 62096
3881:[], # Indices 62096 to 62112
3882:[], # Indices 62112 to 62128
3883:[], # Indices 62128 to 62144
3884:[], # Indices 62144 to 62160
3885:[], # Indices 62160 to 62176
3886:[], # Indices 62176 to 62192
3887:[], # Indices 62192 to 62208
3888:[], # Indices 62208 to 62224
3889:[], # Indices 62224 to 62240
3890:[], # Indices 62240 to 62256
3891:[], # Indices 62256 to 62272
3892:[], # Indices 62272 to 62288
3893:[], # Indices 62288 to 62304
3894:[], # Indices 62304 to 62320
3895:[], # Indices 62320 to 62336
3896:[], # Indices 62336 to 62352
3897:[], # Indices 62352 to 62368
3898:[], # Indices 62368 to 62384
3899:[], # Indices 62384 to 62400
3900:[], # Indices 62400 to 62416
3901:[], # Indices 62416 to 62432
3902:[], # Indices 62432 to 62448
3903:[], # Indices 62448 to 62464
3904:[], # Indices 62464 to 62480
3905:[], # Indices 62480 to 62496
3906:[], # Indices 62496 to 62512
3907:[], # Indices 62512 to 62528
3908:[], # Indices 62528 to 62544
3909:[], # Indices 62544 to 62560
3910:[], # Indices 62560 to 62576
3911:[], # Indices 62576 to 62592
3912:[], # Indices 62592 to 62608
3913:[], # Indices 62608 to 62624
3914:[], # Indices 62624 to 62640
3915:[], # Indices 62640 to 62656
3916:[], # Indices 62656 to 62672
3917:[], # Indices 62672 to 62688
3918:[{'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 94}], # Indices 62688 to 62704
3919:[], # Indices 62704 to 62720
3920:[], # Indices 62720 to 62736
3921:[], # Indices 62736 to 62752
3922:[], # Indices 62752 to 62768
3923:[], # Indices 62768 to 62784
3924:[], # Indices 62784 to 62800
3925:[], # Indices 62800 to 62816
3926:[], # Indices 62816 to 62832
3927:[], # Indices 62832 to 62848
3928:[], # Indices 62848 to 62864
3929:[], # Indices 62864 to 62880
3930:[], # Indices 62880 to 62896
3931:[], # Indices 62896 to 62912
3932:[], # Indices 62912 to 62928
3933:[], # Indices 62928 to 62944
3934:[], # Indices 62944 to 62960
3935:[], # Indices 62960 to 62976
3936:[], # Indices 62976 to 62992
3937:[], # Indices 62992 to 63008
3938:[], # Indices 63008 to 63024
3939:[], # Indices 63024 to 63040
3940:[], # Indices 63040 to 63056
3941:[], # Indices 63056 to 63072
3942:[], # Indices 63072 to 63088
3943:[], # Indices 63088 to 63104
3944:[], # Indices 63104 to 63120
3945:[], # Indices 63120 to 63136
3946:[], # Indices 63136 to 63152
3947:[], # Indices 63152 to 63168
3948:[], # Indices 63168 to 63184
3949:[], # Indices 63184 to 63200
3950:[], # Indices 63200 to 63216
3951:[], # Indices 63216 to 63232
3952:[], # Indices 63232 to 63248
3953:[], # Indices 63248 to 63264
3954:[], # Indices 63264 to 63280
3955:[], # Indices 63280 to 63296
3956:[], # Indices 63296 to 63312
3957:[], # Indices 63312 to 63328
3958:[], # Indices 63328 to 63344
3959:[], # Indices 63344 to 63360
3960:[], # Indices 63360 to 63376
3961:[], # Indices 63376 to 63392
3962:[], # Indices 63392 to 63408
3963:[], # Indices 63408 to 63424
3964:[], # Indices 63424 to 63440
3965:[], # Indices 63440 to 63456
3966:[], # Indices 63456 to 63472
3967:[], # Indices 63472 to 63488
3968:[], # Indices 63488 to 63504
3969:[], # Indices 63504 to 63520
3970:[], # Indices 63520 to 63536
3971:[], # Indices 63536 to 63552
3972:[], # Indices 63552 to 63568
3973:[], # Indices 63568 to 63584
3974:[], # Indices 63584 to 63600
3975:[], # Indices 63600 to 63616
3976:[{'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 91}], # Indices 63616 to 63632
3977:[], # Indices 63632 to 63648
3978:[], # Indices 63648 to 63664
3979:[], # Indices 63664 to 63680
3980:[], # Indices 63680 to 63696
3981:[], # Indices 63696 to 63712
3982:[], # Indices 63712 to 63728
3983:[], # Indices 63728 to 63744
3984:[], # Indices 63744 to 63760
3985:[], # Indices 63760 to 63776
3986:[], # Indices 63776 to 63792
3987:[], # Indices 63792 to 63808
3988:[], # Indices 63808 to 63824
3989:[], # Indices 63824 to 63840
3990:[], # Indices 63840 to 63856
3991:[], # Indices 63856 to 63872
3992:[], # Indices 63872 to 63888
3993:[], # Indices 63888 to 63904
3994:[], # Indices 63904 to 63920
3995:[], # Indices 63920 to 63936
3996:[], # Indices 63936 to 63952
3997:[], # Indices 63952 to 63968
3998:[], # Indices 63968 to 63984
3999:[], # Indices 63984 to 64000
4000:[], # Indices 64000 to 64016
4001:[], # Indices 64016 to 64032
4002:[], # Indices 64032 to 64048
4003:[], # Indices 64048 to 64064
4004:[], # Indices 64064 to 64080
4005:[], # Indices 64080 to 64096
4006:[], # Indices 64096 to 64112
4007:[], # Indices 64112 to 64128
4008:[], # Indices 64128 to 64144
4009:[], # Indices 64144 to 64160
4010:[], # Indices 64160 to 64176
4011:[], # Indices 64176 to 64192
4012:[], # Indices 64192 to 64208
4013:[], # Indices 64208 to 64224
4014:[], # Indices 64224 to 64240
4015:[], # Indices 64240 to 64256
4016:[], # Indices 64256 to 64272
4017:[], # Indices 64272 to 64288
4018:[{'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 94}], # Indices 64288 to 64304
4019:[], # Indices 64304 to 64320
4020:[], # Indices 64320 to 64336
4021:[], # Indices 64336 to 64352
4022:[], # Indices 64352 to 64368
4023:[], # Indices 64368 to 64384
4024:[], # Indices 64384 to 64400
4025:[], # Indices 64400 to 64416
4026:[], # Indices 64416 to 64432
4027:[], # Indices 64432 to 64448
4028:[], # Indices 64448 to 64464
4029:[], # Indices 64464 to 64480
4030:[], # Indices 64480 to 64496
4031:[], # Indices 64496 to 64512
4032:[], # Indices 64512 to 64528
4033:[], # Indices 64528 to 64544
4034:[], # Indices 64544 to 64560
4035:[], # Indices 64560 to 64576
4036:[], # Indices 64576 to 64592
4037:[], # Indices 64592 to 64608
4038:[], # Indices 64608 to 64624
4039:[], # Indices 64624 to 64640
4040:[], # Indices 64640 to 64656
4041:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 100}, {'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 107}, {'index_dec': 5, 'index_bin': '0101', 'val': 14, 'counts': 94}, {'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 106}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 117}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 98}], # Indices 64656 to 64672
4042:[{'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 116}, {'index_dec': 4, 'index_bin': '0100', 'val': 12, 'counts': 93}, {'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 103}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 104}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 105}, {'index_dec': 14, 'index_bin': '1110', 'val': 13, 'counts': 92}], # Indices 64672 to 64688
4043:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 103}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 104}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 102}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 102}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 98}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 106}], # Indices 64688 to 64704
4044:[], # Indices 64704 to 64720
4045:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 322}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 332}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 304}], # Indices 64720 to 64736
4046:[], # Indices 64736 to 64752
4047:[], # Indices 64752 to 64768
4048:[], # Indices 64768 to 64784
4049:[], # Indices 64784 to 64800
4050:[], # Indices 64800 to 64816
4051:[], # Indices 64816 to 64832
4052:[], # Indices 64832 to 64848
4053:[], # Indices 64848 to 64864
4054:[], # Indices 64864 to 64880
4055:[], # Indices 64880 to 64896
4056:[], # Indices 64896 to 64912
4057:[], # Indices 64912 to 64928
4058:[], # Indices 64928 to 64944
4059:[], # Indices 64944 to 64960
4060:[], # Indices 64960 to 64976
4061:[{'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 464}], # Indices 64976 to 64992
4062:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 314}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 308}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 338}], # Indices 64992 to 65008
4063:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 258}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 253}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 279}, {'index_dec': 13, 'index_bin': '1101', 'val': 14, 'counts': 234}], # Indices 65008 to 65024
4064:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 201}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 212}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 191}, {'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 183}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 203}], # Indices 65024 to 65040
4065:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 284}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 239}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 256}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 245}], # Indices 65040 to 65056
4066:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 173}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 183}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 211}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 210}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 200}], # Indices 65056 to 65072
4067:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 322}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 299}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 349}], # Indices 65072 to 65088
4068:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 240}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 293}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 250}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 241}], # Indices 65088 to 65104
4069:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 193}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 182}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 191}, {'index_dec': 9, 'index_bin': '1001', 'val': 14, 'counts': 199}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 214}], # Indices 65104 to 65120
4070:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 396}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 403}], # Indices 65120 to 65136
4071:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 389}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 429}], # Indices 65136 to 65152
4072:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 96}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 101}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 111}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 106}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 103}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 91}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 108}], # Indices 65152 to 65168
4073:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 416}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 371}], # Indices 65168 to 65184
4074:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 393}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 420}], # Indices 65184 to 65200
4075:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 372}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 388}], # Indices 65200 to 65216
4076:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 346}, {'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 322}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 307}], # Indices 65216 to 65232
4077:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 195}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 186}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 196}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 207}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 191}], # Indices 65232 to 65248
4078:[{'index_dec': 1, 'index_bin': '0001', 'val': 14, 'counts': 277}, {'index_dec': 5, 'index_bin': '0101', 'val': 14, 'counts': 235}, {'index_dec': 7, 'index_bin': '0111', 'val': 14, 'counts': 265}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 247}], # Indices 65248 to 65264
4079:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 165}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 194}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 221}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 182}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 212}], # Indices 65264 to 65280
4080:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 336}, {'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 312}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 326}], # Indices 65280 to 65296
4081:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 319}, {'index_dec': 9, 'index_bin': '1001', 'val': 16, 'counts': 336}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 304}], # Indices 65296 to 65312
4082:[{'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 493}], # Indices 65312 to 65328
4083:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 259}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 276}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 228}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 261}], # Indices 65328 to 65344
4084:[{'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 264}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 243}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 253}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 264}], # Indices 65344 to 65360
4085:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 265}, {'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 245}, {'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 245}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 269}], # Indices 65360 to 65376
4086:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 322}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 339}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 308}], # Indices 65376 to 65392
4087:[{'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 385}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 405}], # Indices 65392 to 65408
4088:[{'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 413}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 387}], # Indices 65408 to 65424
4089:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 348}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 302}, {'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 309}], # Indices 65424 to 65440
4090:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 144}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 154}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 143}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 126}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 154}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 141}], # Indices 65440 to 65456
4091:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 301}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 346}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 317}], # Indices 65456 to 65472
4092:[{'index_dec': 12, 'index_bin': '1100', 'val': 12, 'counts': 419}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 403}], # Indices 65472 to 65488
4093:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 191}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 188}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 218}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 205}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 174}], # Indices 65488 to 65504
4094:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 401}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 397}], # Indices 65504 to 65520
4095:[{'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 406}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 395}], # Indices 65520 to 65536
4096:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 256}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 242}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 283}, {'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 243}], # Indices 65536 to 65552
4097:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 246}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 261}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 295}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 222}], # Indices 65552 to 65568
4098:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 190}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 186}, {'index_dec': 10, 'index_bin': '1010', 'val': 13, 'counts': 174}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 224}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 214}], # Indices 65568 to 65584
4099:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 243}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 267}, {'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 240}, {'index_dec': 10, 'index_bin': '1010', 'val': 13, 'counts': 274}], # Indices 65584 to 65600
4100:[{'index_dec': 0, 'index_bin': '0000', 'val': 12, 'counts': 470}], # Indices 65600 to 65616
4101:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 330}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 320}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 324}], # Indices 65616 to 65632
4102:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 298}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 337}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 345}], # Indices 65632 to 65648
4103:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 406}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 369}], # Indices 65648 to 65664
4104:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 411}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 395}], # Indices 65664 to 65680
4105:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 419}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 371}], # Indices 65680 to 65696
4106:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 299}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 341}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 336}], # Indices 65696 to 65712
4107:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 347}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 308}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 319}], # Indices 65712 to 65728
4108:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 102}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 103}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 106}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 100}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 106}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 97}], # Indices 65728 to 65744
4109:[{'index_dec': 1, 'index_bin': '0001', 'val': 15, 'counts': 255}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 234}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 265}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 270}], # Indices 65744 to 65760
4110:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 389}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 414}], # Indices 65760 to 65776
4111:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 187}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 210}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 187}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 189}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 211}], # Indices 65776 to 65792
4112:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 320}, {'index_dec': 13, 'index_bin': '1101', 'val': 13, 'counts': 303}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 352}], # Indices 65792 to 65808
4113:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 232}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 269}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 264}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 259}], # Indices 65808 to 65824
4114:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 330}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 309}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 333}], # Indices 65824 to 65840
4115:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 486}], # Indices 65840 to 65856
4116:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 344}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 313}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 335}], # Indices 65856 to 65872
4117:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 261}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 236}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 246}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 281}], # Indices 65872 to 65888
4118:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 475}], # Indices 65888 to 65904
4119:[{'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 327}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 304}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 327}], # Indices 65904 to 65920
4120:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 318}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 310}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 339}], # Indices 65920 to 65936
4121:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 471}], # Indices 65936 to 65952
4122:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 197}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 193}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 187}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 201}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 197}], # Indices 65952 to 65968
4123:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 397}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 392}], # Indices 65968 to 65984
4124:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 481}], # Indices 65984 to 66000
4125:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 223}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 176}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 198}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 175}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 204}], # Indices 66000 to 66016
4126:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 143}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 152}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 145}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 134}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 132}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 142}], # Indices 66016 to 66032
4127:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 419}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 387}], # Indices 66032 to 66048
4128:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 173}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 205}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 217}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 222}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 174}], # Indices 66048 to 66064
4129:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 275}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 250}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 264}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 235}], # Indices 66064 to 66080
4130:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 208}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 172}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 189}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 197}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 210}], # Indices 66080 to 66096
4131:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 394}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 381}], # Indices 66096 to 66112
4132:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 496}], # Indices 66112 to 66128
4133:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 236}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 253}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 263}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 272}], # Indices 66128 to 66144
4134:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 256}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 235}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 282}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 251}], # Indices 66144 to 66160
4135:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 244}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 269}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 233}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 278}], # Indices 66160 to 66176
4136:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 184}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 211}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 214}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 190}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 184}], # Indices 66176 to 66192
4137:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 483}], # Indices 66192 to 66208
4138:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 151}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 136}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 157}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 124}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 146}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 143}], # Indices 66208 to 66224
4139:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 245}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 252}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 283}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 244}], # Indices 66224 to 66240
4140:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 161}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 145}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 150}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 154}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 124}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 144}], # Indices 66240 to 66256
4141:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 130}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 147}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 134}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 153}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 133}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 149}], # Indices 66256 to 66272
4142:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 324}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 343}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 310}], # Indices 66272 to 66288
4143:[{'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 326}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 300}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 352}], # Indices 66288 to 66304
4144:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 342}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 303}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 305}], # Indices 66304 to 66320
4145:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 396}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 406}], # Indices 66320 to 66336
4146:[], # Indices 66336 to 66352
4147:[{'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 299}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 326}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 340}], # Indices 66352 to 66368
4148:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 132}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 154}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 133}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 125}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 156}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 150}], # Indices 66368 to 66384
4149:[{'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 501}], # Indices 66384 to 66400
4150:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 196}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 186}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 212}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 196}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 191}], # Indices 66400 to 66416
4151:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 407}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 414}], # Indices 66416 to 66432
4152:[], # Indices 66432 to 66448
4153:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 466}], # Indices 66448 to 66464
4154:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 389}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 400}], # Indices 66464 to 66480
4155:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 492}], # Indices 66480 to 66496
4156:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 328}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 330}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 323}], # Indices 66496 to 66512
4157:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 432}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 351}], # Indices 66512 to 66528
4158:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 411}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 388}], # Indices 66528 to 66544
4159:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 417}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 395}], # Indices 66544 to 66560
4160:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 191}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 198}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 195}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 198}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 197}], # Indices 66560 to 66576
4161:[{'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 246}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 277}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 255}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 246}], # Indices 66576 to 66592
4162:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 490}], # Indices 66592 to 66608
4163:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 315}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 355}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 301}], # Indices 66608 to 66624
4164:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 414}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 382}], # Indices 66624 to 66640
4165:[], # Indices 66640 to 66656
4166:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 412}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 391}], # Indices 66656 to 66672
4167:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 238}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 273}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 264}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 249}], # Indices 66672 to 66688
4168:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 478}], # Indices 66688 to 66704
4169:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 322}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 321}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 325}], # Indices 66704 to 66720
4170:[], # Indices 66720 to 66736
4171:[], # Indices 66736 to 66752
4172:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 385}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 403}], # Indices 66752 to 66768
4173:[], # Indices 66768 to 66784
4174:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 479}], # Indices 66784 to 66800
4175:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 496}], # Indices 66800 to 66816
4176:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 489}], # Indices 66816 to 66832
4177:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 302}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 314}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 351}], # Indices 66832 to 66848
4178:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 318}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 345}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 320}], # Indices 66848 to 66864
4179:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 327}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 336}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 320}], # Indices 66864 to 66880
4180:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 470}], # Indices 66880 to 66896
4181:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 473}], # Indices 66896 to 66912
4182:[], # Indices 66912 to 66928
4183:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 247}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 250}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 256}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 271}], # Indices 66928 to 66944
4184:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 408}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 382}], # Indices 66944 to 66960
4185:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 395}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 395}], # Indices 66960 to 66976
4186:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 254}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 254}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 240}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 276}], # Indices 66976 to 66992
4187:[], # Indices 66992 to 67008
4188:[], # Indices 67008 to 67024
4189:[], # Indices 67024 to 67040
4190:[], # Indices 67040 to 67056
4191:[], # Indices 67056 to 67072
4192:[], # Indices 67072 to 67088
4193:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 469}], # Indices 67088 to 67104
4194:[], # Indices 67104 to 67120
4195:[], # Indices 67120 to 67136
4196:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 508}], # Indices 67136 to 67152
4197:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 486}], # Indices 67152 to 67168
4198:[], # Indices 67168 to 67184
4199:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 319}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 322}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 337}], # Indices 67184 to 67200
4200:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 314}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 313}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 331}], # Indices 67200 to 67216
4201:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 380}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 392}], # Indices 67216 to 67232
4202:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 375}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 413}], # Indices 67232 to 67248
4203:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 395}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 396}], # Indices 67248 to 67264
4204:[], # Indices 67264 to 67280
4205:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 358}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 296}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 315}], # Indices 67280 to 67296
4206:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 498}], # Indices 67296 to 67312
4207:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 481}], # Indices 67312 to 67328
4208:[], # Indices 67328 to 67344
4209:[], # Indices 67344 to 67360
4210:[], # Indices 67360 to 67376
4211:[], # Indices 67376 to 67392
4212:[], # Indices 67392 to 67408
4213:[], # Indices 67408 to 67424
4214:[], # Indices 67424 to 67440
4215:[], # Indices 67440 to 67456
4216:[], # Indices 67456 to 67472
4217:[], # Indices 67472 to 67488
4218:[], # Indices 67488 to 67504
4219:[], # Indices 67504 to 67520
4220:[], # Indices 67520 to 67536
4221:[], # Indices 67536 to 67552
4222:[], # Indices 67552 to 67568
4223:[], # Indices 67568 to 67584
4224:[], # Indices 67584 to 67600
4225:[{'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 92}], # Indices 67600 to 67616
4226:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 382}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 418}], # Indices 67616 to 67632
4227:[], # Indices 67632 to 67648
4228:[], # Indices 67648 to 67664
4229:[], # Indices 67664 to 67680
4230:[], # Indices 67680 to 67696
4231:[], # Indices 67696 to 67712
4232:[], # Indices 67712 to 67728
4233:[], # Indices 67728 to 67744
4234:[], # Indices 67744 to 67760
4235:[], # Indices 67760 to 67776
4236:[], # Indices 67776 to 67792
4237:[], # Indices 67792 to 67808
4238:[], # Indices 67808 to 67824
4239:[], # Indices 67824 to 67840
4240:[], # Indices 67840 to 67856
4241:[], # Indices 67856 to 67872
4242:[], # Indices 67872 to 67888
4243:[], # Indices 67888 to 67904
4244:[], # Indices 67904 to 67920
4245:[], # Indices 67920 to 67936
4246:[], # Indices 67936 to 67952
4247:[], # Indices 67952 to 67968
4248:[], # Indices 67968 to 67984
4249:[], # Indices 67984 to 68000
4250:[], # Indices 68000 to 68016
4251:[], # Indices 68016 to 68032
4252:[], # Indices 68032 to 68048
4253:[], # Indices 68048 to 68064
4254:[], # Indices 68064 to 68080
4255:[], # Indices 68080 to 68096
4256:[{'index_dec': 15, 'index_bin': '1111', 'val': 4, 'counts': 91}], # Indices 68096 to 68112
4257:[], # Indices 68112 to 68128
4258:[], # Indices 68128 to 68144
4259:[], # Indices 68144 to 68160
4260:[], # Indices 68160 to 68176
4261:[], # Indices 68176 to 68192
4262:[], # Indices 68192 to 68208
4263:[{'index_dec': 13, 'index_bin': '1101', 'val': 4, 'counts': 92}], # Indices 68208 to 68224
4264:[], # Indices 68224 to 68240
4265:[], # Indices 68240 to 68256
4266:[], # Indices 68256 to 68272
4267:[], # Indices 68272 to 68288
4268:[], # Indices 68288 to 68304
4269:[], # Indices 68304 to 68320
4270:[], # Indices 68320 to 68336
4271:[], # Indices 68336 to 68352
4272:[], # Indices 68352 to 68368
4273:[], # Indices 68368 to 68384
4274:[], # Indices 68384 to 68400
4275:[], # Indices 68400 to 68416
4276:[], # Indices 68416 to 68432
4277:[], # Indices 68432 to 68448
4278:[], # Indices 68448 to 68464
4279:[], # Indices 68464 to 68480
4280:[], # Indices 68480 to 68496
4281:[], # Indices 68496 to 68512
4282:[], # Indices 68512 to 68528
4283:[], # Indices 68528 to 68544
4284:[], # Indices 68544 to 68560
4285:[], # Indices 68560 to 68576
4286:[], # Indices 68576 to 68592
4287:[], # Indices 68592 to 68608
4288:[], # Indices 68608 to 68624
4289:[], # Indices 68624 to 68640
4290:[], # Indices 68640 to 68656
4291:[], # Indices 68656 to 68672
4292:[], # Indices 68672 to 68688
4293:[], # Indices 68688 to 68704
4294:[], # Indices 68704 to 68720
4295:[], # Indices 68720 to 68736
4296:[], # Indices 68736 to 68752
4297:[], # Indices 68752 to 68768
4298:[], # Indices 68768 to 68784
4299:[], # Indices 68784 to 68800
4300:[], # Indices 68800 to 68816
4301:[], # Indices 68816 to 68832
4302:[], # Indices 68832 to 68848
4303:[], # Indices 68848 to 68864
4304:[], # Indices 68864 to 68880
4305:[], # Indices 68880 to 68896
4306:[], # Indices 68896 to 68912
4307:[], # Indices 68912 to 68928
4308:[], # Indices 68928 to 68944
4309:[], # Indices 68944 to 68960
4310:[], # Indices 68960 to 68976
4311:[{'index_dec': 9, 'index_bin': '1001', 'val': 15, 'counts': 256}, {'index_dec': 10, 'index_bin': '1010', 'val': 15, 'counts': 246}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 272}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 250}], # Indices 68976 to 68992
4312:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 141}, {'index_dec': 4, 'index_bin': '0100', 'val': 14, 'counts': 142}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 150}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 153}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 135}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 140}], # Indices 68992 to 69008
4313:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 259}, {'index_dec': 4, 'index_bin': '0100', 'val': 15, 'counts': 279}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 234}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 252}], # Indices 69008 to 69024
4314:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 327}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 295}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 332}], # Indices 69024 to 69040
4315:[{'index_dec': 1, 'index_bin': '0001', 'val': 0, 'counts': 100}, {'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 95}, {'index_dec': 3, 'index_bin': '0011', 'val': 6, 'counts': 104}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 91}, {'index_dec': 12, 'index_bin': '1100', 'val': 6, 'counts': 113}, {'index_dec': 13, 'index_bin': '1101', 'val': 6, 'counts': 112}], # Indices 69040 to 69056
4316:[{'index_dec': 3, 'index_bin': '0011', 'val': 15, 'counts': 212}, {'index_dec': 6, 'index_bin': '0110', 'val': 13, 'counts': 189}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 181}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 206}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 191}], # Indices 69056 to 69072
4317:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 267}, {'index_dec': 7, 'index_bin': '0111', 'val': 14, 'counts': 254}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 247}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 256}], # Indices 69072 to 69088
4318:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 192}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 175}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 215}, {'index_dec': 9, 'index_bin': '1001', 'val': 16, 'counts': 198}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 204}], # Indices 69088 to 69104
4319:[{'index_dec': 0, 'index_bin': '0000', 'val': 12, 'counts': 107}, {'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 102}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 94}, {'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 100}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 94}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 103}], # Indices 69104 to 69120
4320:[], # Indices 69120 to 69136
4321:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 282}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 249}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 273}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 220}], # Indices 69136 to 69152
4322:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 105}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 124}, {'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 108}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 92}, {'index_dec': 14, 'index_bin': '1110', 'val': 17, 'counts': 111}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 97}], # Indices 69152 to 69168
4323:[{'index_dec': 0, 'index_bin': '0000', 'val': 15, 'counts': 135}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 139}, {'index_dec': 5, 'index_bin': '0101', 'val': 15, 'counts': 154}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 126}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 151}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 146}], # Indices 69168 to 69184
4324:[{'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 124}, {'index_dec': 8, 'index_bin': '1000', 'val': 12, 'counts': 114}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 106}, {'index_dec': 14, 'index_bin': '1110', 'val': 18, 'counts': 101}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 101}], # Indices 69184 to 69200
4325:[], # Indices 69200 to 69216
4326:[], # Indices 69216 to 69232
4327:[{'index_dec': 0, 'index_bin': '0000', 'val': 0, 'counts': 201}, {'index_dec': 3, 'index_bin': '0011', 'val': 0, 'counts': 176}, {'index_dec': 6, 'index_bin': '0110', 'val': 0, 'counts': 191}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 201}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 208}], # Indices 69232 to 69248
4328:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 146}, {'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 143}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 136}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 152}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 130}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 143}], # Indices 69248 to 69264
4329:[{'index_dec': 0, 'index_bin': '0000', 'val': 17, 'counts': 473}], # Indices 69264 to 69280
4330:[], # Indices 69280 to 69296
4331:[], # Indices 69296 to 69312
4332:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 151}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 134}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 133}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 152}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 145}, {'index_dec': 15, 'index_bin': '1111', 'val': 13, 'counts': 155}], # Indices 69312 to 69328
4333:[{'index_dec': 4, 'index_bin': '0100', 'val': 15, 'counts': 372}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 429}], # Indices 69328 to 69344
4334:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 156}, {'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 130}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 138}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 158}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 144}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 146}], # Indices 69344 to 69360
4335:[{'index_dec': 2, 'index_bin': '0010', 'val': 14, 'counts': 399}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 402}], # Indices 69360 to 69376
4336:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 150}, {'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 174}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 143}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 135}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 154}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 124}], # Indices 69376 to 69392
4337:[], # Indices 69392 to 69408
4338:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 249}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 250}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 256}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 269}], # Indices 69408 to 69424
4339:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 143}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 132}, {'index_dec': 9, 'index_bin': '1001', 'val': 14, 'counts': 147}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 134}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 135}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 159}], # Indices 69424 to 69440
4340:[{'index_dec': 0, 'index_bin': '0000', 'val': 14, 'counts': 321}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 318}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 322}], # Indices 69440 to 69456
4341:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 191}, {'index_dec': 2, 'index_bin': '0010', 'val': 14, 'counts': 215}, {'index_dec': 7, 'index_bin': '0111', 'val': 13, 'counts': 207}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 167}, {'index_dec': 12, 'index_bin': '1100', 'val': 14, 'counts': 197}], # Indices 69456 to 69472
4342:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 181}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 199}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 207}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 202}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 185}], # Indices 69472 to 69488
4343:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 252}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 264}, {'index_dec': 9, 'index_bin': '1001', 'val': 14, 'counts': 279}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 229}], # Indices 69488 to 69504
4344:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 420}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 375}], # Indices 69504 to 69520
4345:[{'index_dec': 0, 'index_bin': '0000', 'val': 14, 'counts': 203}, {'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 196}, {'index_dec': 6, 'index_bin': '0110', 'val': 15, 'counts': 181}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 208}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 195}], # Indices 69520 to 69536
4346:[{'index_dec': 1, 'index_bin': '0001', 'val': 14, 'counts': 127}, {'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 158}, {'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 153}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 149}, {'index_dec': 11, 'index_bin': '1011', 'val': 15, 'counts': 140}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 132}], # Indices 69536 to 69552
4347:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 252}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 253}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 269}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 250}], # Indices 69552 to 69568
4348:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 130}, {'index_dec': 4, 'index_bin': '0100', 'val': 14, 'counts': 137}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 128}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 135}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 144}, {'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 162}], # Indices 69568 to 69584
4349:[{'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 322}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 307}, {'index_dec': 8, 'index_bin': '1000', 'val': 14, 'counts': 335}], # Indices 69584 to 69600
4350:[{'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 205}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 189}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 205}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 199}, {'index_dec': 15, 'index_bin': '1111', 'val': 15, 'counts': 188}], # Indices 69600 to 69616
4351:[{'index_dec': 1, 'index_bin': '0001', 'val': 13, 'counts': 104}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 102}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 106}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 97}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 91}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 102}], # Indices 69616 to 69632
4352:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 94}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 100}, {'index_dec': 7, 'index_bin': '0111', 'val': 15, 'counts': 98}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 115}, {'index_dec': 10, 'index_bin': '1010', 'val': 16, 'counts': 100}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 94}], # Indices 69632 to 69648
4353:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 134}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 156}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 139}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 155}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 129}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 154}], # Indices 69648 to 69664
4354:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 396}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 387}], # Indices 69664 to 69680
4355:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 381}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 411}], # Indices 69680 to 69696
4356:[], # Indices 69696 to 69712
4357:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 472}], # Indices 69712 to 69728
4358:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 248}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 284}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 240}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 252}], # Indices 69728 to 69744
4359:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 324}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 335}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 318}], # Indices 69744 to 69760
4360:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 328}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 318}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 334}], # Indices 69760 to 69776
4361:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 175}, {'index_dec': 4, 'index_bin': '0100', 'val': 15, 'counts': 176}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 215}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 223}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 201}], # Indices 69776 to 69792
4362:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 147}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 131}, {'index_dec': 3, 'index_bin': '0011', 'val': 14, 'counts': 141}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 154}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 135}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 138}], # Indices 69792 to 69808
4363:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 188}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 190}, {'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 198}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 207}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 180}], # Indices 69808 to 69824
4364:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 268}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 242}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 267}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 247}], # Indices 69824 to 69840
4365:[{'index_dec': 2, 'index_bin': '0010', 'val': 13, 'counts': 309}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 322}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 337}], # Indices 69840 to 69856
4366:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 148}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 157}, {'index_dec': 5, 'index_bin': '0101', 'val': 14, 'counts': 137}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 135}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 142}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 146}], # Indices 69856 to 69872
4367:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 266}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 252}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 241}, {'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 265}], # Indices 69872 to 69888
4368:[{'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 298}, {'index_dec': 13, 'index_bin': '1101', 'val': 13, 'counts': 336}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 330}], # Indices 69888 to 69904
4369:[{'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 253}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 254}, {'index_dec': 5, 'index_bin': '0101', 'val': 13, 'counts': 244}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 273}], # Indices 69904 to 69920
4370:[{'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 116}, {'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 108}, {'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 107}, {'index_dec': 6, 'index_bin': '0110', 'val': 0, 'counts': 103}], # Indices 69920 to 69936
4371:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 110}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 96}, {'index_dec': 6, 'index_bin': '0110', 'val': 13, 'counts': 106}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 96}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 100}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 109}], # Indices 69936 to 69952
4372:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 146}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 132}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 138}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 123}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 171}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 140}], # Indices 69952 to 69968
4373:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 199}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 171}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 172}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 205}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 214}], # Indices 69968 to 69984
4374:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 256}, {'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 253}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 255}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 260}], # Indices 69984 to 70000
4375:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 205}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 182}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 195}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 202}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 190}], # Indices 70000 to 70016
4376:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 249}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 261}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 256}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 258}], # Indices 70016 to 70032
4377:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 305}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 328}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 339}], # Indices 70032 to 70048
4378:[{'index_dec': 1, 'index_bin': '0001', 'val': 14, 'counts': 382}, {'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 406}], # Indices 70048 to 70064
4379:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 210}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 219}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 188}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 163}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 203}], # Indices 70064 to 70080
4380:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 185}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 219}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 188}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 204}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 173}], # Indices 70080 to 70096
4381:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 328}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 335}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 307}], # Indices 70096 to 70112
4382:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 236}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 249}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 278}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 261}], # Indices 70112 to 70128
4383:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 106}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 97}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 98}, {'index_dec': 10, 'index_bin': '1010', 'val': 15, 'counts': 93}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 98}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 109}], # Indices 70128 to 70144
4384:[{'index_dec': 2, 'index_bin': '0010', 'val': 0, 'counts': 323}, {'index_dec': 7, 'index_bin': '0111', 'val': 6, 'counts': 301}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 352}], # Indices 70144 to 70160
4385:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 181}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 186}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 213}, {'index_dec': 14, 'index_bin': '1110', 'val': 13, 'counts': 204}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 198}], # Indices 70160 to 70176
4386:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 201}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 191}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 207}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 187}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 189}], # Indices 70176 to 70192
4387:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 127}, {'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 98}, {'index_dec': 6, 'index_bin': '0110', 'val': 15, 'counts': 116}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 96}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 93}], # Indices 70192 to 70208
4388:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 268}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 273}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 250}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 233}], # Indices 70208 to 70224
4389:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 120}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 94}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 108}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 101}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 99}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 103}], # Indices 70224 to 70240
4390:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 238}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 267}, {'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 266}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 253}], # Indices 70240 to 70256
4391:[{'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 509}], # Indices 70256 to 70272
4392:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 238}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 189}, {'index_dec': 12, 'index_bin': '1100', 'val': 15, 'counts': 186}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 215}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 158}], # Indices 70272 to 70288
4393:[], # Indices 70288 to 70304
4394:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 327}, {'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 347}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 306}], # Indices 70304 to 70320
4395:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 138}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 132}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 165}, {'index_dec': 6, 'index_bin': '0110', 'val': 13, 'counts': 144}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 133}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 145}], # Indices 70320 to 70336
4396:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 215}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 212}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 181}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 178}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 194}], # Indices 70336 to 70352
4397:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 336}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 329}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 307}], # Indices 70352 to 70368
4398:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 92}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 107}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 94}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 115}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 105}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 96}], # Indices 70368 to 70384
4399:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 111}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 94}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 118}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 95}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 96}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 92}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 112}], # Indices 70384 to 70400
4400:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 317}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 330}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 323}], # Indices 70400 to 70416
4401:[{'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 504}], # Indices 70416 to 70432
4402:[{'index_dec': 1, 'index_bin': '0001', 'val': 14, 'counts': 183}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 196}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 218}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 193}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 197}], # Indices 70432 to 70448
4403:[{'index_dec': 5, 'index_bin': '0101', 'val': 12, 'counts': 199}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 190}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 185}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 215}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 187}], # Indices 70448 to 70464
4404:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 224}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 201}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 178}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 188}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 193}], # Indices 70464 to 70480
4405:[{'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 271}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 242}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 266}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 245}], # Indices 70480 to 70496
4406:[], # Indices 70496 to 70512
4407:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 492}], # Indices 70512 to 70528
4408:[], # Indices 70528 to 70544
4409:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 408}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 380}], # Indices 70544 to 70560
4410:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 101}, {'index_dec': 7, 'index_bin': '0111', 'val': 6, 'counts': 99}, {'index_dec': 8, 'index_bin': '1000', 'val': 5, 'counts': 91}, {'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 111}, {'index_dec': 10, 'index_bin': '1010', 'val': 4, 'counts': 109}, {'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 126}], # Indices 70560 to 70576
4411:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 332}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 306}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 336}], # Indices 70576 to 70592
4412:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 264}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 241}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 255}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 264}], # Indices 70592 to 70608
4413:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 382}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 412}], # Indices 70608 to 70624
4414:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 308}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 332}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 328}], # Indices 70624 to 70640
4415:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 210}, {'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 174}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 214}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 178}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 194}], # Indices 70640 to 70656
4416:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 191}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 173}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 205}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 215}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 194}], # Indices 70656 to 70672
4417:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 290}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 327}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 348}], # Indices 70672 to 70688
4418:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 415}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 371}], # Indices 70688 to 70704
4419:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 398}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 399}], # Indices 70704 to 70720
4420:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 376}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 418}], # Indices 70720 to 70736
4421:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 258}, {'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 256}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 250}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 260}], # Indices 70736 to 70752
4422:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 233}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 265}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 270}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 256}], # Indices 70752 to 70768
4423:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 423}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 416}], # Indices 70768 to 70784
4424:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 189}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 213}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 176}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 206}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 196}], # Indices 70784 to 70800
4425:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 292}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 351}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 327}], # Indices 70800 to 70816
4426:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 148}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 130}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 137}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 150}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 153}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 157}], # Indices 70816 to 70832
4427:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 250}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 239}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 256}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 279}], # Indices 70832 to 70848
4428:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 265}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 269}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 229}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 261}], # Indices 70848 to 70864
4429:[{'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 476}], # Indices 70864 to 70880
4430:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 184}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 197}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 193}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 214}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 194}], # Indices 70880 to 70896
4431:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 366}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 438}], # Indices 70896 to 70912
4432:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 412}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 390}], # Indices 70912 to 70928
4433:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 202}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 177}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 207}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 209}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 183}], # Indices 70928 to 70944
4434:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 308}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 320}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 334}], # Indices 70944 to 70960
4435:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 244}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 273}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 249}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 258}], # Indices 70960 to 70976
4436:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 334}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 317}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 323}], # Indices 70976 to 70992
4437:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 499}], # Indices 70992 to 71008
4438:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 185}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 199}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 198}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 205}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 197}], # Indices 71008 to 71024
4439:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 306}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 320}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 336}], # Indices 71024 to 71040
4440:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 367}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 426}], # Indices 71040 to 71056
4441:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 344}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 311}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 317}], # Indices 71056 to 71072
4442:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 407}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 408}], # Indices 71072 to 71088
4443:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 383}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 402}], # Indices 71088 to 71104
4444:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 345}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 323}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 315}], # Indices 71104 to 71120
4445:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 332}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 332}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 306}], # Indices 71120 to 71136
4446:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 260}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 263}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 256}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 245}], # Indices 71136 to 71152
4447:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 206}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 176}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 203}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 185}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 205}], # Indices 71152 to 71168
4448:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 393}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 399}], # Indices 71168 to 71184
4449:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 392}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 419}], # Indices 71184 to 71200
4450:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 255}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 270}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 241}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 258}], # Indices 71200 to 71216
4451:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 425}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 385}], # Indices 71216 to 71232
4452:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 487}], # Indices 71232 to 71248
4453:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 390}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 385}], # Indices 71248 to 71264
4454:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 388}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 390}], # Indices 71264 to 71280
4455:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 246}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 256}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 278}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 244}], # Indices 71280 to 71296
4456:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 483}], # Indices 71296 to 71312
4457:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 479}], # Indices 71312 to 71328
4458:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 438}], # Indices 71328 to 71344
4459:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 508}], # Indices 71344 to 71360
4460:[], # Indices 71360 to 71376
4461:[], # Indices 71376 to 71392
4462:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 498}], # Indices 71392 to 71408
4463:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 516}], # Indices 71408 to 71424
4464:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 468}], # Indices 71424 to 71440
4465:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 483}], # Indices 71440 to 71456
4466:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 481}], # Indices 71456 to 71472
4467:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 506}], # Indices 71472 to 71488
4468:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 480}], # Indices 71488 to 71504
4469:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 517}], # Indices 71504 to 71520
4470:[], # Indices 71520 to 71536
4471:[], # Indices 71536 to 71552
4472:[{'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 480}], # Indices 71552 to 71568
4473:[], # Indices 71568 to 71584
4474:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 189}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 205}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 189}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 181}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 207}], # Indices 71584 to 71600
4475:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 127}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 150}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 131}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 141}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 148}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 142}], # Indices 71600 to 71616
4476:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 481}], # Indices 71616 to 71632
4477:[], # Indices 71632 to 71648
4478:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 461}], # Indices 71648 to 71664
4479:[], # Indices 71664 to 71680
4480:[], # Indices 71680 to 71696
4481:[], # Indices 71696 to 71712
4482:[], # Indices 71712 to 71728
4483:[], # Indices 71728 to 71744
4484:[], # Indices 71744 to 71760
4485:[], # Indices 71760 to 71776
4486:[], # Indices 71776 to 71792
4487:[], # Indices 71792 to 71808
4488:[], # Indices 71808 to 71824
4489:[], # Indices 71824 to 71840
4490:[], # Indices 71840 to 71856
4491:[], # Indices 71856 to 71872
4492:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 463}], # Indices 71872 to 71888
4493:[], # Indices 71888 to 71904
4494:[], # Indices 71904 to 71920
4495:[], # Indices 71920 to 71936
4496:[], # Indices 71936 to 71952
4497:[], # Indices 71952 to 71968
4498:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 474}], # Indices 71968 to 71984
4499:[], # Indices 71984 to 72000
4500:[], # Indices 72000 to 72016
4501:[], # Indices 72016 to 72032
4502:[], # Indices 72032 to 72048
4503:[], # Indices 72048 to 72064
4504:[], # Indices 72064 to 72080
4505:[], # Indices 72080 to 72096
4506:[], # Indices 72096 to 72112
4507:[], # Indices 72112 to 72128
4508:[], # Indices 72128 to 72144
4509:[], # Indices 72144 to 72160
4510:[], # Indices 72160 to 72176
4511:[], # Indices 72176 to 72192
4512:[], # Indices 72192 to 72208
4513:[], # Indices 72208 to 72224
4514:[], # Indices 72224 to 72240
4515:[], # Indices 72240 to 72256
4516:[], # Indices 72256 to 72272
4517:[], # Indices 72272 to 72288
4518:[], # Indices 72288 to 72304
4519:[], # Indices 72304 to 72320
4520:[], # Indices 72320 to 72336
4521:[], # Indices 72336 to 72352
4522:[], # Indices 72352 to 72368
4523:[], # Indices 72368 to 72384
4524:[], # Indices 72384 to 72400
4525:[], # Indices 72400 to 72416
4526:[], # Indices 72416 to 72432
4527:[], # Indices 72432 to 72448
4528:[], # Indices 72448 to 72464
4529:[], # Indices 72464 to 72480
4530:[], # Indices 72480 to 72496
4531:[], # Indices 72496 to 72512
4532:[], # Indices 72512 to 72528
4533:[], # Indices 72528 to 72544
4534:[], # Indices 72544 to 72560
4535:[], # Indices 72560 to 72576
4536:[], # Indices 72576 to 72592
4537:[], # Indices 72592 to 72608
4538:[], # Indices 72608 to 72624
4539:[], # Indices 72624 to 72640
4540:[], # Indices 72640 to 72656
4541:[], # Indices 72656 to 72672
4542:[], # Indices 72672 to 72688
4543:[], # Indices 72688 to 72704
4544:[], # Indices 72704 to 72720
4545:[], # Indices 72720 to 72736
4546:[], # Indices 72736 to 72752
4547:[], # Indices 72752 to 72768
4548:[], # Indices 72768 to 72784
4549:[], # Indices 72784 to 72800
4550:[], # Indices 72800 to 72816
4551:[], # Indices 72816 to 72832
4552:[], # Indices 72832 to 72848
4553:[], # Indices 72848 to 72864
4554:[], # Indices 72864 to 72880
4555:[], # Indices 72880 to 72896
4556:[], # Indices 72896 to 72912
4557:[], # Indices 72912 to 72928
4558:[], # Indices 72928 to 72944
4559:[], # Indices 72944 to 72960
4560:[], # Indices 72960 to 72976
4561:[], # Indices 72976 to 72992
4562:[], # Indices 72992 to 73008
4563:[], # Indices 73008 to 73024
4564:[], # Indices 73024 to 73040
4565:[], # Indices 73040 to 73056
4566:[], # Indices 73056 to 73072
4567:[], # Indices 73072 to 73088
4568:[], # Indices 73088 to 73104
4569:[], # Indices 73104 to 73120
4570:[], # Indices 73120 to 73136
4571:[], # Indices 73136 to 73152
4572:[], # Indices 73152 to 73168
4573:[], # Indices 73168 to 73184
4574:[], # Indices 73184 to 73200
4575:[], # Indices 73200 to 73216
4576:[], # Indices 73216 to 73232
4577:[], # Indices 73232 to 73248
4578:[], # Indices 73248 to 73264
4579:[], # Indices 73264 to 73280
4580:[], # Indices 73280 to 73296
4581:[], # Indices 73296 to 73312
4582:[], # Indices 73312 to 73328
4583:[], # Indices 73328 to 73344
4584:[], # Indices 73344 to 73360
4585:[], # Indices 73360 to 73376
4586:[], # Indices 73376 to 73392
4587:[], # Indices 73392 to 73408
4588:[], # Indices 73408 to 73424
4589:[], # Indices 73424 to 73440
4590:[], # Indices 73440 to 73456
4591:[], # Indices 73456 to 73472
4592:[], # Indices 73472 to 73488
4593:[], # Indices 73488 to 73504
4594:[], # Indices 73504 to 73520
4595:[], # Indices 73520 to 73536
4596:[], # Indices 73536 to 73552
4597:[], # Indices 73552 to 73568
4598:[], # Indices 73568 to 73584
4599:[], # Indices 73584 to 73600
4600:[], # Indices 73600 to 73616
4601:[], # Indices 73616 to 73632
4602:[], # Indices 73632 to 73648
4603:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 143}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 130}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 156}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 149}, {'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 149}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 135}], # Indices 73648 to 73664
4604:[{'index_dec': 2, 'index_bin': '0010', 'val': 13, 'counts': 138}, {'index_dec': 3, 'index_bin': '0011', 'val': 15, 'counts': 138}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 145}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 147}, {'index_dec': 12, 'index_bin': '1100', 'val': 14, 'counts': 131}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 145}], # Indices 73664 to 73680
4605:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 94}, {'index_dec': 4, 'index_bin': '0100', 'val': 0, 'counts': 116}, {'index_dec': 6, 'index_bin': '0110', 'val': 0, 'counts': 111}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 100}, {'index_dec': 14, 'index_bin': '1110', 'val': 5, 'counts': 96}], # Indices 73680 to 73696
4606:[{'index_dec': 0, 'index_bin': '0000', 'val': 14, 'counts': 140}, {'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 155}, {'index_dec': 4, 'index_bin': '0100', 'val': 16, 'counts': 164}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 139}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 146}, {'index_dec': 13, 'index_bin': '1101', 'val': 18, 'counts': 145}], # Indices 73696 to 73712
4607:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 100}, {'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 105}, {'index_dec': 5, 'index_bin': '0101', 'val': 0, 'counts': 113}, {'index_dec': 10, 'index_bin': '1010', 'val': 0, 'counts': 110}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 99}], # Indices 73712 to 73728
4608:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 172}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 203}, {'index_dec': 7, 'index_bin': '0111', 'val': 15, 'counts': 207}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 200}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 202}], # Indices 73728 to 73744
4609:[{'index_dec': 3, 'index_bin': '0011', 'val': 0, 'counts': 157}, {'index_dec': 5, 'index_bin': '0101', 'val': 0, 'counts': 159}, {'index_dec': 9, 'index_bin': '1001', 'val': 6, 'counts': 142}, {'index_dec': 10, 'index_bin': '1010', 'val': 0, 'counts': 146}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 137}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 118}], # Indices 73744 to 73760
4610:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 96}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 93}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 95}, {'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 111}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 115}], # Indices 73760 to 73776
4611:[{'index_dec': 4, 'index_bin': '0100', 'val': 0, 'counts': 332}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 359}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 284}], # Indices 73776 to 73792
4612:[], # Indices 73792 to 73808
4613:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 155}, {'index_dec': 2, 'index_bin': '0010', 'val': 16, 'counts': 147}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 130}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 150}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 134}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 136}], # Indices 73808 to 73824
4614:[], # Indices 73824 to 73840
4615:[], # Indices 73840 to 73856
4616:[], # Indices 73856 to 73872
4617:[], # Indices 73872 to 73888
4618:[], # Indices 73888 to 73904
4619:[], # Indices 73904 to 73920
4620:[], # Indices 73920 to 73936
4621:[], # Indices 73936 to 73952
4622:[], # Indices 73952 to 73968
4623:[], # Indices 73968 to 73984
4624:[{'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 207}, {'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 196}, {'index_dec': 8, 'index_bin': '1000', 'val': 0, 'counts': 187}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 197}, {'index_dec': 13, 'index_bin': '1101', 'val': 0, 'counts': 194}], # Indices 73984 to 74000
4625:[{'index_dec': 4, 'index_bin': '0100', 'val': 0, 'counts': 133}, {'index_dec': 5, 'index_bin': '0101', 'val': 0, 'counts': 134}, {'index_dec': 8, 'index_bin': '1000', 'val': 0, 'counts': 160}, {'index_dec': 10, 'index_bin': '1010', 'val': 0, 'counts': 147}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 147}, {'index_dec': 13, 'index_bin': '1101', 'val': 6, 'counts': 156}], # Indices 74000 to 74016
4626:[], # Indices 74016 to 74032
4627:[{'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 191}, {'index_dec': 5, 'index_bin': '0101', 'val': 0, 'counts': 207}, {'index_dec': 13, 'index_bin': '1101', 'val': 6, 'counts': 197}, {'index_dec': 14, 'index_bin': '1110', 'val': 0, 'counts': 178}, {'index_dec': 15, 'index_bin': '1111', 'val': 6, 'counts': 209}], # Indices 74032 to 74048
4628:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 155}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 143}, {'index_dec': 5, 'index_bin': '0101', 'val': 14, 'counts': 142}, {'index_dec': 8, 'index_bin': '1000', 'val': 12, 'counts': 144}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 160}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 141}], # Indices 74048 to 74064
4629:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 117}, {'index_dec': 3, 'index_bin': '0011', 'val': 6, 'counts': 108}, {'index_dec': 4, 'index_bin': '0100', 'val': 0, 'counts': 100}, {'index_dec': 6, 'index_bin': '0110', 'val': 6, 'counts': 104}, {'index_dec': 8, 'index_bin': '1000', 'val': 0, 'counts': 92}, {'index_dec': 9, 'index_bin': '1001', 'val': 0, 'counts': 119}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 99}], # Indices 74064 to 74080
4630:[{'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 329}, {'index_dec': 6, 'index_bin': '0110', 'val': 0, 'counts': 310}, {'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 334}], # Indices 74080 to 74096
4631:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 251}, {'index_dec': 1, 'index_bin': '0001', 'val': 15, 'counts': 283}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 233}, {'index_dec': 11, 'index_bin': '1011', 'val': 13, 'counts': 257}], # Indices 74096 to 74112
4632:[], # Indices 74112 to 74128
4633:[], # Indices 74128 to 74144
4634:[{'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 93}, {'index_dec': 3, 'index_bin': '0011', 'val': 0, 'counts': 116}, {'index_dec': 8, 'index_bin': '1000', 'val': 0, 'counts': 98}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 99}, {'index_dec': 14, 'index_bin': '1110', 'val': 6, 'counts': 96}, {'index_dec': 15, 'index_bin': '1111', 'val': 0, 'counts': 95}], # Indices 74144 to 74160
4635:[], # Indices 74160 to 74176
4636:[{'index_dec': 1, 'index_bin': '0001', 'val': 0, 'counts': 156}, {'index_dec': 2, 'index_bin': '0010', 'val': 0, 'counts': 135}, {'index_dec': 7, 'index_bin': '0111', 'val': 6, 'counts': 146}, {'index_dec': 9, 'index_bin': '1001', 'val': 0, 'counts': 137}, {'index_dec': 13, 'index_bin': '1101', 'val': 0, 'counts': 140}, {'index_dec': 15, 'index_bin': '1111', 'val': 0, 'counts': 156}], # Indices 74176 to 74192
4637:[], # Indices 74192 to 74208
4638:[], # Indices 74208 to 74224
4639:[{'index_dec': 4, 'index_bin': '0100', 'val': 15, 'counts': 152}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 142}, {'index_dec': 7, 'index_bin': '0111', 'val': 14, 'counts': 129}, {'index_dec': 8, 'index_bin': '1000', 'val': 14, 'counts': 135}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 156}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 140}], # Indices 74224 to 74240
4640:[{'index_dec': 3, 'index_bin': '0011', 'val': 16, 'counts': 102}, {'index_dec': 5, 'index_bin': '0101', 'val': 15, 'counts': 117}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 93}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 97}, {'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 108}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 102}], # Indices 74240 to 74256
4641:[{'index_dec': 0, 'index_bin': '0000', 'val': 12, 'counts': 93}, {'index_dec': 1, 'index_bin': '0001', 'val': 13, 'counts': 104}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 106}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 97}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 111}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 94}], # Indices 74256 to 74272
4642:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 148}, {'index_dec': 7, 'index_bin': '0111', 'val': 0, 'counts': 159}, {'index_dec': 8, 'index_bin': '1000', 'val': 0, 'counts': 154}, {'index_dec': 10, 'index_bin': '1010', 'val': 0, 'counts': 145}, {'index_dec': 11, 'index_bin': '1011', 'val': 6, 'counts': 135}, {'index_dec': 15, 'index_bin': '1111', 'val': 0, 'counts': 144}], # Indices 74272 to 74288
4643:[], # Indices 74288 to 74304
4644:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 105}, {'index_dec': 4, 'index_bin': '0100', 'val': 14, 'counts': 109}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 91}, {'index_dec': 8, 'index_bin': '1000', 'val': 18, 'counts': 103}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 97}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 103}], # Indices 74304 to 74320
4645:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 108}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 92}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 95}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 106}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 110}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 104}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 96}], # Indices 74320 to 74336
4646:[{'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 134}, {'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 161}, {'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 147}, {'index_dec': 6, 'index_bin': '0110', 'val': 6, 'counts': 147}, {'index_dec': 8, 'index_bin': '1000', 'val': 0, 'counts': 156}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 140}], # Indices 74336 to 74352
4647:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 93}, {'index_dec': 1, 'index_bin': '0001', 'val': 5, 'counts': 105}, {'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 100}, {'index_dec': 5, 'index_bin': '0101', 'val': 4, 'counts': 110}, {'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 93}, {'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 109}], # Indices 74352 to 74368
4648:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 97}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 109}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 98}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 98}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 104}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 103}], # Indices 74368 to 74384
4649:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 110}, {'index_dec': 5, 'index_bin': '0101', 'val': 13, 'counts': 108}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 107}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 104}, {'index_dec': 13, 'index_bin': '1101', 'val': 13, 'counts': 100}, {'index_dec': 14, 'index_bin': '1110', 'val': 14, 'counts': 98}], # Indices 74384 to 74400
4650:[{'index_dec': 1, 'index_bin': '0001', 'val': 0, 'counts': 99}, {'index_dec': 2, 'index_bin': '0010', 'val': 6, 'counts': 102}, {'index_dec': 6, 'index_bin': '0110', 'val': 6, 'counts': 95}, {'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 108}, {'index_dec': 10, 'index_bin': '1010', 'val': 6, 'counts': 98}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 98}, {'index_dec': 15, 'index_bin': '1111', 'val': 0, 'counts': 99}], # Indices 74400 to 74416
4651:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 95}, {'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 117}, {'index_dec': 10, 'index_bin': '1010', 'val': 6, 'counts': 98}, {'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 98}, {'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 109}, {'index_dec': 14, 'index_bin': '1110', 'val': 6, 'counts': 98}], # Indices 74416 to 74432
4652:[], # Indices 74432 to 74448
4653:[], # Indices 74448 to 74464
4654:[{'index_dec': 1, 'index_bin': '0001', 'val': 5, 'counts': 208}, {'index_dec': 3, 'index_bin': '0011', 'val': 0, 'counts': 195}, {'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 199}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 189}, {'index_dec': 14, 'index_bin': '1110', 'val': 0, 'counts': 189}], # Indices 74464 to 74480
4655:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 92}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 97}, {'index_dec': 5, 'index_bin': '0101', 'val': 15, 'counts': 94}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 92}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 109}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 111}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 100}], # Indices 74480 to 74496
4656:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 132}, {'index_dec': 1, 'index_bin': '0001', 'val': 15, 'counts': 134}, {'index_dec': 4, 'index_bin': '0100', 'val': 14, 'counts': 151}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 154}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 145}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 138}], # Indices 74496 to 74512
4657:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 168}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 143}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 152}, {'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 132}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 125}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 144}], # Indices 74512 to 74528
4658:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 111}, {'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 92}, {'index_dec': 2, 'index_bin': '0010', 'val': 13, 'counts': 116}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 94}, {'index_dec': 5, 'index_bin': '0101', 'val': 13, 'counts': 106}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 109}], # Indices 74528 to 74544
4659:[], # Indices 74544 to 74560
4660:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 150}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 132}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 138}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 149}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 144}, {'index_dec': 15, 'index_bin': '1111', 'val': 14, 'counts': 157}], # Indices 74560 to 74576
4661:[{'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 94}, {'index_dec': 3, 'index_bin': '0011', 'val': 0, 'counts': 92}, {'index_dec': 4, 'index_bin': '0100', 'val': 0, 'counts': 94}, {'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 123}, {'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 109}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 96}, {'index_dec': 14, 'index_bin': '1110', 'val': 0, 'counts': 94}], # Indices 74576 to 74592
4662:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 215}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 173}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 179}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 213}, {'index_dec': 14, 'index_bin': '1110', 'val': 14, 'counts': 209}], # Indices 74592 to 74608
4663:[{'index_dec': 1, 'index_bin': '0001', 'val': 13, 'counts': 112}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 108}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 106}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 95}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 94}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 99}, {'index_dec': 15, 'index_bin': '1111', 'val': 13, 'counts': 91}], # Indices 74608 to 74624
4664:[{'index_dec': 0, 'index_bin': '0000', 'val': 0, 'counts': 281}, {'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 243}, {'index_dec': 13, 'index_bin': '1101', 'val': 0, 'counts': 256}, {'index_dec': 15, 'index_bin': '1111', 'val': 6, 'counts': 244}], # Indices 74624 to 74640
4665:[{'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 95}, {'index_dec': 2, 'index_bin': '0010', 'val': 0, 'counts': 96}, {'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 93}, {'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 99}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 102}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 118}], # Indices 74640 to 74656
4666:[{'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 98}, {'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 99}, {'index_dec': 7, 'index_bin': '0111', 'val': 6, 'counts': 98}, {'index_dec': 8, 'index_bin': '1000', 'val': 5, 'counts': 98}, {'index_dec': 9, 'index_bin': '1001', 'val': 6, 'counts': 109}, {'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 94}, {'index_dec': 14, 'index_bin': '1110', 'val': 5, 'counts': 100}], # Indices 74656 to 74672
4667:[{'index_dec': 0, 'index_bin': '0000', 'val': 0, 'counts': 92}, {'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 99}, {'index_dec': 7, 'index_bin': '0111', 'val': 0, 'counts': 115}, {'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 105}, {'index_dec': 11, 'index_bin': '1011', 'val': 6, 'counts': 96}, {'index_dec': 14, 'index_bin': '1110', 'val': 6, 'counts': 108}], # Indices 74672 to 74688
4668:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 99}, {'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 108}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 105}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 91}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 108}], # Indices 74688 to 74704
4669:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 98}, {'index_dec': 4, 'index_bin': '0100', 'val': 6, 'counts': 111}, {'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 103}, {'index_dec': 7, 'index_bin': '0111', 'val': 0, 'counts': 108}, {'index_dec': 9, 'index_bin': '1001', 'val': 6, 'counts': 92}], # Indices 74704 to 74720
4670:[{'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 136}, {'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 147}, {'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 141}, {'index_dec': 6, 'index_bin': '0110', 'val': 6, 'counts': 142}, {'index_dec': 14, 'index_bin': '1110', 'val': 5, 'counts': 149}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 151}], # Indices 74720 to 74736
4671:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 150}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 133}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 158}, {'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 135}, {'index_dec': 12, 'index_bin': '1100', 'val': 13, 'counts': 138}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 135}], # Indices 74736 to 74752
4672:[], # Indices 74752 to 74768
4673:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 149}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 141}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 130}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 156}, {'index_dec': 14, 'index_bin': '1110', 'val': 14, 'counts': 150}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 158}], # Indices 74768 to 74784
4674:[{'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 174}, {'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 188}, {'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 202}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 210}, {'index_dec': 13, 'index_bin': '1101', 'val': 6, 'counts': 203}], # Indices 74784 to 74800
4675:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 308}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 342}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 319}], # Indices 74800 to 74816
4676:[], # Indices 74816 to 74832
4677:[{'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 195}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 191}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 193}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 214}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 186}], # Indices 74832 to 74848
4678:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 92}, {'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 104}, {'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 102}, {'index_dec': 4, 'index_bin': '0100', 'val': 0, 'counts': 109}, {'index_dec': 15, 'index_bin': '1111', 'val': 6, 'counts': 111}], # Indices 74848 to 74864
4679:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 238}, {'index_dec': 1, 'index_bin': '0001', 'val': 0, 'counts': 254}, {'index_dec': 12, 'index_bin': '1100', 'val': 0, 'counts': 260}, {'index_dec': 14, 'index_bin': '1110', 'val': 5, 'counts': 272}], # Indices 74864 to 74880
4680:[{'index_dec': 0, 'index_bin': '0000', 'val': 5, 'counts': 105}, {'index_dec': 1, 'index_bin': '0001', 'val': 5, 'counts': 101}, {'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 109}, {'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 108}, {'index_dec': 6, 'index_bin': '0110', 'val': 0, 'counts': 99}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 104}], # Indices 74880 to 74896
4681:[{'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 107}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 98}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 113}, {'index_dec': 9, 'index_bin': '1001', 'val': 14, 'counts': 105}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 101}, {'index_dec': 14, 'index_bin': '1110', 'val': 14, 'counts': 100}], # Indices 74896 to 74912
4682:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 151}, {'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 138}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 135}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 148}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 143}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 157}], # Indices 74912 to 74928
4683:[{'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 109}, {'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 101}, {'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 104}, {'index_dec': 8, 'index_bin': '1000', 'val': 5, 'counts': 93}, {'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 104}, {'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 110}], # Indices 74928 to 74944
4684:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 106}, {'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 101}, {'index_dec': 6, 'index_bin': '0110', 'val': 0, 'counts': 95}, {'index_dec': 8, 'index_bin': '1000', 'val': 5, 'counts': 100}, {'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 122}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 114}], # Indices 74944 to 74960
4685:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 214}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 191}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 186}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 196}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 193}], # Indices 74960 to 74976
4686:[], # Indices 74976 to 74992
4687:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 141}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 141}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 142}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 148}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 155}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 143}], # Indices 74992 to 75008
4688:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 193}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 209}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 193}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 194}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 181}], # Indices 75008 to 75024
4689:[{'index_dec': 0, 'index_bin': '0000', 'val': 14, 'counts': 198}, {'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 190}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 196}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 212}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 180}], # Indices 75024 to 75040
4690:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 145}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 140}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 134}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 150}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 154}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 142}], # Indices 75040 to 75056
4691:[{'index_dec': 4, 'index_bin': '0100', 'val': 6, 'counts': 102}, {'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 91}, {'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 103}, {'index_dec': 8, 'index_bin': '1000', 'val': 5, 'counts': 96}, {'index_dec': 10, 'index_bin': '1010', 'val': 5, 'counts': 97}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 115}], # Indices 75056 to 75072
4692:[{'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 91}, {'index_dec': 4, 'index_bin': '0100', 'val': 13, 'counts': 96}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 113}, {'index_dec': 13, 'index_bin': '1101', 'val': 14, 'counts': 115}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 100}, {'index_dec': 15, 'index_bin': '1111', 'val': 14, 'counts': 100}], # Indices 75072 to 75088
4693:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 258}, {'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 263}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 252}, {'index_dec': 12, 'index_bin': '1100', 'val': 15, 'counts': 251}], # Indices 75088 to 75104
4694:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 105}, {'index_dec': 2, 'index_bin': '0010', 'val': 0, 'counts': 116}, {'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 105}, {'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 101}, {'index_dec': 14, 'index_bin': '1110', 'val': 0, 'counts': 92}, {'index_dec': 15, 'index_bin': '1111', 'val': 6, 'counts': 106}], # Indices 75104 to 75120
4695:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 185}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 206}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 218}, {'index_dec': 14, 'index_bin': '1110', 'val': 14, 'counts': 203}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 177}], # Indices 75120 to 75136
4696:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 109}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 109}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 91}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 105}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 101}], # Indices 75136 to 75152
4697:[{'index_dec': 2, 'index_bin': '0010', 'val': 4, 'counts': 254}, {'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 263}, {'index_dec': 10, 'index_bin': '1010', 'val': 5, 'counts': 244}, {'index_dec': 14, 'index_bin': '1110', 'val': 6, 'counts': 263}], # Indices 75152 to 75168
4698:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 100}, {'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 94}, {'index_dec': 9, 'index_bin': '1001', 'val': 14, 'counts': 100}, {'index_dec': 10, 'index_bin': '1010', 'val': 13, 'counts': 108}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 107}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 109}], # Indices 75168 to 75184
4699:[{'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 272}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 262}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 230}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 260}], # Indices 75184 to 75200
4700:[], # Indices 75200 to 75216
4701:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 143}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 148}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 131}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 146}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 150}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 156}], # Indices 75216 to 75232
4702:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 244}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 263}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 266}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 251}], # Indices 75232 to 75248
4703:[{'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 207}, {'index_dec': 2, 'index_bin': '0010', 'val': 6, 'counts': 195}, {'index_dec': 9, 'index_bin': '1001', 'val': 0, 'counts': 187}, {'index_dec': 11, 'index_bin': '1011', 'val': 0, 'counts': 188}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 199}], # Indices 75248 to 75264
4704:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 97}, {'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 104}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 95}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 116}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 108}], # Indices 75264 to 75280
4705:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 274}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 257}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 258}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 235}], # Indices 75280 to 75296
4706:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 124}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 149}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 148}, {'index_dec': 5, 'index_bin': '0101', 'val': 15, 'counts': 154}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 144}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 147}], # Indices 75296 to 75312
4707:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 93}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 105}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 116}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 110}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 96}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 98}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 106}], # Indices 75312 to 75328
4708:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 99}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 115}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 110}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 100}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 104}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 99}], # Indices 75328 to 75344
4709:[{'index_dec': 1, 'index_bin': '0001', 'val': 14, 'counts': 142}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 155}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 148}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 152}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 133}, {'index_dec': 15, 'index_bin': '1111', 'val': 15, 'counts': 138}], # Indices 75344 to 75360
4710:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 259}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 265}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 243}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 257}], # Indices 75360 to 75376
4711:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 147}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 134}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 136}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 141}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 155}, {'index_dec': 15, 'index_bin': '1111', 'val': 13, 'counts': 148}], # Indices 75376 to 75392
4712:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 106}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 96}, {'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 102}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 97}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 94}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 121}], # Indices 75392 to 75408
4713:[], # Indices 75408 to 75424
4714:[{'index_dec': 0, 'index_bin': '0000', 'val': 14, 'counts': 190}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 202}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 204}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 189}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 196}], # Indices 75424 to 75440
4715:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 149}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 152}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 149}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 132}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 153}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 130}], # Indices 75440 to 75456
4716:[{'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 99}, {'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 104}, {'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 102}, {'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 93}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 112}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 103}], # Indices 75456 to 75472
4717:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 108}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 97}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 107}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 101}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 108}], # Indices 75472 to 75488
4718:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 136}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 148}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 144}, {'index_dec': 10, 'index_bin': '1010', 'val': 13, 'counts': 139}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 158}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 145}], # Indices 75488 to 75504
4719:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 193}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 206}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 170}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 203}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 207}], # Indices 75504 to 75520
4720:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 249}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 261}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 262}, {'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 252}], # Indices 75520 to 75536
4721:[], # Indices 75536 to 75552
4722:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 212}, {'index_dec': 3, 'index_bin': '0011', 'val': 4, 'counts': 182}, {'index_dec': 8, 'index_bin': '1000', 'val': 0, 'counts': 201}, {'index_dec': 10, 'index_bin': '1010', 'val': 6, 'counts': 191}, {'index_dec': 15, 'index_bin': '1111', 'val': 6, 'counts': 191}], # Indices 75552 to 75568
4723:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 141}, {'index_dec': 3, 'index_bin': '0011', 'val': 14, 'counts': 146}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 152}, {'index_dec': 6, 'index_bin': '0110', 'val': 14, 'counts': 151}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 150}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 139}], # Indices 75568 to 75584
4724:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 153}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 135}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 153}, {'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 151}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 144}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 134}], # Indices 75584 to 75600
4725:[{'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 96}, {'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 97}, {'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 95}, {'index_dec': 12, 'index_bin': '1100', 'val': 6, 'counts': 94}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 99}], # Indices 75600 to 75616
4726:[], # Indices 75616 to 75632
4727:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 91}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 104}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 107}, {'index_dec': 8, 'index_bin': '1000', 'val': 12, 'counts': 96}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 93}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 100}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 101}], # Indices 75632 to 75648
4728:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 200}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 185}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 197}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 195}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 204}], # Indices 75648 to 75664
4729:[{'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 142}, {'index_dec': 8, 'index_bin': '1000', 'val': 5, 'counts': 130}, {'index_dec': 11, 'index_bin': '1011', 'val': 6, 'counts': 118}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 151}, {'index_dec': 14, 'index_bin': '1110', 'val': 5, 'counts': 150}, {'index_dec': 15, 'index_bin': '1111', 'val': 6, 'counts': 161}], # Indices 75664 to 75680
4730:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 142}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 139}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 144}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 161}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 152}, {'index_dec': 15, 'index_bin': '1111', 'val': 14, 'counts': 139}], # Indices 75680 to 75696
4731:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 426}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 378}], # Indices 75696 to 75712
4732:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 327}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 318}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 335}], # Indices 75712 to 75728
4733:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 105}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 110}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 97}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 123}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 93}], # Indices 75728 to 75744
4734:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 137}, {'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 150}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 143}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 148}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 137}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 142}], # Indices 75744 to 75760
4735:[], # Indices 75760 to 75776
4736:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 220}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 264}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 253}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 287}], # Indices 75776 to 75792
4737:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 135}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 155}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 139}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 142}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 157}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 153}], # Indices 75792 to 75808
4738:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 221}, {'index_dec': 2, 'index_bin': '0010', 'val': 14, 'counts': 166}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 194}, {'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 216}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 189}], # Indices 75808 to 75824
4739:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 189}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 205}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 198}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 197}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 195}], # Indices 75824 to 75840
4740:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 384}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 413}], # Indices 75840 to 75856
4741:[{'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 202}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 203}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 196}, {'index_dec': 11, 'index_bin': '1011', 'val': 14, 'counts': 188}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 185}], # Indices 75856 to 75872
4742:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 211}, {'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 194}, {'index_dec': 7, 'index_bin': '0111', 'val': 14, 'counts': 180}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 211}, {'index_dec': 15, 'index_bin': '1111', 'val': 13, 'counts': 185}], # Indices 75872 to 75888
4743:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 207}, {'index_dec': 4, 'index_bin': '0100', 'val': 14, 'counts': 175}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 197}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 203}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 190}], # Indices 75888 to 75904
4744:[{'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 95}, {'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 105}, {'index_dec': 8, 'index_bin': '1000', 'val': 4, 'counts': 111}, {'index_dec': 9, 'index_bin': '1001', 'val': 6, 'counts': 103}, {'index_dec': 11, 'index_bin': '1011', 'val': 6, 'counts': 104}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 95}], # Indices 75904 to 75920
4745:[], # Indices 75920 to 75936
4746:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 252}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 245}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 281}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 246}], # Indices 75936 to 75952
4747:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 198}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 193}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 200}, {'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 185}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 195}], # Indices 75952 to 75968
4748:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 100}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 96}, {'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 103}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 118}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 107}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 92}], # Indices 75968 to 75984
4749:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 220}, {'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 178}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 192}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 218}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 178}], # Indices 75984 to 76000
4750:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 117}, {'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 149}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 154}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 151}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 161}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 136}], # Indices 76000 to 76016
4751:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 317}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 329}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 328}], # Indices 76016 to 76032
4752:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 269}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 253}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 254}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 248}], # Indices 76032 to 76048
4753:[{'index_dec': 5, 'index_bin': '0101', 'val': 12, 'counts': 208}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 186}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 195}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 207}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 188}], # Indices 76048 to 76064
4754:[{'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 387}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 398}], # Indices 76064 to 76080
4755:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 196}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 191}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 181}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 206}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 188}], # Indices 76080 to 76096
4756:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 204}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 210}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 187}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 204}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 183}], # Indices 76096 to 76112
4757:[{'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 267}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 260}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 248}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 249}], # Indices 76112 to 76128
4758:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 169}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 199}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 185}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 227}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 197}], # Indices 76128 to 76144
4759:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 408}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 410}], # Indices 76144 to 76160
4760:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 251}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 267}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 277}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 229}], # Indices 76160 to 76176
4761:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 249}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 282}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 243}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 250}], # Indices 76176 to 76192
4762:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 202}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 190}, {'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 192}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 188}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 205}], # Indices 76192 to 76208
4763:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 339}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 321}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 310}], # Indices 76208 to 76224
4764:[{'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 100}, {'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 99}, {'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 117}, {'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 100}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 104}, {'index_dec': 14, 'index_bin': '1110', 'val': 6, 'counts': 95}], # Indices 76224 to 76240
4765:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 197}, {'index_dec': 9, 'index_bin': '1001', 'val': 14, 'counts': 188}, {'index_dec': 10, 'index_bin': '1010', 'val': 10, 'counts': 215}, {'index_dec': 11, 'index_bin': '1011', 'val': 13, 'counts': 185}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 196}], # Indices 76240 to 76256
4766:[{'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 182}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 192}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 203}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 185}, {'index_dec': 15, 'index_bin': '1111', 'val': 13, 'counts': 216}], # Indices 76256 to 76272
4767:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 92}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 103}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 92}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 91}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 104}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 111}], # Indices 76272 to 76288
4768:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 179}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 188}, {'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 183}, {'index_dec': 14, 'index_bin': '1110', 'val': 11, 'counts': 212}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 217}], # Indices 76288 to 76304
4769:[{'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 320}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 331}, {'index_dec': 12, 'index_bin': '1100', 'val': 12, 'counts': 320}], # Indices 76304 to 76320
4770:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 263}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 257}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 228}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 276}], # Indices 76320 to 76336
4771:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 149}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 126}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 125}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 152}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 148}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 148}], # Indices 76336 to 76352
4772:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 250}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 247}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 273}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 254}], # Indices 76352 to 76368
4773:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 188}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 192}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 194}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 188}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 195}], # Indices 76368 to 76384
4774:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 479}], # Indices 76384 to 76400
4775:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 401}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 391}], # Indices 76400 to 76416
4776:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 203}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 214}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 183}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 202}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 194}], # Indices 76416 to 76432
4777:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 272}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 245}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 272}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 235}], # Indices 76432 to 76448
4778:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 177}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 197}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 187}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 223}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 195}], # Indices 76448 to 76464
4779:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 407}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 396}], # Indices 76464 to 76480
4780:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 140}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 152}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 129}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 140}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 147}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 151}], # Indices 76480 to 76496
4781:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 462}], # Indices 76496 to 76512
4782:[], # Indices 76512 to 76528
4783:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 432}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 391}], # Indices 76528 to 76544
4784:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 313}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 340}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 321}], # Indices 76544 to 76560
4785:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 201}, {'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 220}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 184}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 177}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 199}], # Indices 76560 to 76576
4786:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 268}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 280}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 238}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 238}], # Indices 76576 to 76592
4787:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 100}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 105}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 91}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 99}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 103}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 101}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 100}], # Indices 76592 to 76608
4788:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 400}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 390}], # Indices 76608 to 76624
4789:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 379}, {'index_dec': 12, 'index_bin': '1100', 'val': 12, 'counts': 417}], # Indices 76624 to 76640
4790:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 165}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 130}, {'index_dec': 6, 'index_bin': '0110', 'val': 11, 'counts': 144}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 136}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 145}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 139}], # Indices 76640 to 76656
4791:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 330}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 305}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 331}], # Indices 76656 to 76672
4792:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 488}], # Indices 76672 to 76688
4793:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 404}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 390}], # Indices 76688 to 76704
4794:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 349}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 309}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 328}], # Indices 76704 to 76720
4795:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 502}], # Indices 76720 to 76736
4796:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 187}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 194}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 195}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 223}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 187}], # Indices 76736 to 76752
4797:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 472}], # Indices 76752 to 76768
4798:[], # Indices 76768 to 76784
4799:[], # Indices 76784 to 76800
4800:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 409}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 392}], # Indices 76800 to 76816
4801:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 495}], # Indices 76816 to 76832
4802:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 267}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 250}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 232}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 275}], # Indices 76832 to 76848
4803:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 279}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 257}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 228}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 260}], # Indices 76848 to 76864
4804:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 323}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 328}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 325}], # Indices 76864 to 76880
4805:[{'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 406}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 380}], # Indices 76880 to 76896
4806:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 286}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 333}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 342}], # Indices 76896 to 76912
4807:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 249}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 263}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 245}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 267}], # Indices 76912 to 76928
4808:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 320}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 341}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 317}], # Indices 76928 to 76944
4809:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 127}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 148}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 147}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 150}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 147}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 150}], # Indices 76944 to 76960
4810:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 415}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 423}], # Indices 76960 to 76976
4811:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 255}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 231}, {'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 268}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 270}], # Indices 76976 to 76992
4812:[], # Indices 76992 to 77008
4813:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 484}], # Indices 77008 to 77024
4814:[], # Indices 77024 to 77040
4815:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 257}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 269}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 237}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 261}], # Indices 77040 to 77056
4816:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 485}], # Indices 77056 to 77072
4817:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 419}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 373}], # Indices 77072 to 77088
4818:[], # Indices 77088 to 77104
4819:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 340}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 294}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 332}], # Indices 77104 to 77120
4820:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 374}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 427}], # Indices 77120 to 77136
4821:[], # Indices 77136 to 77152
4822:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 484}], # Indices 77152 to 77168
4823:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 314}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 315}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 349}], # Indices 77168 to 77184
4824:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 240}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 247}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 250}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 287}], # Indices 77184 to 77200
4825:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 515}], # Indices 77200 to 77216
4826:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 479}], # Indices 77216 to 77232
4827:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 325}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 324}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 328}], # Indices 77232 to 77248
4828:[], # Indices 77248 to 77264
4829:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 443}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 368}], # Indices 77264 to 77280
4830:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 344}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 322}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 313}], # Indices 77280 to 77296
4831:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 324}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 343}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 310}], # Indices 77296 to 77312
4832:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 485}], # Indices 77312 to 77328
4833:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 474}], # Indices 77328 to 77344
4834:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 383}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 433}], # Indices 77344 to 77360
4835:[], # Indices 77360 to 77376
4836:[], # Indices 77376 to 77392
4837:[], # Indices 77392 to 77408
4838:[], # Indices 77408 to 77424
4839:[], # Indices 77424 to 77440
4840:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 484}], # Indices 77440 to 77456
4841:[], # Indices 77456 to 77472
4842:[], # Indices 77472 to 77488
4843:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 388}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 424}], # Indices 77488 to 77504
4844:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 424}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 358}], # Indices 77504 to 77520
4845:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 491}], # Indices 77520 to 77536
4846:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 496}], # Indices 77536 to 77552
4847:[{'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 414}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 385}], # Indices 77552 to 77568
4848:[], # Indices 77568 to 77584
4849:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 395}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 414}], # Indices 77584 to 77600
4850:[], # Indices 77600 to 77616
4851:[], # Indices 77616 to 77632
4852:[], # Indices 77632 to 77648
4853:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 492}], # Indices 77648 to 77664
4854:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 486}], # Indices 77664 to 77680
4855:[], # Indices 77680 to 77696
4856:[], # Indices 77696 to 77712
4857:[], # Indices 77712 to 77728
4858:[], # Indices 77728 to 77744
4859:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 490}], # Indices 77744 to 77760
4860:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 453}], # Indices 77760 to 77776
4861:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 459}], # Indices 77776 to 77792
4862:[], # Indices 77792 to 77808
4863:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 476}], # Indices 77808 to 77824
4864:[], # Indices 77824 to 77840
4865:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 475}], # Indices 77840 to 77856
4866:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 495}], # Indices 77856 to 77872
4867:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 497}], # Indices 77872 to 77888
4868:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 500}], # Indices 77888 to 77904
4869:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 488}], # Indices 77904 to 77920
4870:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 501}], # Indices 77920 to 77936
4871:[], # Indices 77936 to 77952
4872:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 496}], # Indices 77952 to 77968
4873:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 490}], # Indices 77968 to 77984
4874:[], # Indices 77984 to 78000
4875:[], # Indices 78000 to 78016
4876:[], # Indices 78016 to 78032
4877:[], # Indices 78032 to 78048
4878:[], # Indices 78048 to 78064
4879:[], # Indices 78064 to 78080
4880:[], # Indices 78080 to 78096
4881:[], # Indices 78096 to 78112
4882:[], # Indices 78112 to 78128
4883:[], # Indices 78128 to 78144
4884:[], # Indices 78144 to 78160
4885:[], # Indices 78160 to 78176
4886:[], # Indices 78176 to 78192
4887:[], # Indices 78192 to 78208
4888:[], # Indices 78208 to 78224
4889:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 324}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 311}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 344}], # Indices 78224 to 78240
4890:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 496}], # Indices 78240 to 78256
4891:[], # Indices 78256 to 78272
4892:[], # Indices 78272 to 78288
4893:[], # Indices 78288 to 78304
4894:[], # Indices 78304 to 78320
4895:[], # Indices 78320 to 78336
4896:[], # Indices 78336 to 78352
4897:[], # Indices 78352 to 78368
4898:[{'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 91}], # Indices 78368 to 78384
4899:[], # Indices 78384 to 78400
4900:[], # Indices 78400 to 78416
4901:[], # Indices 78416 to 78432
4902:[], # Indices 78432 to 78448
4903:[], # Indices 78448 to 78464
4904:[], # Indices 78464 to 78480
4905:[], # Indices 78480 to 78496
4906:[], # Indices 78496 to 78512
4907:[], # Indices 78512 to 78528
4908:[], # Indices 78528 to 78544
4909:[], # Indices 78544 to 78560
4910:[], # Indices 78560 to 78576
4911:[], # Indices 78576 to 78592
4912:[], # Indices 78592 to 78608
4913:[], # Indices 78608 to 78624
4914:[], # Indices 78624 to 78640
4915:[], # Indices 78640 to 78656
4916:[], # Indices 78656 to 78672
4917:[], # Indices 78672 to 78688
4918:[], # Indices 78688 to 78704
4919:[], # Indices 78704 to 78720
4920:[], # Indices 78720 to 78736
4921:[], # Indices 78736 to 78752
4922:[], # Indices 78752 to 78768
4923:[], # Indices 78768 to 78784
4924:[], # Indices 78784 to 78800
4925:[], # Indices 78800 to 78816
4926:[], # Indices 78816 to 78832
4927:[], # Indices 78832 to 78848
4928:[], # Indices 78848 to 78864
4929:[], # Indices 78864 to 78880
4930:[], # Indices 78880 to 78896
4931:[], # Indices 78896 to 78912
4932:[], # Indices 78912 to 78928
4933:[], # Indices 78928 to 78944
4934:[], # Indices 78944 to 78960
4935:[], # Indices 78960 to 78976
4936:[], # Indices 78976 to 78992
4937:[], # Indices 78992 to 79008
4938:[], # Indices 79008 to 79024
4939:[], # Indices 79024 to 79040
4940:[], # Indices 79040 to 79056
4941:[], # Indices 79056 to 79072
4942:[], # Indices 79072 to 79088
4943:[], # Indices 79088 to 79104
4944:[], # Indices 79104 to 79120
4945:[{'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 97}], # Indices 79120 to 79136
4946:[], # Indices 79136 to 79152
4947:[], # Indices 79152 to 79168
4948:[], # Indices 79168 to 79184
4949:[], # Indices 79184 to 79200
4950:[], # Indices 79200 to 79216
4951:[], # Indices 79216 to 79232
4952:[], # Indices 79232 to 79248
4953:[], # Indices 79248 to 79264
4954:[], # Indices 79264 to 79280
4955:[], # Indices 79280 to 79296
4956:[], # Indices 79296 to 79312
4957:[], # Indices 79312 to 79328
4958:[], # Indices 79328 to 79344
4959:[], # Indices 79344 to 79360
4960:[], # Indices 79360 to 79376
4961:[], # Indices 79376 to 79392
4962:[], # Indices 79392 to 79408
4963:[], # Indices 79408 to 79424
4964:[], # Indices 79424 to 79440
4965:[], # Indices 79440 to 79456
4966:[], # Indices 79456 to 79472
4967:[], # Indices 79472 to 79488
4968:[], # Indices 79488 to 79504
4969:[], # Indices 79504 to 79520
4970:[], # Indices 79520 to 79536
4971:[], # Indices 79536 to 79552
4972:[], # Indices 79552 to 79568
4973:[], # Indices 79568 to 79584
4974:[], # Indices 79584 to 79600
4975:[], # Indices 79600 to 79616
4976:[], # Indices 79616 to 79632
4977:[], # Indices 79632 to 79648
4978:[], # Indices 79648 to 79664
4979:[], # Indices 79664 to 79680
4980:[], # Indices 79680 to 79696
4981:[], # Indices 79696 to 79712
4982:[], # Indices 79712 to 79728
4983:[], # Indices 79728 to 79744
4984:[], # Indices 79744 to 79760
4985:[], # Indices 79760 to 79776
4986:[], # Indices 79776 to 79792
4987:[], # Indices 79792 to 79808
4988:[], # Indices 79808 to 79824
4989:[], # Indices 79824 to 79840
4990:[], # Indices 79840 to 79856
4991:[], # Indices 79856 to 79872
4992:[], # Indices 79872 to 79888
4993:[], # Indices 79888 to 79904
4994:[], # Indices 79904 to 79920
4995:[], # Indices 79920 to 79936
4996:[], # Indices 79936 to 79952
4997:[], # Indices 79952 to 79968
4998:[], # Indices 79968 to 79984
4999:[], # Indices 79984 to 80000
5000:[{'index_dec': 1, 'index_bin': '0001', 'val': 4, 'counts': 91}], # Indices 80000 to 80016
5001:[], # Indices 80016 to 80032
5002:[], # Indices 80032 to 80048
5003:[], # Indices 80048 to 80064
5004:[], # Indices 80064 to 80080
5005:[], # Indices 80080 to 80096
5006:[], # Indices 80096 to 80112
5007:[], # Indices 80112 to 80128
5008:[], # Indices 80128 to 80144
5009:[], # Indices 80144 to 80160
5010:[], # Indices 80160 to 80176
5011:[], # Indices 80176 to 80192
5012:[], # Indices 80192 to 80208
5013:[], # Indices 80208 to 80224
5014:[], # Indices 80224 to 80240
5015:[], # Indices 80240 to 80256
5016:[], # Indices 80256 to 80272
5017:[], # Indices 80272 to 80288
5018:[], # Indices 80288 to 80304
5019:[], # Indices 80304 to 80320
5020:[], # Indices 80320 to 80336
5021:[], # Indices 80336 to 80352
5022:[], # Indices 80352 to 80368
5023:[], # Indices 80368 to 80384
5024:[], # Indices 80384 to 80400
5025:[], # Indices 80400 to 80416
5026:[], # Indices 80416 to 80432
5027:[], # Indices 80432 to 80448
5028:[], # Indices 80448 to 80464
5029:[], # Indices 80464 to 80480
5030:[], # Indices 80480 to 80496
5031:[], # Indices 80496 to 80512
5032:[], # Indices 80512 to 80528
5033:[], # Indices 80528 to 80544
5034:[], # Indices 80544 to 80560
5035:[], # Indices 80560 to 80576
5036:[], # Indices 80576 to 80592
5037:[], # Indices 80592 to 80608
5038:[], # Indices 80608 to 80624
5039:[], # Indices 80624 to 80640
5040:[], # Indices 80640 to 80656
5041:[], # Indices 80656 to 80672
5042:[], # Indices 80672 to 80688
5043:[], # Indices 80688 to 80704
5044:[], # Indices 80704 to 80720
5045:[], # Indices 80720 to 80736
5046:[], # Indices 80736 to 80752
5047:[], # Indices 80752 to 80768
5048:[], # Indices 80768 to 80784
5049:[], # Indices 80784 to 80800
5050:[], # Indices 80800 to 80816
5051:[], # Indices 80816 to 80832
5052:[], # Indices 80832 to 80848
5053:[], # Indices 80848 to 80864
5054:[], # Indices 80864 to 80880
5055:[], # Indices 80880 to 80896
5056:[], # Indices 80896 to 80912
5057:[], # Indices 80912 to 80928
5058:[], # Indices 80928 to 80944
5059:[], # Indices 80944 to 80960
5060:[], # Indices 80960 to 80976
5061:[], # Indices 80976 to 80992
5062:[], # Indices 80992 to 81008
5063:[], # Indices 81008 to 81024
5064:[], # Indices 81024 to 81040
5065:[], # Indices 81040 to 81056
5066:[], # Indices 81056 to 81072
5067:[], # Indices 81072 to 81088
5068:[], # Indices 81088 to 81104
5069:[], # Indices 81104 to 81120
5070:[], # Indices 81120 to 81136
5071:[], # Indices 81136 to 81152
5072:[], # Indices 81152 to 81168
5073:[], # Indices 81168 to 81184
5074:[], # Indices 81184 to 81200
5075:[], # Indices 81200 to 81216
5076:[], # Indices 81216 to 81232
5077:[], # Indices 81232 to 81248
5078:[], # Indices 81248 to 81264
5079:[], # Indices 81264 to 81280
5080:[], # Indices 81280 to 81296
5081:[], # Indices 81296 to 81312
5082:[], # Indices 81312 to 81328
5083:[], # Indices 81328 to 81344
5084:[], # Indices 81344 to 81360
5085:[], # Indices 81360 to 81376
5086:[], # Indices 81376 to 81392
5087:[], # Indices 81392 to 81408
5088:[], # Indices 81408 to 81424
5089:[], # Indices 81424 to 81440
5090:[], # Indices 81440 to 81456
5091:[], # Indices 81456 to 81472
5092:[], # Indices 81472 to 81488
5093:[], # Indices 81488 to 81504
5094:[], # Indices 81504 to 81520
5095:[], # Indices 81520 to 81536
5096:[], # Indices 81536 to 81552
5097:[], # Indices 81552 to 81568
5098:[], # Indices 81568 to 81584
5099:[], # Indices 81584 to 81600
5100:[], # Indices 81600 to 81616
5101:[], # Indices 81616 to 81632
5102:[], # Indices 81632 to 81648
5103:[], # Indices 81648 to 81664
5104:[], # Indices 81664 to 81680
5105:[], # Indices 81680 to 81696
5106:[], # Indices 81696 to 81712
5107:[], # Indices 81712 to 81728
5108:[], # Indices 81728 to 81744
5109:[], # Indices 81744 to 81760
5110:[], # Indices 81760 to 81776
5111:[], # Indices 81776 to 81792
5112:[], # Indices 81792 to 81808
5113:[], # Indices 81808 to 81824
5114:[], # Indices 81824 to 81840
5115:[], # Indices 81840 to 81856
5116:[], # Indices 81856 to 81872
5117:[], # Indices 81872 to 81888
5118:[], # Indices 81888 to 81904
5119:[], # Indices 81904 to 81920
5120:[], # Indices 81920 to 81936
5121:[], # Indices 81936 to 81952
5122:[], # Indices 81952 to 81968
5123:[], # Indices 81968 to 81984
5124:[], # Indices 81984 to 82000
5125:[], # Indices 82000 to 82016
5126:[], # Indices 82016 to 82032
5127:[], # Indices 82032 to 82048
5128:[], # Indices 82048 to 82064
5129:[], # Indices 82064 to 82080
5130:[], # Indices 82080 to 82096
5131:[], # Indices 82096 to 82112
5132:[], # Indices 82112 to 82128
5133:[], # Indices 82128 to 82144
5134:[], # Indices 82144 to 82160
5135:[], # Indices 82160 to 82176
5136:[], # Indices 82176 to 82192
5137:[], # Indices 82192 to 82208
5138:[], # Indices 82208 to 82224
5139:[], # Indices 82224 to 82240
5140:[], # Indices 82240 to 82256
5141:[], # Indices 82256 to 82272
5142:[], # Indices 82272 to 82288
5143:[], # Indices 82288 to 82304
5144:[], # Indices 82304 to 82320
5145:[], # Indices 82320 to 82336
5146:[], # Indices 82336 to 82352
5147:[], # Indices 82352 to 82368
5148:[], # Indices 82368 to 82384
5149:[], # Indices 82384 to 82400
5150:[], # Indices 82400 to 82416
5151:[], # Indices 82416 to 82432
5152:[], # Indices 82432 to 82448
5153:[], # Indices 82448 to 82464
5154:[], # Indices 82464 to 82480
5155:[], # Indices 82480 to 82496
5156:[], # Indices 82496 to 82512
5157:[], # Indices 82512 to 82528
5158:[], # Indices 82528 to 82544
5159:[], # Indices 82544 to 82560
5160:[], # Indices 82560 to 82576
5161:[], # Indices 82576 to 82592
5162:[], # Indices 82592 to 82608
5163:[], # Indices 82608 to 82624
5164:[], # Indices 82624 to 82640
5165:[], # Indices 82640 to 82656
5166:[], # Indices 82656 to 82672
5167:[], # Indices 82672 to 82688
5168:[], # Indices 82688 to 82704
5169:[], # Indices 82704 to 82720
5170:[], # Indices 82720 to 82736
5171:[], # Indices 82736 to 82752
5172:[], # Indices 82752 to 82768
5173:[], # Indices 82768 to 82784
5174:[], # Indices 82784 to 82800
5175:[], # Indices 82800 to 82816
5176:[], # Indices 82816 to 82832
5177:[], # Indices 82832 to 82848
5178:[], # Indices 82848 to 82864
5179:[], # Indices 82864 to 82880
5180:[], # Indices 82880 to 82896
5181:[], # Indices 82896 to 82912
5182:[], # Indices 82912 to 82928
5183:[], # Indices 82928 to 82944
5184:[], # Indices 82944 to 82960
5185:[], # Indices 82960 to 82976
5186:[{'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 140}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 148}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 146}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 141}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 135}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 146}], # Indices 82976 to 82992
5187:[{'index_dec': 1, 'index_bin': '0001', 'val': 6, 'counts': 281}, {'index_dec': 3, 'index_bin': '0011', 'val': 6, 'counts': 249}, {'index_dec': 4, 'index_bin': '0100', 'val': 6, 'counts': 248}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 246}], # Indices 82992 to 83008
5188:[], # Indices 83008 to 83024
5189:[], # Indices 83024 to 83040
5190:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 305}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 334}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 335}], # Indices 83040 to 83056
5191:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 118}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 111}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 98}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 91}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 109}], # Indices 83056 to 83072
5192:[], # Indices 83072 to 83088
5193:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 317}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 348}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 317}], # Indices 83088 to 83104
5194:[], # Indices 83104 to 83120
5195:[], # Indices 83120 to 83136
5196:[], # Indices 83136 to 83152
5197:[], # Indices 83152 to 83168
5198:[], # Indices 83168 to 83184
5199:[], # Indices 83184 to 83200
5200:[], # Indices 83200 to 83216
5201:[], # Indices 83216 to 83232
5202:[], # Indices 83232 to 83248
5203:[], # Indices 83248 to 83264
5204:[], # Indices 83264 to 83280
5205:[], # Indices 83280 to 83296
5206:[], # Indices 83296 to 83312
5207:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 476}], # Indices 83312 to 83328
5208:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 491}], # Indices 83328 to 83344
5209:[], # Indices 83344 to 83360
5210:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 493}], # Indices 83360 to 83376
5211:[], # Indices 83376 to 83392
5212:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 246}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 289}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 234}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 255}], # Indices 83392 to 83408
5213:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 261}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 255}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 242}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 266}], # Indices 83408 to 83424
5214:[{'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 206}, {'index_dec': 5, 'index_bin': '0101', 'val': 11, 'counts': 189}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 186}, {'index_dec': 12, 'index_bin': '1100', 'val': 16, 'counts': 188}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 206}], # Indices 83424 to 83440
5215:[{'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 265}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 260}, {'index_dec': 14, 'index_bin': '1110', 'val': 5, 'counts': 251}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 248}], # Indices 83440 to 83456
5216:[], # Indices 83456 to 83472
5217:[], # Indices 83472 to 83488
5218:[], # Indices 83488 to 83504
5219:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 477}], # Indices 83504 to 83520
5220:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 308}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 331}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 329}], # Indices 83520 to 83536
5221:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 193}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 204}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 217}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 193}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 170}], # Indices 83536 to 83552
5222:[{'index_dec': 0, 'index_bin': '0000', 'val': 6, 'counts': 142}, {'index_dec': 4, 'index_bin': '0100', 'val': 6, 'counts': 150}, {'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 156}, {'index_dec': 6, 'index_bin': '0110', 'val': 6, 'counts': 130}, {'index_dec': 8, 'index_bin': '1000', 'val': 6, 'counts': 135}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 154}], # Indices 83552 to 83568
5223:[], # Indices 83568 to 83584
5224:[], # Indices 83584 to 83600
5225:[], # Indices 83600 to 83616
5226:[], # Indices 83616 to 83632
5227:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 509}], # Indices 83632 to 83648
5228:[], # Indices 83648 to 83664
5229:[{'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 476}], # Indices 83664 to 83680
5230:[], # Indices 83680 to 83696
5231:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 488}], # Indices 83696 to 83712
5232:[{'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 141}, {'index_dec': 7, 'index_bin': '0111', 'val': 6, 'counts': 147}, {'index_dec': 9, 'index_bin': '1001', 'val': 6, 'counts': 135}, {'index_dec': 10, 'index_bin': '1010', 'val': 6, 'counts': 147}, {'index_dec': 11, 'index_bin': '1011', 'val': 6, 'counts': 149}, {'index_dec': 12, 'index_bin': '1100', 'val': 6, 'counts': 146}], # Indices 83712 to 83728
5233:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 206}, {'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 166}, {'index_dec': 2, 'index_bin': '0010', 'val': 17, 'counts': 192}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 201}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 210}], # Indices 83728 to 83744
5234:[], # Indices 83744 to 83760
5235:[], # Indices 83760 to 83776
5236:[], # Indices 83776 to 83792
5237:[], # Indices 83792 to 83808
5238:[], # Indices 83808 to 83824
5239:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 197}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 198}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 190}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 190}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 209}], # Indices 83824 to 83840
5240:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 99}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 99}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 98}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 105}, {'index_dec': 6, 'index_bin': '0110', 'val': 17, 'counts': 92}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 102}, {'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 101}], # Indices 83840 to 83856
5241:[], # Indices 83856 to 83872
5242:[], # Indices 83872 to 83888
5243:[], # Indices 83888 to 83904
5244:[], # Indices 83904 to 83920
5245:[], # Indices 83920 to 83936
5246:[], # Indices 83936 to 83952
5247:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 488}], # Indices 83952 to 83968
5248:[], # Indices 83968 to 83984
5249:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 489}], # Indices 83984 to 84000
5250:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 471}], # Indices 84000 to 84016
5251:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 498}], # Indices 84016 to 84032
5252:[], # Indices 84032 to 84048
5253:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 481}], # Indices 84048 to 84064
5254:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 501}], # Indices 84064 to 84080
5255:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 330}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 300}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 343}], # Indices 84080 to 84096
5256:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 319}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 331}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 323}], # Indices 84096 to 84112
5257:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 189}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 197}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 201}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 188}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 201}], # Indices 84112 to 84128
5258:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 204}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 212}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 178}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 193}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 177}], # Indices 84128 to 84144
5259:[{'index_dec': 3, 'index_bin': '0011', 'val': 6, 'counts': 166}, {'index_dec': 4, 'index_bin': '0100', 'val': 6, 'counts': 152}, {'index_dec': 9, 'index_bin': '1001', 'val': 6, 'counts': 131}, {'index_dec': 10, 'index_bin': '1010', 'val': 6, 'counts': 138}, {'index_dec': 13, 'index_bin': '1101', 'val': 6, 'counts': 151}, {'index_dec': 14, 'index_bin': '1110', 'val': 6, 'counts': 135}], # Indices 84144 to 84160
5260:[{'index_dec': 10, 'index_bin': '1010', 'val': 5, 'counts': 158}, {'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 145}, {'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 138}, {'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 142}, {'index_dec': 14, 'index_bin': '1110', 'val': 5, 'counts': 150}, {'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 149}], # Indices 84160 to 84176
5261:[], # Indices 84176 to 84192
5262:[], # Indices 84192 to 84208
5263:[], # Indices 84208 to 84224
5264:[], # Indices 84224 to 84240
5265:[], # Indices 84240 to 84256
5266:[], # Indices 84256 to 84272
5267:[], # Indices 84272 to 84288
5268:[], # Indices 84288 to 84304
5269:[], # Indices 84304 to 84320
5270:[], # Indices 84320 to 84336
5271:[], # Indices 84336 to 84352
5272:[], # Indices 84352 to 84368
5273:[], # Indices 84368 to 84384
5274:[], # Indices 84384 to 84400
5275:[], # Indices 84400 to 84416
5276:[], # Indices 84416 to 84432
5277:[], # Indices 84432 to 84448
5278:[], # Indices 84448 to 84464
5279:[], # Indices 84464 to 84480
5280:[], # Indices 84480 to 84496
5281:[], # Indices 84496 to 84512
5282:[], # Indices 84512 to 84528
5283:[], # Indices 84528 to 84544
5284:[], # Indices 84544 to 84560
5285:[], # Indices 84560 to 84576
5286:[], # Indices 84576 to 84592
5287:[], # Indices 84592 to 84608
5288:[], # Indices 84608 to 84624
5289:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 464}], # Indices 84624 to 84640
5290:[], # Indices 84640 to 84656
5291:[], # Indices 84656 to 84672
5292:[], # Indices 84672 to 84688
5293:[], # Indices 84688 to 84704
5294:[], # Indices 84704 to 84720
5295:[], # Indices 84720 to 84736
5296:[], # Indices 84736 to 84752
5297:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 402}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 407}], # Indices 84752 to 84768
5298:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 341}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 303}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 334}], # Indices 84768 to 84784
5299:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 259}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 266}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 266}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 233}], # Indices 84784 to 84800
5300:[], # Indices 84800 to 84816
5301:[], # Indices 84816 to 84832
5302:[], # Indices 84832 to 84848
5303:[], # Indices 84848 to 84864
5304:[], # Indices 84864 to 84880
5305:[], # Indices 84880 to 84896
5306:[{'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 92}], # Indices 84896 to 84912
5307:[], # Indices 84912 to 84928
5308:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 365}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 430}], # Indices 84928 to 84944
5309:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 466}], # Indices 84944 to 84960
5310:[], # Indices 84960 to 84976
5311:[], # Indices 84976 to 84992
5312:[], # Indices 84992 to 85008
5313:[], # Indices 85008 to 85024
5314:[], # Indices 85024 to 85040
5315:[], # Indices 85040 to 85056
5316:[], # Indices 85056 to 85072
5317:[], # Indices 85072 to 85088
5318:[], # Indices 85088 to 85104
5319:[], # Indices 85104 to 85120
5320:[], # Indices 85120 to 85136
5321:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 514}], # Indices 85136 to 85152
5322:[], # Indices 85152 to 85168
5323:[], # Indices 85168 to 85184
5324:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 480}], # Indices 85184 to 85200
5325:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 202}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 203}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 193}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 203}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 187}], # Indices 85200 to 85216
5326:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 484}], # Indices 85216 to 85232
5327:[], # Indices 85232 to 85248
5328:[], # Indices 85248 to 85264
5329:[], # Indices 85264 to 85280
5330:[], # Indices 85280 to 85296
5331:[], # Indices 85296 to 85312
5332:[], # Indices 85312 to 85328
5333:[], # Indices 85328 to 85344
5334:[], # Indices 85344 to 85360
5335:[], # Indices 85360 to 85376
5336:[], # Indices 85376 to 85392
5337:[], # Indices 85392 to 85408
5338:[], # Indices 85408 to 85424
5339:[], # Indices 85424 to 85440
5340:[{'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 91}], # Indices 85440 to 85456
5341:[], # Indices 85456 to 85472
5342:[], # Indices 85472 to 85488
5343:[], # Indices 85488 to 85504
5344:[], # Indices 85504 to 85520
5345:[], # Indices 85520 to 85536
5346:[], # Indices 85536 to 85552
5347:[], # Indices 85552 to 85568
5348:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 498}], # Indices 85568 to 85584
5349:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 189}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 192}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 226}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 190}, {'index_dec': 15, 'index_bin': '1111', 'val': 15, 'counts': 186}], # Indices 85584 to 85600
5350:[], # Indices 85600 to 85616
5351:[], # Indices 85616 to 85632
5352:[], # Indices 85632 to 85648
5353:[], # Indices 85648 to 85664
5354:[], # Indices 85664 to 85680
5355:[], # Indices 85680 to 85696
5356:[], # Indices 85696 to 85712
5357:[], # Indices 85712 to 85728
5358:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 507}], # Indices 85728 to 85744
5359:[], # Indices 85744 to 85760
5360:[], # Indices 85760 to 85776
5361:[{'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 493}], # Indices 85776 to 85792
5362:[], # Indices 85792 to 85808
5363:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 481}], # Indices 85808 to 85824
5364:[], # Indices 85824 to 85840
5365:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 405}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 359}], # Indices 85840 to 85856
5366:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 104}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 92}, {'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 109}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 103}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 91}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 91}, {'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 106}], # Indices 85856 to 85872
5367:[], # Indices 85872 to 85888
5368:[], # Indices 85888 to 85904
5369:[], # Indices 85904 to 85920
5370:[], # Indices 85920 to 85936
5371:[], # Indices 85936 to 85952
5372:[], # Indices 85952 to 85968
5373:[], # Indices 85968 to 85984
5374:[], # Indices 85984 to 86000
5375:[], # Indices 86000 to 86016
5376:[], # Indices 86016 to 86032
5377:[], # Indices 86032 to 86048
5378:[], # Indices 86048 to 86064
5379:[], # Indices 86064 to 86080
5380:[], # Indices 86080 to 86096
5381:[], # Indices 86096 to 86112
5382:[], # Indices 86112 to 86128
5383:[], # Indices 86128 to 86144
5384:[], # Indices 86144 to 86160
5385:[], # Indices 86160 to 86176
5386:[], # Indices 86176 to 86192
5387:[], # Indices 86192 to 86208
5388:[], # Indices 86208 to 86224
5389:[], # Indices 86224 to 86240
5390:[], # Indices 86240 to 86256
5391:[], # Indices 86256 to 86272
5392:[], # Indices 86272 to 86288
5393:[], # Indices 86288 to 86304
5394:[], # Indices 86304 to 86320
5395:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 383}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 394}], # Indices 86320 to 86336
5396:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 382}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 411}], # Indices 86336 to 86352
5397:[{'index_dec': 5, 'index_bin': '0101', 'val': 14, 'counts': 320}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 310}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 344}], # Indices 86352 to 86368
5398:[], # Indices 86368 to 86384
5399:[{'index_dec': 8, 'index_bin': '1000', 'val': 13, 'counts': 509}], # Indices 86384 to 86400
5400:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 470}], # Indices 86400 to 86416
5401:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 459}], # Indices 86416 to 86432
5402:[], # Indices 86432 to 86448
5403:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 515}], # Indices 86448 to 86464
5404:[], # Indices 86464 to 86480
5405:[{'index_dec': 8, 'index_bin': '1000', 'val': 11, 'counts': 466}], # Indices 86480 to 86496
5406:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 339}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 332}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 312}], # Indices 86496 to 86512
5407:[], # Indices 86512 to 86528
5408:[], # Indices 86528 to 86544
5409:[], # Indices 86544 to 86560
5410:[], # Indices 86560 to 86576
5411:[], # Indices 86576 to 86592
5412:[], # Indices 86592 to 86608
5413:[], # Indices 86608 to 86624
5414:[], # Indices 86624 to 86640
5415:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 474}], # Indices 86640 to 86656
5416:[], # Indices 86656 to 86672
5417:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 490}], # Indices 86672 to 86688
5418:[], # Indices 86688 to 86704
5419:[], # Indices 86704 to 86720
5420:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 498}], # Indices 86720 to 86736
5421:[{'index_dec': 6, 'index_bin': '0110', 'val': 19, 'counts': 491}], # Indices 86736 to 86752
5422:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 338}, {'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 332}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 315}], # Indices 86752 to 86768
5423:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 479}], # Indices 86768 to 86784
5424:[], # Indices 86784 to 86800
5425:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 477}], # Indices 86800 to 86816
5426:[], # Indices 86816 to 86832
5427:[{'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 473}], # Indices 86832 to 86848
5428:[{'index_dec': 5, 'index_bin': '0101', 'val': 12, 'counts': 314}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 321}, {'index_dec': 9, 'index_bin': '1001', 'val': 13, 'counts': 339}], # Indices 86848 to 86864
5429:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 507}], # Indices 86864 to 86880
5430:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 418}, {'index_dec': 14, 'index_bin': '1110', 'val': 14, 'counts': 381}], # Indices 86880 to 86896
5431:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 249}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 274}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 264}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 237}], # Indices 86896 to 86912
5432:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 399}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 389}], # Indices 86912 to 86928
5433:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 344}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 334}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 298}], # Indices 86928 to 86944
5434:[], # Indices 86944 to 86960
5435:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 484}], # Indices 86960 to 86976
5436:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 343}, {'index_dec': 10, 'index_bin': '1010', 'val': 19, 'counts': 323}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 300}], # Indices 86976 to 86992
5437:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 424}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 382}], # Indices 86992 to 87008
5438:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 411}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 406}], # Indices 87008 to 87024
5439:[{'index_dec': 14, 'index_bin': '1110', 'val': 17, 'counts': 457}], # Indices 87024 to 87040
5440:[], # Indices 87040 to 87056
5441:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 381}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 438}], # Indices 87056 to 87072
5442:[{'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 485}], # Indices 87072 to 87088
5443:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 462}], # Indices 87088 to 87104
5444:[{'index_dec': 4, 'index_bin': '0100', 'val': 18, 'counts': 431}], # Indices 87104 to 87120
5445:[], # Indices 87120 to 87136
5446:[{'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 467}], # Indices 87136 to 87152
5447:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 394}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 397}], # Indices 87152 to 87168
5448:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 398}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 407}], # Indices 87168 to 87184
5449:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 386}, {'index_dec': 10, 'index_bin': '1010', 'val': 8, 'counts': 417}], # Indices 87184 to 87200
5450:[], # Indices 87200 to 87216
5451:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 320}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 289}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 361}], # Indices 87216 to 87232
5452:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 293}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 371}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 311}], # Indices 87232 to 87248
5453:[], # Indices 87248 to 87264
5454:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 395}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 385}], # Indices 87264 to 87280
5455:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 395}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 394}], # Indices 87280 to 87296
5456:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 496}], # Indices 87296 to 87312
5457:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 477}], # Indices 87312 to 87328
5458:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 339}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 307}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 333}], # Indices 87328 to 87344
5459:[{'index_dec': 2, 'index_bin': '0010', 'val': 14, 'counts': 468}], # Indices 87344 to 87360
5460:[{'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 412}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 393}], # Indices 87360 to 87376
5461:[], # Indices 87376 to 87392
5462:[{'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 404}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 417}], # Indices 87392 to 87408
5463:[{'index_dec': 15, 'index_bin': '1111', 'val': 14, 'counts': 476}], # Indices 87408 to 87424
5464:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 397}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 402}], # Indices 87424 to 87440
5465:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 321}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 312}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 334}], # Indices 87440 to 87456
5466:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 395}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 420}], # Indices 87456 to 87472
5467:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 419}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 377}], # Indices 87472 to 87488
5468:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 492}], # Indices 87488 to 87504
5469:[{'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 379}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 401}], # Indices 87504 to 87520
5470:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 423}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 400}], # Indices 87520 to 87536
5471:[{'index_dec': 9, 'index_bin': '1001', 'val': 19, 'counts': 319}, {'index_dec': 13, 'index_bin': '1101', 'val': 13, 'counts': 303}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 347}], # Indices 87536 to 87552
5472:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 250}, {'index_dec': 3, 'index_bin': '0011', 'val': 13, 'counts': 256}, {'index_dec': 6, 'index_bin': '0110', 'val': 8, 'counts': 254}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 264}], # Indices 87552 to 87568
5473:[{'index_dec': 0, 'index_bin': '0000', 'val': 11, 'counts': 316}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 320}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 329}], # Indices 87568 to 87584
5474:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 395}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 389}], # Indices 87584 to 87600
5475:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 343}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 315}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 315}], # Indices 87600 to 87616
5476:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 489}], # Indices 87616 to 87632
5477:[{'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 384}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 400}], # Indices 87632 to 87648
5478:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 494}], # Indices 87648 to 87664
5479:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 401}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 410}], # Indices 87664 to 87680
5480:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 474}], # Indices 87680 to 87696
5481:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 492}], # Indices 87696 to 87712
5482:[{'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 390}, {'index_dec': 14, 'index_bin': '1110', 'val': 16, 'counts': 406}], # Indices 87712 to 87728
5483:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 411}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 386}], # Indices 87728 to 87744
5484:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 492}], # Indices 87744 to 87760
5485:[], # Indices 87760 to 87776
5486:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 239}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 242}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 283}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 260}], # Indices 87776 to 87792
5487:[], # Indices 87792 to 87808
5488:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 487}], # Indices 87808 to 87824
5489:[{'index_dec': 1, 'index_bin': '0001', 'val': 17, 'counts': 190}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 191}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 193}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 218}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 188}], # Indices 87824 to 87840
5490:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 312}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 352}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 316}], # Indices 87840 to 87856
5491:[{'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 504}], # Indices 87856 to 87872
5492:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 193}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 174}, {'index_dec': 10, 'index_bin': '1010', 'val': 14, 'counts': 206}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 185}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 220}], # Indices 87872 to 87888
5493:[{'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 513}], # Indices 87888 to 87904
5494:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 270}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 256}, {'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 256}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 242}], # Indices 87904 to 87920
5495:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 391}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 407}], # Indices 87920 to 87936
5496:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 346}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 324}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 305}], # Indices 87936 to 87952
5497:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 386}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 411}], # Indices 87952 to 87968
5498:[{'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 425}, {'index_dec': 14, 'index_bin': '1110', 'val': 16, 'counts': 381}], # Indices 87968 to 87984
5499:[{'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 382}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 423}], # Indices 87984 to 88000
5500:[{'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 407}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 380}], # Indices 88000 to 88016
5501:[], # Indices 88016 to 88032
5502:[{'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 422}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 383}], # Indices 88032 to 88048
5503:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 340}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 319}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 305}], # Indices 88048 to 88064
5504:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 411}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 370}], # Indices 88064 to 88080
5505:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 489}], # Indices 88080 to 88096
5506:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 383}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 421}], # Indices 88096 to 88112
5507:[], # Indices 88112 to 88128
5508:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 187}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 204}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 176}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 192}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 222}], # Indices 88128 to 88144
5509:[{'index_dec': 12, 'index_bin': '1100', 'val': 11, 'counts': 461}], # Indices 88144 to 88160
5510:[{'index_dec': 0, 'index_bin': '0000', 'val': 13, 'counts': 261}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 240}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 256}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 267}], # Indices 88160 to 88176
5511:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 391}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 400}], # Indices 88176 to 88192
5512:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 506}], # Indices 88192 to 88208
5513:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 328}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 312}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 338}], # Indices 88208 to 88224
5514:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 262}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 249}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 241}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 272}], # Indices 88224 to 88240
5515:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 313}, {'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 334}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 326}], # Indices 88240 to 88256
5516:[{'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 478}], # Indices 88256 to 88272
5517:[{'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 407}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 398}], # Indices 88272 to 88288
5518:[{'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 522}], # Indices 88288 to 88304
5519:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 240}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 257}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 267}, {'index_dec': 14, 'index_bin': '1110', 'val': 18, 'counts': 260}], # Indices 88304 to 88320
5520:[{'index_dec': 7, 'index_bin': '0111', 'val': 11, 'counts': 186}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 199}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 189}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 218}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 189}], # Indices 88320 to 88336
5521:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 95}, {'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 93}, {'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 113}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 99}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 95}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 92}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 104}], # Indices 88336 to 88352
5522:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 481}], # Indices 88352 to 88368
5523:[{'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 228}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 168}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 185}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 201}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 196}], # Indices 88368 to 88384
5524:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 254}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 266}, {'index_dec': 8, 'index_bin': '1000', 'val': 12, 'counts': 231}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 273}], # Indices 88384 to 88400
5525:[{'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 375}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 409}], # Indices 88400 to 88416
5526:[{'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 467}], # Indices 88416 to 88432
5527:[{'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 239}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 282}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 240}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 263}], # Indices 88432 to 88448
5528:[{'index_dec': 0, 'index_bin': '0000', 'val': 16, 'counts': 243}, {'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 248}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 265}, {'index_dec': 13, 'index_bin': '1101', 'val': 14, 'counts': 268}], # Indices 88448 to 88464
5529:[{'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 483}], # Indices 88464 to 88480
5530:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 487}], # Indices 88480 to 88496
5531:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 390}, {'index_dec': 14, 'index_bin': '1110', 'val': 12, 'counts': 395}], # Indices 88496 to 88512
5532:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 259}, {'index_dec': 6, 'index_bin': '0110', 'val': 15, 'counts': 281}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 237}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 247}], # Indices 88512 to 88528
5533:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 275}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 220}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 282}, {'index_dec': 11, 'index_bin': '1011', 'val': 8, 'counts': 247}], # Indices 88528 to 88544
5534:[{'index_dec': 2, 'index_bin': '0010', 'val': 16, 'counts': 260}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 262}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 262}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 240}], # Indices 88544 to 88560
5535:[], # Indices 88560 to 88576
5536:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 244}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 239}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 290}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 251}], # Indices 88576 to 88592
5537:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 257}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 242}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 247}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 278}], # Indices 88592 to 88608
5538:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 417}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 401}], # Indices 88608 to 88624
5539:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 340}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 313}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 308}], # Indices 88624 to 88640
5540:[{'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 486}], # Indices 88640 to 88656
5541:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 325}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 317}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 330}], # Indices 88656 to 88672
5542:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 484}], # Indices 88672 to 88688
5543:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 313}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 307}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 338}], # Indices 88688 to 88704
5544:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 184}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 176}, {'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 212}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 211}, {'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 197}], # Indices 88704 to 88720
5545:[{'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 324}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 327}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 322}], # Indices 88720 to 88736
5546:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 486}], # Indices 88736 to 88752
5547:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 339}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 315}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 315}], # Indices 88752 to 88768
5548:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 411}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 398}], # Indices 88768 to 88784
5549:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 381}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 417}], # Indices 88784 to 88800
5550:[{'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 476}], # Indices 88800 to 88816
5551:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 215}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 184}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 199}, {'index_dec': 12, 'index_bin': '1100', 'val': 9, 'counts': 195}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 196}], # Indices 88816 to 88832
5552:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 319}, {'index_dec': 1, 'index_bin': '0001', 'val': 11, 'counts': 323}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 328}], # Indices 88832 to 88848
5553:[{'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 262}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 257}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 270}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 235}], # Indices 88848 to 88864
5554:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 503}], # Indices 88864 to 88880
5555:[{'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 492}], # Indices 88880 to 88896
5556:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 269}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 240}, {'index_dec': 7, 'index_bin': '0111', 'val': 12, 'counts': 253}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 262}], # Indices 88896 to 88912
5557:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 179}, {'index_dec': 5, 'index_bin': '0101', 'val': 12, 'counts': 191}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 206}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 196}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 204}], # Indices 88912 to 88928
5558:[{'index_dec': 2, 'index_bin': '0010', 'val': 8, 'counts': 166}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 159}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 124}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 144}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 137}, {'index_dec': 15, 'index_bin': '1111', 'val': 10, 'counts': 142}], # Indices 88928 to 88944
5559:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 497}], # Indices 88944 to 88960
5560:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 193}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 196}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 195}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 206}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 192}], # Indices 88960 to 88976
5561:[{'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 534}], # Indices 88976 to 88992
5562:[{'index_dec': 1, 'index_bin': '0001', 'val': 13, 'counts': 406}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 409}], # Indices 88992 to 89008
5563:[{'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 504}], # Indices 89008 to 89024
5564:[{'index_dec': 5, 'index_bin': '0101', 'val': 14, 'counts': 444}], # Indices 89024 to 89040
5565:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 148}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 143}, {'index_dec': 12, 'index_bin': '1100', 'val': 16, 'counts': 136}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 131}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 134}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 157}], # Indices 89040 to 89056
5566:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 330}, {'index_dec': 5, 'index_bin': '0101', 'val': 9, 'counts': 323}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 321}], # Indices 89056 to 89072
5567:[{'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 394}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 405}], # Indices 89072 to 89088
5568:[{'index_dec': 2, 'index_bin': '0010', 'val': 11, 'counts': 298}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 336}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 336}], # Indices 89088 to 89104
5569:[{'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 326}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 325}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 312}], # Indices 89104 to 89120
5570:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 323}, {'index_dec': 5, 'index_bin': '0101', 'val': 18, 'counts': 324}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 325}], # Indices 89120 to 89136
5571:[{'index_dec': 7, 'index_bin': '0111', 'val': 14, 'counts': 497}], # Indices 89136 to 89152
5572:[{'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 383}, {'index_dec': 11, 'index_bin': '1011', 'val': 10, 'counts': 424}], # Indices 89152 to 89168
5573:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 410}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 400}], # Indices 89168 to 89184
5574:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 255}, {'index_dec': 10, 'index_bin': '1010', 'val': 12, 'counts': 254}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 262}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 253}], # Indices 89184 to 89200
5575:[{'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 476}], # Indices 89200 to 89216
5576:[{'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 375}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 431}], # Indices 89216 to 89232
5577:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 185}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 219}, {'index_dec': 9, 'index_bin': '1001', 'val': 11, 'counts': 217}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 174}, {'index_dec': 11, 'index_bin': '1011', 'val': 12, 'counts': 189}], # Indices 89232 to 89248
5578:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 329}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 318}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 332}], # Indices 89248 to 89264
5579:[], # Indices 89264 to 89280
5580:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 263}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 253}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 260}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 248}], # Indices 89280 to 89296
5581:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 338}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 312}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 312}], # Indices 89296 to 89312
5582:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 154}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 142}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 145}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 137}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 140}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 144}], # Indices 89312 to 89328
5583:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 274}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 250}, {'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 251}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 249}], # Indices 89328 to 89344
5584:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 232}, {'index_dec': 4, 'index_bin': '0100', 'val': 15, 'counts': 178}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 176}, {'index_dec': 9, 'index_bin': '1001', 'val': 16, 'counts': 193}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 191}], # Indices 89344 to 89360
5585:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 312}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 330}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 327}], # Indices 89360 to 89376
5586:[{'index_dec': 5, 'index_bin': '0101', 'val': 12, 'counts': 304}, {'index_dec': 8, 'index_bin': '1000', 'val': 10, 'counts': 323}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 343}], # Indices 89376 to 89392
5587:[{'index_dec': 0, 'index_bin': '0000', 'val': 8, 'counts': 121}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 91}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 115}, {'index_dec': 8, 'index_bin': '1000', 'val': 19, 'counts': 104}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 107}], # Indices 89392 to 89408
5588:[{'index_dec': 4, 'index_bin': '0100', 'val': 8, 'counts': 319}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 323}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 314}], # Indices 89408 to 89424
5589:[{'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 391}, {'index_dec': 13, 'index_bin': '1101', 'val': 15, 'counts': 391}], # Indices 89424 to 89440
5590:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 216}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 205}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 171}, {'index_dec': 12, 'index_bin': '1100', 'val': 15, 'counts': 202}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 184}], # Indices 89440 to 89456
5591:[{'index_dec': 1, 'index_bin': '0001', 'val': 10, 'counts': 107}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 113}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 109}, {'index_dec': 9, 'index_bin': '1001', 'val': 10, 'counts': 93}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 92}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 105}], # Indices 89456 to 89472
5592:[{'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 95}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 102}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 109}, {'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 111}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 101}], # Indices 89472 to 89488
5593:[{'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 234}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 274}, {'index_dec': 9, 'index_bin': '1001', 'val': 8, 'counts': 254}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 262}], # Indices 89488 to 89504
5594:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 309}, {'index_dec': 7, 'index_bin': '0111', 'val': 8, 'counts': 332}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 346}], # Indices 89504 to 89520
5595:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 329}, {'index_dec': 12, 'index_bin': '1100', 'val': 12, 'counts': 336}, {'index_dec': 14, 'index_bin': '1110', 'val': 9, 'counts': 315}], # Indices 89520 to 89536
5596:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 382}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 387}], # Indices 89536 to 89552
5597:[{'index_dec': 14, 'index_bin': '1110', 'val': 8, 'counts': 452}], # Indices 89552 to 89568
5598:[{'index_dec': 1, 'index_bin': '0001', 'val': 12, 'counts': 176}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 142}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 143}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 136}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 136}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 145}], # Indices 89568 to 89584
5599:[{'index_dec': 2, 'index_bin': '0010', 'val': 12, 'counts': 319}, {'index_dec': 3, 'index_bin': '0011', 'val': 12, 'counts': 344}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 309}], # Indices 89584 to 89600
5600:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 275}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 256}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 256}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 237}], # Indices 89600 to 89616
5601:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 135}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 146}, {'index_dec': 4, 'index_bin': '0100', 'val': 9, 'counts': 147}, {'index_dec': 6, 'index_bin': '0110', 'val': 18, 'counts': 137}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 155}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 138}], # Indices 89616 to 89632
5602:[{'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 248}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 250}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 268}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 258}], # Indices 89632 to 89648
5603:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 131}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 168}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 139}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 136}, {'index_dec': 12, 'index_bin': '1100', 'val': 7, 'counts': 164}, {'index_dec': 15, 'index_bin': '1111', 'val': 11, 'counts': 142}], # Indices 89648 to 89664
5604:[{'index_dec': 0, 'index_bin': '0000', 'val': 10, 'counts': 253}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 240}, {'index_dec': 5, 'index_bin': '0101', 'val': 13, 'counts': 273}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 258}], # Indices 89664 to 89680
5605:[{'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 261}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 243}, {'index_dec': 13, 'index_bin': '1101', 'val': 9, 'counts': 240}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 280}], # Indices 89680 to 89696
5606:[{'index_dec': 6, 'index_bin': '0110', 'val': 16, 'counts': 297}, {'index_dec': 7, 'index_bin': '0111', 'val': 10, 'counts': 338}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 347}], # Indices 89696 to 89712
5607:[{'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 149}, {'index_dec': 2, 'index_bin': '0010', 'val': 17, 'counts': 147}, {'index_dec': 4, 'index_bin': '0100', 'val': 7, 'counts': 159}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 139}, {'index_dec': 12, 'index_bin': '1100', 'val': 10, 'counts': 144}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 132}], # Indices 89712 to 89728
5608:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 141}, {'index_dec': 8, 'index_bin': '1000', 'val': 18, 'counts': 144}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 148}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 137}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 149}, {'index_dec': 15, 'index_bin': '1111', 'val': 12, 'counts': 130}], # Indices 89728 to 89744
5609:[{'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 156}, {'index_dec': 5, 'index_bin': '0101', 'val': 10, 'counts': 131}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 154}, {'index_dec': 9, 'index_bin': '1001', 'val': 9, 'counts': 132}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 136}, {'index_dec': 13, 'index_bin': '1101', 'val': 11, 'counts': 143}], # Indices 89744 to 89760
5610:[{'index_dec': 0, 'index_bin': '0000', 'val': 7, 'counts': 139}, {'index_dec': 1, 'index_bin': '0001', 'val': 7, 'counts': 143}, {'index_dec': 6, 'index_bin': '0110', 'val': 9, 'counts': 138}, {'index_dec': 10, 'index_bin': '1010', 'val': 9, 'counts': 126}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 161}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 157}], # Indices 89760 to 89776
5611:[{'index_dec': 0, 'index_bin': '0000', 'val': 12, 'counts': 250}, {'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 253}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 275}, {'index_dec': 13, 'index_bin': '1101', 'val': 12, 'counts': 246}], # Indices 89776 to 89792
5612:[{'index_dec': 15, 'index_bin': '1111', 'val': 8, 'counts': 465}], # Indices 89792 to 89808
5613:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 206}, {'index_dec': 3, 'index_bin': '0011', 'val': 18, 'counts': 192}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 186}, {'index_dec': 9, 'index_bin': '1001', 'val': 12, 'counts': 197}, {'index_dec': 10, 'index_bin': '1010', 'val': 11, 'counts': 206}], # Indices 89808 to 89824
5614:[{'index_dec': 3, 'index_bin': '0011', 'val': 11, 'counts': 336}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 318}, {'index_dec': 15, 'index_bin': '1111', 'val': 9, 'counts': 315}], # Indices 89824 to 89840
5615:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 117}, {'index_dec': 4, 'index_bin': '0100', 'val': 10, 'counts': 133}, {'index_dec': 10, 'index_bin': '1010', 'val': 7, 'counts': 170}, {'index_dec': 11, 'index_bin': '1011', 'val': 11, 'counts': 138}, {'index_dec': 12, 'index_bin': '1100', 'val': 8, 'counts': 155}, {'index_dec': 14, 'index_bin': '1110', 'val': 7, 'counts': 143}], # Indices 89840 to 89856
5616:[{'index_dec': 11, 'index_bin': '1011', 'val': 16, 'counts': 489}], # Indices 89856 to 89872
5617:[{'index_dec': 1, 'index_bin': '0001', 'val': 9, 'counts': 135}, {'index_dec': 4, 'index_bin': '0100', 'val': 18, 'counts': 135}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 165}, {'index_dec': 6, 'index_bin': '0110', 'val': 7, 'counts': 161}, {'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 131}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 153}], # Indices 89872 to 89888
5618:[{'index_dec': 0, 'index_bin': '0000', 'val': 9, 'counts': 192}, {'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 197}, {'index_dec': 8, 'index_bin': '1000', 'val': 9, 'counts': 194}, {'index_dec': 11, 'index_bin': '1011', 'val': 9, 'counts': 195}, {'index_dec': 13, 'index_bin': '1101', 'val': 8, 'counts': 201}], # Indices 89888 to 89904
5619:[{'index_dec': 2, 'index_bin': '0010', 'val': 10, 'counts': 256}, {'index_dec': 3, 'index_bin': '0011', 'val': 9, 'counts': 265}, {'index_dec': 4, 'index_bin': '0100', 'val': 11, 'counts': 261}, {'index_dec': 6, 'index_bin': '0110', 'val': 10, 'counts': 242}], # Indices 89904 to 89920
5620:[{'index_dec': 1, 'index_bin': '0001', 'val': 18, 'counts': 135}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 132}, {'index_dec': 7, 'index_bin': '0111', 'val': 9, 'counts': 141}, {'index_dec': 9, 'index_bin': '1001', 'val': 7, 'counts': 149}, {'index_dec': 13, 'index_bin': '1101', 'val': 7, 'counts': 162}, {'index_dec': 15, 'index_bin': '1111', 'val': 7, 'counts': 147}], # Indices 89920 to 89936
5621:[{'index_dec': 1, 'index_bin': '0001', 'val': 8, 'counts': 244}, {'index_dec': 2, 'index_bin': '0010', 'val': 9, 'counts': 273}, {'index_dec': 3, 'index_bin': '0011', 'val': 8, 'counts': 263}, {'index_dec': 5, 'index_bin': '0101', 'val': 8, 'counts': 244}], # Indices 89936 to 89952
5622:[{'index_dec': 2, 'index_bin': '0010', 'val': 7, 'counts': 251}, {'index_dec': 5, 'index_bin': '0101', 'val': 7, 'counts': 261}, {'index_dec': 11, 'index_bin': '1011', 'val': 7, 'counts': 254}, {'index_dec': 14, 'index_bin': '1110', 'val': 10, 'counts': 258}], # Indices 89952 to 89968
5623:[{'index_dec': 8, 'index_bin': '1000', 'val': 8, 'counts': 391}, {'index_dec': 10, 'index_bin': '1010', 'val': 17, 'counts': 396}], # Indices 89968 to 89984
5624:[], # Indices 89984 to 90000
5625:[], # Indices 90000 to 90016
5626:[], # Indices 90016 to 90032
5627:[], # Indices 90032 to 90048
5628:[], # Indices 90048 to 90064
5629:[], # Indices 90064 to 90080
5630:[], # Indices 90080 to 90096
5631:[], # Indices 90096 to 90112
5632:[], # Indices 90112 to 90128
5633:[], # Indices 90128 to 90144
5634:[], # Indices 90144 to 90160
5635:[], # Indices 90160 to 90176
5636:[], # Indices 90176 to 90192
5637:[], # Indices 90192 to 90208
5638:[], # Indices 90208 to 90224
5639:[], # Indices 90224 to 90240
5640:[], # Indices 90240 to 90256
5641:[], # Indices 90256 to 90272
5642:[], # Indices 90272 to 90288
5643:[], # Indices 90288 to 90304
5644:[{'index_dec': 1, 'index_bin': '0001', 'val': 19, 'counts': 146}, {'index_dec': 2, 'index_bin': '0010', 'val': 18, 'counts': 140}, {'index_dec': 3, 'index_bin': '0011', 'val': 10, 'counts': 142}, {'index_dec': 6, 'index_bin': '0110', 'val': 12, 'counts': 140}, {'index_dec': 7, 'index_bin': '0111', 'val': 7, 'counts': 138}, {'index_dec': 13, 'index_bin': '1101', 'val': 10, 'counts': 144}], # Indices 90304 to 90320
5645:[], # Indices 90320 to 90336
5646:[], # Indices 90336 to 90352
5647:[], # Indices 90352 to 90368
5648:[], # Indices 90368 to 90384
5649:[], # Indices 90384 to 90400
5650:[], # Indices 90400 to 90416
5651:[], # Indices 90416 to 90432
5652:[], # Indices 90432 to 90448
5653:[], # Indices 90448 to 90464
5654:[], # Indices 90464 to 90480
5655:[], # Indices 90480 to 90496
5656:[], # Indices 90496 to 90512
5657:[], # Indices 90512 to 90528
5658:[], # Indices 90528 to 90544
5659:[], # Indices 90544 to 90560
5660:[], # Indices 90560 to 90576
5661:[], # Indices 90576 to 90592
5662:[], # Indices 90592 to 90608
5663:[], # Indices 90608 to 90624
5664:[], # Indices 90624 to 90640
5665:[], # Indices 90640 to 90656
5666:[], # Indices 90656 to 90672
5667:[], # Indices 90672 to 90688
5668:[], # Indices 90688 to 90704
5669:[], # Indices 90704 to 90720
5670:[], # Indices 90720 to 90736
5671:[], # Indices 90736 to 90752
5672:[], # Indices 90752 to 90768
5673:[], # Indices 90768 to 90784
5674:[], # Indices 90784 to 90800
5675:[], # Indices 90800 to 90816
5676:[], # Indices 90816 to 90832
5677:[], # Indices 90832 to 90848
5678:[], # Indices 90848 to 90864
5679:[], # Indices 90864 to 90880
5680:[], # Indices 90880 to 90896
5681:[], # Indices 90896 to 90912
5682:[], # Indices 90912 to 90928
5683:[], # Indices 90928 to 90944
5684:[], # Indices 90944 to 90960
5685:[], # Indices 90960 to 90976
5686:[], # Indices 90976 to 90992
5687:[], # Indices 90992 to 91008
5688:[], # Indices 91008 to 91024
5689:[], # Indices 91024 to 91040
5690:[], # Indices 91040 to 91056
5691:[], # Indices 91056 to 91072
5692:[], # Indices 91072 to 91088
5693:[], # Indices 91088 to 91104
5694:[], # Indices 91104 to 91120
5695:[], # Indices 91120 to 91136
5696:[], # Indices 91136 to 91152
5697:[], # Indices 91152 to 91168
5698:[], # Indices 91168 to 91184
5699:[], # Indices 91184 to 91200
5700:[], # Indices 91200 to 91216
5701:[], # Indices 91216 to 91232
5702:[], # Indices 91232 to 91248
5703:[], # Indices 91248 to 91264
5704:[], # Indices 91264 to 91280
5705:[], # Indices 91280 to 91296
5706:[], # Indices 91296 to 91312
5707:[], # Indices 91312 to 91328
5708:[], # Indices 91328 to 91344
5709:[], # Indices 91344 to 91360
5710:[], # Indices 91360 to 91376
5711:[], # Indices 91376 to 91392
5712:[], # Indices 91392 to 91408
5713:[], # Indices 91408 to 91424
5714:[], # Indices 91424 to 91440
5715:[], # Indices 91440 to 91456
5716:[], # Indices 91456 to 91472
5717:[], # Indices 91472 to 91488
5718:[], # Indices 91488 to 91504
5719:[], # Indices 91504 to 91520
5720:[], # Indices 91520 to 91536
5721:[], # Indices 91536 to 91552
5722:[], # Indices 91552 to 91568
5723:[], # Indices 91568 to 91584
5724:[], # Indices 91584 to 91600
5725:[], # Indices 91600 to 91616
5726:[], # Indices 91616 to 91632
5727:[], # Indices 91632 to 91648
5728:[], # Indices 91648 to 91664
5729:[], # Indices 91664 to 91680
5730:[], # Indices 91680 to 91696
5731:[], # Indices 91696 to 91712
5732:[], # Indices 91712 to 91728
5733:[], # Indices 91728 to 91744
5734:[], # Indices 91744 to 91760
5735:[], # Indices 91760 to 91776
5736:[{'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 98}], # Indices 91776 to 91792
5737:[], # Indices 91792 to 91808
5738:[], # Indices 91808 to 91824
5739:[], # Indices 91824 to 91840
5740:[], # Indices 91840 to 91856
5741:[], # Indices 91856 to 91872
5742:[], # Indices 91872 to 91888
5743:[], # Indices 91888 to 91904
5744:[], # Indices 91904 to 91920
5745:[], # Indices 91920 to 91936
5746:[], # Indices 91936 to 91952
5747:[], # Indices 91952 to 91968
5748:[], # Indices 91968 to 91984
5749:[], # Indices 91984 to 92000
5750:[], # Indices 92000 to 92016
5751:[], # Indices 92016 to 92032
5752:[], # Indices 92032 to 92048
5753:[], # Indices 92048 to 92064
5754:[], # Indices 92064 to 92080
5755:[], # Indices 92080 to 92096
5756:[], # Indices 92096 to 92112
5757:[], # Indices 92112 to 92128
5758:[], # Indices 92128 to 92144
5759:[], # Indices 92144 to 92160
5760:[], # Indices 92160 to 92176
5761:[], # Indices 92176 to 92192
5762:[], # Indices 92192 to 92208
5763:[], # Indices 92208 to 92224
5764:[], # Indices 92224 to 92240
5765:[], # Indices 92240 to 92256
5766:[], # Indices 92256 to 92272
5767:[], # Indices 92272 to 92288
5768:[], # Indices 92288 to 92304
5769:[], # Indices 92304 to 92320
5770:[], # Indices 92320 to 92336
5771:[], # Indices 92336 to 92352
5772:[], # Indices 92352 to 92368
5773:[], # Indices 92368 to 92384
5774:[], # Indices 92384 to 92400
5775:[], # Indices 92400 to 92416
5776:[], # Indices 92416 to 92432
5777:[], # Indices 92432 to 92448
5778:[], # Indices 92448 to 92464
5779:[], # Indices 92464 to 92480
5780:[], # Indices 92480 to 92496
5781:[], # Indices 92496 to 92512
5782:[], # Indices 92512 to 92528
5783:[], # Indices 92528 to 92544
5784:[], # Indices 92544 to 92560
5785:[], # Indices 92560 to 92576
5786:[], # Indices 92576 to 92592
5787:[], # Indices 92592 to 92608
5788:[], # Indices 92608 to 92624
5789:[], # Indices 92624 to 92640
5790:[], # Indices 92640 to 92656
5791:[], # Indices 92656 to 92672
5792:[], # Indices 92672 to 92688
5793:[], # Indices 92688 to 92704
5794:[], # Indices 92704 to 92720
5795:[], # Indices 92720 to 92736
5796:[], # Indices 92736 to 92752
5797:[], # Indices 92752 to 92768
5798:[], # Indices 92768 to 92784
5799:[], # Indices 92784 to 92800
5800:[], # Indices 92800 to 92816
5801:[], # Indices 92816 to 92832
5802:[], # Indices 92832 to 92848
5803:[], # Indices 92848 to 92864
5804:[], # Indices 92864 to 92880
5805:[], # Indices 92880 to 92896
5806:[], # Indices 92896 to 92912
5807:[], # Indices 92912 to 92928
5808:[], # Indices 92928 to 92944
5809:[], # Indices 92944 to 92960
5810:[], # Indices 92960 to 92976
5811:[], # Indices 92976 to 92992
5812:[], # Indices 92992 to 93008
5813:[], # Indices 93008 to 93024
5814:[], # Indices 93024 to 93040
5815:[], # Indices 93040 to 93056
5816:[], # Indices 93056 to 93072
5817:[], # Indices 93072 to 93088
5818:[], # Indices 93088 to 93104
5819:[], # Indices 93104 to 93120
5820:[], # Indices 93120 to 93136
5821:[], # Indices 93136 to 93152
5822:[], # Indices 93152 to 93168
5823:[], # Indices 93168 to 93184
5824:[], # Indices 93184 to 93200
5825:[], # Indices 93200 to 93216
5826:[], # Indices 93216 to 93232
5827:[], # Indices 93232 to 93248
5828:[], # Indices 93248 to 93264
5829:[], # Indices 93264 to 93280
5830:[], # Indices 93280 to 93296
5831:[], # Indices 93296 to 93312
5832:[], # Indices 93312 to 93328
5833:[], # Indices 93328 to 93344
5834:[], # Indices 93344 to 93360
5835:[], # Indices 93360 to 93376
5836:[], # Indices 93376 to 93392
5837:[], # Indices 93392 to 93408
5838:[], # Indices 93408 to 93424
5839:[], # Indices 93424 to 93440
5840:[], # Indices 93440 to 93456
5841:[], # Indices 93456 to 93472
5842:[], # Indices 93472 to 93488
5843:[], # Indices 93488 to 93504
5844:[], # Indices 93504 to 93520
5845:[], # Indices 93520 to 93536
5846:[], # Indices 93536 to 93552
5847:[], # Indices 93552 to 93568
5848:[], # Indices 93568 to 93584
5849:[], # Indices 93584 to 93600
5850:[], # Indices 93600 to 93616
5851:[], # Indices 93616 to 93632
5852:[], # Indices 93632 to 93648
5853:[], # Indices 93648 to 93664
5854:[], # Indices 93664 to 93680
5855:[], # Indices 93680 to 93696
5856:[], # Indices 93696 to 93712
5857:[], # Indices 93712 to 93728
5858:[], # Indices 93728 to 93744
5859:[], # Indices 93744 to 93760
5860:[], # Indices 93760 to 93776
5861:[], # Indices 93776 to 93792
5862:[], # Indices 93792 to 93808
5863:[], # Indices 93808 to 93824
5864:[], # Indices 93824 to 93840
5865:[], # Indices 93840 to 93856
5866:[], # Indices 93856 to 93872
5867:[], # Indices 93872 to 93888
5868:[], # Indices 93888 to 93904
5869:[], # Indices 93904 to 93920
5870:[], # Indices 93920 to 93936
5871:[], # Indices 93936 to 93952
5872:[], # Indices 93952 to 93968
5873:[], # Indices 93968 to 93984
5874:[], # Indices 93984 to 94000
5875:[], # Indices 94000 to 94016
5876:[], # Indices 94016 to 94032
5877:[], # Indices 94032 to 94048
5878:[], # Indices 94048 to 94064
5879:[], # Indices 94064 to 94080
5880:[], # Indices 94080 to 94096
5881:[], # Indices 94096 to 94112
5882:[], # Indices 94112 to 94128
5883:[], # Indices 94128 to 94144
5884:[], # Indices 94144 to 94160
5885:[], # Indices 94160 to 94176
5886:[], # Indices 94176 to 94192
5887:[], # Indices 94192 to 94208
5888:[], # Indices 94208 to 94224
5889:[], # Indices 94224 to 94240
5890:[], # Indices 94240 to 94256
5891:[], # Indices 94256 to 94272
5892:[], # Indices 94272 to 94288
5893:[], # Indices 94288 to 94304
5894:[], # Indices 94304 to 94320
5895:[], # Indices 94320 to 94336
5896:[], # Indices 94336 to 94352
5897:[], # Indices 94352 to 94368
5898:[], # Indices 94368 to 94384
5899:[], # Indices 94384 to 94400
5900:[], # Indices 94400 to 94416
5901:[], # Indices 94416 to 94432
5902:[], # Indices 94432 to 94448
5903:[], # Indices 94448 to 94464
5904:[], # Indices 94464 to 94480
5905:[], # Indices 94480 to 94496
5906:[], # Indices 94496 to 94512
5907:[], # Indices 94512 to 94528
5908:[], # Indices 94528 to 94544
5909:[], # Indices 94544 to 94560
5910:[], # Indices 94560 to 94576
5911:[], # Indices 94576 to 94592
5912:[], # Indices 94592 to 94608
5913:[], # Indices 94608 to 94624
5914:[], # Indices 94624 to 94640
5915:[], # Indices 94640 to 94656
5916:[], # Indices 94656 to 94672
5917:[], # Indices 94672 to 94688
5918:[], # Indices 94688 to 94704
5919:[], # Indices 94704 to 94720
5920:[], # Indices 94720 to 94736
5921:[], # Indices 94736 to 94752
5922:[], # Indices 94752 to 94768
5923:[], # Indices 94768 to 94784
5924:[], # Indices 94784 to 94800
5925:[], # Indices 94800 to 94816
5926:[], # Indices 94816 to 94832
5927:[], # Indices 94832 to 94848
5928:[], # Indices 94848 to 94864
5929:[], # Indices 94864 to 94880
5930:[{'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 93}], # Indices 94880 to 94896
5931:[], # Indices 94896 to 94912
5932:[], # Indices 94912 to 94928
5933:[], # Indices 94928 to 94944
5934:[], # Indices 94944 to 94960
5935:[], # Indices 94960 to 94976
5936:[], # Indices 94976 to 94992
5937:[], # Indices 94992 to 95008
5938:[], # Indices 95008 to 95024
5939:[], # Indices 95024 to 95040
5940:[], # Indices 95040 to 95056
5941:[], # Indices 95056 to 95072
5942:[], # Indices 95072 to 95088
5943:[], # Indices 95088 to 95104
5944:[], # Indices 95104 to 95120
5945:[], # Indices 95120 to 95136
5946:[], # Indices 95136 to 95152
5947:[], # Indices 95152 to 95168
5948:[], # Indices 95168 to 95184
5949:[], # Indices 95184 to 95200
5950:[], # Indices 95200 to 95216
5951:[], # Indices 95216 to 95232
5952:[], # Indices 95232 to 95248
5953:[], # Indices 95248 to 95264
5954:[], # Indices 95264 to 95280
5955:[], # Indices 95280 to 95296
5956:[{'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 98}], # Indices 95296 to 95312
5957:[], # Indices 95312 to 95328
5958:[], # Indices 95328 to 95344
5959:[], # Indices 95344 to 95360
5960:[], # Indices 95360 to 95376
5961:[], # Indices 95376 to 95392
5962:[], # Indices 95392 to 95408
5963:[], # Indices 95408 to 95424
5964:[], # Indices 95424 to 95440
5965:[], # Indices 95440 to 95456
5966:[], # Indices 95456 to 95472
5967:[], # Indices 95472 to 95488
5968:[], # Indices 95488 to 95504
5969:[], # Indices 95504 to 95520
5970:[], # Indices 95520 to 95536
5971:[], # Indices 95536 to 95552
5972:[], # Indices 95552 to 95568
5973:[], # Indices 95568 to 95584
5974:[], # Indices 95584 to 95600
5975:[], # Indices 95600 to 95616
5976:[], # Indices 95616 to 95632
5977:[], # Indices 95632 to 95648
5978:[], # Indices 95648 to 95664
5979:[], # Indices 95664 to 95680
5980:[], # Indices 95680 to 95696
5981:[], # Indices 95696 to 95712
5982:[], # Indices 95712 to 95728
5983:[], # Indices 95728 to 95744
5984:[], # Indices 95744 to 95760
5985:[], # Indices 95760 to 95776
5986:[], # Indices 95776 to 95792
5987:[], # Indices 95792 to 95808
5988:[], # Indices 95808 to 95824
5989:[], # Indices 95824 to 95840
5990:[], # Indices 95840 to 95856
5991:[], # Indices 95856 to 95872
5992:[], # Indices 95872 to 95888
5993:[], # Indices 95888 to 95904
5994:[], # Indices 95904 to 95920
5995:[], # Indices 95920 to 95936
5996:[], # Indices 95936 to 95952
5997:[], # Indices 95952 to 95968
5998:[], # Indices 95968 to 95984
5999:[], # Indices 95984 to 96000
6000:[], # Indices 96000 to 96016
6001:[], # Indices 96016 to 96032
6002:[], # Indices 96032 to 96048
6003:[], # Indices 96048 to 96064
6004:[], # Indices 96064 to 96080
6005:[], # Indices 96080 to 96096
6006:[], # Indices 96096 to 96112
6007:[{'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 91}], # Indices 96112 to 96128
6008:[], # Indices 96128 to 96144
6009:[], # Indices 96144 to 96160
6010:[], # Indices 96160 to 96176
6011:[], # Indices 96176 to 96192
6012:[], # Indices 96192 to 96208
6013:[], # Indices 96208 to 96224
6014:[], # Indices 96224 to 96240
6015:[], # Indices 96240 to 96256
6016:[], # Indices 96256 to 96272
6017:[], # Indices 96272 to 96288
6018:[], # Indices 96288 to 96304
6019:[], # Indices 96304 to 96320
6020:[], # Indices 96320 to 96336
6021:[], # Indices 96336 to 96352
6022:[], # Indices 96352 to 96368
6023:[], # Indices 96368 to 96384
6024:[{'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 91}], # Indices 96384 to 96400
6025:[], # Indices 96400 to 96416
6026:[], # Indices 96416 to 96432
6027:[], # Indices 96432 to 96448
6028:[], # Indices 96448 to 96464
6029:[], # Indices 96464 to 96480
6030:[], # Indices 96480 to 96496
6031:[], # Indices 96496 to 96512
6032:[], # Indices 96512 to 96528
6033:[], # Indices 96528 to 96544
6034:[], # Indices 96544 to 96560
6035:[], # Indices 96560 to 96576
6036:[], # Indices 96576 to 96592
6037:[], # Indices 96592 to 96608
6038:[], # Indices 96608 to 96624
6039:[], # Indices 96624 to 96640
6040:[], # Indices 96640 to 96656
6041:[], # Indices 96656 to 96672
6042:[], # Indices 96672 to 96688
6043:[], # Indices 96688 to 96704
6044:[], # Indices 96704 to 96720
6045:[{'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 91}], # Indices 96720 to 96736
6046:[], # Indices 96736 to 96752
6047:[], # Indices 96752 to 96768
6048:[], # Indices 96768 to 96784
6049:[], # Indices 96784 to 96800
6050:[], # Indices 96800 to 96816
6051:[], # Indices 96816 to 96832
6052:[], # Indices 96832 to 96848
6053:[], # Indices 96848 to 96864
6054:[], # Indices 96864 to 96880
6055:[], # Indices 96880 to 96896
6056:[], # Indices 96896 to 96912
6057:[], # Indices 96912 to 96928
6058:[], # Indices 96928 to 96944
6059:[], # Indices 96944 to 96960
6060:[], # Indices 96960 to 96976
6061:[], # Indices 96976 to 96992
6062:[], # Indices 96992 to 97008
6063:[], # Indices 97008 to 97024
6064:[], # Indices 97024 to 97040
6065:[], # Indices 97040 to 97056
6066:[], # Indices 97056 to 97072
6067:[], # Indices 97072 to 97088
6068:[], # Indices 97088 to 97104
6069:[], # Indices 97104 to 97120
6070:[], # Indices 97120 to 97136
6071:[], # Indices 97136 to 97152
6072:[], # Indices 97152 to 97168
6073:[], # Indices 97168 to 97184
6074:[], # Indices 97184 to 97200
6075:[{'index_dec': 5, 'index_bin': '0101', 'val': 5, 'counts': 98}], # Indices 97200 to 97216
6076:[], # Indices 97216 to 97232
6077:[], # Indices 97232 to 97248
6078:[], # Indices 97248 to 97264
6079:[], # Indices 97264 to 97280
6080:[], # Indices 97280 to 97296
6081:[], # Indices 97296 to 97312
6082:[], # Indices 97312 to 97328
6083:[], # Indices 97328 to 97344
6084:[], # Indices 97344 to 97360
6085:[], # Indices 97360 to 97376
6086:[], # Indices 97376 to 97392
6087:[], # Indices 97392 to 97408
6088:[], # Indices 97408 to 97424
6089:[], # Indices 97424 to 97440
6090:[], # Indices 97440 to 97456
6091:[], # Indices 97456 to 97472
6092:[], # Indices 97472 to 97488
6093:[], # Indices 97488 to 97504
6094:[], # Indices 97504 to 97520
6095:[], # Indices 97520 to 97536
6096:[], # Indices 97536 to 97552
6097:[], # Indices 97552 to 97568
6098:[], # Indices 97568 to 97584
6099:[], # Indices 97584 to 97600
6100:[], # Indices 97600 to 97616
6101:[], # Indices 97616 to 97632
6102:[], # Indices 97632 to 97648
6103:[], # Indices 97648 to 97664
6104:[], # Indices 97664 to 97680
6105:[], # Indices 97680 to 97696
6106:[], # Indices 97696 to 97712
6107:[], # Indices 97712 to 97728
6108:[], # Indices 97728 to 97744
6109:[], # Indices 97744 to 97760
6110:[], # Indices 97760 to 97776
6111:[], # Indices 97776 to 97792
6112:[], # Indices 97792 to 97808
6113:[], # Indices 97808 to 97824
6114:[], # Indices 97824 to 97840
6115:[], # Indices 97840 to 97856
6116:[], # Indices 97856 to 97872
6117:[], # Indices 97872 to 97888
6118:[], # Indices 97888 to 97904
6119:[], # Indices 97904 to 97920
6120:[], # Indices 97920 to 97936
6121:[], # Indices 97936 to 97952
6122:[], # Indices 97952 to 97968
6123:[], # Indices 97968 to 97984
6124:[], # Indices 97984 to 98000
6125:[], # Indices 98000 to 98016
6126:[], # Indices 98016 to 98032
6127:[], # Indices 98032 to 98048
6128:[], # Indices 98048 to 98064
6129:[], # Indices 98064 to 98080
6130:[], # Indices 98080 to 98096
6131:[], # Indices 98096 to 98112
6132:[], # Indices 98112 to 98128
6133:[], # Indices 98128 to 98144
6134:[], # Indices 98144 to 98160
6135:[], # Indices 98160 to 98176
6136:[], # Indices 98176 to 98192
6137:[], # Indices 98192 to 98208
6138:[], # Indices 98208 to 98224
6139:[], # Indices 98224 to 98240
6140:[], # Indices 98240 to 98256
6141:[], # Indices 98256 to 98272
6142:[], # Indices 98272 to 98288
6143:[], # Indices 98288 to 98304
6144:[], # Indices 98304 to 98320
6145:[], # Indices 98320 to 98336
6146:[], # Indices 98336 to 98352
6147:[], # Indices 98352 to 98368
6148:[], # Indices 98368 to 98384
6149:[], # Indices 98384 to 98400
6150:[], # Indices 98400 to 98416
6151:[], # Indices 98416 to 98432
6152:[], # Indices 98432 to 98448
6153:[], # Indices 98448 to 98464
6154:[], # Indices 98464 to 98480
6155:[], # Indices 98480 to 98496
6156:[], # Indices 98496 to 98512
6157:[], # Indices 98512 to 98528
6158:[], # Indices 98528 to 98544
6159:[], # Indices 98544 to 98560
6160:[], # Indices 98560 to 98576
6161:[], # Indices 98576 to 98592
6162:[], # Indices 98592 to 98608
6163:[], # Indices 98608 to 98624
6164:[], # Indices 98624 to 98640
6165:[], # Indices 98640 to 98656
6166:[], # Indices 98656 to 98672
6167:[], # Indices 98672 to 98688
6168:[], # Indices 98688 to 98704
6169:[], # Indices 98704 to 98720
6170:[], # Indices 98720 to 98736
6171:[], # Indices 98736 to 98752
6172:[], # Indices 98752 to 98768
6173:[], # Indices 98768 to 98784
6174:[], # Indices 98784 to 98800
6175:[], # Indices 98800 to 98816
6176:[], # Indices 98816 to 98832
6177:[], # Indices 98832 to 98848
6178:[], # Indices 98848 to 98864
6179:[], # Indices 98864 to 98880
6180:[], # Indices 98880 to 98896
6181:[], # Indices 98896 to 98912
6182:[], # Indices 98912 to 98928
6183:[], # Indices 98928 to 98944
6184:[], # Indices 98944 to 98960
6185:[], # Indices 98960 to 98976
6186:[], # Indices 98976 to 98992
6187:[{'index_dec': 15, 'index_bin': '1111', 'val': 4, 'counts': 91}], # Indices 98992 to 99008
6188:[], # Indices 99008 to 99024
6189:[], # Indices 99024 to 99040
6190:[], # Indices 99040 to 99056
6191:[], # Indices 99056 to 99072
6192:[], # Indices 99072 to 99088
6193:[], # Indices 99088 to 99104
6194:[], # Indices 99104 to 99120
6195:[], # Indices 99120 to 99136
6196:[], # Indices 99136 to 99152
6197:[], # Indices 99152 to 99168
6198:[], # Indices 99168 to 99184
6199:[], # Indices 99184 to 99200
6200:[], # Indices 99200 to 99216
6201:[], # Indices 99216 to 99232
6202:[], # Indices 99232 to 99248
6203:[], # Indices 99248 to 99264
6204:[], # Indices 99264 to 99280
6205:[], # Indices 99280 to 99296
6206:[], # Indices 99296 to 99312
6207:[], # Indices 99312 to 99328
6208:[], # Indices 99328 to 99344
6209:[], # Indices 99344 to 99360
6210:[], # Indices 99360 to 99376
6211:[], # Indices 99376 to 99392
6212:[], # Indices 99392 to 99408
6213:[], # Indices 99408 to 99424
6214:[], # Indices 99424 to 99440
6215:[], # Indices 99440 to 99456
6216:[], # Indices 99456 to 99472
6217:[], # Indices 99472 to 99488
6218:[], # Indices 99488 to 99504
6219:[], # Indices 99504 to 99520
6220:[], # Indices 99520 to 99536
6221:[], # Indices 99536 to 99552
6222:[], # Indices 99552 to 99568
6223:[], # Indices 99568 to 99584
6224:[], # Indices 99584 to 99600
6225:[], # Indices 99600 to 99616
6226:[], # Indices 99616 to 99632
6227:[], # Indices 99632 to 99648
6228:[], # Indices 99648 to 99664
6229:[], # Indices 99664 to 99680
6230:[], # Indices 99680 to 99696
6231:[], # Indices 99696 to 99712
6232:[], # Indices 99712 to 99728
6233:[], # Indices 99728 to 99744
6234:[], # Indices 99744 to 99760
6235:[], # Indices 99760 to 99776
6236:[], # Indices 99776 to 99792
6237:[], # Indices 99792 to 99808
6238:[], # Indices 99808 to 99824
6239:[], # Indices 99824 to 99840
6240:[], # Indices 99840 to 99856
6241:[], # Indices 99856 to 99872
6242:[], # Indices 99872 to 99888
6243:[], # Indices 99888 to 99904
6244:[], # Indices 99904 to 99920
6245:[], # Indices 99920 to 99936
6246:[], # Indices 99936 to 99952
6247:[], # Indices 99952 to 99968
6248:[], # Indices 99968 to 99984
6249:[], # Indices 99984 to 100000
6250:[], # Indices 100000 to 100016
6251:[], # Indices 100016 to 100032
6252:[], # Indices 100032 to 100048
6253:[], # Indices 100048 to 100064
6254:[], # Indices 100064 to 100080
6255:[], # Indices 100080 to 100096
6256:[], # Indices 100096 to 100112
6257:[], # Indices 100112 to 100128
6258:[], # Indices 100128 to 100144
6259:[], # Indices 100144 to 100160
6260:[], # Indices 100160 to 100176
6261:[], # Indices 100176 to 100192
6262:[], # Indices 100192 to 100208
6263:[], # Indices 100208 to 100224
6264:[], # Indices 100224 to 100240
6265:[], # Indices 100240 to 100256
6266:[], # Indices 100256 to 100272
6267:[], # Indices 100272 to 100288
6268:[], # Indices 100288 to 100304
6269:[], # Indices 100304 to 100320
6270:[], # Indices 100320 to 100336
6271:[], # Indices 100336 to 100352
6272:[], # Indices 100352 to 100368
6273:[], # Indices 100368 to 100384
6274:[], # Indices 100384 to 100400
6275:[], # Indices 100400 to 100416
6276:[], # Indices 100416 to 100432
6277:[], # Indices 100432 to 100448
6278:[], # Indices 100448 to 100464
6279:[], # Indices 100464 to 100480
6280:[], # Indices 100480 to 100496
6281:[], # Indices 100496 to 100512
6282:[], # Indices 100512 to 100528
6283:[], # Indices 100528 to 100544
6284:[], # Indices 100544 to 100560
6285:[], # Indices 100560 to 100576
6286:[], # Indices 100576 to 100592
6287:[], # Indices 100592 to 100608
6288:[], # Indices 100608 to 100624
6289:[], # Indices 100624 to 100640
6290:[], # Indices 100640 to 100656
6291:[], # Indices 100656 to 100672
6292:[], # Indices 100672 to 100688
6293:[], # Indices 100688 to 100704
6294:[], # Indices 100704 to 100720
6295:[], # Indices 100720 to 100736
6296:[], # Indices 100736 to 100752
6297:[], # Indices 100752 to 100768
6298:[], # Indices 100768 to 100784
6299:[], # Indices 100784 to 100800
6300:[{'index_dec': 11, 'index_bin': '1011', 'val': 5, 'counts': 91}], # Indices 100800 to 100816
6301:[], # Indices 100816 to 100832
6302:[], # Indices 100832 to 100848
6303:[], # Indices 100848 to 100864
6304:[], # Indices 100864 to 100880
6305:[], # Indices 100880 to 100896
6306:[], # Indices 100896 to 100912
6307:[], # Indices 100912 to 100928
6308:[], # Indices 100928 to 100944
6309:[], # Indices 100944 to 100960
6310:[], # Indices 100960 to 100976
6311:[], # Indices 100976 to 100992
6312:[], # Indices 100992 to 101008
6313:[], # Indices 101008 to 101024
6314:[], # Indices 101024 to 101040
6315:[], # Indices 101040 to 101056
6316:[], # Indices 101056 to 101072
6317:[], # Indices 101072 to 101088
6318:[], # Indices 101088 to 101104
6319:[], # Indices 101104 to 101120
6320:[], # Indices 101120 to 101136
6321:[], # Indices 101136 to 101152
6322:[], # Indices 101152 to 101168
6323:[], # Indices 101168 to 101184
6324:[], # Indices 101184 to 101200
6325:[], # Indices 101200 to 101216
6326:[], # Indices 101216 to 101232
6327:[], # Indices 101232 to 101248
6328:[], # Indices 101248 to 101264
6329:[], # Indices 101264 to 101280
6330:[], # Indices 101280 to 101296
6331:[], # Indices 101296 to 101312
6332:[], # Indices 101312 to 101328
6333:[], # Indices 101328 to 101344
6334:[], # Indices 101344 to 101360
6335:[], # Indices 101360 to 101376
6336:[], # Indices 101376 to 101392
6337:[], # Indices 101392 to 101408
6338:[], # Indices 101408 to 101424
6339:[], # Indices 101424 to 101440
6340:[], # Indices 101440 to 101456
6341:[], # Indices 101456 to 101472
6342:[], # Indices 101472 to 101488
6343:[], # Indices 101488 to 101504
6344:[], # Indices 101504 to 101520
6345:[], # Indices 101520 to 101536
6346:[], # Indices 101536 to 101552
6347:[], # Indices 101552 to 101568
6348:[], # Indices 101568 to 101584
6349:[], # Indices 101584 to 101600
6350:[], # Indices 101600 to 101616
6351:[], # Indices 101616 to 101632
6352:[], # Indices 101632 to 101648
6353:[], # Indices 101648 to 101664
6354:[], # Indices 101664 to 101680
6355:[], # Indices 101680 to 101696
6356:[], # Indices 101696 to 101712
6357:[], # Indices 101712 to 101728
6358:[], # Indices 101728 to 101744
6359:[], # Indices 101744 to 101760
6360:[], # Indices 101760 to 101776
6361:[], # Indices 101776 to 101792
6362:[], # Indices 101792 to 101808
6363:[], # Indices 101808 to 101824
6364:[], # Indices 101824 to 101840
6365:[], # Indices 101840 to 101856
6366:[], # Indices 101856 to 101872
6367:[], # Indices 101872 to 101888
6368:[], # Indices 101888 to 101904
6369:[], # Indices 101904 to 101920
6370:[], # Indices 101920 to 101936
6371:[], # Indices 101936 to 101952
6372:[], # Indices 101952 to 101968
6373:[], # Indices 101968 to 101984
6374:[], # Indices 101984 to 102000
6375:[], # Indices 102000 to 102016
6376:[], # Indices 102016 to 102032
6377:[], # Indices 102032 to 102048
6378:[], # Indices 102048 to 102064
6379:[], # Indices 102064 to 102080
6380:[], # Indices 102080 to 102096
6381:[], # Indices 102096 to 102112
6382:[], # Indices 102112 to 102128
6383:[], # Indices 102128 to 102144
6384:[], # Indices 102144 to 102160
6385:[], # Indices 102160 to 102176
6386:[], # Indices 102176 to 102192
6387:[], # Indices 102192 to 102208
6388:[], # Indices 102208 to 102224
6389:[], # Indices 102224 to 102240
6390:[], # Indices 102240 to 102256
6391:[], # Indices 102256 to 102272
6392:[], # Indices 102272 to 102288
6393:[], # Indices 102288 to 102304
6394:[], # Indices 102304 to 102320
6395:[], # Indices 102320 to 102336
6396:[], # Indices 102336 to 102352
6397:[], # Indices 102352 to 102368
6398:[], # Indices 102368 to 102384
6399:[], # Indices 102384 to 102400
6400:[], # Indices 102400 to 102416
6401:[], # Indices 102416 to 102432
6402:[], # Indices 102432 to 102448
6403:[], # Indices 102448 to 102464
6404:[], # Indices 102464 to 102480
6405:[], # Indices 102480 to 102496
6406:[], # Indices 102496 to 102512
6407:[], # Indices 102512 to 102528
6408:[], # Indices 102528 to 102544
6409:[], # Indices 102544 to 102560
6410:[], # Indices 102560 to 102576
6411:[], # Indices 102576 to 102592
6412:[], # Indices 102592 to 102608
6413:[], # Indices 102608 to 102624
6414:[], # Indices 102624 to 102640
6415:[], # Indices 102640 to 102656
6416:[], # Indices 102656 to 102672
6417:[], # Indices 102672 to 102688
6418:[], # Indices 102688 to 102704
6419:[], # Indices 102704 to 102720
6420:[], # Indices 102720 to 102736
6421:[], # Indices 102736 to 102752
6422:[], # Indices 102752 to 102768
6423:[], # Indices 102768 to 102784
6424:[], # Indices 102784 to 102800
6425:[], # Indices 102800 to 102816
6426:[], # Indices 102816 to 102832
6427:[], # Indices 102832 to 102848
6428:[], # Indices 102848 to 102864
6429:[], # Indices 102864 to 102880
6430:[{'index_dec': 8, 'index_bin': '1000', 'val': 5, 'counts': 92}], # Indices 102880 to 102896
6431:[], # Indices 102896 to 102912
6432:[], # Indices 102912 to 102928
6433:[], # Indices 102928 to 102944
6434:[], # Indices 102944 to 102960
6435:[], # Indices 102960 to 102976
6436:[], # Indices 102976 to 102992
6437:[], # Indices 102992 to 103008
6438:[], # Indices 103008 to 103024
6439:[], # Indices 103024 to 103040
6440:[], # Indices 103040 to 103056
6441:[], # Indices 103056 to 103072
6442:[], # Indices 103072 to 103088
6443:[], # Indices 103088 to 103104
6444:[], # Indices 103104 to 103120
6445:[], # Indices 103120 to 103136
6446:[], # Indices 103136 to 103152
6447:[], # Indices 103152 to 103168
6448:[], # Indices 103168 to 103184
6449:[], # Indices 103184 to 103200
6450:[], # Indices 103200 to 103216
6451:[], # Indices 103216 to 103232
6452:[], # Indices 103232 to 103248
6453:[], # Indices 103248 to 103264
6454:[], # Indices 103264 to 103280
6455:[], # Indices 103280 to 103296
6456:[], # Indices 103296 to 103312
6457:[], # Indices 103312 to 103328
6458:[], # Indices 103328 to 103344
6459:[], # Indices 103344 to 103360
6460:[], # Indices 103360 to 103376
6461:[], # Indices 103376 to 103392
6462:[], # Indices 103392 to 103408
6463:[], # Indices 103408 to 103424
6464:[], # Indices 103424 to 103440
6465:[], # Indices 103440 to 103456
6466:[], # Indices 103456 to 103472
6467:[], # Indices 103472 to 103488
6468:[], # Indices 103488 to 103504
6469:[], # Indices 103504 to 103520
6470:[], # Indices 103520 to 103536
6471:[], # Indices 103536 to 103552
6472:[], # Indices 103552 to 103568
6473:[], # Indices 103568 to 103584
6474:[], # Indices 103584 to 103600
6475:[], # Indices 103600 to 103616
6476:[], # Indices 103616 to 103632
6477:[], # Indices 103632 to 103648
6478:[], # Indices 103648 to 103664
6479:[], # Indices 103664 to 103680
6480:[], # Indices 103680 to 103696
6481:[], # Indices 103696 to 103712
6482:[], # Indices 103712 to 103728
6483:[], # Indices 103728 to 103744
6484:[], # Indices 103744 to 103760
6485:[], # Indices 103760 to 103776
6486:[], # Indices 103776 to 103792
6487:[], # Indices 103792 to 103808
6488:[], # Indices 103808 to 103824
6489:[], # Indices 103824 to 103840
6490:[], # Indices 103840 to 103856
6491:[], # Indices 103856 to 103872
6492:[], # Indices 103872 to 103888
6493:[], # Indices 103888 to 103904
6494:[], # Indices 103904 to 103920
6495:[], # Indices 103920 to 103936
6496:[], # Indices 103936 to 103952
6497:[], # Indices 103952 to 103968
6498:[], # Indices 103968 to 103984
6499:[], # Indices 103984 to 104000
6500:[], # Indices 104000 to 104016
6501:[], # Indices 104016 to 104032
6502:[], # Indices 104032 to 104048
6503:[], # Indices 104048 to 104064
6504:[], # Indices 104064 to 104080
6505:[], # Indices 104080 to 104096
6506:[], # Indices 104096 to 104112
6507:[], # Indices 104112 to 104128
6508:[], # Indices 104128 to 104144
6509:[], # Indices 104144 to 104160
6510:[], # Indices 104160 to 104176
6511:[], # Indices 104176 to 104192
6512:[], # Indices 104192 to 104208
6513:[], # Indices 104208 to 104224
6514:[], # Indices 104224 to 104240
6515:[], # Indices 104240 to 104256
6516:[], # Indices 104256 to 104272
6517:[], # Indices 104272 to 104288
6518:[], # Indices 104288 to 104304
6519:[], # Indices 104304 to 104320
6520:[], # Indices 104320 to 104336
6521:[], # Indices 104336 to 104352
6522:[], # Indices 104352 to 104368
6523:[], # Indices 104368 to 104384
6524:[], # Indices 104384 to 104400
6525:[{'index_dec': 10, 'index_bin': '1010', 'val': 4, 'counts': 91}], # Indices 104400 to 104416
6526:[], # Indices 104416 to 104432
6527:[], # Indices 104432 to 104448
6528:[], # Indices 104448 to 104464
6529:[], # Indices 104464 to 104480
6530:[], # Indices 104480 to 104496
6531:[], # Indices 104496 to 104512
6532:[], # Indices 104512 to 104528
6533:[], # Indices 104528 to 104544
6534:[], # Indices 104544 to 104560
6535:[], # Indices 104560 to 104576
6536:[{'index_dec': 15, 'index_bin': '1111', 'val': 5, 'counts': 95}], # Indices 104576 to 104592
6537:[], # Indices 104592 to 104608
6538:[], # Indices 104608 to 104624
6539:[], # Indices 104624 to 104640
6540:[], # Indices 104640 to 104656
6541:[], # Indices 104656 to 104672
6542:[], # Indices 104672 to 104688
6543:[], # Indices 104688 to 104704
6544:[], # Indices 104704 to 104720
6545:[], # Indices 104720 to 104736
6546:[], # Indices 104736 to 104752
6547:[], # Indices 104752 to 104768
6548:[], # Indices 104768 to 104784
6549:[], # Indices 104784 to 104800
6550:[], # Indices 104800 to 104816
6551:[], # Indices 104816 to 104832
6552:[], # Indices 104832 to 104848
6553:[], # Indices 104848 to 104864
6554:[], # Indices 104864 to 104880
6555:[], # Indices 104880 to 104896
6556:[], # Indices 104896 to 104912
6557:[], # Indices 104912 to 104928
6558:[], # Indices 104928 to 104944
6559:[], # Indices 104944 to 104960
6560:[], # Indices 104960 to 104976
6561:[], # Indices 104976 to 104992
6562:[], # Indices 104992 to 105008
6563:[{'index_dec': 10, 'index_bin': '1010', 'val': 5, 'counts': 91}], # Indices 105008 to 105024
6564:[], # Indices 105024 to 105040
6565:[], # Indices 105040 to 105056
6566:[], # Indices 105056 to 105072
6567:[], # Indices 105072 to 105088
6568:[], # Indices 105088 to 105104
6569:[], # Indices 105104 to 105120
6570:[], # Indices 105120 to 105136
6571:[], # Indices 105136 to 105152
6572:[{'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 95}], # Indices 105152 to 105168
6573:[], # Indices 105168 to 105184
6574:[], # Indices 105184 to 105200
6575:[], # Indices 105200 to 105216
6576:[], # Indices 105216 to 105232
6577:[], # Indices 105232 to 105248
6578:[], # Indices 105248 to 105264
6579:[], # Indices 105264 to 105280
6580:[], # Indices 105280 to 105296
6581:[], # Indices 105296 to 105312
6582:[], # Indices 105312 to 105328
6583:[], # Indices 105328 to 105344
6584:[], # Indices 105344 to 105360
6585:[], # Indices 105360 to 105376
6586:[], # Indices 105376 to 105392
6587:[], # Indices 105392 to 105408
6588:[], # Indices 105408 to 105424
6589:[], # Indices 105424 to 105440
6590:[], # Indices 105440 to 105456
6591:[], # Indices 105456 to 105472
6592:[], # Indices 105472 to 105488
6593:[], # Indices 105488 to 105504
6594:[], # Indices 105504 to 105520
6595:[], # Indices 105520 to 105536
6596:[], # Indices 105536 to 105552
6597:[], # Indices 105552 to 105568
6598:[], # Indices 105568 to 105584
6599:[], # Indices 105584 to 105600
6600:[], # Indices 105600 to 105616
6601:[], # Indices 105616 to 105632
6602:[], # Indices 105632 to 105648
6603:[], # Indices 105648 to 105664
6604:[], # Indices 105664 to 105680
6605:[], # Indices 105680 to 105696
6606:[], # Indices 105696 to 105712
6607:[], # Indices 105712 to 105728
6608:[], # Indices 105728 to 105744
6609:[], # Indices 105744 to 105760
6610:[], # Indices 105760 to 105776
6611:[], # Indices 105776 to 105792
6612:[], # Indices 105792 to 105808
6613:[], # Indices 105808 to 105824
6614:[], # Indices 105824 to 105840
6615:[], # Indices 105840 to 105856
6616:[], # Indices 105856 to 105872
6617:[], # Indices 105872 to 105888
6618:[], # Indices 105888 to 105904
6619:[], # Indices 105904 to 105920
6620:[], # Indices 105920 to 105936
6621:[], # Indices 105936 to 105952
6622:[], # Indices 105952 to 105968
6623:[], # Indices 105968 to 105984
6624:[], # Indices 105984 to 106000
6625:[], # Indices 106000 to 106016
6626:[], # Indices 106016 to 106032
6627:[], # Indices 106032 to 106048
6628:[], # Indices 106048 to 106064
6629:[], # Indices 106064 to 106080
6630:[], # Indices 106080 to 106096
6631:[], # Indices 106096 to 106112
6632:[], # Indices 106112 to 106128
6633:[], # Indices 106128 to 106144
6634:[], # Indices 106144 to 106160
6635:[], # Indices 106160 to 106176
6636:[], # Indices 106176 to 106192
6637:[], # Indices 106192 to 106208
6638:[], # Indices 106208 to 106224
6639:[], # Indices 106224 to 106240
6640:[], # Indices 106240 to 106256
6641:[], # Indices 106256 to 106272
6642:[], # Indices 106272 to 106288
6643:[], # Indices 106288 to 106304
6644:[], # Indices 106304 to 106320
6645:[], # Indices 106320 to 106336
6646:[{'index_dec': 10, 'index_bin': '1010', 'val': 4, 'counts': 96}], # Indices 106336 to 106352
6647:[], # Indices 106352 to 106368
6648:[], # Indices 106368 to 106384
6649:[], # Indices 106384 to 106400
6650:[], # Indices 106400 to 106416
6651:[], # Indices 106416 to 106432
6652:[], # Indices 106432 to 106448
6653:[], # Indices 106448 to 106464
6654:[], # Indices 106464 to 106480
6655:[], # Indices 106480 to 106496
6656:[], # Indices 106496 to 106512
6657:[], # Indices 106512 to 106528
6658:[], # Indices 106528 to 106544
6659:[], # Indices 106544 to 106560
6660:[], # Indices 106560 to 106576
6661:[], # Indices 106576 to 106592
6662:[], # Indices 106592 to 106608
6663:[], # Indices 106608 to 106624
6664:[], # Indices 106624 to 106640
6665:[], # Indices 106640 to 106656
6666:[], # Indices 106656 to 106672
6667:[], # Indices 106672 to 106688
6668:[], # Indices 106688 to 106704
6669:[], # Indices 106704 to 106720
6670:[], # Indices 106720 to 106736
6671:[], # Indices 106736 to 106752
6672:[], # Indices 106752 to 106768
6673:[], # Indices 106768 to 106784
6674:[], # Indices 106784 to 106800
6675:[], # Indices 106800 to 106816
6676:[], # Indices 106816 to 106832
6677:[], # Indices 106832 to 106848
6678:[], # Indices 106848 to 106864
6679:[], # Indices 106864 to 106880
6680:[], # Indices 106880 to 106896
6681:[], # Indices 106896 to 106912
6682:[], # Indices 106912 to 106928
6683:[], # Indices 106928 to 106944
6684:[], # Indices 106944 to 106960
6685:[], # Indices 106960 to 106976
6686:[], # Indices 106976 to 106992
6687:[], # Indices 106992 to 107008
6688:[], # Indices 107008 to 107024
6689:[], # Indices 107024 to 107040
6690:[], # Indices 107040 to 107056
6691:[], # Indices 107056 to 107072
6692:[], # Indices 107072 to 107088
6693:[], # Indices 107088 to 107104
6694:[], # Indices 107104 to 107120
6695:[], # Indices 107120 to 107136
6696:[], # Indices 107136 to 107152
6697:[], # Indices 107152 to 107168
6698:[], # Indices 107168 to 107184
6699:[], # Indices 107184 to 107200
6700:[], # Indices 107200 to 107216
6701:[], # Indices 107216 to 107232
6702:[], # Indices 107232 to 107248
6703:[], # Indices 107248 to 107264
6704:[], # Indices 107264 to 107280
6705:[], # Indices 107280 to 107296
6706:[{'index_dec': 9, 'index_bin': '1001', 'val': 5, 'counts': 92}], # Indices 107296 to 107312
6707:[], # Indices 107312 to 107328
6708:[], # Indices 107328 to 107344
6709:[], # Indices 107344 to 107360
6710:[], # Indices 107360 to 107376
6711:[], # Indices 107376 to 107392
6712:[], # Indices 107392 to 107408
6713:[], # Indices 107408 to 107424
6714:[], # Indices 107424 to 107440
6715:[], # Indices 107440 to 107456
6716:[], # Indices 107456 to 107472
6717:[], # Indices 107472 to 107488
6718:[], # Indices 107488 to 107504
6719:[], # Indices 107504 to 107520
6720:[], # Indices 107520 to 107536
6721:[], # Indices 107536 to 107552
6722:[], # Indices 107552 to 107568
6723:[], # Indices 107568 to 107584
6724:[], # Indices 107584 to 107600
6725:[], # Indices 107600 to 107616
6726:[], # Indices 107616 to 107632
6727:[], # Indices 107632 to 107648
6728:[], # Indices 107648 to 107664
6729:[], # Indices 107664 to 107680
6730:[], # Indices 107680 to 107696
6731:[], # Indices 107696 to 107712
6732:[], # Indices 107712 to 107728
6733:[], # Indices 107728 to 107744
6734:[], # Indices 107744 to 107760
6735:[], # Indices 107760 to 107776
6736:[], # Indices 107776 to 107792
6737:[], # Indices 107792 to 107808
6738:[], # Indices 107808 to 107824
6739:[], # Indices 107824 to 107840
6740:[], # Indices 107840 to 107856
6741:[{'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 92}], # Indices 107856 to 107872
6742:[], # Indices 107872 to 107888
6743:[], # Indices 107888 to 107904
6744:[], # Indices 107904 to 107920
6745:[], # Indices 107920 to 107936
6746:[], # Indices 107936 to 107952
6747:[], # Indices 107952 to 107968
6748:[], # Indices 107968 to 107984
6749:[], # Indices 107984 to 108000
6750:[], # Indices 108000 to 108016
6751:[], # Indices 108016 to 108032
6752:[], # Indices 108032 to 108048
6753:[{'index_dec': 6, 'index_bin': '0110', 'val': 5, 'counts': 93}], # Indices 108048 to 108064
6754:[], # Indices 108064 to 108080
6755:[], # Indices 108080 to 108096
6756:[], # Indices 108096 to 108112
6757:[], # Indices 108112 to 108128
6758:[], # Indices 108128 to 108144
6759:[], # Indices 108144 to 108160
6760:[], # Indices 108160 to 108176
6761:[], # Indices 108176 to 108192
6762:[], # Indices 108192 to 108208
6763:[], # Indices 108208 to 108224
6764:[], # Indices 108224 to 108240
6765:[], # Indices 108240 to 108256
6766:[], # Indices 108256 to 108272
6767:[], # Indices 108272 to 108288
6768:[], # Indices 108288 to 108304
6769:[], # Indices 108304 to 108320
6770:[], # Indices 108320 to 108336
6771:[], # Indices 108336 to 108352
6772:[], # Indices 108352 to 108368
6773:[], # Indices 108368 to 108384
6774:[], # Indices 108384 to 108400
6775:[], # Indices 108400 to 108416
6776:[], # Indices 108416 to 108432
6777:[], # Indices 108432 to 108448
6778:[], # Indices 108448 to 108464
6779:[], # Indices 108464 to 108480
6780:[], # Indices 108480 to 108496
6781:[], # Indices 108496 to 108512
6782:[], # Indices 108512 to 108528
6783:[], # Indices 108528 to 108544
6784:[], # Indices 108544 to 108560
6785:[], # Indices 108560 to 108576
6786:[], # Indices 108576 to 108592
6787:[], # Indices 108592 to 108608
6788:[], # Indices 108608 to 108624
6789:[], # Indices 108624 to 108640
6790:[], # Indices 108640 to 108656
6791:[], # Indices 108656 to 108672
6792:[], # Indices 108672 to 108688
6793:[], # Indices 108688 to 108704
6794:[], # Indices 108704 to 108720
6795:[], # Indices 108720 to 108736
6796:[], # Indices 108736 to 108752
6797:[], # Indices 108752 to 108768
6798:[], # Indices 108768 to 108784
6799:[], # Indices 108784 to 108800
6800:[], # Indices 108800 to 108816
6801:[], # Indices 108816 to 108832
6802:[], # Indices 108832 to 108848
6803:[], # Indices 108848 to 108864
6804:[], # Indices 108864 to 108880
6805:[], # Indices 108880 to 108896
6806:[], # Indices 108896 to 108912
6807:[], # Indices 108912 to 108928
6808:[], # Indices 108928 to 108944
6809:[], # Indices 108944 to 108960
6810:[], # Indices 108960 to 108976
6811:[], # Indices 108976 to 108992
6812:[], # Indices 108992 to 109008
6813:[], # Indices 109008 to 109024
6814:[], # Indices 109024 to 109040
6815:[], # Indices 109040 to 109056
6816:[], # Indices 109056 to 109072
6817:[], # Indices 109072 to 109088
6818:[], # Indices 109088 to 109104
6819:[], # Indices 109104 to 109120
6820:[], # Indices 109120 to 109136
6821:[], # Indices 109136 to 109152
6822:[], # Indices 109152 to 109168
6823:[], # Indices 109168 to 109184
6824:[], # Indices 109184 to 109200
6825:[], # Indices 109200 to 109216
6826:[], # Indices 109216 to 109232
6827:[], # Indices 109232 to 109248
6828:[], # Indices 109248 to 109264
6829:[], # Indices 109264 to 109280
6830:[], # Indices 109280 to 109296
6831:[], # Indices 109296 to 109312
6832:[], # Indices 109312 to 109328
6833:[], # Indices 109328 to 109344
6834:[], # Indices 109344 to 109360
6835:[], # Indices 109360 to 109376
6836:[], # Indices 109376 to 109392
6837:[], # Indices 109392 to 109408
6838:[], # Indices 109408 to 109424
6839:[], # Indices 109424 to 109440
6840:[], # Indices 109440 to 109456
6841:[], # Indices 109456 to 109472
6842:[], # Indices 109472 to 109488
6843:[], # Indices 109488 to 109504
6844:[], # Indices 109504 to 109520
6845:[], # Indices 109520 to 109536
6846:[], # Indices 109536 to 109552
6847:[], # Indices 109552 to 109568
6848:[], # Indices 109568 to 109584
6849:[], # Indices 109584 to 109600
6850:[], # Indices 109600 to 109616
6851:[], # Indices 109616 to 109632
6852:[], # Indices 109632 to 109648
6853:[], # Indices 109648 to 109664
6854:[], # Indices 109664 to 109680
6855:[], # Indices 109680 to 109696
6856:[], # Indices 109696 to 109712
6857:[], # Indices 109712 to 109728
6858:[], # Indices 109728 to 109744
6859:[], # Indices 109744 to 109760
6860:[], # Indices 109760 to 109776
6861:[], # Indices 109776 to 109792
6862:[], # Indices 109792 to 109808
6863:[], # Indices 109808 to 109824
6864:[], # Indices 109824 to 109840
6865:[], # Indices 109840 to 109856
6866:[], # Indices 109856 to 109872
6867:[], # Indices 109872 to 109888
6868:[], # Indices 109888 to 109904
6869:[], # Indices 109904 to 109920
6870:[], # Indices 109920 to 109936
6871:[], # Indices 109936 to 109952
6872:[], # Indices 109952 to 109968
6873:[], # Indices 109968 to 109984
6874:[], # Indices 109984 to 110000
6875:[], # Indices 110000 to 110016
6876:[], # Indices 110016 to 110032
6877:[], # Indices 110032 to 110048
6878:[], # Indices 110048 to 110064
6879:[], # Indices 110064 to 110080
6880:[], # Indices 110080 to 110096
6881:[], # Indices 110096 to 110112
6882:[], # Indices 110112 to 110128
6883:[], # Indices 110128 to 110144
6884:[], # Indices 110144 to 110160
6885:[], # Indices 110160 to 110176
6886:[], # Indices 110176 to 110192
6887:[], # Indices 110192 to 110208
6888:[], # Indices 110208 to 110224
6889:[], # Indices 110224 to 110240
6890:[], # Indices 110240 to 110256
6891:[], # Indices 110256 to 110272
6892:[], # Indices 110272 to 110288
6893:[], # Indices 110288 to 110304
6894:[], # Indices 110304 to 110320
6895:[], # Indices 110320 to 110336
6896:[], # Indices 110336 to 110352
6897:[], # Indices 110352 to 110368
6898:[], # Indices 110368 to 110384
6899:[], # Indices 110384 to 110400
6900:[], # Indices 110400 to 110416
6901:[], # Indices 110416 to 110432
6902:[], # Indices 110432 to 110448
6903:[], # Indices 110448 to 110464
6904:[], # Indices 110464 to 110480
6905:[], # Indices 110480 to 110496
6906:[], # Indices 110496 to 110512
6907:[], # Indices 110512 to 110528
6908:[], # Indices 110528 to 110544
6909:[], # Indices 110544 to 110560
6910:[], # Indices 110560 to 110576
6911:[], # Indices 110576 to 110592
6912:[], # Indices 110592 to 110608
6913:[], # Indices 110608 to 110624
6914:[], # Indices 110624 to 110640
6915:[], # Indices 110640 to 110656
6916:[], # Indices 110656 to 110672
6917:[], # Indices 110672 to 110688
6918:[], # Indices 110688 to 110704
6919:[], # Indices 110704 to 110720
6920:[], # Indices 110720 to 110736
6921:[], # Indices 110736 to 110752
6922:[], # Indices 110752 to 110768
6923:[], # Indices 110768 to 110784
6924:[], # Indices 110784 to 110800
6925:[], # Indices 110800 to 110816
6926:[], # Indices 110816 to 110832
6927:[], # Indices 110832 to 110848
6928:[], # Indices 110848 to 110864
6929:[], # Indices 110864 to 110880
6930:[], # Indices 110880 to 110896
6931:[], # Indices 110896 to 110912
6932:[], # Indices 110912 to 110928
6933:[], # Indices 110928 to 110944
6934:[], # Indices 110944 to 110960
6935:[], # Indices 110960 to 110976
6936:[], # Indices 110976 to 110992
6937:[], # Indices 110992 to 111008
6938:[], # Indices 111008 to 111024
6939:[], # Indices 111024 to 111040
6940:[], # Indices 111040 to 111056
6941:[], # Indices 111056 to 111072
6942:[], # Indices 111072 to 111088
6943:[], # Indices 111088 to 111104
6944:[], # Indices 111104 to 111120
6945:[], # Indices 111120 to 111136
6946:[], # Indices 111136 to 111152
6947:[], # Indices 111152 to 111168
6948:[], # Indices 111168 to 111184
6949:[], # Indices 111184 to 111200
6950:[], # Indices 111200 to 111216
6951:[], # Indices 111216 to 111232
6952:[], # Indices 111232 to 111248
6953:[], # Indices 111248 to 111264
6954:[], # Indices 111264 to 111280
6955:[], # Indices 111280 to 111296
6956:[], # Indices 111296 to 111312
6957:[], # Indices 111312 to 111328
6958:[], # Indices 111328 to 111344
6959:[], # Indices 111344 to 111360
6960:[], # Indices 111360 to 111376
6961:[], # Indices 111376 to 111392
6962:[], # Indices 111392 to 111408
6963:[], # Indices 111408 to 111424
6964:[], # Indices 111424 to 111440
6965:[], # Indices 111440 to 111456
6966:[], # Indices 111456 to 111472
6967:[], # Indices 111472 to 111488
6968:[], # Indices 111488 to 111504
6969:[], # Indices 111504 to 111520
6970:[], # Indices 111520 to 111536
6971:[], # Indices 111536 to 111552
6972:[], # Indices 111552 to 111568
6973:[], # Indices 111568 to 111584
6974:[], # Indices 111584 to 111600
6975:[], # Indices 111600 to 111616
6976:[], # Indices 111616 to 111632
6977:[], # Indices 111632 to 111648
6978:[], # Indices 111648 to 111664
6979:[], # Indices 111664 to 111680
6980:[], # Indices 111680 to 111696
6981:[], # Indices 111696 to 111712
6982:[], # Indices 111712 to 111728
6983:[], # Indices 111728 to 111744
6984:[], # Indices 111744 to 111760
6985:[], # Indices 111760 to 111776
6986:[], # Indices 111776 to 111792
6987:[], # Indices 111792 to 111808
6988:[], # Indices 111808 to 111824
6989:[], # Indices 111824 to 111840
6990:[], # Indices 111840 to 111856
6991:[], # Indices 111856 to 111872
6992:[], # Indices 111872 to 111888
6993:[], # Indices 111888 to 111904
6994:[], # Indices 111904 to 111920
6995:[], # Indices 111920 to 111936
6996:[], # Indices 111936 to 111952
6997:[], # Indices 111952 to 111968
6998:[], # Indices 111968 to 111984
6999:[], # Indices 111984 to 112000
7000:[], # Indices 112000 to 112016
7001:[], # Indices 112016 to 112032
7002:[], # Indices 112032 to 112048
7003:[], # Indices 112048 to 112064
7004:[], # Indices 112064 to 112080
7005:[], # Indices 112080 to 112096
7006:[], # Indices 112096 to 112112
7007:[], # Indices 112112 to 112128
7008:[], # Indices 112128 to 112144
7009:[], # Indices 112144 to 112160
7010:[], # Indices 112160 to 112176
7011:[], # Indices 112176 to 112192
7012:[], # Indices 112192 to 112208
7013:[], # Indices 112208 to 112224
7014:[], # Indices 112224 to 112240
7015:[], # Indices 112240 to 112256
7016:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 474}], # Indices 112256 to 112272
7017:[], # Indices 112272 to 112288
7018:[{'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 91}], # Indices 112288 to 112304
7019:[], # Indices 112304 to 112320
7020:[], # Indices 112320 to 112336
7021:[], # Indices 112336 to 112352
7022:[], # Indices 112352 to 112368
7023:[], # Indices 112368 to 112384
7024:[], # Indices 112384 to 112400
7025:[], # Indices 112400 to 112416
7026:[], # Indices 112416 to 112432
7027:[], # Indices 112432 to 112448
7028:[], # Indices 112448 to 112464
7029:[], # Indices 112464 to 112480
7030:[], # Indices 112480 to 112496
7031:[], # Indices 112496 to 112512
7032:[], # Indices 112512 to 112528
7033:[], # Indices 112528 to 112544
7034:[], # Indices 112544 to 112560
7035:[], # Indices 112560 to 112576
7036:[], # Indices 112576 to 112592
7037:[], # Indices 112592 to 112608
7038:[], # Indices 112608 to 112624
7039:[], # Indices 112624 to 112640
7040:[], # Indices 112640 to 112656
7041:[], # Indices 112656 to 112672
7042:[], # Indices 112672 to 112688
7043:[], # Indices 112688 to 112704
7044:[], # Indices 112704 to 112720
7045:[], # Indices 112720 to 112736
7046:[], # Indices 112736 to 112752
7047:[{'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 91}], # Indices 112752 to 112768
7048:[], # Indices 112768 to 112784
7049:[], # Indices 112784 to 112800
7050:[], # Indices 112800 to 112816
7051:[], # Indices 112816 to 112832
7052:[], # Indices 112832 to 112848
7053:[], # Indices 112848 to 112864
7054:[], # Indices 112864 to 112880
7055:[], # Indices 112880 to 112896
7056:[], # Indices 112896 to 112912
7057:[], # Indices 112912 to 112928
7058:[], # Indices 112928 to 112944
7059:[], # Indices 112944 to 112960
7060:[], # Indices 112960 to 112976
7061:[], # Indices 112976 to 112992
7062:[], # Indices 112992 to 113008
7063:[], # Indices 113008 to 113024
7064:[], # Indices 113024 to 113040
7065:[], # Indices 113040 to 113056
7066:[], # Indices 113056 to 113072
7067:[], # Indices 113072 to 113088
7068:[], # Indices 113088 to 113104
7069:[], # Indices 113104 to 113120
7070:[], # Indices 113120 to 113136
7071:[], # Indices 113136 to 113152
7072:[], # Indices 113152 to 113168
7073:[], # Indices 113168 to 113184
7074:[], # Indices 113184 to 113200
7075:[], # Indices 113200 to 113216
7076:[], # Indices 113216 to 113232
7077:[], # Indices 113232 to 113248
7078:[], # Indices 113248 to 113264
7079:[], # Indices 113264 to 113280
7080:[], # Indices 113280 to 113296
7081:[], # Indices 113296 to 113312
7082:[], # Indices 113312 to 113328
7083:[], # Indices 113328 to 113344
7084:[], # Indices 113344 to 113360
7085:[], # Indices 113360 to 113376
7086:[], # Indices 113376 to 113392
7087:[], # Indices 113392 to 113408
7088:[], # Indices 113408 to 113424
7089:[], # Indices 113424 to 113440
7090:[], # Indices 113440 to 113456
7091:[], # Indices 113456 to 113472
7092:[], # Indices 113472 to 113488
7093:[], # Indices 113488 to 113504
7094:[], # Indices 113504 to 113520
7095:[], # Indices 113520 to 113536
7096:[], # Indices 113536 to 113552
7097:[], # Indices 113552 to 113568
7098:[], # Indices 113568 to 113584
7099:[], # Indices 113584 to 113600
7100:[], # Indices 113600 to 113616
7101:[], # Indices 113616 to 113632
7102:[], # Indices 113632 to 113648
7103:[], # Indices 113648 to 113664
7104:[], # Indices 113664 to 113680
7105:[], # Indices 113680 to 113696
7106:[], # Indices 113696 to 113712
7107:[], # Indices 113712 to 113728
7108:[], # Indices 113728 to 113744
7109:[], # Indices 113744 to 113760
7110:[], # Indices 113760 to 113776
7111:[], # Indices 113776 to 113792
7112:[], # Indices 113792 to 113808
7113:[], # Indices 113808 to 113824
7114:[], # Indices 113824 to 113840
7115:[], # Indices 113840 to 113856
7116:[], # Indices 113856 to 113872
7117:[], # Indices 113872 to 113888
7118:[], # Indices 113888 to 113904
7119:[], # Indices 113904 to 113920
7120:[], # Indices 113920 to 113936
7121:[], # Indices 113936 to 113952
7122:[], # Indices 113952 to 113968
7123:[], # Indices 113968 to 113984
7124:[], # Indices 113984 to 114000
7125:[], # Indices 114000 to 114016
7126:[], # Indices 114016 to 114032
7127:[], # Indices 114032 to 114048
7128:[{'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 91}], # Indices 114048 to 114064
7129:[], # Indices 114064 to 114080
7130:[], # Indices 114080 to 114096
7131:[], # Indices 114096 to 114112
7132:[], # Indices 114112 to 114128
7133:[], # Indices 114128 to 114144
7134:[], # Indices 114144 to 114160
7135:[], # Indices 114160 to 114176
7136:[], # Indices 114176 to 114192
7137:[], # Indices 114192 to 114208
7138:[], # Indices 114208 to 114224
7139:[], # Indices 114224 to 114240
7140:[], # Indices 114240 to 114256
7141:[], # Indices 114256 to 114272
7142:[], # Indices 114272 to 114288
7143:[], # Indices 114288 to 114304
7144:[], # Indices 114304 to 114320
7145:[], # Indices 114320 to 114336
7146:[], # Indices 114336 to 114352
7147:[], # Indices 114352 to 114368
7148:[], # Indices 114368 to 114384
7149:[], # Indices 114384 to 114400
7150:[], # Indices 114400 to 114416
7151:[], # Indices 114416 to 114432
7152:[], # Indices 114432 to 114448
7153:[], # Indices 114448 to 114464
7154:[], # Indices 114464 to 114480
7155:[], # Indices 114480 to 114496
7156:[], # Indices 114496 to 114512
7157:[], # Indices 114512 to 114528
7158:[], # Indices 114528 to 114544
7159:[], # Indices 114544 to 114560
7160:[], # Indices 114560 to 114576
7161:[], # Indices 114576 to 114592
7162:[], # Indices 114592 to 114608
7163:[], # Indices 114608 to 114624
7164:[], # Indices 114624 to 114640
7165:[], # Indices 114640 to 114656
7166:[], # Indices 114656 to 114672
7167:[], # Indices 114672 to 114688
7168:[], # Indices 114688 to 114704
7169:[], # Indices 114704 to 114720
7170:[], # Indices 114720 to 114736
7171:[], # Indices 114736 to 114752
7172:[], # Indices 114752 to 114768
7173:[], # Indices 114768 to 114784
7174:[], # Indices 114784 to 114800
7175:[], # Indices 114800 to 114816
7176:[], # Indices 114816 to 114832
7177:[], # Indices 114832 to 114848
7178:[{'index_dec': 8, 'index_bin': '1000', 'val': 7, 'counts': 486}], # Indices 114848 to 114864
7179:[], # Indices 114864 to 114880
7180:[], # Indices 114880 to 114896
7181:[], # Indices 114896 to 114912
7182:[], # Indices 114912 to 114928
7183:[], # Indices 114928 to 114944
7184:[], # Indices 114944 to 114960
7185:[], # Indices 114960 to 114976
7186:[], # Indices 114976 to 114992
7187:[], # Indices 114992 to 115008
7188:[], # Indices 115008 to 115024
7189:[], # Indices 115024 to 115040
7190:[], # Indices 115040 to 115056
7191:[], # Indices 115056 to 115072
7192:[], # Indices 115072 to 115088
7193:[], # Indices 115088 to 115104
7194:[], # Indices 115104 to 115120
7195:[], # Indices 115120 to 115136
7196:[], # Indices 115136 to 115152
7197:[], # Indices 115152 to 115168
7198:[], # Indices 115168 to 115184
7199:[], # Indices 115184 to 115200
7200:[], # Indices 115200 to 115216
7201:[], # Indices 115216 to 115232
7202:[], # Indices 115232 to 115248
7203:[], # Indices 115248 to 115264
7204:[], # Indices 115264 to 115280
7205:[], # Indices 115280 to 115296
7206:[], # Indices 115296 to 115312
7207:[], # Indices 115312 to 115328
7208:[], # Indices 115328 to 115344
7209:[], # Indices 115344 to 115360
7210:[], # Indices 115360 to 115376
7211:[], # Indices 115376 to 115392
7212:[], # Indices 115392 to 115408
7213:[], # Indices 115408 to 115424
7214:[], # Indices 115424 to 115440
7215:[], # Indices 115440 to 115456
7216:[], # Indices 115456 to 115472
7217:[], # Indices 115472 to 115488
7218:[], # Indices 115488 to 115504
7219:[], # Indices 115504 to 115520
7220:[], # Indices 115520 to 115536
7221:[], # Indices 115536 to 115552
7222:[], # Indices 115552 to 115568
7223:[], # Indices 115568 to 115584
7224:[], # Indices 115584 to 115600
7225:[], # Indices 115600 to 115616
7226:[], # Indices 115616 to 115632
7227:[], # Indices 115632 to 115648
7228:[], # Indices 115648 to 115664
7229:[], # Indices 115664 to 115680
7230:[], # Indices 115680 to 115696
7231:[], # Indices 115696 to 115712
7232:[], # Indices 115712 to 115728
7233:[], # Indices 115728 to 115744
7234:[], # Indices 115744 to 115760
7235:[], # Indices 115760 to 115776
7236:[], # Indices 115776 to 115792
7237:[], # Indices 115792 to 115808
7238:[], # Indices 115808 to 115824
7239:[], # Indices 115824 to 115840
7240:[], # Indices 115840 to 115856
7241:[], # Indices 115856 to 115872
7242:[], # Indices 115872 to 115888
7243:[], # Indices 115888 to 115904
7244:[], # Indices 115904 to 115920
7245:[], # Indices 115920 to 115936
7246:[], # Indices 115936 to 115952
7247:[], # Indices 115952 to 115968
7248:[], # Indices 115968 to 115984
7249:[], # Indices 115984 to 116000
7250:[], # Indices 116000 to 116016
7251:[], # Indices 116016 to 116032
7252:[{'index_dec': 4, 'index_bin': '0100', 'val': 5, 'counts': 95}], # Indices 116032 to 116048
7253:[], # Indices 116048 to 116064
7254:[], # Indices 116064 to 116080
7255:[], # Indices 116080 to 116096
7256:[], # Indices 116096 to 116112
7257:[], # Indices 116112 to 116128
7258:[], # Indices 116128 to 116144
7259:[{'index_dec': 3, 'index_bin': '0011', 'val': 7, 'counts': 471}], # Indices 116144 to 116160
7260:[], # Indices 116160 to 116176
7261:[], # Indices 116176 to 116192
7262:[], # Indices 116192 to 116208
7263:[], # Indices 116208 to 116224
7264:[], # Indices 116224 to 116240
7265:[], # Indices 116240 to 116256
7266:[], # Indices 116256 to 116272
7267:[], # Indices 116272 to 116288
7268:[], # Indices 116288 to 116304
7269:[], # Indices 116304 to 116320
7270:[], # Indices 116320 to 116336
7271:[], # Indices 116336 to 116352
7272:[], # Indices 116352 to 116368
7273:[], # Indices 116368 to 116384
7274:[], # Indices 116384 to 116400
7275:[], # Indices 116400 to 116416
7276:[], # Indices 116416 to 116432
7277:[], # Indices 116432 to 116448
7278:[], # Indices 116448 to 116464
7279:[], # Indices 116464 to 116480
7280:[], # Indices 116480 to 116496
7281:[], # Indices 116496 to 116512
7282:[], # Indices 116512 to 116528
7283:[], # Indices 116528 to 116544
7284:[], # Indices 116544 to 116560
7285:[], # Indices 116560 to 116576
7286:[], # Indices 116576 to 116592
7287:[], # Indices 116592 to 116608
7288:[], # Indices 116608 to 116624
7289:[], # Indices 116624 to 116640
7290:[], # Indices 116640 to 116656
7291:[], # Indices 116656 to 116672
7292:[], # Indices 116672 to 116688
7293:[], # Indices 116688 to 116704
7294:[], # Indices 116704 to 116720
7295:[], # Indices 116720 to 116736
7296:[], # Indices 116736 to 116752
7297:[], # Indices 116752 to 116768
7298:[], # Indices 116768 to 116784
7299:[], # Indices 116784 to 116800
7300:[], # Indices 116800 to 116816
7301:[], # Indices 116816 to 116832
7302:[], # Indices 116832 to 116848
7303:[], # Indices 116848 to 116864
7304:[], # Indices 116864 to 116880
7305:[], # Indices 116880 to 116896
7306:[], # Indices 116896 to 116912
7307:[], # Indices 116912 to 116928
7308:[], # Indices 116928 to 116944
7309:[], # Indices 116944 to 116960
7310:[], # Indices 116960 to 116976
7311:[], # Indices 116976 to 116992
7312:[], # Indices 116992 to 117008
7313:[], # Indices 117008 to 117024
7314:[], # Indices 117024 to 117040
7315:[], # Indices 117040 to 117056
7316:[], # Indices 117056 to 117072
7317:[], # Indices 117072 to 117088
7318:[], # Indices 117088 to 117104
7319:[], # Indices 117104 to 117120
7320:[], # Indices 117120 to 117136
7321:[], # Indices 117136 to 117152
7322:[], # Indices 117152 to 117168
7323:[], # Indices 117168 to 117184
7324:[], # Indices 117184 to 117200
7325:[], # Indices 117200 to 117216
7326:[], # Indices 117216 to 117232
7327:[], # Indices 117232 to 117248
7328:[], # Indices 117248 to 117264
7329:[], # Indices 117264 to 117280
7330:[], # Indices 117280 to 117296
7331:[], # Indices 117296 to 117312
7332:[], # Indices 117312 to 117328
7333:[], # Indices 117328 to 117344
7334:[], # Indices 117344 to 117360
7335:[], # Indices 117360 to 117376
7336:[], # Indices 117376 to 117392
7337:[], # Indices 117392 to 117408
7338:[], # Indices 117408 to 117424
7339:[], # Indices 117424 to 117440
7340:[], # Indices 117440 to 117456
7341:[], # Indices 117456 to 117472
7342:[], # Indices 117472 to 117488
7343:[], # Indices 117488 to 117504
7344:[], # Indices 117504 to 117520
7345:[], # Indices 117520 to 117536
7346:[], # Indices 117536 to 117552
7347:[], # Indices 117552 to 117568
7348:[], # Indices 117568 to 117584
7349:[], # Indices 117584 to 117600
7350:[], # Indices 117600 to 117616
7351:[], # Indices 117616 to 117632
7352:[], # Indices 117632 to 117648
7353:[], # Indices 117648 to 117664
7354:[{'index_dec': 7, 'index_bin': '0111', 'val': 5, 'counts': 91}], # Indices 117664 to 117680
7355:[], # Indices 117680 to 117696
7356:[], # Indices 117696 to 117712
7357:[], # Indices 117712 to 117728
7358:[], # Indices 117728 to 117744
7359:[], # Indices 117744 to 117760
7360:[], # Indices 117760 to 117776
7361:[], # Indices 117776 to 117792
7362:[], # Indices 117792 to 117808
7363:[], # Indices 117808 to 117824
7364:[], # Indices 117824 to 117840
7365:[], # Indices 117840 to 117856
7366:[], # Indices 117856 to 117872
7367:[], # Indices 117872 to 117888
7368:[], # Indices 117888 to 117904
7369:[], # Indices 117904 to 117920
7370:[], # Indices 117920 to 117936
7371:[], # Indices 117936 to 117952
7372:[], # Indices 117952 to 117968
7373:[], # Indices 117968 to 117984
7374:[], # Indices 117984 to 118000
7375:[], # Indices 118000 to 118016
7376:[], # Indices 118016 to 118032
7377:[], # Indices 118032 to 118048
7378:[], # Indices 118048 to 118064
7379:[], # Indices 118064 to 118080
7380:[], # Indices 118080 to 118096
7381:[], # Indices 118096 to 118112
7382:[], # Indices 118112 to 118128
7383:[], # Indices 118128 to 118144
7384:[], # Indices 118144 to 118160
7385:[], # Indices 118160 to 118176
7386:[], # Indices 118176 to 118192
7387:[], # Indices 118192 to 118208
7388:[], # Indices 118208 to 118224
7389:[], # Indices 118224 to 118240
7390:[], # Indices 118240 to 118256
7391:[], # Indices 118256 to 118272
7392:[], # Indices 118272 to 118288
7393:[], # Indices 118288 to 118304
7394:[], # Indices 118304 to 118320
7395:[], # Indices 118320 to 118336
7396:[], # Indices 118336 to 118352
7397:[], # Indices 118352 to 118368
7398:[], # Indices 118368 to 118384
7399:[], # Indices 118384 to 118400
7400:[], # Indices 118400 to 118416
7401:[], # Indices 118416 to 118432
7402:[], # Indices 118432 to 118448
7403:[], # Indices 118448 to 118464
7404:[], # Indices 118464 to 118480
7405:[], # Indices 118480 to 118496
7406:[], # Indices 118496 to 118512
7407:[], # Indices 118512 to 118528
7408:[], # Indices 118528 to 118544
7409:[], # Indices 118544 to 118560
7410:[], # Indices 118560 to 118576
7411:[], # Indices 118576 to 118592
7412:[], # Indices 118592 to 118608
7413:[], # Indices 118608 to 118624
7414:[], # Indices 118624 to 118640
7415:[], # Indices 118640 to 118656
7416:[], # Indices 118656 to 118672
7417:[], # Indices 118672 to 118688
7418:[], # Indices 118688 to 118704
7419:[], # Indices 118704 to 118720
7420:[], # Indices 118720 to 118736
7421:[], # Indices 118736 to 118752
7422:[], # Indices 118752 to 118768
7423:[], # Indices 118768 to 118784
7424:[], # Indices 118784 to 118800
7425:[], # Indices 118800 to 118816
7426:[], # Indices 118816 to 118832
7427:[], # Indices 118832 to 118848
7428:[], # Indices 118848 to 118864
7429:[], # Indices 118864 to 118880
7430:[], # Indices 118880 to 118896
7431:[], # Indices 118896 to 118912
7432:[], # Indices 118912 to 118928
7433:[], # Indices 118928 to 118944
7434:[], # Indices 118944 to 118960
7435:[], # Indices 118960 to 118976
7436:[], # Indices 118976 to 118992
7437:[], # Indices 118992 to 119008
7438:[], # Indices 119008 to 119024
7439:[], # Indices 119024 to 119040
7440:[], # Indices 119040 to 119056
7441:[], # Indices 119056 to 119072
7442:[], # Indices 119072 to 119088
7443:[], # Indices 119088 to 119104
7444:[], # Indices 119104 to 119120
7445:[], # Indices 119120 to 119136
7446:[], # Indices 119136 to 119152
7447:[], # Indices 119152 to 119168
7448:[], # Indices 119168 to 119184
7449:[], # Indices 119184 to 119200
7450:[], # Indices 119200 to 119216
7451:[], # Indices 119216 to 119232
7452:[], # Indices 119232 to 119248
7453:[], # Indices 119248 to 119264
7454:[], # Indices 119264 to 119280
7455:[], # Indices 119280 to 119296
7456:[], # Indices 119296 to 119312
7457:[], # Indices 119312 to 119328
7458:[], # Indices 119328 to 119344
7459:[], # Indices 119344 to 119360
7460:[], # Indices 119360 to 119376
7461:[], # Indices 119376 to 119392
7462:[], # Indices 119392 to 119408
7463:[], # Indices 119408 to 119424
7464:[], # Indices 119424 to 119440
7465:[], # Indices 119440 to 119456
7466:[], # Indices 119456 to 119472
7467:[], # Indices 119472 to 119488
7468:[], # Indices 119488 to 119504
7469:[], # Indices 119504 to 119520
7470:[], # Indices 119520 to 119536
7471:[], # Indices 119536 to 119552
7472:[], # Indices 119552 to 119568
7473:[], # Indices 119568 to 119584
7474:[], # Indices 119584 to 119600
7475:[], # Indices 119600 to 119616
7476:[], # Indices 119616 to 119632
7477:[], # Indices 119632 to 119648
7478:[], # Indices 119648 to 119664
7479:[], # Indices 119664 to 119680
7480:[], # Indices 119680 to 119696
7481:[], # Indices 119696 to 119712
7482:[], # Indices 119712 to 119728
7483:[], # Indices 119728 to 119744
7484:[], # Indices 119744 to 119760
7485:[], # Indices 119760 to 119776
7486:[], # Indices 119776 to 119792
7487:[], # Indices 119792 to 119808
7488:[], # Indices 119808 to 119824
7489:[], # Indices 119824 to 119840
7490:[], # Indices 119840 to 119856
7491:[], # Indices 119856 to 119872
7492:[], # Indices 119872 to 119888
7493:[], # Indices 119888 to 119904
7494:[], # Indices 119904 to 119920
7495:[], # Indices 119920 to 119936
7496:[], # Indices 119936 to 119952
7497:[], # Indices 119952 to 119968
7498:[], # Indices 119968 to 119984
7499:[], # Indices 119984 to 120000
7500:[], # Indices 120000 to 120016
7501:[], # Indices 120016 to 120032
7502:[], # Indices 120032 to 120048
7503:[], # Indices 120048 to 120064
7504:[], # Indices 120064 to 120080
7505:[], # Indices 120080 to 120096
7506:[], # Indices 120096 to 120112
7507:[], # Indices 120112 to 120128
7508:[], # Indices 120128 to 120144
7509:[], # Indices 120144 to 120160
7510:[], # Indices 120160 to 120176
7511:[], # Indices 120176 to 120192
7512:[], # Indices 120192 to 120208
7513:[], # Indices 120208 to 120224
7514:[], # Indices 120224 to 120240
7515:[], # Indices 120240 to 120256
7516:[], # Indices 120256 to 120272
7517:[], # Indices 120272 to 120288
7518:[], # Indices 120288 to 120304
7519:[], # Indices 120304 to 120320
7520:[], # Indices 120320 to 120336
7521:[], # Indices 120336 to 120352
7522:[], # Indices 120352 to 120368
7523:[], # Indices 120368 to 120384
7524:[], # Indices 120384 to 120400
7525:[], # Indices 120400 to 120416
7526:[], # Indices 120416 to 120432
7527:[], # Indices 120432 to 120448
7528:[], # Indices 120448 to 120464
7529:[], # Indices 120464 to 120480
7530:[], # Indices 120480 to 120496
7531:[], # Indices 120496 to 120512
7532:[], # Indices 120512 to 120528
7533:[], # Indices 120528 to 120544
7534:[], # Indices 120544 to 120560
7535:[], # Indices 120560 to 120576
7536:[], # Indices 120576 to 120592
7537:[], # Indices 120592 to 120608
7538:[], # Indices 120608 to 120624
7539:[], # Indices 120624 to 120640
7540:[], # Indices 120640 to 120656
7541:[], # Indices 120656 to 120672
7542:[], # Indices 120672 to 120688
7543:[], # Indices 120688 to 120704
7544:[], # Indices 120704 to 120720
7545:[], # Indices 120720 to 120736
7546:[], # Indices 120736 to 120752
7547:[], # Indices 120752 to 120768
7548:[], # Indices 120768 to 120784
7549:[], # Indices 120784 to 120800
7550:[], # Indices 120800 to 120816
7551:[], # Indices 120816 to 120832
7552:[], # Indices 120832 to 120848
7553:[], # Indices 120848 to 120864
7554:[], # Indices 120864 to 120880
7555:[], # Indices 120880 to 120896
7556:[], # Indices 120896 to 120912
7557:[], # Indices 120912 to 120928
7558:[], # Indices 120928 to 120944
7559:[{'index_dec': 2, 'index_bin': '0010', 'val': 5, 'counts': 92}], # Indices 120944 to 120960
7560:[], # Indices 120960 to 120976
7561:[], # Indices 120976 to 120992
7562:[], # Indices 120992 to 121008
7563:[], # Indices 121008 to 121024
7564:[], # Indices 121024 to 121040
7565:[], # Indices 121040 to 121056
7566:[], # Indices 121056 to 121072
7567:[], # Indices 121072 to 121088
7568:[], # Indices 121088 to 121104
7569:[], # Indices 121104 to 121120
7570:[], # Indices 121120 to 121136
7571:[], # Indices 121136 to 121152
7572:[], # Indices 121152 to 121168
7573:[], # Indices 121168 to 121184
7574:[], # Indices 121184 to 121200
7575:[], # Indices 121200 to 121216
7576:[], # Indices 121216 to 121232
7577:[], # Indices 121232 to 121248
7578:[], # Indices 121248 to 121264
7579:[], # Indices 121264 to 121280
7580:[], # Indices 121280 to 121296
7581:[], # Indices 121296 to 121312
7582:[], # Indices 121312 to 121328
7583:[], # Indices 121328 to 121344
7584:[], # Indices 121344 to 121360
7585:[], # Indices 121360 to 121376
7586:[], # Indices 121376 to 121392
7587:[], # Indices 121392 to 121408
7588:[], # Indices 121408 to 121424
7589:[], # Indices 121424 to 121440
7590:[], # Indices 121440 to 121456
7591:[], # Indices 121456 to 121472
7592:[], # Indices 121472 to 121488
7593:[], # Indices 121488 to 121504
7594:[], # Indices 121504 to 121520
7595:[], # Indices 121520 to 121536
7596:[], # Indices 121536 to 121552
7597:[], # Indices 121552 to 121568
7598:[], # Indices 121568 to 121584
7599:[], # Indices 121584 to 121600
7600:[], # Indices 121600 to 121616
7601:[], # Indices 121616 to 121632
7602:[], # Indices 121632 to 121648
7603:[], # Indices 121648 to 121664
7604:[], # Indices 121664 to 121680
7605:[], # Indices 121680 to 121696
7606:[], # Indices 121696 to 121712
7607:[], # Indices 121712 to 121728
7608:[], # Indices 121728 to 121744
7609:[], # Indices 121744 to 121760
7610:[], # Indices 121760 to 121776
7611:[], # Indices 121776 to 121792
7612:[], # Indices 121792 to 121808
7613:[], # Indices 121808 to 121824
7614:[], # Indices 121824 to 121840
7615:[], # Indices 121840 to 121856
7616:[], # Indices 121856 to 121872
7617:[], # Indices 121872 to 121888
7618:[], # Indices 121888 to 121904
7619:[], # Indices 121904 to 121920
7620:[], # Indices 121920 to 121936
7621:[], # Indices 121936 to 121952
7622:[], # Indices 121952 to 121968
7623:[], # Indices 121968 to 121984
7624:[], # Indices 121984 to 122000
7625:[], # Indices 122000 to 122016
7626:[], # Indices 122016 to 122032
7627:[], # Indices 122032 to 122048
7628:[], # Indices 122048 to 122064
7629:[], # Indices 122064 to 122080
7630:[], # Indices 122080 to 122096
7631:[], # Indices 122096 to 122112
7632:[], # Indices 122112 to 122128
7633:[], # Indices 122128 to 122144
7634:[], # Indices 122144 to 122160
7635:[], # Indices 122160 to 122176
7636:[], # Indices 122176 to 122192
7637:[], # Indices 122192 to 122208
7638:[], # Indices 122208 to 122224
7639:[], # Indices 122224 to 122240
7640:[], # Indices 122240 to 122256
7641:[], # Indices 122256 to 122272
7642:[], # Indices 122272 to 122288
7643:[], # Indices 122288 to 122304
7644:[], # Indices 122304 to 122320
7645:[], # Indices 122320 to 122336
7646:[], # Indices 122336 to 122352
7647:[], # Indices 122352 to 122368
7648:[], # Indices 122368 to 122384
7649:[], # Indices 122384 to 122400
7650:[], # Indices 122400 to 122416
7651:[], # Indices 122416 to 122432
7652:[], # Indices 122432 to 122448
7653:[], # Indices 122448 to 122464
7654:[], # Indices 122464 to 122480
7655:[], # Indices 122480 to 122496
7656:[], # Indices 122496 to 122512
7657:[], # Indices 122512 to 122528
7658:[], # Indices 122528 to 122544
7659:[], # Indices 122544 to 122560
7660:[], # Indices 122560 to 122576
7661:[], # Indices 122576 to 122592
7662:[], # Indices 122592 to 122608
7663:[], # Indices 122608 to 122624
7664:[], # Indices 122624 to 122640
7665:[], # Indices 122640 to 122656
7666:[], # Indices 122656 to 122672
7667:[], # Indices 122672 to 122688
7668:[], # Indices 122688 to 122704
7669:[], # Indices 122704 to 122720
7670:[], # Indices 122720 to 122736
7671:[], # Indices 122736 to 122752
7672:[], # Indices 122752 to 122768
7673:[], # Indices 122768 to 122784
7674:[], # Indices 122784 to 122800
7675:[], # Indices 122800 to 122816
7676:[], # Indices 122816 to 122832
7677:[], # Indices 122832 to 122848
7678:[], # Indices 122848 to 122864
7679:[], # Indices 122864 to 122880
7680:[], # Indices 122880 to 122896
7681:[], # Indices 122896 to 122912
7682:[], # Indices 122912 to 122928
7683:[], # Indices 122928 to 122944
7684:[], # Indices 122944 to 122960
7685:[], # Indices 122960 to 122976
7686:[], # Indices 122976 to 122992
7687:[], # Indices 122992 to 123008
7688:[], # Indices 123008 to 123024
7689:[], # Indices 123024 to 123040
7690:[], # Indices 123040 to 123056
7691:[], # Indices 123056 to 123072
7692:[], # Indices 123072 to 123088
7693:[], # Indices 123088 to 123104
7694:[], # Indices 123104 to 123120
7695:[], # Indices 123120 to 123136
7696:[], # Indices 123136 to 123152
7697:[], # Indices 123152 to 123168
7698:[], # Indices 123168 to 123184
7699:[], # Indices 123184 to 123200
7700:[], # Indices 123200 to 123216
7701:[], # Indices 123216 to 123232
7702:[], # Indices 123232 to 123248
7703:[], # Indices 123248 to 123264
7704:[], # Indices 123264 to 123280
7705:[], # Indices 123280 to 123296
7706:[], # Indices 123296 to 123312
7707:[], # Indices 123312 to 123328
7708:[], # Indices 123328 to 123344
7709:[], # Indices 123344 to 123360
7710:[], # Indices 123360 to 123376
7711:[], # Indices 123376 to 123392
7712:[], # Indices 123392 to 123408
7713:[], # Indices 123408 to 123424
7714:[], # Indices 123424 to 123440
7715:[], # Indices 123440 to 123456
7716:[], # Indices 123456 to 123472
7717:[{'index_dec': 6, 'index_bin': '0110', 'val': 4, 'counts': 96}], # Indices 123472 to 123488
7718:[], # Indices 123488 to 123504
7719:[], # Indices 123504 to 123520
7720:[], # Indices 123520 to 123536
7721:[], # Indices 123536 to 123552
7722:[], # Indices 123552 to 123568
7723:[], # Indices 123568 to 123584
7724:[], # Indices 123584 to 123600
7725:[], # Indices 123600 to 123616
7726:[], # Indices 123616 to 123632
7727:[], # Indices 123632 to 123648
7728:[], # Indices 123648 to 123664
7729:[{'index_dec': 12, 'index_bin': '1100', 'val': 5, 'counts': 91}], # Indices 123664 to 123680
7730:[], # Indices 123680 to 123696
7731:[], # Indices 123696 to 123712
7732:[], # Indices 123712 to 123728
7733:[], # Indices 123728 to 123744
7734:[], # Indices 123744 to 123760
7735:[], # Indices 123760 to 123776
7736:[], # Indices 123776 to 123792
7737:[], # Indices 123792 to 123808
7738:[], # Indices 123808 to 123824
7739:[], # Indices 123824 to 123840
7740:[], # Indices 123840 to 123856
7741:[], # Indices 123856 to 123872
7742:[], # Indices 123872 to 123888
7743:[], # Indices 123888 to 123904
7744:[], # Indices 123904 to 123920
7745:[], # Indices 123920 to 123936
7746:[], # Indices 123936 to 123952
7747:[], # Indices 123952 to 123968
7748:[], # Indices 123968 to 123984
7749:[], # Indices 123984 to 124000
7750:[], # Indices 124000 to 124016
7751:[], # Indices 124016 to 124032
7752:[], # Indices 124032 to 124048
7753:[], # Indices 124048 to 124064
7754:[], # Indices 124064 to 124080
7755:[], # Indices 124080 to 124096
7756:[], # Indices 124096 to 124112
7757:[], # Indices 124112 to 124128
7758:[], # Indices 124128 to 124144
7759:[], # Indices 124144 to 124160
7760:[], # Indices 124160 to 124176
7761:[], # Indices 124176 to 124192
7762:[], # Indices 124192 to 124208
7763:[], # Indices 124208 to 124224
7764:[], # Indices 124224 to 124240
7765:[], # Indices 124240 to 124256
7766:[], # Indices 124256 to 124272
7767:[], # Indices 124272 to 124288
7768:[], # Indices 124288 to 124304
7769:[], # Indices 124304 to 124320
7770:[], # Indices 124320 to 124336
7771:[], # Indices 124336 to 124352
7772:[], # Indices 124352 to 124368
7773:[], # Indices 124368 to 124384
7774:[], # Indices 124384 to 124400
7775:[], # Indices 124400 to 124416
7776:[], # Indices 124416 to 124432
7777:[], # Indices 124432 to 124448
7778:[], # Indices 124448 to 124464
7779:[], # Indices 124464 to 124480
7780:[], # Indices 124480 to 124496
7781:[], # Indices 124496 to 124512
7782:[], # Indices 124512 to 124528
7783:[], # Indices 124528 to 124544
7784:[], # Indices 124544 to 124560
7785:[], # Indices 124560 to 124576
7786:[], # Indices 124576 to 124592
7787:[], # Indices 124592 to 124608
7788:[], # Indices 124608 to 124624
7789:[], # Indices 124624 to 124640
7790:[], # Indices 124640 to 124656
7791:[], # Indices 124656 to 124672
7792:[], # Indices 124672 to 124688
7793:[], # Indices 124688 to 124704
7794:[], # Indices 124704 to 124720
7795:[], # Indices 124720 to 124736
7796:[], # Indices 124736 to 124752
7797:[], # Indices 124752 to 124768
7798:[], # Indices 124768 to 124784
7799:[], # Indices 124784 to 124800
7800:[], # Indices 124800 to 124816
7801:[], # Indices 124816 to 124832
7802:[], # Indices 124832 to 124848
7803:[], # Indices 124848 to 124864
7804:[], # Indices 124864 to 124880
7805:[], # Indices 124880 to 124896
7806:[], # Indices 124896 to 124912
7807:[], # Indices 124912 to 124928
7808:[], # Indices 124928 to 124944
7809:[], # Indices 124944 to 124960
7810:[], # Indices 124960 to 124976
7811:[], # Indices 124976 to 124992
7812:[], # Indices 124992 to 125008
7813:[], # Indices 125008 to 125024
7814:[], # Indices 125024 to 125040
7815:[], # Indices 125040 to 125056
7816:[], # Indices 125056 to 125072
7817:[], # Indices 125072 to 125088
7818:[], # Indices 125088 to 125104
7819:[], # Indices 125104 to 125120
7820:[], # Indices 125120 to 125136
7821:[], # Indices 125136 to 125152
7822:[], # Indices 125152 to 125168
7823:[], # Indices 125168 to 125184
7824:[], # Indices 125184 to 125200
7825:[], # Indices 125200 to 125216
7826:[], # Indices 125216 to 125232
7827:[], # Indices 125232 to 125248
7828:[], # Indices 125248 to 125264
7829:[], # Indices 125264 to 125280
7830:[], # Indices 125280 to 125296
7831:[], # Indices 125296 to 125312
7832:[], # Indices 125312 to 125328
7833:[], # Indices 125328 to 125344
7834:[], # Indices 125344 to 125360
7835:[], # Indices 125360 to 125376
7836:[], # Indices 125376 to 125392
7837:[], # Indices 125392 to 125408
7838:[], # Indices 125408 to 125424
7839:[], # Indices 125424 to 125440
7840:[], # Indices 125440 to 125456
7841:[], # Indices 125456 to 125472
7842:[], # Indices 125472 to 125488
7843:[], # Indices 125488 to 125504
7844:[], # Indices 125504 to 125520
7845:[], # Indices 125520 to 125536
7846:[], # Indices 125536 to 125552
7847:[], # Indices 125552 to 125568
7848:[], # Indices 125568 to 125584
7849:[], # Indices 125584 to 125600
7850:[], # Indices 125600 to 125616
7851:[], # Indices 125616 to 125632
7852:[], # Indices 125632 to 125648
7853:[], # Indices 125648 to 125664
7854:[], # Indices 125664 to 125680
7855:[], # Indices 125680 to 125696
7856:[], # Indices 125696 to 125712
7857:[], # Indices 125712 to 125728
7858:[], # Indices 125728 to 125744
7859:[], # Indices 125744 to 125760
7860:[], # Indices 125760 to 125776
7861:[], # Indices 125776 to 125792
7862:[], # Indices 125792 to 125808
7863:[], # Indices 125808 to 125824
7864:[], # Indices 125824 to 125840
7865:[], # Indices 125840 to 125856
7866:[{'index_dec': 1, 'index_bin': '0001', 'val': 4, 'counts': 94}], # Indices 125856 to 125872
7867:[], # Indices 125872 to 125888
7868:[], # Indices 125888 to 125904
7869:[], # Indices 125904 to 125920
7870:[], # Indices 125920 to 125936
7871:[], # Indices 125936 to 125952
7872:[], # Indices 125952 to 125968
7873:[], # Indices 125968 to 125984
7874:[], # Indices 125984 to 126000
7875:[], # Indices 126000 to 126016
7876:[], # Indices 126016 to 126032
7877:[], # Indices 126032 to 126048
7878:[], # Indices 126048 to 126064
7879:[], # Indices 126064 to 126080
7880:[], # Indices 126080 to 126096
7881:[], # Indices 126096 to 126112
7882:[], # Indices 126112 to 126128
7883:[], # Indices 126128 to 126144
7884:[], # Indices 126144 to 126160
7885:[], # Indices 126160 to 126176
7886:[], # Indices 126176 to 126192
7887:[], # Indices 126192 to 126208
7888:[], # Indices 126208 to 126224
7889:[], # Indices 126224 to 126240
7890:[], # Indices 126240 to 126256
7891:[], # Indices 126256 to 126272
7892:[], # Indices 126272 to 126288
7893:[], # Indices 126288 to 126304
7894:[], # Indices 126304 to 126320
7895:[], # Indices 126320 to 126336
7896:[], # Indices 126336 to 126352
7897:[], # Indices 126352 to 126368
7898:[], # Indices 126368 to 126384
7899:[], # Indices 126384 to 126400
7900:[], # Indices 126400 to 126416
7901:[], # Indices 126416 to 126432
7902:[], # Indices 126432 to 126448
7903:[], # Indices 126448 to 126464
7904:[], # Indices 126464 to 126480
7905:[], # Indices 126480 to 126496
7906:[], # Indices 126496 to 126512
7907:[], # Indices 126512 to 126528
7908:[], # Indices 126528 to 126544
7909:[], # Indices 126544 to 126560
7910:[], # Indices 126560 to 126576
7911:[], # Indices 126576 to 126592
7912:[], # Indices 126592 to 126608
7913:[], # Indices 126608 to 126624
7914:[], # Indices 126624 to 126640
7915:[], # Indices 126640 to 126656
7916:[], # Indices 126656 to 126672
7917:[], # Indices 126672 to 126688
7918:[], # Indices 126688 to 126704
7919:[], # Indices 126704 to 126720
7920:[], # Indices 126720 to 126736
7921:[], # Indices 126736 to 126752
7922:[], # Indices 126752 to 126768
7923:[], # Indices 126768 to 126784
7924:[], # Indices 126784 to 126800
7925:[], # Indices 126800 to 126816
7926:[], # Indices 126816 to 126832
7927:[], # Indices 126832 to 126848
7928:[], # Indices 126848 to 126864
7929:[], # Indices 126864 to 126880
7930:[{'index_dec': 3, 'index_bin': '0011', 'val': 5, 'counts': 92}], # Indices 126880 to 126896
7931:[], # Indices 126896 to 126912
7932:[], # Indices 126912 to 126928
7933:[{'index_dec': 5, 'index_bin': '0101', 'val': 6, 'counts': 92}], # Indices 126928 to 126944
7934:[], # Indices 126944 to 126960
7935:[], # Indices 126960 to 126976
7936:[], # Indices 126976 to 126992
7937:[], # Indices 126992 to 127008
7938:[], # Indices 127008 to 127024
7939:[], # Indices 127024 to 127040
7940:[], # Indices 127040 to 127056
7941:[], # Indices 127056 to 127072
7942:[], # Indices 127072 to 127088
7943:[], # Indices 127088 to 127104
7944:[], # Indices 127104 to 127120
7945:[], # Indices 127120 to 127136
7946:[], # Indices 127136 to 127152
7947:[], # Indices 127152 to 127168
7948:[], # Indices 127168 to 127184
7949:[], # Indices 127184 to 127200
7950:[], # Indices 127200 to 127216
7951:[], # Indices 127216 to 127232
7952:[], # Indices 127232 to 127248
7953:[], # Indices 127248 to 127264
7954:[], # Indices 127264 to 127280
7955:[], # Indices 127280 to 127296
7956:[], # Indices 127296 to 127312
7957:[], # Indices 127312 to 127328
7958:[], # Indices 127328 to 127344
7959:[], # Indices 127344 to 127360
7960:[], # Indices 127360 to 127376
7961:[], # Indices 127376 to 127392
7962:[], # Indices 127392 to 127408
7963:[], # Indices 127408 to 127424
7964:[], # Indices 127424 to 127440
7965:[], # Indices 127440 to 127456
7966:[], # Indices 127456 to 127472
7967:[], # Indices 127472 to 127488
7968:[], # Indices 127488 to 127504
7969:[], # Indices 127504 to 127520
7970:[], # Indices 127520 to 127536
7971:[], # Indices 127536 to 127552
7972:[], # Indices 127552 to 127568
7973:[], # Indices 127568 to 127584
7974:[], # Indices 127584 to 127600
7975:[], # Indices 127600 to 127616
7976:[], # Indices 127616 to 127632
7977:[], # Indices 127632 to 127648
7978:[], # Indices 127648 to 127664
7979:[], # Indices 127664 to 127680
7980:[], # Indices 127680 to 127696
7981:[], # Indices 127696 to 127712
7982:[], # Indices 127712 to 127728
7983:[], # Indices 127728 to 127744
7984:[], # Indices 127744 to 127760
7985:[], # Indices 127760 to 127776
7986:[], # Indices 127776 to 127792
7987:[], # Indices 127792 to 127808
7988:[], # Indices 127808 to 127824
7989:[], # Indices 127824 to 127840
7990:[], # Indices 127840 to 127856
7991:[], # Indices 127856 to 127872
7992:[], # Indices 127872 to 127888
7993:[], # Indices 127888 to 127904
7994:[], # Indices 127904 to 127920
7995:[], # Indices 127920 to 127936
7996:[], # Indices 127936 to 127952
7997:[], # Indices 127952 to 127968
7998:[], # Indices 127968 to 127984
7999:[], # Indices 127984 to 128000
8000:[], # Indices 128000 to 128016
8001:[], # Indices 128016 to 128032
8002:[], # Indices 128032 to 128048
8003:[], # Indices 128048 to 128064
8004:[], # Indices 128064 to 128080
8005:[], # Indices 128080 to 128096
8006:[], # Indices 128096 to 128112
8007:[], # Indices 128112 to 128128
8008:[], # Indices 128128 to 128144
8009:[], # Indices 128144 to 128160
8010:[], # Indices 128160 to 128176
8011:[], # Indices 128176 to 128192
8012:[], # Indices 128192 to 128208
8013:[], # Indices 128208 to 128224
8014:[], # Indices 128224 to 128240
8015:[], # Indices 128240 to 128256
8016:[], # Indices 128256 to 128272
8017:[], # Indices 128272 to 128288
8018:[], # Indices 128288 to 128304
8019:[], # Indices 128304 to 128320
8020:[], # Indices 128320 to 128336
8021:[], # Indices 128336 to 128352
8022:[], # Indices 128352 to 128368
8023:[], # Indices 128368 to 128384
8024:[], # Indices 128384 to 128400
8025:[], # Indices 128400 to 128416
8026:[], # Indices 128416 to 128432
8027:[], # Indices 128432 to 128448
8028:[], # Indices 128448 to 128464
8029:[], # Indices 128464 to 128480
8030:[], # Indices 128480 to 128496
8031:[], # Indices 128496 to 128512
8032:[], # Indices 128512 to 128528
8033:[], # Indices 128528 to 128544
8034:[], # Indices 128544 to 128560
8035:[], # Indices 128560 to 128576
8036:[], # Indices 128576 to 128592
8037:[], # Indices 128592 to 128608
8038:[], # Indices 128608 to 128624
8039:[], # Indices 128624 to 128640
8040:[], # Indices 128640 to 128656
8041:[], # Indices 128656 to 128672
8042:[], # Indices 128672 to 128688
8043:[], # Indices 128688 to 128704
8044:[], # Indices 128704 to 128720
8045:[], # Indices 128720 to 128736
8046:[], # Indices 128736 to 128752
8047:[], # Indices 128752 to 128768
8048:[], # Indices 128768 to 128784
8049:[], # Indices 128784 to 128800
8050:[], # Indices 128800 to 128816
8051:[], # Indices 128816 to 128832
8052:[], # Indices 128832 to 128848
8053:[], # Indices 128848 to 128864
8054:[], # Indices 128864 to 128880
8055:[], # Indices 128880 to 128896
8056:[], # Indices 128896 to 128912
8057:[], # Indices 128912 to 128928
8058:[], # Indices 128928 to 128944
8059:[], # Indices 128944 to 128960
8060:[], # Indices 128960 to 128976
8061:[], # Indices 128976 to 128992
8062:[], # Indices 128992 to 129008
8063:[], # Indices 129008 to 129024
8064:[], # Indices 129024 to 129040
8065:[], # Indices 129040 to 129056
8066:[], # Indices 129056 to 129072
8067:[], # Indices 129072 to 129088
8068:[], # Indices 129088 to 129104
8069:[], # Indices 129104 to 129120
8070:[], # Indices 129120 to 129136
8071:[], # Indices 129136 to 129152
8072:[], # Indices 129152 to 129168
8073:[], # Indices 129168 to 129184
8074:[], # Indices 129184 to 129200
8075:[], # Indices 129200 to 129216
8076:[], # Indices 129216 to 129232
8077:[], # Indices 129232 to 129248
8078:[], # Indices 129248 to 129264
8079:[], # Indices 129264 to 129280
8080:[], # Indices 129280 to 129296
8081:[], # Indices 129296 to 129312
8082:[], # Indices 129312 to 129328
8083:[], # Indices 129328 to 129344
8084:[], # Indices 129344 to 129360
8085:[], # Indices 129360 to 129376
8086:[], # Indices 129376 to 129392
8087:[], # Indices 129392 to 129408
8088:[], # Indices 129408 to 129424
8089:[], # Indices 129424 to 129440
8090:[], # Indices 129440 to 129456
8091:[], # Indices 129456 to 129472
8092:[], # Indices 129472 to 129488
8093:[], # Indices 129488 to 129504
8094:[], # Indices 129504 to 129520
8095:[], # Indices 129520 to 129536
8096:[], # Indices 129536 to 129552
8097:[], # Indices 129552 to 129568
8098:[{'index_dec': 10, 'index_bin': '1010', 'val': 5, 'counts': 92}], # Indices 129568 to 129584
8099:[], # Indices 129584 to 129600
8100:[], # Indices 129600 to 129616
8101:[], # Indices 129616 to 129632
8102:[], # Indices 129632 to 129648
8103:[], # Indices 129648 to 129664
8104:[], # Indices 129664 to 129680
8105:[], # Indices 129680 to 129696
8106:[], # Indices 129696 to 129712
8107:[], # Indices 129712 to 129728
8108:[], # Indices 129728 to 129744
8109:[], # Indices 129744 to 129760
8110:[], # Indices 129760 to 129776
8111:[], # Indices 129776 to 129792
8112:[], # Indices 129792 to 129808
8113:[], # Indices 129808 to 129824
8114:[], # Indices 129824 to 129840
8115:[], # Indices 129840 to 129856
8116:[], # Indices 129856 to 129872
8117:[], # Indices 129872 to 129888
8118:[], # Indices 129888 to 129904
8119:[], # Indices 129904 to 129920
8120:[], # Indices 129920 to 129936
8121:[], # Indices 129936 to 129952
8122:[], # Indices 129952 to 129968
8123:[], # Indices 129968 to 129984
8124:[], # Indices 129984 to 130000
8125:[], # Indices 130000 to 130016
8126:[], # Indices 130016 to 130032
8127:[], # Indices 130032 to 130048
8128:[], # Indices 130048 to 130064
8129:[], # Indices 130064 to 130080
8130:[], # Indices 130080 to 130096
8131:[], # Indices 130096 to 130112
8132:[], # Indices 130112 to 130128
8133:[], # Indices 130128 to 130144
8134:[], # Indices 130144 to 130160
8135:[], # Indices 130160 to 130176
8136:[], # Indices 130176 to 130192
8137:[], # Indices 130192 to 130208
8138:[], # Indices 130208 to 130224
8139:[], # Indices 130224 to 130240
8140:[], # Indices 130240 to 130256
8141:[], # Indices 130256 to 130272
8142:[], # Indices 130272 to 130288
8143:[], # Indices 130288 to 130304
8144:[], # Indices 130304 to 130320
8145:[], # Indices 130320 to 130336
8146:[], # Indices 130336 to 130352
8147:[], # Indices 130352 to 130368
8148:[], # Indices 130368 to 130384
8149:[], # Indices 130384 to 130400
8150:[], # Indices 130400 to 130416
8151:[], # Indices 130416 to 130432
8152:[{'index_dec': 13, 'index_bin': '1101', 'val': 5, 'counts': 93}], # Indices 130432 to 130448
8153:[], # Indices 130448 to 130464
8154:[], # Indices 130464 to 130480
8155:[], # Indices 130480 to 130496
8156:[], # Indices 130496 to 130512
8157:[], # Indices 130512 to 130528
8158:[], # Indices 130528 to 130544
8159:[], # Indices 130544 to 130560
8160:[], # Indices 130560 to 130576
8161:[], # Indices 130576 to 130592
8162:[], # Indices 130592 to 130608
8163:[], # Indices 130608 to 130624
8164:[], # Indices 130624 to 130640
8165:[], # Indices 130640 to 130656
8166:[], # Indices 130656 to 130672
8167:[], # Indices 130672 to 130688
8168:[], # Indices 130688 to 130704
8169:[], # Indices 130704 to 130720
8170:[], # Indices 130720 to 130736
8171:[], # Indices 130736 to 130752
8172:[], # Indices 130752 to 130768
8173:[], # Indices 130768 to 130784
8174:[], # Indices 130784 to 130800
8175:[], # Indices 130800 to 130816
8176:[], # Indices 130816 to 130832
8177:[], # Indices 130832 to 130848
8178:[], # Indices 130848 to 130864
8179:[], # Indices 130864 to 130880
8180:[], # Indices 130880 to 130896
8181:[], # Indices 130896 to 130912
8182:[], # Indices 130912 to 130928
8183:[], # Indices 130928 to 130944
8184:[], # Indices 130944 to 130960
8185:[], # Indices 130960 to 130976
8186:[], # Indices 130976 to 130992
8187:[], # Indices 130992 to 131008
8188:[], # Indices 131008 to 131024
8189:[], # Indices 131024 to 131040
8190:[], # Indices 131040 to 131056
8191:[], # Indices 131056 to 131072
}


index_array = []
for i in dict_val:
    for sol in dict_val[int(i)]:
        index_array.append(i*nb_break + sol['index_dec'])

for i in index_array:
    print(f"SNR Index: {i};  		SNR value: {round(snrs[i],3)}")
