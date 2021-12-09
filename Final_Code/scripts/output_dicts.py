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

nb_break = 2**7 #size of blocks
broken_snrs = [snrs[i:i + nb_break] for i in range(0, len(snrs), nb_break)]
dict_val = {
0:[{'index_dec': 13, 'index_bin': '0001101', 'val': 7, 'counts': 75}, {'index_dec': 38, 'index_bin': '0100110', 'val': 8, 'counts': 62}, {'index_dec': 63, 'index_bin': '0111111', 'val': 8, 'counts': 63}], # Indices 0 to 128
1:[{'index_dec': 33, 'index_bin': '0100001', 'val': 7, 'counts': 66}, {'index_dec': 40, 'index_bin': '0101000', 'val': 7, 'counts': 73}], # Indices 128 to 256
2:[{'index_dec': 28, 'index_bin': '0011100', 'val': 7, 'counts': 82}], # Indices 256 to 384
3:[], # Indices 384 to 512
4:[{'index_dec': 65, 'index_bin': '1000001', 'val': 7, 'counts': 67}, {'index_dec': 90, 'index_bin': '1011010', 'val': 7, 'counts': 82}], # Indices 512 to 640
5:[], # Indices 640 to 768
6:[], # Indices 768 to 896
7:[{'index_dec': 18, 'index_bin': '0010010', 'val': 13, 'counts': 80}], # Indices 896 to 1024
8:[{'index_dec': 96, 'index_bin': '1100000', 'val': 7, 'counts': 71}, {'index_dec': 97, 'index_bin': '1100001', 'val': 9, 'counts': 71}, {'index_dec': 99, 'index_bin': '1100011', 'val': 9, 'counts': 69}], # Indices 1024 to 1152
9:[], # Indices 1152 to 1280
10:[{'index_dec': 66, 'index_bin': '1000010', 'val': 7, 'counts': 69}, {'index_dec': 71, 'index_bin': '1000111', 'val': 11, 'counts': 69}, {'index_dec': 75, 'index_bin': '1001011', 'val': 7, 'counts': 74}, {'index_dec': 118, 'index_bin': '1110110', 'val': 8, 'counts': 67}], # Indices 1280 to 1408
11:[{'index_dec': 41, 'index_bin': '0101001', 'val': 7, 'counts': 59}, {'index_dec': 59, 'index_bin': '0111011', 'val': 9, 'counts': 46}, {'index_dec': 78, 'index_bin': '1001110', 'val': 7, 'counts': 62}, {'index_dec': 81, 'index_bin': '1010001', 'val': 7, 'counts': 61}, {'index_dec': 104, 'index_bin': '1101000', 'val': 8, 'counts': 62}, {'index_dec': 112, 'index_bin': '1110000', 'val': 7, 'counts': 69}], # Indices 1408 to 1536
12:[{'index_dec': 2, 'index_bin': '0000010', 'val': 7, 'counts': 66}, {'index_dec': 7, 'index_bin': '0000111', 'val': 7, 'counts': 60}, {'index_dec': 9, 'index_bin': '0001001', 'val': 7, 'counts': 63}], # Indices 1536 to 1664
13:[{'index_dec': 124, 'index_bin': '1111100', 'val': 7, 'counts': 60}], # Indices 1664 to 1792
14:[{'index_dec': 12, 'index_bin': '0001100', 'val': 7, 'counts': 64}, {'index_dec': 14, 'index_bin': '0001110', 'val': 8, 'counts': 57}, {'index_dec': 25, 'index_bin': '0011001', 'val': 9, 'counts': 55}, {'index_dec': 36, 'index_bin': '0100100', 'val': 9, 'counts': 55}, {'index_dec': 37, 'index_bin': '0100101', 'val': 8, 'counts': 51}, {'index_dec': 38, 'index_bin': '0100110', 'val': 8, 'counts': 53}, {'index_dec': 44, 'index_bin': '0101100', 'val': 7, 'counts': 51}, {'index_dec': 53, 'index_bin': '0110101', 'val': 7, 'counts': 55}, {'index_dec': 60, 'index_bin': '0111100', 'val': 7, 'counts': 50}, {'index_dec': 61, 'index_bin': '0111101', 'val': 8, 'counts': 44}, {'index_dec': 105, 'index_bin': '1101001', 'val': 7, 'counts': 61}, {'index_dec': 114, 'index_bin': '1110010', 'val': 7, 'counts': 50}, {'index_dec': 120, 'index_bin': '1111000', 'val': 7, 'counts': 52}], # Indices 1792 to 1920
15:[{'index_dec': 11, 'index_bin': '0001011', 'val': 8, 'counts': 70}, {'index_dec': 13, 'index_bin': '0001101', 'val': 9, 'counts': 65}, {'index_dec': 47, 'index_bin': '0101111', 'val': 8, 'counts': 64}, {'index_dec': 49, 'index_bin': '0110001', 'val': 8, 'counts': 68}], # Indices 1920 to 2048
16:[], # Indices 2048 to 2176
17:[], # Indices 2176 to 2304
18:[{'index_dec': 39, 'index_bin': '0100111', 'val': 7, 'counts': 64}, {'index_dec': 47, 'index_bin': '0101111', 'val': 7, 'counts': 54}, {'index_dec': 55, 'index_bin': '0110111', 'val': 7, 'counts': 53}, {'index_dec': 68, 'index_bin': '1000100', 'val': 9, 'counts': 64}, {'index_dec': 73, 'index_bin': '1001001', 'val': 8, 'counts': 65}, {'index_dec': 75, 'index_bin': '1001011', 'val': 8, 'counts': 61}, {'index_dec': 94, 'index_bin': '1011110', 'val': 8, 'counts': 56}, {'index_dec': 99, 'index_bin': '1100011', 'val': 8, 'counts': 52}, {'index_dec': 119, 'index_bin': '1110111', 'val': 10, 'counts': 55}], # Indices 2304 to 2432
19:[], # Indices 2432 to 2560
20:[{'index_dec': 109, 'index_bin': '1101101', 'val': 8, 'counts': 77}, {'index_dec': 120, 'index_bin': '1111000', 'val': 7, 'counts': 78}], # Indices 2560 to 2688
21:[{'index_dec': 1, 'index_bin': '0000001', 'val': 7, 'counts': 79}, {'index_dec': 62, 'index_bin': '0111110', 'val': 7, 'counts': 63}, {'index_dec': 95, 'index_bin': '1011111', 'val': 7, 'counts': 58}, {'index_dec': 100, 'index_bin': '1100100', 'val': 8, 'counts': 67}, {'index_dec': 123, 'index_bin': '1111011', 'val': 7, 'counts': 59}], # Indices 2688 to 2816
22:[{'index_dec': 1, 'index_bin': '0000001', 'val': 11, 'counts': 63}, {'index_dec': 5, 'index_bin': '0000101', 'val': 10, 'counts': 56}, {'index_dec': 22, 'index_bin': '0010110', 'val': 13, 'counts': 68}, {'index_dec': 27, 'index_bin': '0011011', 'val': 7, 'counts': 69}, {'index_dec': 41, 'index_bin': '0101001', 'val': 8, 'counts': 68}, {'index_dec': 61, 'index_bin': '0111101', 'val': 7, 'counts': 50}, {'index_dec': 75, 'index_bin': '1001011', 'val': 14, 'counts': 61}, {'index_dec': 77, 'index_bin': '1001101', 'val': 10, 'counts': 56}, {'index_dec': 88, 'index_bin': '1011000', 'val': 8, 'counts': 51}, {'index_dec': 124, 'index_bin': '1111100', 'val': 8, 'counts': 48}], # Indices 2816 to 2944
23:[], # Indices 2944 to 3072
24:[{'index_dec': 69, 'index_bin': '1000101', 'val': 7, 'counts': 63}], # Indices 3072 to 3200
25:[{'index_dec': 5, 'index_bin': '0000101', 'val': 7, 'counts': 57}, {'index_dec': 20, 'index_bin': '0010100', 'val': 9, 'counts': 58}, {'index_dec': 27, 'index_bin': '0011011', 'val': 10, 'counts': 42}, {'index_dec': 29, 'index_bin': '0011101', 'val': 7, 'counts': 46}, {'index_dec': 34, 'index_bin': '0100010', 'val': 7, 'counts': 63}, {'index_dec': 63, 'index_bin': '0111111', 'val': 10, 'counts': 58}, {'index_dec': 75, 'index_bin': '1001011', 'val': 10, 'counts': 68}, {'index_dec': 96, 'index_bin': '1100000', 'val': 8, 'counts': 64}, {'index_dec': 103, 'index_bin': '1100111', 'val': 9, 'counts': 64}, {'index_dec': 111, 'index_bin': '1101111', 'val': 9, 'counts': 58}, {'index_dec': 113, 'index_bin': '1110001', 'val': 7, 'counts': 65}], # Indices 3200 to 3328
26:[], # Indices 3328 to 3456
27:[], # Indices 3456 to 3584
28:[], # Indices 3584 to 3712
29:[], # Indices 3712 to 3840
30:[], # Indices 3840 to 3968
31:[{'index_dec': 17, 'index_bin': '0010001', 'val': 7, 'counts': 38}, {'index_dec': 19, 'index_bin': '0010011', 'val': 7, 'counts': 47}, {'index_dec': 23, 'index_bin': '0010111', 'val': 14, 'counts': 48}, {'index_dec': 42, 'index_bin': '0101010', 'val': 7, 'counts': 40}, {'index_dec': 45, 'index_bin': '0101101', 'val': 7, 'counts': 38}, {'index_dec': 54, 'index_bin': '0110110', 'val': 7, 'counts': 50}, {'index_dec': 57, 'index_bin': '0111001', 'val': 7, 'counts': 40}, {'index_dec': 64, 'index_bin': '1000000', 'val': 7, 'counts': 37}, {'index_dec': 65, 'index_bin': '1000001', 'val': 7, 'counts': 59}, {'index_dec': 77, 'index_bin': '1001101', 'val': 7, 'counts': 47}, {'index_dec': 83, 'index_bin': '1010011', 'val': 7, 'counts': 45}, {'index_dec': 90, 'index_bin': '1011010', 'val': 7, 'counts': 38}, {'index_dec': 91, 'index_bin': '1011011', 'val': 7, 'counts': 32}, {'index_dec': 92, 'index_bin': '1011100', 'val': 7, 'counts': 45}, {'index_dec': 93, 'index_bin': '1011101', 'val': 7, 'counts': 58}, {'index_dec': 96, 'index_bin': '1100000', 'val': 7, 'counts': 43}, {'index_dec': 99, 'index_bin': '1100011', 'val': 7, 'counts': 39}, {'index_dec': 100, 'index_bin': '1100100', 'val': 7, 'counts': 44}, {'index_dec': 106, 'index_bin': '1101010', 'val': 7, 'counts': 41}, {'index_dec': 115, 'index_bin': '1110011', 'val': 8, 'counts': 46}, {'index_dec': 125, 'index_bin': '1111101', 'val': 8, 'counts': 47}], # Indices 3968 to 4096
32:[{'index_dec': 0, 'index_bin': '0000000', 'val': 8, 'counts': 49}, {'index_dec': 1, 'index_bin': '0000001', 'val': 7, 'counts': 62}, {'index_dec': 10, 'index_bin': '0001010', 'val': 7, 'counts': 56}, {'index_dec': 12, 'index_bin': '0001100', 'val': 7, 'counts': 73}, {'index_dec': 18, 'index_bin': '0010010', 'val': 7, 'counts': 54}, {'index_dec': 19, 'index_bin': '0010011', 'val': 7, 'counts': 47}, {'index_dec': 22, 'index_bin': '0010110', 'val': 7, 'counts': 58}, {'index_dec': 37, 'index_bin': '0100101', 'val': 8, 'counts': 66}, {'index_dec': 46, 'index_bin': '0101110', 'val': 8, 'counts': 61}, {'index_dec': 63, 'index_bin': '0111111', 'val': 8, 'counts': 53}, {'index_dec': 65, 'index_bin': '1000001', 'val': 7, 'counts': 47}], # Indices 4096 to 4224
33:[{'index_dec': 97, 'index_bin': '1100001', 'val': 9, 'counts': 54}, {'index_dec': 100, 'index_bin': '1100100', 'val': 7, 'counts': 68}, {'index_dec': 111, 'index_bin': '1101111', 'val': 8, 'counts': 78}, {'index_dec': 114, 'index_bin': '1110010', 'val': 7, 'counts': 68}], # Indices 4224 to 4352
34:[{'index_dec': 13, 'index_bin': '0001101', 'val': 7, 'counts': 54}, {'index_dec': 21, 'index_bin': '0010101', 'val': 7, 'counts': 66}, {'index_dec': 34, 'index_bin': '0100010', 'val': 9, 'counts': 73}, {'index_dec': 57, 'index_bin': '0111001', 'val': 7, 'counts': 57}, {'index_dec': 94, 'index_bin': '1011110', 'val': 8, 'counts': 64}, {'index_dec': 95, 'index_bin': '1011111', 'val': 7, 'counts': 67}, {'index_dec': 120, 'index_bin': '1111000', 'val': 12, 'counts': 78}], # Indices 4352 to 4480
}

index_array = []
for i in dict_val:
    for sol in dict_val[int(i)]:
        index_array.append(i*nb_break + sol['index_dec'])

p = []
ind = 0
for i in np.rint(snrs.tolist()).astype(np.int64)[:2**17]:
    if i > 15:
        p.append((i,ind))
    ind += 1

print(p)
