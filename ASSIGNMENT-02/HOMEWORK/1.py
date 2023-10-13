def hospital_fee(**kwargs):
    highest_fee = 0
    highest_payers = []

    for payer, fee in kwargs.items():
        if fee > highest_fee:
            highest_fee = fee
            highest_payers = [payer]
        elif fee == highest_fee:
            highest_payers.append(payer)

    return highest_fee, highest_payers

max_amount, max_payer = hospital_fee(Neymar=1000, Dembele=600, Reus=500, Bale=1000)
print(f"Highest fee was {max_amount} tk which was paid by {', '.join(max_payer)}.")

max_amount, max_payer = hospital_fee(Mashrafe=400, Bumrah=900, Steyn=1200, Cummins=900, Wood=400, Marsh=700)
print(f"Highest fee was {max_amount} tk which was paid by {', '.join(max_payer)}.")
