import LOYcaller

cl = LOYcaller.call_loy("/Volumes/Gottmik/UKBB/updated_files/sub_l2r_chrY.txt", "/Volumes/Gottmik/UKBB/updated_files/sub_l2r_chrX.txt", 
"/Volumes/Gottmik/UKBB/updated_files/sub_famData.fam")
cl.save_output("male_mlrr.txt")

loyP = LOYcaller.mLRRYtoPer("male_mlrr.txt")
loyP.write_csv("male_mlrr_loyP.txt")
