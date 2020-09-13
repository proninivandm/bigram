import textgen
parser = textgen.argparse.ArgumentParser(description='text fit')
parser.add_argument('--seed', dest='seed', type=int, help='rnd_seed')
parser.add_argument('--len', dest='len', type=int, help='len of output')
with open('txt_model.pickle', 'rb') as fl:
    my_model=textgen.pickle.load(fl)
my_model.generate(parser.parse_args().seed, parser.parse_args().len)