kuhan_pituus = float(input("Kuhan pituus senttimetreinä: "))
kuha_mitta = 37
if kuhan_pituus < 37:
    puuttuva_mitta = kuha_mitta - kuhan_pituus
    print(f"Laske kuha takaisin järveen. Kuhan tulee olla {puuttuva_mitta}cm pidempi.")
else:
    print("Kuha on täysimittainen.")