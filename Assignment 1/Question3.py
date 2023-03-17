
# When the probability of payout of M1 machine is 15%
# Let case 'PA' be the probability that machine M1 does not pay out
# Let case 'PB' be the probability that machine M2 does not pay out
PA = 0.85
PB = 0.95
P_M1 = 0.5
# Calculate the probability of selecting M1 in the case of not pay out
P_notPayout = PA * P_M1/((PA+PB)/2)
# Calculate the probability of selecting M1 in the case of pay out
P_Payout = (1-PA) * P_M1/((1-PA+1-PB)/2)

print(P_notPayout)
print(P_Payout)










