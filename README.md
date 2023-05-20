# FODs_scalling_for_lobedness_project
**Algorithm**
Start from the energy-minimizing FOD position vectors {a_i} and nuclear position 
vectors {R_alpha}. Associate a nuclear position R_i with each FOD a_i by first calculating 
abs(a_i-R_alpha). Look at the {R_alpha} that are within 2 .5 Angstroms of a given a_i, Choose 
the one that belongs to the nearest non-hydrogen nucleus. If there is no non-hydrogen in this range, 
choose the nearest hydrogen nucleus. If this choice yields two nuclei that are equidistant from 
a_i, within a tolerance of 0.05 Angstrom, redefine the R_i vector as the average of the two nuclear 
positions.

           Then scale to find new FOD position a_i':

a_i'-R_i = 0.5*(a_i-R_i).

or equivalently

a_i' = 0.5*(a_i+R_i).

This should scale the FODs closer to the nuclei,
preferentially toward the non-hydrogen nuclei,
and move the double-bond FODs closer to the 
bond axis.
![image](https://github.com/Rajkishor46/FODs_scalling_for_lobedness_project/assets/66030028/5c1e9db4-46b1-4a43-a5c5-5946cd6d9295)
