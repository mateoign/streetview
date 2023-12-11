import images_individual as ii


INPUT = 'data/Q1ProjectStructureList.xlsx'
OUTPATH = 'data/images/'


if __name__== "__main__":
    # Phi to Kelly is training set
    ii.images_phi(INPUT, OUTPATH)
    ii.images_alex()
    ii.images_sunny('data/structure_coordinates.json', OUTPATH)
    ii.images_kelly(OUTPATH)
    
    # Noel and Josh are validation set
    #ii.images_noel(OUTPATH)
    #ii.images_joshua('data/joshua_structures.json', OUTPATH)
    ###ii.images_tram(OUTPATH)
    # The rest were unused because it was too much and made the model run slow
    #ii.images_mateo(OUTPATH)
    #ii.images_derek()
    #ii.images_lauren()
    #ii.images_kevin('data/kevin_structures.json', OUTPATH)
