import LOYcaller

cl = LOYcaller.call_loy("/path/to/file/sub_l2r_chrY.txt", "/path/to/file/sub_l2r_chrX.txt", 
"/path/to/file/sub_famData.fam")
cl.save_output("male_mlrr.txt")

loyP = LOYcaller.mLRRYtoPer("male_mlrr.txt")
loyP.write_csv("male_mlrr_loyP.txt")
