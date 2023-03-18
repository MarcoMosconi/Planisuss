from vegetobs.setup import vegetobs

def grow():

    for key in vegetobs:
        vegetobs[key].grow()
        