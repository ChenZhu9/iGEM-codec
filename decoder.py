from decode import *
msg_in = "SJTU-Mulan"
nsym=4
msg = rs_encode_msg([ord(x) for x in msg_in], nsym)
msg[1]=56
synd = rs_calc_syndromes(msg, nsym)
err_loc = rs_find_error_locator(synd, nsym)
pos = rs_find_errors(err_loc[::-1], len(msg)) # find the errors locations
print(pos)
msg = rs_correct_errata(msg, synd, pos)
for i in range (len(msg_in)):
    print(chr(msg[i]), end='')
