import sys, os, argparse

print()
print("###### Build site pages ######");
print("PYTHON VERSION: " + ".".join(map(str, sys.version_info[:3])))
print("# Script call: " + " ".join(sys.argv) + "\n----------");

parser = argparse.ArgumentParser(description="Gets stats from a bunch of abyss assemblies.");
parser.add_argument("--all", dest="all", help="Build all pages", action="store_true", default=False);
parser.add_argument("--index", dest="index", help="Without --all: build index.html. With --all: exlude index.html", action="store_true", default=False);
parser.add_argument("--annotation", dest="annotation", help="Without --all: build annotation.html. With --all: exlude annotation.html", action="store_true", default=False);
parser.add_argument("--molevol", dest="molevol", help="Without --all: build mol_evol.html. With --all: exlude mol_evol.html", action="store_true", default=False);
args = parser.parse_args();
# Input options.

#cwd = os.getcwd();
os.chdir("generators");

pages = {
    'index' : args.index,
    'annotation' : args.annotation,
    'molevol' : args.molevol,
}

if args.all:
    pages = { page : False if pages[page] == True else True for page in pages };

if pages['index']:
    os.system("python index_generator.py");

if pages['annotation']:
    os.system("Rscript annotation_generator.r");

if pages['molevol']:
    os.system("Rscript mol_evol_generator.r");

print("----------\nDone!");


