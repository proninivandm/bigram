import textgen
parser = textgen.argparse.ArgumentParser(description='text fit')
parser.add_argument('-f', dest='folder', type=str, help='path to txt files')
my_model=textgen.Textgen()
my_model.fit(parser.parse_args().folder)
with open('txt_model.pickle', 'wb') as fl:
    textgen.pickle.dump(my_model, fl)

