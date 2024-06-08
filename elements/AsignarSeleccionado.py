from elements.mejoras import AttackeRapido, BalasRapidas, MasVida, LifeRegen

def AsignarSeleccionado(seleccionado, player):
    if seleccionado == AttackeRapido:
        seleccionado(seleccionado=True, player=player)

    elif seleccionado == BalasRapidas:
        seleccionado(seleccionado=True, player=player)
    
    elif seleccionado == MasVida:
        seleccionado(seleccionado=True, player=player)
    
    elif seleccionado == LifeRegen:
        seleccionado(seleccionado=True, player=player)
    
